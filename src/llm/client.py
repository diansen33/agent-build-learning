"""LLM 调用层：封装 chat 与结构化输出。

使用 OpenAI 兼容接口（支持官方 OpenAI 及任意兼容第三方端点）。
通过 settings 配置 base_url / api_key / model。
"""
import json

from openai import OpenAI
from pydantic import BaseModel

from config.settings import settings

_client: OpenAI | None = None


def get_client() -> OpenAI:
    """惰性创建并复用 OpenAI 客户端单例。"""
    global _client
    if _client is None:
        _client = OpenAI(
            api_key=settings.openai_api_key,
            base_url=settings.openai_base_url,
        )
    return _client


def chat(
    prompt: str,
    system: str | None = None,
    temperature: float = 0.3,
) -> str:
    """简单 chat 调用，返回文本响应。"""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    resp = get_client().chat.completions.create(
        model=settings.openai_model,
        messages=messages,
        temperature=temperature,
    )
    return resp.choices[0].message.content or ""


def chat_structured(
    prompt: str,
    schema: type[BaseModel],
    system: str | None = None,
    temperature: float = 0.3,
) -> BaseModel:
    """调用 LLM 并返回符合 schema 的结构化对象。

    策略：在 prompt 中附带 JSON Schema，要求模型只输出 JSON；
    优先启用 response_format json_object，兼容接口不支持时自动降级。
    最后用 Pydantic 校验解析。
    """
    schema_desc = json.dumps(
        schema.model_json_schema(), ensure_ascii=False, indent=2
    )
    full_prompt = (
        f"{prompt}\n\n"
        f"请严格按照以下 JSON Schema 返回结果，只输出合法 JSON，"
        f"不要输出任何解释或额外内容：\n{schema_desc}"
    )

    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": full_prompt})

    kwargs: dict = {
        "model": settings.openai_model,
        "messages": messages,
        "temperature": temperature,
    }
    # 优先尝试 JSON 模式，部分兼容接口不支持则降级为普通调用
    try:
        resp = get_client().chat.completions.create(
            **kwargs, response_format={"type": "json_object"}
        )
    except Exception:
        resp = get_client().chat.completions.create(**kwargs)

    content = resp.choices[0].message.content or ""
    data = json.loads(content)
    return schema.model_validate(data)
