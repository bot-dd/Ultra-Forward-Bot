import threading
from flask import Flask
from pyrogram import Client

# Flask App
app = Flask(__name__)

@app.route('/')
def home():
    return "Silicon Bot is Running!"


# Function to run Flask
def run_flask():
    app.run(host="0.0.0.0", port=8000)

# Function to run Bot
def run_bot():
    bot.run()

if __name__ == "__main__":
    # Run Flask in separate thread
    threading.Thread(target=run_flask).start()
    # Run Bot in main thread
    run_bot()
