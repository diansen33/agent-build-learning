"""研究助手 Agent 命令行入口。

Step 0：无子命令输出 "hello"。
Step 1：新增 `search <query>` 子命令，打印 arXiv 检索到的前 N 篇论文。
后续阶段会继续添加 summarize / agent / pipeline 子命令。
"""
import typer

app = typer.Typer(help="研究助手 Agent CLI")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """无子命令时打印 hello，验证骨架可用。"""
    if ctx.invoked_subcommand is None:
        typer.echo("hello")


@app.command()
def search(
    query: str = typer.Argument(..., help="检索关键词"),
    top: int = typer.Option(5, "--top", "-n", help="返回前 N 篇"),
) -> None:
    """搜索 arXiv 论文，打印前 N 篇标题与作者。"""
    from src.search.arxiv import search_arxiv

    papers = search_arxiv(query, max_results=top)
    if not papers:
        typer.echo("未找到相关论文。")
        return

    typer.echo(f"找到 {len(papers)} 篇论文：\n")
    for i, p in enumerate(papers, 1):
        authors = ", ".join(p["authors"][:3]) or "未知"
        typer.echo(f"{i}. {p['title']}")
        typer.echo(f"   作者: {authors}")
        typer.echo(f"   分类: {p['primary_category']}  发表: {_year(p['published'])}")
        typer.echo(f"   链接: {p['url']}\n")


def _year(iso: str) -> str:
    """从 ISO 时间串里取年份。"""
    return iso[:4] if iso else "未知"


if __name__ == "__main__":
    app()
