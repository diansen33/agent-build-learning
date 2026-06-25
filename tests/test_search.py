"""arXiv 检索单测：mock 一次 arXiv 响应，验证解析与清洗。"""
from src.search import arxiv


# 一份精简但要素齐全的 arXiv Atom feed
# - 标题含 LaTeX $x^2$
# - 摘要含换行与 LaTeX $E=mc^2$
# - 两个作者、pdf link、primary_category
SAMPLE_FEED = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>http://arxiv.org/abs/1234.5678v1</id>
    <updated>2023-02-01T00:00:00Z</updated>
    <published>2023-01-01T00:00:00Z</published>
    <title>Sample Title $x^2$</title>
    <summary>Line one\nLine two with $E=mc^2$ formula.</summary>
    <author><name>Author One</name></author>
    <author><name>Author Two</name></author>
    <link href="http://arxiv.org/pdf/1234.5678v1" title="pdf" rel="related"/>
    <arxiv:primary_category term="cs.AI"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/9876.5432v1</id>
    <updated>2023-03-01T00:00:00Z</updated>
    <published>2023-02-15T00:00:00Z</published>
    <title>Second Paper</title>
    <summary>Clean abstract text.</summary>
    <author><name>Solo Author</name></author>
    <link href="http://arxiv.org/pdf/9876.5432v1" title="pdf" rel="related"/>
    <arxiv:primary_category term="cs.CL"/>
  </entry>
</feed>"""


class _FakeResponse:
    def __init__(self, text: str):
        self.text = text

    def raise_for_status(self) -> None:
        pass


def test_search_arxiv_parses_and_cleans(monkeypatch):
    """mock httpx.get 返回固定 feed，验证字段抽取与文本清洗。"""

    def fake_get(url, params=None, timeout=None, **kwargs):
        return _FakeResponse(SAMPLE_FEED)

    monkeypatch.setattr(arxiv.httpx, "get", fake_get)

    papers = arxiv.search_arxiv("dummy query", max_results=2)

    assert len(papers) == 2

    first = papers[0]
    # 基本字段
    assert first["id"] == "http://arxiv.org/abs/1234.5678v1"
    assert first["url"] == "http://arxiv.org/abs/1234.5678v1"
    assert first["published"] == "2023-01-01T00:00:00Z"
    assert first["pdf_url"] == "http://arxiv.org/pdf/1234.5678v1"
    assert first["primary_category"] == "cs.AI"
    # 作者
    assert first["authors"] == ["Author One", "Author Two"]
    # 清洗：标题去除 LaTeX
    assert first["title"] == "Sample Title"
    # 清洗：摘要换行折叠为空格、LaTeX 去除
    assert first["abstract"] == "Line one Line two with formula."
    # 第二篇
    assert papers[1]["title"] == "Second Paper"
    assert papers[1]["authors"] == ["Solo Author"]
    assert papers[1]["primary_category"] == "cs.CL"


def test_parse_atom_handles_empty_feed():
    """空 feed 应返回空列表，不报错。"""
    empty_feed = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<feed xmlns="http://www.w3.org/2005/Atom"></feed>'
    )
    assert arxiv._parse_atom(empty_feed) == []
