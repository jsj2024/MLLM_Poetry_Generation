"""
UI组件模块 - Components
定义Gradio界面组件和渲染逻辑
"""
import functools
from datetime import datetime
from typing import Dict, List, Any, Tuple
import gradio as gr
from PIL import Image

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from config.config import (
    DEFAULT_FORMAT,
    DEFAULT_STYLE,
    MAX_RECENT_ENTRIES,
    IMAGE_UPLOAD_HEIGHT,
    CHATBOT_HEIGHT,
    POEM_OUTPUT_LINES,
    FOLLOW_UP_SUGGESTIONS,
    APP_AUTHOR,
    APP_COURSE,
    APP_VERSION,
)
from src.constants.templates import (
    FORMAT_GUIDE,
    STYLE_GUIDE,
    HERO_HTML_TEMPLATE,
    FOOTER_HTML_TEMPLATE,
    RECENT_CARD_TEMPLATE,
    RECENT_EMPTY_TEMPLATE,
)
from src.utils.image_processor import (
    analyze_image_profile,
    encode_image_to_data_uri,
    preprocess_image,
)
from src.utils.prompt_builder import (
    format_prompt_preview,
    style_prompt_preview,
    apply_suggestion,
)

# 类型别名
ChatHistory = List[Tuple[str, str]]


def render_recent_creations(entries: List[Dict[str, Any]]) -> str:
    """
    渲染最近创作记录的HTML
    
    Args:
        entries: 创作记录列表
        
    Returns:
        HTML字符串
    """
    if not entries:
        return RECENT_EMPTY_TEMPLATE
    
    cards: List[str] = []
    for entry in entries:
        # 格式化历史对话
        history_html = "<br>".join(
            f"<strong>用户：</strong>{user}<br><strong>AI：</strong>{resp[:100]}{'...' if len(resp) > 100 else ''}"
            for user, resp in entry["history"]
        )
        
        # 使用模板生成卡片
        card = RECENT_CARD_TEMPLATE.format(
            image=entry["image"],
            format_name=entry["format"],
            style_name=entry["style"],
            time=entry["timestamp"],
            prompt=entry["prompt"][:50] + ("..." if len(entry["prompt"]) > 50 else ""),
            history=history_html,
        )
        cards.append(card)
    
    return f"<div class='recent-grid'>{''.join(cards)}</div>"


def handle_image_upload(image: Any) -> Tuple[
    Dict[str, Any],  # style_selector更新
    str,             # style_hint
    str,             # tone_chip
    str,             # scene_chip
    str,             # mood_chip
    str,             # recommend_chip
]:
    """
    处理图片上传事件
    
    当用户上传图片时：
    1. 分析图片特征
    2. 推荐合适的创作风格
    3. 更新UI显示
    
    Args:
        image: 上传的图片数组
        
    Returns:
        多个UI组件的更新值
    """
    if image is None:
        # 图片为空时返回默认状态
        return (
            gr.update(value=DEFAULT_STYLE),
            style_prompt_preview(DEFAULT_STYLE),
            "🍑 色调：<strong>等待上传</strong>",
            "🏞️ 场景：上传图片以分析场景",
            "💫 情感：生成后将展示情绪风格",
            "⭐ AI 推荐风格：<strong>婉约抒情风</strong>",
        )
    
    # 转换为PIL图像并分析
    image_pil = Image.fromarray(image).convert("RGB")
    profile = analyze_image_profile(image_pil)
    
    # 格式化分析结果
    tone_text = f"🍑 色调：<strong>{profile['tone']}</strong>"
    scene_text = f"🏞️ 场景：{profile['scene']}"
    mood_text = f"💫 情感：{profile['mood']}"
    recommend_text = f"⭐ AI 推荐风格：<strong>{profile['style']}</strong>"
    
    return (
        gr.update(value=profile["style"]),
        style_prompt_preview(profile["style"]),
        tone_text,
        scene_text,
        mood_text,
        recommend_text,
    )


def chat_with_image(
    image: Any,
    format_choice: str,
    style_choice: str,
    user_instruction: str,
    max_new_tokens: int,
    top_p: float,
    temperature: float,
    history: ChatHistory | None,
    recent_creations: List[Dict[str, Any]] | None,
    model_manager,  # ModelManager实例
) -> Tuple[
    ChatHistory,                    # chatbot
    Dict[str, Any],                 # prompt_box (清空)
    ChatHistory,                    # history_state
    str,                            # poem_output
    Dict[str, Any],                 # suggestion_group (显示)
    List[Dict[str, Any]],          # recent_state
    str,                            # recent_panel (HTML)
]:
    """
    执行诗词生成并更新界面
    
    Args:
        image: 上传的图片
        format_choice: 诗词格式
        style_choice: 创作风格
        user_instruction: 用户提示
        max_new_tokens: 最大生成token数
        top_p: Top-p参数
        temperature: 温度参数
        history: 对话历史
        recent_creations: 最近创作记录
        model_manager: 模型管理器实例
        
    Returns:
        更新后的各个UI组件状态
    """
    # 验证输入
    if image is None:
        raise gr.Error("请先上传图片，再开始创作对话。")
    
    # 初始化状态
    history = history or []
    recent_creations = recent_creations or []
    
    # 预处理图像
    image_pil = Image.fromarray(image).convert("RGB")
    
    # 构建消息
    from src.utils.prompt_builder import build_messages
    messages = build_messages(
        image_pil,
        format_choice,
        style_choice,
        user_instruction,
        history
    )
    
    try:
        # 调用模型生成
        generated_text = model_manager.generate(
            messages=messages,
            image=image_pil,
            max_new_tokens=max_new_tokens,
            top_p=top_p,
            temperature=temperature,
        )
    except RuntimeError as exc:
        raise gr.Error(str(exc)) from exc
    
    # 更新历史记录
    user_record = user_instruction.strip() or "（未额外输入提示，使用默认风格创作）"
    updated_history = history + [(user_record, generated_text)]
    
    # 创建新的创作记录
    recent_entry = {
        "format": format_choice,
        "style": style_choice,
        "prompt": user_record,
        "history": updated_history[-10:],  # 只保存最近10轮对话
        "image": encode_image_to_data_uri(image_pil),
        "timestamp": datetime.now().strftime("%H:%M:%S"),
    }
    
    # 更新最近创作列表
    updated_recent = [recent_entry] + recent_creations
    updated_recent = updated_recent[:MAX_RECENT_ENTRIES]
    
    return (
        updated_history,           # 更新对话框
        {"value": ""},            # 清空输入框
        updated_history,           # 更新历史状态
        generated_text,            # 更新诗词输出
        gr.update(visible=True),   # 显示优化建议
        updated_recent,            # 更新创作记录
        render_recent_creations(updated_recent),  # 渲染创作记录
    )


def reset_conversation(
    recent_creations: List[Dict[str, Any]] | None
) -> Tuple[
    ChatHistory,
    Dict[str, Any],
    ChatHistory,
    str,
    Dict[str, Any],
    List[Dict[str, Any]],
    str,
]:
    """
    重置对话状态
    
    清空对话历史和输出，但保留最近创作记录
    
    Args:
        recent_creations: 最近创作记录
        
    Returns:
        重置后的各个UI组件状态
    """
    entries = recent_creations or []
    return (
        [],                         # 清空对话框
        {"value": ""},             # 清空输入框
        [],                         # 清空历史
        "",                         # 清空输出
        gr.update(visible=False),   # 隐藏建议
        entries,                    # 保留创作记录
        render_recent_creations(entries),
    )


def create_hero_section() -> gr.HTML:
    """创建Hero区域"""
    return gr.HTML(HERO_HTML_TEMPLATE)


def create_footer_section() -> gr.HTML:
    """创建页脚区域"""
    footer_html = FOOTER_HTML_TEMPLATE.format(
        author=APP_AUTHOR,
        course=APP_COURSE,
        version=APP_VERSION,
    )
    return gr.HTML(footer_html)