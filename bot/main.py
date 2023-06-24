import telebot
import os
import sys

# from dotenv import load_dotenv

# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

# load_dotenv(dotenv_path)
# botToken = os.environ.get("TELEGRAM_BOT_TOKEN")

botToken = sys.argv[1]
# print(botToken)

bot = telebot.TeleBot(token=botToken)


@bot.message_handler(commands=['start'])
def startFunction(message):
    bot.send_message(message.chat.id,"Привет! Это бот для разделения пакетика чая с другими! А так же моно позвать кого-ниубдь на чаепитие или самому прийти!")


@bot.message_handler(content_types=["location"])
def location(message):
    print(message.location)

bot.polling()