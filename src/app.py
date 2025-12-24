"""
主应用模块 - Application
构建Gradio Web应用界面
"""
import functools
import gradio as gr

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from config.config import (
    APP_TITLE,
    DEFAULT_FORMAT,
    DEFAULT_STYLE,
    DEFAULT_MAX_TOKENS,
    DEFAULT_TOP_P,
    DEFAULT_TEMPERATURE,
    IMAGE_UPLOAD_HEIGHT,
    CHATBOT_HEIGHT,
    POEM_OUTPUT_LINES,
    FOLLOW_UP_SUGGESTIONS,
)
from src.constants.templates import FORMAT_GUIDE, STYLE_GUIDE
from src.ui.styles import CUSTOM_CSS
from src.ui.components import (
    create_hero_section,
    create_footer_section,
    handle_image_upload,
    chat_with_image,
    reset_conversation,
    render_recent_creations,
)
from src.utils.prompt_builder import (
    format_prompt_preview,
    style_prompt_preview,
    apply_suggestion,
)
from src.models.model_manager import get_model_manager


def create_gradio_app() -> gr.Blocks:
    """
    创建Gradio应用界面
    
    构建完整的Web界面，包括：
    - 图片上传与分析
    - 格式和风格选择
    - 多轮对话
    - 诗词生成与优化
    - 创作历史记录
    
    Returns:
        Gradio Blocks应用实例
    """
    # 获取模型管理器
    model_manager = get_model_manager()
    
    with gr.Blocks(
        title=APP_TITLE,
        theme=gr.themes.Soft(),
        css=CUSTOM_CSS
    ) as demo:
        
        create_hero_section()
        
        with gr.Row(elem_classes="page-layout"):
            
            with gr.Column():
                
                with gr.Group(elem_classes="panel-card"):
                    with gr.Row():
                        # 图片上传区
                        with gr.Column(scale=7, elem_classes="image-frame"):
                            image_input = gr.Image(
                                type="numpy",
                                label=None,
                                height=IMAGE_UPLOAD_HEIGHT,
                                show_download_button=False,
                            )
                        
                        # AI分析显示区
                        with gr.Column(scale=5):
                            gr.Markdown(
                                "AI 图片分析",
                                elem_classes="analysis-heading"
                            )
                            analysis_stack = gr.Column(elem_classes="analysis-stack")
                            with analysis_stack:
                                tone_chip = gr.Markdown(
                                    "🍑 色调：<strong>等待上传</strong>",
                                    elem_classes="analysis-pill tone-pill"
                                )
                                scene_chip = gr.Markdown(
                                    "🏞️ 场景：上传图片以分析场景",
                                    elem_classes="analysis-pill scene-pill"
                                )
                                mood_chip = gr.Markdown(
                                    "💫 情感：生成后将展示情绪风格",
                                    elem_classes="analysis-pill mood-pill"
                                )
                                recommend_chip = gr.Markdown(
                                    "⭐ AI 推荐风格：<strong>婉约抒情风</strong>",
                                    elem_classes="analysis-pill recommend-pill"
                                )
                
                with gr.Group(elem_classes="panel-card"):
                    gr.Markdown("选择诗词风格", elem_classes="section-title")
                    gr.Markdown(
                        "AI 会根据图片辅助推荐，可继续微调。",
                        elem_classes="section-subtitle"
                    )
                    style_selector = gr.Radio(
                        choices=list(STYLE_GUIDE.keys()),
                        value=DEFAULT_STYLE,
                        label=None,
                        elem_classes="card-radio",
                    )
                    style_hint = gr.Markdown(
                        style_prompt_preview(DEFAULT_STYLE),
                        elem_classes="card-hint"
                    )
                
                with gr.Group(elem_classes="panel-card"):
                    gr.Markdown("选择诗词结构", elem_classes="section-title")
                    gr.Markdown(
                        "结合使用场景选择篇幅与节奏。",
                        elem_classes="section-subtitle"
                    )
                    format_selector = gr.Radio(
                        choices=list(FORMAT_GUIDE.keys()),
                        value=DEFAULT_FORMAT,
                        label=None,
                        elem_classes="card-radio",
                    )
                    format_hint = gr.Markdown(
                        format_prompt_preview(DEFAULT_FORMAT),
                        elem_classes="card-hint"
                    )
                
                with gr.Group(elem_classes="panel-card"):
                    gr.Markdown("补充灵感", elem_classes="section-title")
                    prompt_box = gr.Textbox(
                        lines=2,
                        label="额外灵感提示（可留空）",
                        placeholder="示例：突出秋景意象，加入离别情绪",
                    )
                    gr.Markdown(
                        """
                        **输入建议**
                        - 可补充关键意象、情绪或典故提示。
                        - 留空即按推荐风格自动创作。
                        """
                    )
            
            with gr.Column():
                

                with gr.Group(elem_classes="panel-card output-card"):
                    chatbot = gr.Chatbot(
                        label="多轮对话 · 诗心合创",
                        height=CHATBOT_HEIGHT,
                        bubble_full_width=False,
                    )
                    poem_output = gr.Textbox(
                        label="可复制分享的诗意文案",
                        lines=POEM_OUTPUT_LINES,
                        show_copy_button=True,
                        elem_classes="poem-output",
                    )
                    

                    suggestion_group = gr.Group(
                        visible=False,
                        elem_classes="suggestion-box"
                    )
                    with suggestion_group:
                        gr.Markdown(
                            "💡 **调整提示**：若想修改初次创作，可参考下列方向补充指令。"
                        )

                        for idx in range(0, len(FOLLOW_UP_SUGGESTIONS), 3):
                            with gr.Row():
                                for label, snippet in FOLLOW_UP_SUGGESTIONS[idx : idx + 3]:
                                    btn = gr.Button(label, size="sm")
                                    btn.click(
                                        functools.partial(
                                            apply_suggestion,
                                            snippet=snippet
                                        ),
                                        inputs=prompt_box,
                                        outputs=prompt_box,
                                    )
                    
                    # --- 操作按钮 ---
                    with gr.Row():
                        submit_btn = gr.Button(
                            "✨ 发送并创作",
                            variant="primary"
                        )
                        clear_btn = gr.Button(
                            "🧹 清除对话",
                            variant="secondary"
                        )
                    
                    gr.Markdown(
                        """
                        **使用与分享建议**
                        - 上传图片 + 选择格式/风格，即可生成专属诗意文案，可多轮微调。
                        - 将文案复制到朋友圈/小红书时，可额外附上一句高光总结句。
                        - 若需经典诗句化用，可在灵感提示中补充意象或作者，模型自动融合。
                        """
                    )
                
                # --- 最近创作 ---
                with gr.Group(elem_classes="panel-card"):
                    gr.Markdown("✨ 最近创作", elem_classes="section-title")
                    recent_panel = gr.Markdown(
                        "<div class='recent-empty'>暂无创作记录。</div>"
                    )

        history_state = gr.State([])  # 对话历史
        recent_state = gr.State([])   # 创作记录
        max_tokens_state = gr.State(DEFAULT_MAX_TOKENS)
        top_p_state = gr.State(DEFAULT_TOP_P)
        temperature_state = gr.State(DEFAULT_TEMPERATURE)
        

        
        # 提交按钮 - 生成诗词
        submit_btn.click(
            fn=lambda *args: chat_with_image(*args, model_manager),
            inputs=[
                image_input,
                format_selector,
                style_selector,
                prompt_box,
                max_tokens_state,
                top_p_state,
                temperature_state,
                history_state,
                recent_state,
            ],
            outputs=[
                chatbot,
                prompt_box,
                history_state,
                poem_output,
                suggestion_group,
                recent_state,
                recent_panel,
            ],
        )
        
        # 清除按钮 - 重置对话
        clear_btn.click(
            fn=reset_conversation,
            inputs=[recent_state],
            outputs=[
                chatbot,
                prompt_box,
                history_state,
                poem_output,
                suggestion_group,
                recent_state,
                recent_panel,
            ],
        )
        
        # 格式选择变化 - 更新提示
        format_selector.change(
            fn=lambda choice: format_prompt_preview(choice),
            inputs=format_selector,
            outputs=format_hint,
        )
        
        # 风格选择变化 - 更新提示
        style_selector.change(
            fn=lambda choice: style_prompt_preview(choice),
            inputs=style_selector,
            outputs=style_hint,
        )
        
        # 图片上传 - 分析并推荐
        image_input.change(
            fn=handle_image_upload,
            inputs=image_input,
            outputs=[
                style_selector,
                style_hint,
                tone_chip,
                scene_chip,
                mood_chip,
                recommend_chip,
            ],
        )
        
        create_footer_section()
    
    return demo