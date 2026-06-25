"""单篇论文总结器：输入论文 dict → 输出 PaperSummary。"""
from src.llm.client import chat_structured
from src.llm.schemas import PaperSummary
from config.prompts import SUMMARY_TEMPLATE, SYSTEM_PROMPT
from src.utils.text import truncate


def summarize_paper(paper: dict) -> PaperSummary:
    """对单篇论文生成结构化总结。

    Args:
        paper: search_arxiv 返回的标准化论文 dict。

    Returns:
        PaperSummary 结构化对象（problem / method / pros / cons）。
    """
    prompt = SUMMARY_TEMPLATE.format(
        title=paper.get("title", ""),
        authors="、".join(paper.get("authors", [])[:5]) or "未知",
        published=(paper.get("published", "未知") or "未知")[:10],
        category=paper.get("primary_category", "未知"),
        abstract=truncate(paper.get("abstract", ""), max_chars=3000),
    )
    summary = chat_structured(
        prompt, schema=PaperSummary, system=SYSTEM_PROMPT
    )
    # 用原始论文标题覆盖，避免模型自行改写标题
    summary.title = paper.get("title", summary.title)
    return summary
