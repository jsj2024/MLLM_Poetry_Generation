"""
Prompt构建模块 - Prompt Builder
负责构建多模态对话消息和系统提示词
"""
from typing import List, Dict, Any
from PIL import Image

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from src.constants.templates import FORMAT_GUIDE, STYLE_GUIDE, SYSTEM_PROMPT_TEMPLATE

# 定义类型别名
ChatHistory = List[tuple[str, str]]


def build_messages(
    image: Image.Image,
    format_choice: str,
    style_choice: str,
    user_instruction: str,
    history: ChatHistory,
) -> List[Dict[str, Any]]:
    """
    构建多模态对话消息列表
    
    将历史对话、当前图像和用户需求组合成符合模型要求的消息格式。
    消息格式遵循标准的对话模板：
    [
        {"role": "user", "content": [...]},
        {"role": "assistant", "content": [...]},
        ...
    ]
    
    Args:
        image: PIL图像对象
        format_choice: 选择的诗词格式（如"五言绝句"）
        style_choice: 选择的创作风格（如"婉约抒情风"）
        user_instruction: 用户额外的灵感提示
        history: 历史对话记录，格式为 [(用户消息, AI回复), ...]
        
    Returns:
        符合模型输入格式的消息列表
        
    Example:
        >>> messages = build_messages(
        ...     image=img,
        ...     format_choice="五言绝句",
        ...     style_choice="婉约抒情风",
        ...     user_instruction="突出秋景",
        ...     history=[]
        ... )
        >>> print(messages[0]['role'])
        user
    """
    messages: List[Dict[str, Any]] = []
    
    # 添加历史对话轮次
    for user_turn, assistant_turn in history:
        messages.append({
            "role": "user",
            "content": [{"type": "text", "text": user_turn}]
        })
        if assistant_turn:
            messages.append({
                "role": "assistant",
                "content": [{"type": "text", "text": assistant_turn}]
            })
    
    # 获取格式和风格指导
    format_instruction = FORMAT_GUIDE.get(format_choice, {}).get("instruction", "")
    style_instruction = STYLE_GUIDE.get(style_choice, {}).get("instruction", "")
    
    # 构建系统提示词
    prompt_lines = [
        "你是一位具备古典文学素养的多模态文案创作者",
        "请仔细观察图片内容，抽取其中的关键意象、氛围与色彩。",
        f"作品格式要求：{format_instruction}",
        f"风格与语气参考：{style_instruction}",
        "务必让诗词意象与图片内容高度匹配，避免虚假描述。",
    ]
    
    # 添加用户自定义指令
    cleaned_instruction = user_instruction.strip()
    if cleaned_instruction:
        prompt_lines.append(f"附加灵感提示：{cleaned_instruction}")
    
    prompt_lines.append("最后，请按要求输出作品，不要额外解释。")
    
    # 添加当前轮次（包含图像和文本）
    messages.append({
        "role": "user",
        "content": [
            {"type": "image", "image": image},
            {"type": "text", "text": "\n".join(prompt_lines)},
        ],
    })
    
    return messages


def apply_suggestion(current_text: str, snippet: str) -> str:
    """
    将优化建议应用到当前文本
    
    如果当前文本非空，会在末尾添加分号再追加建议；
    否则直接返回建议文本。
    
    Args:
        current_text: 当前的提示文本
        snippet: 要添加的建议片段
        
    Returns:
        合并后的文本
        
    Example:
        >>> apply_suggestion("突出秋景", "加入离别情绪")
        '突出秋景；加入离别情绪'
        >>> apply_suggestion("", "加入离别情绪")
        '加入离别情绪'
    """
    current = (current_text or "").strip()
    
    if current:
        # 如果当前文本没有以标点结尾，添加分号
        if not current.endswith(("。", "！", "？", "；")):
            current += "；"
        return f"{current}{snippet}"
    
    return snippet


def format_prompt_preview(format_name: str) -> str:
    """
    生成格式选项的预览文本
    
    Args:
        format_name: 格式名称
        
    Returns:
        格式化的预览文本
        
    Example:
        >>> format_prompt_preview("五言绝句")
        '**五言绝句**：短篇幅（4×5字），节奏紧凑，适合突显单一意象。'
    """
    guide = FORMAT_GUIDE.get(format_name, {})
    description = guide.get('description', '无描述')
    return f"**{format_name}**：{description}"


def style_prompt_preview(style_name: str) -> str:
    """
    生成风格选项的预览文本
    
    Args:
        style_name: 风格名称
        
    Returns:
        格式化的预览文本
        
    Example:
        >>> style_prompt_preview("婉约抒情风")
        '**婉约抒情风**：柔美细腻，适合江南、花海、月夜等浪漫画面。'
    """
    guide = STYLE_GUIDE.get(style_name, {})
    description = guide.get('description', '无描述')
    return f"**{style_name}**：{description}"


def validate_inputs(
    format_choice: str,
    style_choice: str,
) -> tuple[bool, str]:
    """
    验证用户输入是否有效
    
    Args:
        format_choice: 格式选择
        style_choice: 风格选择
        
    Returns:
        (是否有效, 错误信息)
        
    Example:
        >>> validate_inputs("五言绝句", "婉约抒情风")
        (True, '')
        >>> validate_inputs("不存在的格式", "婉约抒情风")
        (False, '无效的格式选择')
    """
    if format_choice not in FORMAT_GUIDE:
        return False, "无效的格式选择"
    
    if style_choice not in STYLE_GUIDE:
        return False, "无效的风格选择"
    
    return True, ""


def get_format_metadata(format_name: str) -> Dict[str, Any]:
    return FORMAT_GUIDE.get(format_name, {})


def get_style_metadata(style_name: str) -> Dict[str, Any]:
    return STYLE_GUIDE.get(style_name, {})