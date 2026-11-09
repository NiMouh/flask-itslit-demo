import os
from datetime import datetime

import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template
from flask_cors import CORS
from itslitlib import cprint, colorize


def create_app() -> Flask:
    load_dotenv()

    app = Flask(__name__)
    CORS(app)

    app.config["APP_NAME"] = os.getenv("APP_NAME", "Flask ItsLit Demo")
    app.config["QUOTE_API_URL"] = os.getenv(
        "QUOTE_API_URL", "https://api.quotable.io/random"
    )

    # Terminal startup banner using itslitlib.
    cprint(
        f"Starting {app.config['APP_NAME']}...",
        color="bright_cyan",
        styles=["bold", "underline"],
    )

    @app.get("/")
    def index():
        banner = colorize("Flask + itslitlib", color="bright_green", styles="bold")
        return render_template(
            "index.html",
            app_name=app.config["APP_NAME"],
            banner=banner,
            now=datetime.utcnow().isoformat() + "Z",
        )

    @app.get("/health")
    def health():
        cprint("Health check requested", color="yellow", styles="bold")
        return jsonify({"status": "ok", "service": app.config["APP_NAME"]}), 200

    @app.get("/api/quote")
    def quote():
        try:
            response = requests.get(app.config["QUOTE_API_URL"], timeout=5)
            response.raise_for_status()
            payload = response.json()

            data = {
                "content": payload.get("content", "No quote returned."),
                "author": payload.get("author", "Unknown"),
                "source": "remote",
            }
            cprint("Quote request succeeded", color="green", styles="bold")
            return jsonify(data), 200
        except requests.RequestException as exc:
            cprint(f"Quote request failed: {exc}", color="bright_red", styles="bold")
            return (
                jsonify(
                    {
                        "content": "Stay curious. Build, test, and iterate.",
                        "author": "Local Fallback",
                        "source": "fallback",
                        "detail": str(exc),
                    }
                ),
                200,
            )

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
