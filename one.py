from telegram.ext import Updater, CommandHandler
from flask import Flask, request

app = Flask(__name__)

# Set up your Telegram bot token
bot_token = 'YOUR_TELEGRAM_BOT_TOKEN'

# Set up your TradingView alert webhook URL
webhook_url = '/tradingview-webhook'

# Configure the Telegram bot
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

@app.route(webhook_url, methods=['POST'])
def handle_webhook():
    data = request.get_json()

    # Extract the message from the TradingView alert
    message = data['message']

    # Extract the details you want from the message
    symbol = message['symbol']
    condition = message['condition']

    # Send the extracted details to your Telegram bot
    chat_id = 'YOUR_TELEGRAM_CHAT_ID'
    text = f"New TradingView Alert:\nSymbol: {symbol}\nCondition: {condition}"
    updater.bot.send_message(chat_id=chat_id, text=text)

    return 'OK'

if __name__ == '__main__':
    # Start the Telegram bot
    updater.start_polling()

    # Start the Flask server
    app.run(port=3000)
