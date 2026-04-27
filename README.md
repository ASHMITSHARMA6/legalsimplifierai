# LegalEase — AI Legal Document Simplifier (Prototype)

A small Python  that demonstrates how to simplify complex legal text into plain English using the OpenAI API. This repository is intended as a local prototype you can add to your resume.

IMPORTANT: If you must avoid leaving an "AI trace" on public artifacts, do not claim use of proprietary LLMs in public materials. This prototype demonstrates an approach using the OpenAI API — be sure to comply with your institution's policies before publishing.

What’s included
- `legal_ease/` — the package containing core logic and CLI
- `tests/` — unit tests that mock the OpenAI API
- `requirements.txt` — Python dependencies

Quick start

1. Create a virtual environment and install deps:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Set your OpenAI API key in the `OPENAI_API_KEY` environment variable. The CLI and library will also accept an explicit key.

3. Run the CLI to simplify a file:

```bash
python -m legal_ease.cli input.txt
```

Notes for resume use
- If you add this to your resume as a project, describe it as a "prototype for simplifying legal documents using NLP techniques" and avoid naming the underlying provider if you specifically need to hide AI usage. That said, be honest about capabilities and limitations when asked in interviews.
