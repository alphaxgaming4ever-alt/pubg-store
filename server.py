from flask import Flask, request, jsonify
import requests
import os

app = Flask("pubg_store")

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = "1338644072"


@app.route("/")
def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.route("/order", methods=["POST"])
def order():

    data = request.get_json()

    product = data.get("product", "")
    price = data.get("price", "")
    player_id = data.get("player_id", "")
    telegram = data.get("telegram", "")

    message = (
        "🎮 НОВЫЙ ЗАКАЗ PUBG UC\n\n"
        f"📦 Товар: {product}\n"
        f"💰 Цена: {price}\n"
        f"🆔 PUBG ID: {player_id}\n"
        f"📱 Telegram: {telegram}"
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    try:

        response = requests.post(
            url,
            json={
                "chat_id": CHAT_ID,
                "text": message
            },
            timeout=10
        )

        if response.ok:
            return jsonify({"success": True})

        return jsonify({"success": False}), 500

    except Exception as error:

        print(error)


        return jsonify({"success": False}), 500
        
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
