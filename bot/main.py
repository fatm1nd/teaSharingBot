import telebot
import secret
import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

load_dotenv(dotenv_path)
botToken = os.environ.get("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(token=botToken)





@bot.message_handler(content_types=["location"])
def location(message):
    print(message.location)

bot.polling()