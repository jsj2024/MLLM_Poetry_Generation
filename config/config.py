"""
配置文件 - Configuration File
存储系统全局配置参数
"""
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
EXAMPLES_DIR = PROJECT_ROOT / "examples"

MODEL_PATH = os.getenv("MODEL_PATH", "/home/jsj/llms/Qwen3-VL-8B-Instruct")

# 模型加载配置
DEVICE_MAP = "auto"  
MODEL_DTYPE = "bfloat16"  
TRUST_REMOTE_CODE = True  

DEFAULT_MAX_TOKENS = 512  
DEFAULT_TOP_P = 0.8  
DEFAULT_TEMPERATURE = 0.7  # 温度参数（控制随机性）

# 生成参数范围
MAX_TOKENS_MIN = 128
MAX_TOKENS_MAX = 1024
TOP_P_MIN = 0.1
TOP_P_MAX = 1.0
TEMPERATURE_MIN = 0.1
TEMPERATURE_MAX = 2.0

# UI配置

DEFAULT_FORMAT = "五言绝句"  
DEFAULT_STYLE = "婉约抒情风"  

# 界面参数
MAX_RECENT_ENTRIES = 6  
IMAGE_UPLOAD_HEIGHT = 360  
CHATBOT_HEIGHT = 360  
POEM_OUTPUT_LINES = 6  


SERVER_NAME = "0.0.0.0"  
SERVER_PORT = 7860  
SHARE = True  

# 图像分析参数
IMAGE_ANALYSIS_SIZE = (256, 256)  
IMAGE_SAVE_QUALITY = 85  # JPEG保存质量（1-100）

# 色调判断阈值
BRIGHTNESS_HIGH_THRESHOLD = 0.62  # 高亮度阈值
BRIGHTNESS_LOW_THRESHOLD = 0.38  # 低亮度阈值
SATURATION_HIGH_THRESHOLD = 0.28  # 高饱和度阈值
COLOR_DOMINANCE_THRESHOLD = 1.05  # 颜色主导阈值

# GPU性能优化
ENABLE_TF32 = True  # 启用TF32加速（适用于Ampere及以上架构）
CUDNN_BENCHMARK = True  # 启用CUDNN benchmark

MIN_GPU_COUNT = 1  


DEBUG_MODE = False  # 调试模式
VERBOSE_LOGGING = False  # 详细日志输出

FOLLOW_UP_SUGGESTIONS = [
    ("强化画面意象", "请丰富图中主要物象的质感与动态描写，让画面更鲜活。"),
    ("增强情绪张力", "请增强整首诗的情绪起伏，加入更具感染力的情感表达。"),
    ("融入文化典故", "请引入恰当的经典诗句或典故，让作品更具文化厚度。"),
    ("突出时间气息", "请点明画面的季节、时辰或天气变化，增强现场感。"),
    ("调整节奏结构", "请在诗句之间增加转折或对比,让节奏更富层次。"),
]

APP_TITLE = "AI诗意镜 - 一拍即得，诗意天成"
APP_DESCRIPTION = "基于多模态大语言模型的智能古典诗词生成系统"
APP_VERSION = "1.0.0"
APP_AUTHOR = "jsj 等人"
APP_COURSE = "软件工程实践"