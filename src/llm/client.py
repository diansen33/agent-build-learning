"""LLM 客户"""LLM 客户端：封装 chat 与 structured output。

使用 OpenAI SDK，兼容任何 OpenAI 接口"""LLM 客户端：封装 chat 与 structured output。

使用 OpenAI SDK，兼容任何 OpenAI 接口格式的提供方（OpenAI 官方、
DeepSeek、通义千问、本地 Ollama 等），只需在 .env 中配置
OPENAI_BASE_URL 和 OPENAI_MODEL。
"""
from typing import TypeVar

from openai import OpenAI
from pydantic"""LLM 客户端：封装 chat 与 structured output。

使用 OpenAI SDK，兼容任何 OpenAI 接口格式的提供方（OpenAI 官方、
DeepSeek、通义千问、本地 Ollama 等），只需在 .env 中配置
OPENAI_BASE_URL 和 OPENAI_MODEL。
"""
from typing import TypeVar

from openai import OpenAI
from pydantic import BaseModel

from config.prompts import SYSTEM_PROM"""LLM 客户端：封装 chat 与 structured output。

使用 OpenAI SDK，兼容任何 OpenAI 接口格式的提供方（OpenAI 官方、
DeepSeek、通义千问、本地 Ollama 等），只需在 .env 中配置
OPENAI_BASE_URL 和 OPENAI_MODEL。
"""
from typing import TypeVar

from openai import OpenAI
from pydantic import BaseModel

from config.prompts import SYSTEM_PROMPT
from config.settings import settings

T = TypeVar("T", bound=BaseModel)


"""LLM 客户端：封装 chat 与 structured output。

使用 OpenAI SDK，兼容任何 OpenAI 接口格式的提供方（OpenAI 官方、
DeepSeek、通义千问、本地 Ollama 等），只需在 .env 中配置
OPENAI_BASE_URL 和 OPENAI_MODEL。
"""
from typing import TypeVar

from openai import OpenAI
from pydantic import BaseModel

from config.prompts import SYSTEM_PROMPT
from config.settings import settings

T = TypeVar("T", bound=BaseModel)


def _get_client() -> OpenAI:
"""LLM 客户端：封装 chat 与 structured output。

使用 OpenAI SDK，兼容任何 OpenAI 接口格式的提供方（OpenAI 官方、
DeepSeek、通义千问、本地 Ollama 等），只需在 .env 中配置
OPENAI_BASE_URL 和 OPENAI_MODEL。
"""
from typing import TypeVar

from openai import OpenAI
from pydantic import BaseModel

from config.prompts import SYSTEM_PROMPT
from config.settings import settings

T = TypeVar("T", bound=BaseModel)


def _get_client() -> OpenAI:
    """创建 OpenAI 客户端（懒加载，每次调用新建，简单可靠）。"""
    if not settings.openai_api_key:
        raise RuntimeError(
            "未配置 OPENAI_API"""LLM 客户端：封装 chat 与 structured output。

使用 OpenAI SDK，兼容任何 OpenAI 接口格式的提供方（OpenAI 官方、
DeepSeek、通义千问、本地 Ollama 等），只需在 .env 中配置
OPENAI_BASE_URL 和 OPENAI_MODEL。
"""
from typing import TypeVar

from openai import OpenAI
from pydantic import BaseModel

from config.prompts import SYSTEM_PROMPT
from config.settings import settings

T = TypeVar("T", bound=BaseModel)


def _get_client() -> OpenAI:
    """创建 OpenAI 客户端（懒加载，每次调用新建，简单可靠）。"""
    if not settings.openai_api_key:
        raise RuntimeError(
            "未配置 OPENAI_API_KEY，请在 .env 文件中设置。"
            "参考 .env.example。"
"""LLM 客户端：封装 chat 与 structured output。

使用 OpenAI SDK，兼容任何 OpenAI 接口格式的提供方（OpenAI 官方、
DeepSeek、通义千问、本地 Ollama 等），只需在 .env 中配置
OPENAI_BASE_URL 和 OPENAI_MODEL。
"""
from typing import TypeVar

from openai import OpenAI
from pydantic import BaseModel

from config.prompts import SYSTEM_PROMPT
from config.settings import settings

T = TypeVar("T", bound=BaseModel)


def _get_client() -> OpenAI:
    """创建 OpenAI 客户端（懒加载，每次调用新建，简单可靠）。"""
    if not settings.openai_api_key:
        raise RuntimeError(
            "未配置 OPENAI_API_KEY，请在 .env 文件中设置。"
            "参考 .env.example。"
        )
    return OpenAI(
        api_key=settings.openai_api_key,
        base_url=settings.open"""LLM 客户端：封装 chat 与 structured output。

使用 OpenAI SDK，兼容任何 OpenAI 接口格式的提供方（OpenAI 官方、
DeepSeek、通义千问、本地 Ollama 等），只需在 .env 中配置
OPENAI_BASE_URL 和 OPENAI_MODEL。
"""
from typing import TypeVar

from openai import OpenAI
from pydantic import BaseModel

from config.prompts import SYSTEM_PROMPT
from config.settings import settings

T = TypeVar("T", bound=BaseModel)


def _get_client() -> OpenAI:
    """创建 OpenAI 客户端（懒加载，每次调用新建，简单可靠）。"""
    if not settings.openai_api_key:
        raise RuntimeError(
            "未配置 OPENAI_API_KEY，请在 .env 文件中设置。"
            "参考 .env.example。"
        )
    return OpenAI(
        api_key=settings.openai_api_key,
        base_url=settings.openai_base_url,
    )


def chat(
    user_prompt: str,
    system_prompt: str"""LLM 客户端：封装 chat 与 structured output。

使用 OpenAI SDK，兼容任何 OpenAI 接口格式的提供方（OpenAI 官方、
DeepSeek、通义千问、本地 Ollama 等），只需在 .env 中配置
OPENAI_BASE_URL 和 OPENAI_MODEL。
"""
from typing import TypeVar

from openai import OpenAI
from pydantic import BaseModel

from config.prompts import SYSTEM_PROMPT
from config.settings import settings

T = TypeVar("T", bound=BaseModel)


def _get_client() -> OpenAI:
    """创建 OpenAI 客户端（懒加载，每次调用新建，简单可靠）。"""
    if not settings.openai_api_key:
        raise RuntimeError(
            "未配置 OPENAI_API_KEY，请在 .env 文件中设置。"
            "参考 .env.example。"
        )
    return OpenAI(
        api_key=settings.openai_api_key,
        base_url=settings.openai_base_url,
    )


def chat(
    user_prompt: str,
    system_prompt: str = SYSTEM_PROMPT,
    temperature: float = 0.3,
) -> str:
    """普通对话：返回模型文本回复。

"""LLM 客户端：封装 chat 与 structured output。

使用 OpenAI SDK，兼容任何 OpenAI 接口格式的提供方（OpenAI 官方、
DeepSeek、通义千问、本地 Ollama 等），只需在 .env 中配置
OPENAI_BASE_URL 和 OPENAI_MODEL。
"""
from typing import TypeVar

from openai import OpenAI
from pydantic import BaseModel

from config.prompts import SYSTEM_PROMPT
from config.settings import settings

T = TypeVar("T", bound=BaseModel)


def _get_client() -> OpenAI:
    """创建 OpenAI 客户端（懒加载，每次调用新建，简单可靠）。"""
    if not settings.openai_api_key:
        raise RuntimeError(
            "未配置 OPENAI_API_KEY，请在 .env 文件中设置。"
            "参考 .env.example。"
        )
    return OpenAI(
        api_key=settings.openai_api_key,
        base_url=settings.openai_base_url,
    )


def chat(
    user_prompt: str,
    system_prompt: str = SYSTEM_PROMPT,
    temperature: float = 0.3,
) -> str:
    """普通对话：返回模型文本回复。

    Args:
        user_prompt: 用户提示词。
        system_prompt: 系统提示词，"""LLM 客户端：封装 chat 与 structured output。

使用 OpenAI SDK，兼容任何 OpenAI 接口格式的提供方（OpenAI 官方、
DeepSeek、通义千问、本地 Ollama 等），只需在 .env 中配置
OPENAI_BASE_URL 和 OPENAI_MODEL。
"""
from typing import TypeVar

from openai import OpenAI
from pydantic import BaseModel

from config.prompts import SYSTEM_PROMPT
from config.settings import settings

T = TypeVar("T", bound=BaseModel)


def _get_client() -> OpenAI:
    """创建 OpenAI 客户端（懒加载，每次调用新建，简单可靠）。"""
    if not settings.openai_api_key:
        raise RuntimeError(
            "未配置 OPENAI_API_KEY，请在 .env 文件中设置。"
            "参考 .env.example。"
        )
    return OpenAI(
        api_key=settings.openai_api_key,
        base_url=settings.openai_base_url,
    )


def chat(
    user_prompt: str,
    system_prompt: str = SYSTEM_PROMPT,
    temperature: float = 0.3,
) -> str:
    """普通对话：返回模型文本回复。

    Args:
        user_prompt: 用户提示词。
        system_prompt: 系统提示词，默认用 SYSTEM_PROMPT。
        temperature: 采样温度，总结任务建议低值。
"""LLM 客户端：封装 chat 与 structured output。

使用 OpenAI SDK，兼容任何 OpenAI 接口格式的提供方（OpenAI 官方、
DeepSeek、通义千问、本地 Ollama 等），只需在 .env 中配置
OPENAI_BASE_URL 和 OPENAI_MODEL。
"""
from typing import TypeVar

from openai import OpenAI
from pydantic import BaseModel

from config.prompts import SYSTEM_PROMPT
from config.settings import settings

T = TypeVar("T", bound=BaseModel)


def _get_client() -> OpenAI:
    """创建 OpenAI 客户端（懒加载，每次调用新建，简单可靠）。"""
    if not settings.openai_api_key:
        raise RuntimeError(
            "未配置 OPENAI_API_KEY，请在 .env 文件中设置。"
            "参考 .env.example。"
        )
    return OpenAI(
        api_key=settings.openai_api_key,
        base_url=settings.openai_base_url,
    )


def chat(
    user_prompt: str,
    system_prompt: str = SYSTEM_PROMPT,
    temperature: float = 0.3,
) -> str:
    """普通对话：返回模型文本回复。

    Args:
        user_prompt: 用户提示词。
        system_prompt: 系统提示词，默认用 SYSTEM_PROMPT。
        temperature: 采样温度，总结任务建议低值。
    """
    client = _get_client()
    resp"""LLM 客户端：封装 chat 与 structured output。

使用 OpenAI SDK，兼容任何 OpenAI 接口格式的提供方（OpenAI 官方、
DeepSeek、通义千问、本地 Ollama 等），只需在 .env 中配置
OPENAI_BASE_URL 和 OPENAI_MODEL。
"""
from typing import TypeVar

from openai import OpenAI
from pydantic import BaseModel

from config.prompts import SYSTEM_PROMPT
from config.settings import settings

T = TypeVar("T", bound=BaseModel)


def _get_client() -> OpenAI:
    """创建 OpenAI 客户端（懒加载，每次调用新建，简单可靠）。"""
    if not settings.openai_api_key:
        raise RuntimeError(
            "未配置 OPENAI_API_KEY，请在 .env 文件中设置。"
            "参考 .env.example。"
        )
    return OpenAI(
        api_key=settings.openai_api_key,
        base_url=settings.openai_base_url,
    )


def chat(
    user_prompt: str,
    system_prompt: str = SYSTEM_PROMPT,
    temperature: float = 0.3,
) -> str:
    """普通对话：返回模型文本回复。

    Args:
        user_prompt: 用户提示词。
        system_prompt: 系统提示词，默认用 SYSTEM_PROMPT。
        temperature: 采样温度，总结任务建议低值。
    """
    client = _get_client()
    resp = client.chat.completions.create(
        model=settings.openai_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
    )
    return resp.choices[0].message.content or ""


def chat_structured(
"""LLM 客户端：封装 chat 与 structured output。

使用 OpenAI SDK，兼容任何 OpenAI 接口格式的提供方（OpenAI 官方、
DeepSeek、通义千问、本地 Ollama 等），只需在 .env 中配置
OPENAI_BASE_URL 和 OPENAI_MODEL。
"""
from typing import TypeVar

from openai import OpenAI
from pydantic import BaseModel

from config.prompts import SYSTEM_PROMPT
from config.settings import settings

T = TypeVar("T", bound=BaseModel)


def _get_client() -> OpenAI:
    """创建 OpenAI 客户端（懒加载，每次调用新建，简单可靠）。"""
    if not settings.openai_api_key:
        raise RuntimeError(
            "未配置 OPENAI_API_KEY，请在 .env 文件中设置。"
            "参考 .env.example。"
        )
    return OpenAI(
        api_key=settings.openai_api_key,
        base_url=settings.openai_base_url,
    )


def chat(
    user_prompt: str,
    system_prompt: str = SYSTEM_PROMPT,
    temperature: float = 0.3,
) -> str:
    """普通对话：返回模型文本回复。

    Args:
        user_prompt: 用户提示词。
        system_prompt: 系统提示词，默认用 SYSTEM_PROMPT。
        temperature: 采样温度，总结任务建议低值。
    """
    client = _get_client()
    resp = client.chat.completions.create(
        model=settings.openai_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
    )
    return resp.choices[0].message.content or ""


def chat_structured(
    user_prompt: str,
    response_model: type[T],
    system_prompt: str = SYSTEM"""LLM 客户端：封装 chat 与 structured output。

使用 OpenAI SDK，兼容任何 OpenAI 接口格式的提供方（OpenAI 官方、
DeepSeek、通义千问、本地 Ollama 等），只需在 .env 中配置
OPENAI_BASE_URL 和 OPENAI_MODEL。
"""
from typing import TypeVar

from openai import OpenAI
from pydantic import BaseModel

from config.prompts import SYSTEM_PROMPT
from config.settings import settings

T = TypeVar("T", bound=BaseModel)


def _get_client() -> OpenAI:
    """创建 OpenAI 客户端（懒加载，每次调用新建，简单可靠）。"""
    if not settings.openai_api_key:
        raise RuntimeError(
            "未配置 OPENAI_API_KEY，请在 .env 文件中设置。"
            "参考 .env.example。"
        )
    return OpenAI(
        api_key=settings.openai_api_key,
        base_url=settings.openai_base_url,
    )


def chat(
    user_prompt: str,
    system_prompt: str = SYSTEM_PROMPT,
    temperature: float = 0.3,
) -> str:
    """普通对话：返回模型文本回复。

    Args:
        user_prompt: 用户提示词。
        system_prompt: 系统提示词，默认用 SYSTEM_PROMPT。
        temperature: 采样温度，总结任务建议低值。
    """
    client = _get_client()
    resp = client.chat.completions.create(
        model=settings.openai_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
    )
    return resp.choices[0].message.content or ""


def chat_structured(
    user_prompt: str,
    response_model: type[T],
    system_prompt: str = SYSTEM_PROMPT,
    temperature: float = 0.3,
) -> T:
    """结构化输出：返回按 Pydantic 模"""LLM 客户端：封装 chat 与 structured output。

使用 OpenAI SDK，兼容任何 OpenAI 接口格式的提供方（OpenAI 官方、
DeepSeek、通义千问、本地 Ollama 等），只需在 .env 中配置
OPENAI_BASE_URL 和 OPENAI_MODEL。
"""
from typing import TypeVar

from openai import OpenAI
from pydantic import BaseModel

from config.prompts import SYSTEM_PROMPT
from config.settings import settings

T = TypeVar("T", bound=BaseModel)


def _get_client() -> OpenAI:
    """创建 OpenAI 客户端（懒加载，每次调用新建，简单可靠）。"""
    if not settings.openai_api_key:
        raise RuntimeError(
            "未配置 OPENAI_API_KEY，请在 .env 文件中设置。"
            "参考 .env.example。"
        )
    return OpenAI(
        api_key=settings.openai_api_key,
        base_url=settings.openai_base_url,
    )


def chat(
    user_prompt: str,
    system_prompt: str = SYSTEM_PROMPT,
    temperature: float = 0.3,
) -> str:
    """普通对话：返回模型文本回复。

    Args:
        user_prompt: 用户提示词。
        system_prompt: 系统提示词，默认用 SYSTEM_PROMPT。
        temperature: 采样温度，总结任务建议低值。
    """
    client = _get_client()
    resp = client.chat.completions.create(
        model=settings.openai_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
    )
    return resp.choices[0].message.content or ""


def chat_structured(
    user_prompt: str,
    response_model: type[T],
    system_prompt: str = SYSTEM_PROMPT,
    temperature: float = 0.3,
) -> T:
    """结构化输出：返回按 Pydantic 模型解析的结果。

    使用 OpenAI 的 structured output（response_format），
    模型"""LLM 客户端：封装 chat 与 structured output。

使用 OpenAI SDK，兼容任何 OpenAI 接口格式的提供方（OpenAI 官方、
DeepSeek、通义千问、本地 Ollama 等），只需在 .env 中配置
OPENAI_BASE_URL 和 OPENAI_MODEL。
"""
from typing import TypeVar

from openai import OpenAI
from pydantic import BaseModel

from config.prompts import SYSTEM_PROMPT
from config.settings import settings

T = TypeVar("T", bound=BaseModel)


def _get_client() -> OpenAI:
    """创建 OpenAI 客户端（懒加载，每次调用新建，简单可靠）。"""
    if not settings.openai_api_key:
        raise RuntimeError(
            "未配置 OPENAI_API_KEY，请在 .env 文件中设置。"
            "参考 .env.example。"
        )
    return OpenAI(
        api_key=settings.openai_api_key,
        base_url=settings.openai_base_url,
    )


def chat(
    user_prompt: str,
    system_prompt: str = SYSTEM_PROMPT,
    temperature: float = 0.3,
) -> str:
    """普通对话：返回模型文本回复。

    Args:
        user_prompt: 用户提示词。
        system_prompt: 系统提示词，默认用 SYSTEM_PROMPT。
        temperature: 采样温度，总结任务建议低值。
    """
    client = _get_client()
    resp = client.chat.completions.create(
        model=settings.openai_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
    )
    return resp.choices[0].message.content or ""


def chat_structured(
    user_prompt: str,
    response_model: type[T],
    system_prompt: str = SYSTEM_PROMPT,
    temperature: float = 0.3,
) -> T:
    """结构化输出：返回按 Pydantic 模型解析的结果。

    使用 OpenAI 的 structured output（response_format），
    模型返回的 JSON 会被自动解析为 response_model"""LLM 客户端：封装 chat 与 structured output。

使用 OpenAI SDK，兼容任何 OpenAI 接口格式的提供方（OpenAI 官方、
DeepSeek、通义千问、本地 Ollama 等），只需在 .env 中配置
OPENAI_BASE_URL 和 OPENAI_MODEL。
"""
from typing import TypeVar

from openai import OpenAI
from pydantic import BaseModel

from config.prompts import SYSTEM_PROMPT
from config.settings import settings

T = TypeVar("T", bound=BaseModel)


def _get_client() -> OpenAI:
    """创建 OpenAI 客户端（懒加载，每次调用新建，简单可靠）。"""
    if not settings.openai_api_key:
        raise RuntimeError(
            "未配置 OPENAI_API_KEY，请在 .env 文件中设置。"
            "参考 .env.example。"
        )
    return OpenAI(
        api_key=settings.openai_api_key,
        base_url=settings.openai_base_url,
    )


def chat(
    user_prompt: str,
    system_prompt: str = SYSTEM_PROMPT,
    temperature: float = 0.3,
) -> str:
    """普通对话：返回模型文本回复。

    Args:
        user_prompt: 用户提示词。
        system_prompt: 系统提示词，默认用 SYSTEM_PROMPT。
        temperature: 采样温度，总结任务建议低值。
    """
    client = _get_client()
    resp = client.chat.completions.create(
        model=settings.openai_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
    )
    return resp.choices[0].message.content or ""


def chat_structured(
    user_prompt: str,
    response_model: type[T],
    system_prompt: str = SYSTEM_PROMPT,
    temperature: float = 0.3,
) -> T:
    """结构化输出：返回按 Pydantic 模型解析的结果。

    使用 OpenAI 的 structured output（response_format），
    模型返回的 JSON 会被自动解析为 response_model 实例。

    Args:
        user_prompt: 用户提示词。
        response_model:"""LLM 客户端：封装 chat 与 structured output。

使用 OpenAI SDK，兼容任何 OpenAI 接口格式的提供方（OpenAI 官方、
DeepSeek、通义千问、本地 Ollama 等），只需在 .env 中配置
OPENAI_BASE_URL 和 OPENAI_MODEL。
"""
from typing import TypeVar

from openai import OpenAI
from pydantic import BaseModel

from config.prompts import SYSTEM_PROMPT
from config.settings import settings

T = TypeVar("T", bound=BaseModel)


def _get_client() -> OpenAI:
    """创建 OpenAI 客户端（懒加载，每次调用新建，简单可靠）。"""
    if not settings.openai_api_key:
        raise RuntimeError(
            "未配置 OPENAI_API_KEY，请在 .env 文件中设置。"
            "参考 .env.example。"
        )
    return OpenAI(
        api_key=settings.openai_api_key,
        base_url=settings.openai_base_url,
    )


def chat(
    user_prompt: str,
    system_prompt: str = SYSTEM_PROMPT,
    temperature: float = 0.3,
) -> str:
    """普通对话：返回模型文本回复。

    Args:
        user_prompt: 用户提示词。
        system_prompt: 系统提示词，默认用 SYSTEM_PROMPT。
        temperature: 采样温度，总结任务建议低值。
    """
    client = _get_client()
    resp = client.chat.completions.create(
        model=settings.openai_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
    )
    return resp.choices[0].message.content or ""


def chat_structured(
    user_prompt: str,
    response_model: type[T],
    system_prompt: str = SYSTEM_PROMPT,
    temperature: float = 0.3,
) -> T:
    """结构化输出：返回按 Pydantic 模型解析的结果。

    使用 OpenAI 的 structured output（response_format），
    模型返回的 JSON 会被自动解析为 response_model 实例。

    Args:
        user_prompt: 用户提示词。
        response_model: 期望的 Pydantic 模型类。
        system_prompt: 系统提示词。
        temperature: 采样温度。
    """
