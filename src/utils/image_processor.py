"""
图像处理模块 - Image Processor
负责图像分析、特征提取和编码转换
"""
import base64
import io
from typing import Dict
import numpy as np
from PIL import Image

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from config.config import (
    IMAGE_ANALYSIS_SIZE,
    IMAGE_SAVE_QUALITY,
    BRIGHTNESS_HIGH_THRESHOLD,
    BRIGHTNESS_LOW_THRESHOLD,
    SATURATION_HIGH_THRESHOLD,
    COLOR_DOMINANCE_THRESHOLD,
)


def encode_image_to_data_uri(image: Image.Image) -> str:
    """
    将PIL图像编码为Data URI格式
    
    Args:
        image: PIL图像对象
        
    Returns:
        Base64编码的Data URI字符串
        
    Example:
        >>> img = Image.open("test.jpg")
        >>> uri = encode_image_to_data_uri(img)
        >>> print(uri[:50])
        data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQ...
    """
    buf = io.BytesIO()
    image.save(buf, format="JPEG", quality=IMAGE_SAVE_QUALITY)
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")
    return f"data:image/jpeg;base64,{b64}"


def analyze_image_profile(image: Image.Image) -> Dict[str, str]:
    """
    基于颜色和亮度的启发式图像特征分析
    
    通过分析图像的RGB颜色分布、亮度和饱和度，推断：
    - 适合的创作风格
    - 色调特征
    - 场景类型
    - 情绪氛围
    
    Args:
        image: PIL图像对象
        
    Returns:
        包含分析结果的字典，包含以下键：
        - style: 推荐的创作风格
        - tone: 色调特征
        - scene: 场景类型
        - mood: 情绪氛围
        
    Example:
        >>> img = Image.open("sunset.jpg")
        >>> profile = analyze_image_profile(img)
        >>> print(profile)
        {
            'style': '豪放壮阔风',
            'tone': '明丽暖意',
            'scene': '霞染天际',
            'mood': '壮阔豪迈'
        }
    """
    resized = image.resize(IMAGE_ANALYSIS_SIZE)
    arr = np.asarray(resized).astype("float32") / 255.0

    mean_rgb = arr.mean(axis=(0, 1))  
    std_rgb = arr.std(axis=(0, 1))    

    brightness = float(arr.mean())
    saturation = float(
        np.sqrt(
            ((arr - arr.mean(axis=2, keepdims=True)) ** 2).mean(axis=2)
        ).mean()
    )
    
    red, green, blue = mean_rgb
    
    
    if green >= red * COLOR_DOMINANCE_THRESHOLD and green >= blue * 1.05:
        # 绿色主导 → 田园风格
        style = "田园归隐风"
    elif blue >= max(red, green) * COLOR_DOMINANCE_THRESHOLD or (
        brightness < 0.5 and blue >= red and blue >= green
    ):
        style = "禅意空灵风"
    elif red >= max(green, blue) * COLOR_DOMINANCE_THRESHOLD or (
        saturation > SATURATION_HIGH_THRESHOLD and red > blue
    ):
        style = "豪放壮阔风"
    elif brightness < BRIGHTNESS_LOW_THRESHOLD or (
        std_rgb.mean() > 0.18 and red > green and red > blue
    ):
        style = "边塞苍茫风"
    else:
        style = "婉约抒情风"
    
    
    if brightness > BRIGHTNESS_HIGH_THRESHOLD and red >= blue:
        tone = "明丽暖意"
    elif brightness < BRIGHTNESS_LOW_THRESHOLD:
        tone = "沉郁苍茫"
    elif blue >= red * COLOR_DOMINANCE_THRESHOLD:
        tone = "清冷高远"
    else:
        tone = "柔和恬淡"
    
    # 场景判断
    
    if green >= max(red, blue):
        scene = "田园乡野"
    elif blue >= max(red, green):
        scene = "山水景观"
    elif red >= max(green, blue):
        scene = "霞染天际"
    else:
        scene = "人文意境"
    
    
    if saturation > SATURATION_HIGH_THRESHOLD:
        mood = "壮阔豪迈"
    elif brightness < 0.42:
        mood = "沉静空灵"
    elif green > red and brightness > 0.5:
        mood = "闲适恬淡"
    else:
        mood = "温润抒情"
    
    return {
        "style": style,
        "tone": tone,
        "scene": scene,
        "mood": mood,
    }


def validate_image(image: Image.Image) -> bool:
    try:
        # 检查图像尺寸
        if image.width < 32 or image.height < 32:
            return False
        
        # 检查图像模式
        if image.mode not in ['RGB', 'RGBA', 'L']:
            return False
        
        return True
    except Exception:
        return False


def preprocess_image(image: Image.Image) -> Image.Image:
    if image.mode != 'RGB':
        return image.convert('RGB')
    return image


def get_image_info(image: Image.Image) -> Dict[str, any]:
    return {
        "width": image.width,
        "height": image.height,
        "mode": image.mode,
        "format": image.format,
        "size_kb": len(image.tobytes()) / 1024,
    }