"""研究助手 Agent 命令行入口。

Step 0：跑通骨架，无子命令时输出 "hello"。
后续阶段会在此添加 search / summarize / agent / pipeline 子命令。
"""
import typer

app = typer.Typer(help="研究助手 Agent CLI")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """无子命令时打印 hello，验证骨架可用。"""
    if ctx.invoked_subcommand is None:
        typer.echo("hello")


if __name__ == "__main__":
    app()
