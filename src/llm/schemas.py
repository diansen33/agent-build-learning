"""Pydantic 模型：LLM 结构化输出的 schema。"""
from pydantic import BaseModel, Field


class PaperSummary(BaseModel):
    """单篇论文的结构化总结。"""

    title: str = Field(description="论文标题")
    problem: str = Field(description="论文试图解决的问题")
    method: str = Field(description="使用的方法或技术路线")
    pros: str = Field(description="方法或结果的优点")
    cons: str = Field(description="方法或结果的局限或不足")
