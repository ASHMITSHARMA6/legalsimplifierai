import os
from typing import Optional

from .prompts import DEFAULT_PROMPT

# Import openai if available; provide a lightweight fallback object so tests can
# import this module and patch ChatCompletion.create without requiring the
# real `openai` package to be installed.
try:
    import openai
except Exception:
    class _DummyChatCompletion:
        @staticmethod
        def create(*args, **kwargs):
            raise RuntimeError("OpenAI package not installed")

    class _DummyOpenAI:
        ChatCompletion = _DummyChatCompletion

    openai = _DummyOpenAI()


class OpenAIClient:
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-3.5-turbo"):
        key = api_key or os.environ.get("OPENAI_API_KEY")
        if not key:
            raise ValueError("OpenAI API key required via parameter or OPENAI_API_KEY env var")
        # If real openai is present, set the key; if it's the dummy, this will
        # create an attribute but cannot make real requests (tests patch methods).
        try:
            openai.api_key = key
        except Exception:
            setattr(openai, "api_key", key)
        self.model = model

    def simplify_text(self, text: str, max_tokens: int = 1024) -> str:
        prompt = DEFAULT_PROMPT + "\n\n" + text
        # Use chat completion for better instruction following
        resp = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=0.0,
        )
        # Extract assistant response
        choices = resp.get("choices") or []
        if not choices:
            raise RuntimeError("No response from OpenAI API")
        return choices[0]["message"]["content"].strip()


import os
from typing import Optional

from .prompts import DEFAULT_PROMPT

# Import openai if available; provide a lightweight fallback object so tests can
# import this module and patch ChatCompletion.create without requiring the
# real `openai` package to be installed.
try:
    import openai
except Exception:
    class _DummyChatCompletion:
        @staticmethod
        def create(*args, **kwargs):
            raise RuntimeError("OpenAI package not installed")

    class _DummyOpenAI:
        ChatCompletion = _DummyChatCompletion

    openai = _DummyOpenAI()


class OpenAIClient:
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-3.5-turbo"):
        key = api_key or os.environ.get("OPENAI_API_KEY")
        if not key:
            raise ValueError("OpenAI API key required via parameter or OPENAI_API_KEY env var")
        # If real openai is present, set the key; if it's the dummy, this will
        # create an attribute but cannot make real requests (tests patch methods).
        try:
            openai.api_key = key
        except Exception:
            setattr(openai, "api_key", key)
        self.model = model

    def simplify_text(self, text: str, max_tokens: int = 1024) -> str:
        prompt = DEFAULT_PROMPT + "\n\n" + text
        # Use chat completion for better instruction following
        resp = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=0.0,
        )
        # Extract assistant response
        choices = resp.get("choices") or []
        if not choices:
            raise RuntimeError("No response from OpenAI API")
        return choices[0]["message"]["content"].strip()


# Convenience function
def simplify_text(text: str, api_key: Optional[str] = None, model: str = "gpt-3.5-turbo") -> str:
    client = OpenAIClient(api_key=api_key, model=model)
    return client.simplify_text(text)
