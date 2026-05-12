
from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "PUT_BOT_TOKEN_HERE"
CHAT_ID = "PUT_CHAT_ID_HERE"

@app.route("/")
def home():
    return "Whale Alert Server Running"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    message = data.get("message", "No message received")

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(telegram_url, json=payload)

    return {"status": "success"}
