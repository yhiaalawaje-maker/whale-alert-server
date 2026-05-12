from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8258871315:AAHs4RjV2d5UR-IHZTB0_5eEIBamxTafXZE"

@app.route("/")
def home():
    return "Whale Alert Server Running"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    chat_id = data["message"]["chat"]["id"]
    text = data["message"]["text"]

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": f"Received: {text}"
    }

    requests.post(telegram_url, json=payload)

    return {"status": "success"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
