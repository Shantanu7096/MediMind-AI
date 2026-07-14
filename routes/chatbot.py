from flask import Blueprint
from flask import render_template
from flask import request
from flask import jsonify

from flask_login import login_required

from ai.chatbot import ask_ai

chatbot_bp = Blueprint(
    "chatbot",
    __name__
)


# ==========================================================
# Chatbot Page
# ==========================================================

@chatbot_bp.route("/chatbot", methods=["GET"])
@login_required
def chatbot():

    return render_template(
        "chatbot.html"
    )


# ==========================================================
# Chat API
# ==========================================================

@chatbot_bp.route("/chatbot", methods=["POST"])
@login_required
def chat():

    data = request.get_json()

    if not data:

        return jsonify({

            "reply": "No message received."

        }), 400

    message = data.get(

        "message",

        ""

    ).strip()

    if message == "":

        return jsonify({

            "reply": "Please enter a message."

        })

    try:

        reply = ask_ai(

            message

        )

    except Exception:

        reply = "⚠️ AI service is currently unavailable. Please try again."

    return jsonify({

        "reply": reply

    })


# ==========================================================
# Health Check
# ==========================================================

@chatbot_bp.route("/chatbot_status")
@login_required
def chatbot_status():

    return jsonify({

        "status": "Running",

        "version": "2.0",

        "ai": "Google Gemini"

    })