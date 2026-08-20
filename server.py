from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask("pubg_store")

import os
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = "1338644072"

@app.route("/")
def home():
    return send_from_directory(".", "index.html")


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


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)