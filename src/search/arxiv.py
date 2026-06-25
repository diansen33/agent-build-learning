"""arXiv API 客户端。

arXiv 提供 Atom feed 接口：
    http://export.arxiv.org/api/query?search_query=all:<q>&max_results=N

返回值为标准 XML（Atom 命名空间），这里用标准库 xml.etree 解析为
标准化的论文 dict 列表，供上层（reader / summarizer / cli）复用。
"""
import xml.etree.ElementTree as ET

import httpx

from config.settings import settings
from src.utils.text import clean_text

# Atom 命名空间
_ATOM = "{http://www.w3.org/2005/Atom}"
# arXiv 扩展命名空间（primary_category 等用）
_ARXIV = "{http://arxiv.org/schemas/atom}"


def search_arxiv(query: str, max_results: int | None = None) -> list[dict]:
    """调用 arXiv API 搜索论文。

    Args:
        query: 检索关键词（会作为 all: 字段查询标题/摘要/作者等）。
        max_results: 返回数量上限，缺省取 settings.arxiv_max_results。

    Returns:
        标准化论文 dict 列表，每项含：
        id / title / authors / abstract / published / updated /
        pdf_url / primary_category / url。
    """
    if max_results is None:
        max_results = settings.arxiv_max_results

    params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": max_results,
        "sortBy": "relevance",
        "sortOrder": "descending",
    }
    resp = httpx.get(
        settings.arxiv_api_url,
        params=params,
        timeout=settings.arxiv_timeout,
        follow_redirects=True,
    )
    resp.raise_for_status()
    return _parse_atom(resp.text)


def _parse_atom(xml_text: str) -> list[dict]:
    """解析 arXiv Atom feed 为标准化论文列表。"""
    root = ET.fromstring(xml_text)
    papers: list[dict] = []
    for entry in root.findall(f"{_ATOM}entry"):
        arxiv_id = _text(entry, "id")
        papers.append(
            {
                "id": arxiv_id,
                "title": clean_text(_text(entry, "title")),
                "authors": [
                    clean_text(_text(a, "name"))
                    for a in entry.findall(f"{_ATOM}author")
                ],
                "abstract": clean_text(_text(entry, "summary")),
                "published": _text(entry, "published"),
                "updated": _text(entry, "updated"),
                "pdf_url": _link(entry, "pdf") or arxiv_id.replace("/abs/", "/pdf/"),
                "primary_category": _attr(entry, f"{_ARXIV}primary_category", "term"),
                "url": arxiv_id,
            }
        )
    return papers


# ---------- XML 小工具 ----------


def _text(parent: ET.Element, tag: str) -> str:
    """取某个子元素的文本，找不到返回空串。"""
    el = parent.find(f"{_ATOM}{tag}")
    return (el.text or "").strip() if el is not None else ""


def _link(parent: ET.Element, title: str) -> str:
    """取 <link title="..."> 的 href。"""
    for link in parent.findall(f"{_ATOM}link"):
        if link.get("title") == title:
            return link.get("href", "")
    return ""


def _attr(parent: ET.Element, tag: str, attr: str) -> str:
    """取某个子元素的属性值。tag 须含命名空间前缀。"""
    el = parent.find(tag)
    return el.get(attr, "") if el is not None else ""
