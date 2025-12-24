"""
常量模板 - Templates and Constants
定义诗词格式、风格等常量模板
"""
from typing import Dict, List, Tuple

# 诗词格式模板 
FORMAT_GUIDE: Dict[str, Dict[str, str]] = {
    "五言绝句": {
        "instruction": (
            "创作1首五言绝句：共4句，每句5字；押平声韵（平水韵/新韵二选一，不混押）；"
            "平仄符合基本格律（忌孤平、三平尾）；用词通俗无生僻字；"
            "必须紧扣图片核心元素，不脱离画面主题。"
        ),
        "description": "短篇幅（4×5字），节奏紧凑，适合突显单一意象。",
        "total_chars": 20,
        "lines": 4,
        "chars_per_line": 5,
    },
    "七言绝句": {
        "instruction": (
            "创作1首七言绝句：共4句，每句7字；押平声韵（平水韵/新韵统一，不换韵）；"
            "平仄符合常见格律（如平起平收、仄起平收）；用词易懂无生僻字；"
            "需围绕图片画面创作，诗词与场景匹配。"
        ),
        "description": "短篇幅（4×7字），信息更饱满，适合情绪冲击型画面。",
        "total_chars": 28,
        "lines": 4,
        "chars_per_line": 7,
    },
    "五言律诗": {
        "instruction": (
            "创作1首五言律诗：共8句，每句5字；押平声韵（全程同一韵部，平水韵/新韵）；"
            "中间两联（3-4句、5-6句）需对仗（词性相对，可宽对）；"
            "平仄合规（句内交替、联间相粘）；用词通俗无生僻字；"
            "需完整呈现图片关键元素，逻辑连贯。"
        ),
        "description": "中篇幅（8×5字），层次分明，适合元素较多的画面。",
        "total_chars": 40,
        "lines": 8,
        "chars_per_line": 5,
    },
    "七言律诗": {
        "instruction": (
            "创作1首七言律诗：共8句，每句7字；押平声韵（平水韵/新韵统一，不换韵）；"
            "中间两联（3-4句、5-6句）需工整对仗；"
            "平仄合规（忌孤平、三平尾，联间相粘）；用词浅显无生僻字；"
            "需结合图片画面展开，意境与场景一致。"
        ),
        "description": "中长篇幅（8×7字），叙事充足，适合大场景或旅记。",
        "total_chars": 56,
        "lines": 8,
        "chars_per_line": 7,
    },
    "词（自动匹配词牌）": {
        "instruction": (
            "创作 1 首词：按所选风格匹配以下词牌（3 选 1，优先适配画面氛围），"
            "严格遵循所选词牌的字数、句数、韵脚（平 / 仄韵）和基本格律；"
            "用词通俗无生僻字；必须紧扣图片核心元素，不脱离画面主题。"
            "1. 婉约抒情风：《雨霖铃》《点绛唇》《一剪梅》；"
            "2. 豪放壮阔风：《满江红》《破阵子》《贺新郎》；"
            "3. 田园归隐风：《浣溪沙》《采桑子》《行香子》；"
            "4. 禅意空灵风：《捣练子》《相见欢》《阮郎归》；"
            "5. 边塞苍茫风：《渔家傲》《凉州词》《诉衷情令》。"
        ),
        "description": "词体（44-100+字），韵律丰富，适合情绪层次复杂的作品。",
        "total_chars": "44-100+",
        "lines": "变长",
        "chars_per_line": "变长",
    },
}

# 创作风格模板 
STYLE_GUIDE: Dict[str, Dict[str, str]] = {
    "婉约抒情风": {
        "instruction": (
            "风格为婉约抒情：语言细腻、情感含蓄，忌直白豪放；"
            "气质柔美雅致，传递温和/内敛情绪；"
            "贴合图片画面氛围，与柔美类场景自然融合；"
            "避免雄浑、苍凉表述。"
        ),
        "description": "柔美细腻，适合江南、花海、月夜等浪漫画面。",
        "keywords": ["细腻", "含蓄", "柔美", "温和"],
        "suitable_scenes": ["江南水乡", "花海", "月夜", "春景"],
    },
    "豪放壮阔风": {
        "instruction": (
            "风格为豪放壮阔：语言雄浑有力、气势大气，忌柔媚细腻；"
            "气质开阔震撼，传递对自然伟力的赞叹；"
            "贴合图片画面氛围，与宏大类场景匹配；"
            "避免含蓄、柔弱表述。"
        ),
        "description": "气势宏伟，适合山河、海天、星空等震撼景象。",
        "keywords": ["雄浑", "大气", "震撼", "伟岸"],
        "suitable_scenes": ["高山", "大海", "星空", "瀑布"],
    },
    "田园归隐风": {
        "instruction": (
            "风格为田园归隐：语言质朴自然、通俗平实，忌华丽辞藻；"
            "气质宁静闲适，传递淡泊/平和态度；"
            "贴合图片画面氛围，与生活化场景一致；"
            "避免宏大、激昂表述。"
        ),
        "description": "恬淡闲适，适合乡村、农舍、竹林等生活场景。",
        "keywords": ["质朴", "宁静", "闲适", "淡泊"],
        "suitable_scenes": ["乡村", "农舍", "竹林", "田园"],
    },
    "禅意空灵风": {
        "instruction": (
            "风格为禅意空灵：语言简练清淡、留白感强，忌复杂修辞；"
            "气质清幽静谧，传递平和/淡然哲思；"
            "贴合图片画面氛围，与清幽类场景契合；"
            "避免密集意象、浓烈情绪。"
        ),
        "description": "清幽淡然，适合古寺、薄雾、孤松等静谧氛围。",
        "keywords": ["简练", "清淡", "静谧", "淡然"],
        "suitable_scenes": ["古寺", "薄雾", "孤松", "山泉"],
    },
    "边塞苍茫风": {
        "instruction": (
            "风格为边塞苍茫：语言苍凉雄浑、刚劲有力，忌细腻柔美；"
            "气质辽阔悲壮，传递对旷野的感慨；"
            "贴合图片画面氛围，与苍茫类场景匹配；"
            "避免温婉、闲适表述。"
        ),
        "description": "苍凉壮烈，适合沙漠、雪山、戈壁等边塞画面。",
        "keywords": ["苍凉", "雄浑", "辽阔", "悲壮"],
        "suitable_scenes": ["沙漠", "雪山", "戈壁", "荒原"],
    },
}

# 优化建议模板 
FOLLOW_UP_SUGGESTIONS: List[Tuple[str, str]] = [
    ("强化画面意象", "请丰富图中主要物象的质感与动态描写，让画面更鲜活。"),
    ("增强情绪张力", "请增强整首诗的情绪起伏，加入更具感染力的情感表达。"),
    ("融入文化典故", "请引入恰当的经典诗句或典故，让作品更具文化厚度。"),
    ("突出时间气息", "请点明画面的季节、时辰或天气变化，增强现场感。"),
    ("调整节奏结构", "请在诗句之间增加转折或对比，让节奏更富层次。"),
]

# Prompt模板 
SYSTEM_PROMPT_TEMPLATE = """你是一位具备古典文学素养的多模态文案创作者，正在完成"AI人文通识课 hty"作业。
请仔细观察图片内容，抽取其中的关键意象、氛围与色彩。
作品格式要求：{format_instruction}
风格与语气参考：{style_instruction}
务必让诗词意象与图片内容高度匹配，避免虚假描述。
{user_instruction}
最后，请按要求输出作品，不要额外解释。"""

# 图像分析标签 
TONE_LABELS = {
    "明丽暖意": {"color": "#cc6f2b", "icon": "🍑"},
    "沉郁苍茫": {"color": "#5a5a5a", "icon": "🌫️"},
    "清冷高远": {"color": "#1d4ed8", "icon": "❄️"},
    "柔和恬淡": {"color": "#8b7355", "icon": "🍂"},
}

SCENE_LABELS = {
    "田园乡野": {"color": "#1f7a55", "icon": "🌾"},
    "山水景观": {"color": "#0ea5e9", "icon": "🏔️"},
    "霞染天际": {"color": "#dc2626", "icon": "🌅"},
    "人文意境": {"color": "#7c3aed", "icon": "🏛️"},
}

MOOD_LABELS = {
    "壮阔豪迈": {"color": "#b91c1c", "icon": "⚡"},
    "沉静空灵": {"color": "#6b7280", "icon": "🧘"},
    "闲适恬淡": {"color": "#059669", "icon": "☕"},
    "温润抒情": {"color": "#db2777", "icon": "💐"},
}

# HTML模板片段
HERO_HTML_TEMPLATE = """
<div class="hero">
  <h1>📜 AI诗意镜 - 一拍即得，诗意天成</h1>
  <p>✨ 上传美景图片，AI智能生成古典诗词 ✨</p>
  <p>支持五言绝句、七言绝句、律诗、词等多种格式，一拍即得，诗意天成。</p>
  <div class="badge-line">
    <span class="badge"><i class="ri-ai-line"></i> 图像理解 × 诗词生成</span>
    <span class="badge"><i class="ri-palette-line"></i> 格式风格双重可控</span>
    <span class="badge"><i class="ri-share-line"></i> 一键复制 · 快速分享</span>
  </div>
</div>
"""

FOOTER_HTML_TEMPLATE = """
<div class="footer">
  本项目由{author}创作 · 本地私有化部署保障素材安全<br>
  {course} | 版本 {version}
</div>
"""

RECENT_CARD_TEMPLATE = """
<div class="recent-card">
  <img src="{image}">
  <div class="recent-title">{format_name} · {style_name}</div>
  <div class="recent-meta">{time}</div>
  <div class="recent-meta">灵感：{prompt}</div>
  <div class="recent-history">{history}</div>
</div>
"""

RECENT_EMPTY_TEMPLATE = """
<div class='recent-empty'>暂无创作记录，快来上传图片吧～</div>
"""

# 分析标签HTML模板 
ANALYSIS_PILL_TEMPLATE = """
<div class="analysis-pill {css_class}">
  <span>{icon}</span>
  <span><strong>{label}：</strong>{value}</span>
</div>
"""