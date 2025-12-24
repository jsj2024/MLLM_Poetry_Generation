"""
应用启动脚本 - Run Script
启动Gradio Web应用
"""
import os
import sys
from pathlib import Path

# 添加项目根目录到Python路径
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

from config.config import (
    SERVER_NAME,
    SERVER_PORT,
    SHARE,
    EXAMPLES_DIR,
)
from src.app import create_gradio_app
from src.models.model_manager import initialize_model


def ensure_directories():
    """确保必要的目录存在"""
    # 创建示例图片目录
    if not EXAMPLES_DIR.exists():
        EXAMPLES_DIR.mkdir(parents=True, exist_ok=True)
        print(f"✓ 已创建示例目录：{EXAMPLES_DIR}")
        print("  提示：可将示例图片放入此目录用于演示。")


def print_startup_banner():
    """打印启动横幅"""
    banner = """
    ╔════════════════════════════════════════════════════════════╗
    ║                                                            ║
    ║           📜 AI诗意镜 - 一拍即得，诗意天成                 ║
    ║                                                            ║
    ║        基于多模态大语言模型的智能古典诗词生成系统            ║
    ║                                                            ║
    ╚════════════════════════════════════════════════════════════╝
    """
    print(banner)


def main():
    """主函数"""
    try:
        # 打印启动横幅
        print_startup_banner()
        
        # 确保目录存在
        print("正在检查项目目录...")
        ensure_directories()
        print()
        
        # 初始化模型
        print("正在初始化模型...")
        print("=" * 80)
        model_manager = initialize_model()
        print()
        
        # 打印模型信息
        print("模型信息：")
        model_info = model_manager.get_model_info()
        for key, value in model_info.items():
            print(f"  - {key}: {value}")
        print("=" * 80)
        print()
        
        # 创建Gradio应用
        print("正在构建Web界面...")
        app = create_gradio_app()
        print("✓ Web界面构建完成")
        print()
        
        # 启动服务器
        print("=" * 80)
        print("正在启动服务器...")
        print(f"  - 服务器地址: {SERVER_NAME}")
        print(f"  - 端口: {SERVER_PORT}")
        print(f"  - 公共链接: {'已启用' if SHARE else '未启用'}")
        print("=" * 80)
        print()
        
        # 启动应用
        app.launch(
            server_name=SERVER_NAME,
            server_port=SERVER_PORT,
            share=SHARE,
        )
        
    except KeyboardInterrupt:
        print("\n")
        print("=" * 80)
        print("收到中断信号，正在关闭应用...")
        print("=" * 80)
        sys.exit(0)
        
    except Exception as e:
        print("\n")
        print("=" * 80)
        print(f"❌ 启动失败：{str(e)}")
        print("=" * 80)
        print("\n请检查：")
        print("  1. 模型路径是否正确（config/config.py中的MODEL_PATH）")
        print("  2. GPU是否可用（需要CUDA环境）")
        print("  3. 依赖包是否完整安装（pip install -r requirements.txt）")
        print()
        sys.exit(1)


if __name__ == "__main__":
    main()