"""文本清洗工具：摘要清洗、超长截断。"""
import re


def clean_text(text: str) -> str:
    """清洗文本：去除换行、多余空白、LaTeX 残留。

    arXiv 摘要里常见：
    - 多余换行与连续空格
    - 行内 LaTeX 公式 $...$
    - 首尾空白
    """
    if not text:
        return ""
    # 去除行内 LaTeX 公式 $...$
    text = re.sub(r"\$[^$]*\$", "", text)
    # 换行折叠为空格
    text = text.replace("\n", " ").replace("\r", " ")
    # 多个空白合并为单个
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def truncate(text: str, max_chars: int = 4000) -> str:
    """按字符数截断超长文本，尽量在词边界断开。"""
    if len(text) <= max_chars:
        return text
    cut = text[:max_chars].rsplit(" ", 1)[0]
    return cut + "…"
