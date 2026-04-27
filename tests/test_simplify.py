import pytest
from unittest.mock import patch, MagicMock

from legal_ease.simplify import OpenAIClient


def test_simplify_text_returns_response():
    fake_resp = {
        "choices": [{"message": {"content": "Simplified text here."}}]
    }

    with patch("legal_ease.simplify.openai.ChatCompletion.create", return_value=fake_resp):
        client = OpenAIClient(api_key="test")
        out = client.simplify_text("Original legal text.")
        assert out == "Simplified text here."
import pytest
from unittest.mock import patch, MagicMock

from legal_ease.simplify import OpenAIClient


def test_simplify_text_returns_response():
    fake_resp = {
        "choices": [{"message": {"content": "Simplified text here."}}]
    }

    with patch("legal_ease.simplify.openai.ChatCompletion.create", return_value=fake_resp):
        client = OpenAIClient(api_key="test")
        out = client.simplify_text("Original legal text.")
        assert out == "Simplified text here."
