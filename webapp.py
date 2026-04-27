import os

try:
    from flask import Flask, render_template, request, redirect, url_for, flash
except Exception:  # pragma: no cover - helps local import without flask installed
    Flask = None
    render_template = None
    request = None
    redirect = None
    url_for = None
    flash = None

from legal_ease.simplify import OpenAIClient


if Flask:
    app = Flask(__name__)
    app.secret_key = os.environ.get("FLASK_SECRET", "dev-secret")


    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html", original="", simplified=None)


    @app.route("/simplify", methods=["POST"])
    def simplify():
        # prefer uploaded PDF text if present
        uploaded = request.files.get("file_upload")
        text = ""
        pdf_error = False
        if uploaded and uploaded.filename:
            # Try to extract text from uploaded PDF
            try:
                from PyPDF2 import PdfReader

                reader = PdfReader(uploaded.stream)
                pages = []
                for p in reader.pages:
                    pages.append(p.extract_text() or "")
                text = "\n\n".join(pages).strip()
            except Exception:
                pdf_error = True
                text = ""

        if not text:
            text = request.form.get("legal_text", "").strip()

        if pdf_error and not text:
            flash("We couldn't extract text from that PDF. Try another PDF or paste text directly.")
            return render_template("index.html", original="", simplified=None)

        if not text:
            flash("Please paste some legal text or upload a PDF to simplify.")
            return render_template("index.html", original="", simplified=None)

        # Use OPENAI_API_KEY env var if set; otherwise run in demo mode
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            simplified = "[Demo] This is where the simplified text will appear. Set OPENAI_API_KEY to enable real simplification."
        else:
            client = OpenAIClient(api_key=api_key)
            simplified = client.simplify_text(text)

        return render_template("index.html", original=text, simplified=simplified)


    if __name__ == "__main__":
        app.run(debug=True, host="127.0.0.1", port=5000)
else:
    # If Flask isn't installed, importing this module won't crash; attempting
    # to run the server will raise a clear error.
    def _require_flask():
        raise RuntimeError("Flask is required to run the web UI. Install with `pip install Flask`.")

    index = _require_flask
    simplify = _require_flask
