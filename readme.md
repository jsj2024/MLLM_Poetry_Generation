# AI诗意镜 - AI Poetry Mirror

<div align="center">

📜 **一拍即得，诗意天成**

基于多模态大语言模型的智能古典诗词生成系统

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Gradio](https://img.shields.io/badge/Gradio-4.0+-orange.svg)](https://gradio.app/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)

</div>

## 📖 项目简介

AI诗意镜是一个基于 Qwen3-VL-8B-Instruct 多模态视觉语言模型的智能诗词创作系统。用户只需上传一张图片，系统就能智能分析图像特征（色调、场景、情感等），并根据用户选择的诗词格式和风格，自动生成符合古典诗词格律的作品。

### ✨ 核心特性

- 🎨 **智能图像分析**：自动识别图片的色调、场景类型和情感氛围
- 📝 **多种诗词格式**：支持五言/七言绝句、五言/七言律诗、词（自动匹配词牌）
- 🎭 **五大创作风格**：婉约抒情、豪放壮阔、田园归隐、禅意空灵、边塞苍茫
- 💬 **多轮对话优化**：支持连续对话，逐步优化诗词效果
- 🔄 **实时预览与复制**：一键复制生成的诗词文案
- 📚 **创作历史记录**：自动保存最近的创作记录

## 🏗️ 项目架构

```
mllm-for-poetry-generation/
├── README.md                 # 项目说明文档
├── requirements.txt          # Python依赖包列表
├── .gitignore               # Git忽略文件配置
├── run.py                   # 应用启动入口
├── config/                  # 配置文件目录
│   └── config.py           # 系统配置参数
├── src/                     # 源代码目录
│   ├── __init__.py
│   ├── app.py              # Gradio应用主逻辑
│   ├── models/             # 模型管理模块
│   │   ├── __init__.py
│   │   └── model_manager.py  # 模型加载与推理
│   ├── utils/              # 工具函数模块
│   │   ├── __init__.py
│   │   ├── image_processor.py  # 图像处理与分析
│   │   └── prompt_builder.py   # Prompt构建工具
│   ├── ui/                 # UI界面模块
│   │   ├── __init__.py
│   │   ├── components.py   # Gradio组件定义
│   │   └── styles.py       # CSS样式定义
│   └── constants/          # 常量定义模块
│       ├── __init__.py
│       └── templates.py    # 诗词格式与风格模板
└── examples/               # 示例图片目录
    └── .gitkeep
```

## 🚀 快速开始

### 环境要求

- **Python**: 3.8+
- **CUDA**: 11.8+ (推荐)
- **GPU**: NVIDIA GPU with 16GB+ VRAM (推荐使用 A100/H800 等)
- **操作系统**: Linux (推荐 Ubuntu 20.04+)

### 安装步骤

1. **克隆项目**

```bash
git clone https://github.com/your-username/ai-poetry-mirror.git
cd ai-poetry-mirror
```

2. **创建虚拟环境**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或 venv\Scripts\activate  # Windows
```

3. **安装依赖**

```bash
pip install -r requirements.txt
```

4. **下载模型**

下载 [Qwen3-VL-8B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct) 模型到本地，并在 `config/config.py` 中配置模型路径：

```python
MODEL_PATH = "/path/to/Qwen3-VL-8B-Instruct"
```

5. **启动应用**

```bash
python run.py
```

应用将在本地启动，默认访问地址：`http://localhost:7860`

## 📚 使用指南

### 基本使用流程

1. **上传图片**：点击上传区域，选择一张风景或意境图片
2. **智能分析**：系统自动分析图片特征，推荐适合的创作风格
3. **选择格式**：根据需求选择诗词格式（绝句、律诗或词）
4. **调整风格**：可微调AI推荐的风格，或自行选择
5. **补充灵感**（可选）：输入额外的意象、情绪或典故提示
6. **生成诗词**：点击"发送并创作"，等待AI生成作品
7. **多轮优化**：若不满意，可使用调整建议继续优化

### 诗词格式说明

| 格式 | 句数 | 每句字数 | 总字数 | 特点 |
|------|------|----------|--------|------|
| 五言绝句 | 4 | 5 | 20 | 简洁精炼，适合单一意象 |
| 七言绝句 | 4 | 7 | 28 | 信息饱满，适合情绪冲击 |
| 五言律诗 | 8 | 5 | 40 | 层次分明，适合复杂场景 |
| 七言律诗 | 8 | 7 | 56 | 叙事充足，适合大场景 |
| 词 | 变长 | 变长 | 44-100+ | 韵律丰富，情绪层次复杂 |

### 创作风格特点

- **婉约抒情风**：柔美细腻，适合江南、花海、月夜等浪漫画面
- **豪放壮阔风**：气势宏伟，适合山河、海天、星空等震撼景象
- **田园归隐风**：恬淡闲适，适合乡村、农舍、竹林等生活场景
- **禅意空灵风**：清幽淡然，适合古寺、薄雾、孤松等静谧氛围
- **边塞苍茫风**：苍凉壮烈，适合沙漠、雪山、戈壁等边塞画面

## 🔧 配置说明

主要配置项位于 `config/config.py`：

```python
# 模型配置
MODEL_PATH = "/path/to/Qwen3-VL-8B-Instruct"  # 模型路径
DEVICE_MAP = "auto"                            # 设备映射策略

# 生成参数
DEFAULT_MAX_TOKENS = 512                       # 最大生成token数
DEFAULT_TOP_P = 0.8                           # Top-p采样参数
DEFAULT_TEMPERATURE = 0.7                     # 温度参数

# UI配置
DEFAULT_FORMAT = "五言绝句"                    # 默认诗词格式
DEFAULT_STYLE = "婉约抒情风"                   # 默认创作风格
MAX_RECENT_ENTRIES = 6                        # 最近创作记录数量

# 服务器配置
SERVER_NAME = "0.0.0.0"                       # 服务器地址
SERVER_PORT = 7860                            # 服务器端口
SHARE = True                                  # 是否生成公共链接
```

## 🎯 技术特点

### 1. 图像智能分析

基于颜色空间分析（HSV/RGB）实现启发式图像特征提取：
- **色调分析**：识别明丽暖意、沉郁苍茫、清冷高远、柔和恬淡
- **场景判断**：区分田园乡野、山水景观、霞染天际、人文意境
- **情绪推断**：判断壮阔豪迈、沉静空灵、闲适恬淡、温润抒情

### 2. 多轮对话优化

支持连续对话模式，用户可以：
- 追加意象描述要求
- 调整情感倾向
- 融入特定典故
- 修改节奏结构

### 3. 格律约束

严格遵循古典诗词格律规范：
- 押韵规则（平水韵/新韵）
- 平仄格律（避免孤平、三平尾）
- 对仗要求（律诗颔联、颈联）
- 词牌格式（自动匹配合适词牌）

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

### 开发流程

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 代码规范

- 遵循 PEP 8 Python代码规范
- 使用类型注解（Type Hints）
- 添加适当的文档字符串（Docstrings）
- 保持函数功能单一、职责清晰

## 📄 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 🙏 致谢

- **Qwen团队**：提供强大的多模态视觉语言模型
- **Gradio团队**：提供优雅的Web界面框架
- **南京大学**：提供学术研究支持

## 📮 联系方式

- **作者**：jsj 等人
- **课程**：软件工程实践
- **机构**：南京大学电子科学与工程学院

---

<div align="center">
Made with ❤️ for AI + 软件工程实践
</div>
