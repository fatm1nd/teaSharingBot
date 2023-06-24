import telebot
import secret


bot = telebot.TeleBot(token=secret.TELEGRAM_BOT_TOKEN)

@bot.message_handler(content_types=["location"])
def location(message):
    