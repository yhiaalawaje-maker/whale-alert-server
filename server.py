from flask import Flask, request
import requests
import json
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/")
def home():
    return "Whale Alert Server Running"

@app.route("/webhook", methods=["POST"])
def webhook():
    raw_data = request.data.decode("utf-8")

    if not raw_data:
        raw_data = "تنبيه جديد من TradingView"

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": raw_data
    }

    try:
        r = requests.post(telegram_url, json=payload, timeout=10)
        print("Telegram status:", r.status_code)
        print(r.text)
        return "OK", 200

    except Exception as e:
        print("Telegram error:", str(e))
        return "ERROR", 500


    

    
    
    
        

    
    
    
    

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
