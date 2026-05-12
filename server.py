from flask import Flask, request
import requests
import json

app = Flask(__name__)

BOT_TOKEN = "حط_توكن_البوت"
CHAT_ID = "حط_ايدي_التليجرام"

@app.route("/")
def home():
    return "Whale Alert Server Running"

@app.route("/webhook", methods=["POST"])
def webhook():

    raw_data = request.data.decode("utf-8")

    try:
        data = json.loads(raw_data)
    except:
        data = {"message": raw_data}

    signal = data.get("signal", "ALERT")
    symbol = data.get("symbol", "SPX")
    price = data.get("price", "")
    time = data.get("time", "")

    message = f"""
🚨 تنبيه جديد

📈 الإشارة: {signal}
💰 الأصل: {symbol}
📍 السعر: {price}
⏰ الوقت: {time}
"""

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(telegram_url, json=payload)

    return {"status": "success"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
