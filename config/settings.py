"""全局配置：读取 .env，导出 settings 单例。"""
import os
from dataclasses import dataclass

from dotenv import load_dotenv

from pathlib import Path

# 加载项目根目录下的 .env（不存在则忽略）
load_dotenv(Path(__file__).resolve().parent.parent / ".env")


@dataclass
class Settings:
    """全局配置。真实 key 放 .env，不写死在代码里。"""

    # LLM
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    openai_base_url: str = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    # arXiv
    arxiv_max_results: int = int(os.getenv("ARXIV_MAX_RESULTS", "5"))
    arxiv_api_url: str = os.getenv("ARXIV_API_URL", "https://export.arxiv.org/api/query")
    arxiv_timeout: float = float(os.getenv("ARXIV_TIMEOUT", "30"))
    # arXiv 代理（国内网络下 export.arxiv.org 常超时，走 Clash 等本地代理）
    arxiv_proxy: str = os.getenv("ARXIV_PROXY", "")


settings = Settings()
