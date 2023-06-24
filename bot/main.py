import telebot
import os
import sys
from telebot import types 

# TODO: make /tea@123123 command as identify specific teaBag


botToken = ""
try:
    botToken = sys.argv[1]
except:
    raise Exception("TELEGRAM_BOT_TOKEN is missing. Add token to .env at you root project or add to arguments 'python3 main.py \"token\"'")
bot = telebot.TeleBot(token=botToken)


@bot.message_handler(commands=['start'])
def startFunction(message):
    bot.send_message(message.chat.id,"Привет! Это бот для разделения пакетика чая с другими! А так же можно позвать кого-ниубдь на чаепитие или самому прийти!")

    markup = types.ReplyKeyboardMarkup(row_width=2)
    getTeaBagButton = types.KeyboardButton("Получить ☕️")
    giveTeaBagButton = types.KeyboardButton("Отдать ☕️")
    inviteToTeaDrinkingButton = types.KeyboardButton("Прийти на 🫖")
    goToTeaDrinkingButton = types.KeyboardButton("Пригласить на 🫖")
    markup.add(getTeaBagButton,inviteToTeaDrinkingButton,giveTeaBagButton,goToTeaDrinkingButton)
    bot.send_message(message.chat.id,"Выберите хотите получить/отдать пакетик чая или прийти/пригласить на чаепитие:",reply_markup=markup)


@bot.message_handler(func=lambda message : message.text == "Получить ☕️" or message.text == "Отдать ☕️")
def teaBagHandler(message):
    if message.text == "Получить ☕️":
        pass
    elif message.text == "Отдать ☕️":
        bot.send_message(message.chat.id,"Невероятно круто! Какой чай ты хочешь отдать? Напиши название, вкус (опционально)")
        bot.register_next_step_handler_by_chat_id(message.chat.id,giveTeaBagFunction)


def giveTeaBagFunction(message):
    bot.send_message(message.chat.id,"Сколько раз чай был заварен? \n Если ты решил пожертвовать новый пакетик, то напиши 0. Число должно быть больше либо равно нулю.")
    description = message.text
    bot.register_next_step_handler_by_chat_id(message.chat.id,giveTeaBagFunctionSecondStep,description)

def giveTeaBagFunctionSecondStep(message,description):
    tries = -1
    try:
        tries = int(message.text)
        bot.send_message(message.chat.id, "Отлично! Теперь отправь свою геолокацию. Это можно сделать вложением через мобильное приложение. \n\
                         Или отправь долготу и широту через пробел (например как '48.741261 55.754196'). Скопировать из мобильных карт.")
        bot.register_next_step_handler_by_chat_id(message.chat.id,location, description, tries)
    except ValueError:
        # Пользователь ввел не число
        bot.send_message(message.chat.id,"Ой, ты ввел не число! Попробуй еще раз!")
        bot.register_next_step_handler_by_chat_id(message.chat.id,giveTeaBagFunctionSecondStep,description)
    except:
        bot.send_message(message.chat.id,"Ой, произошла какая-то ошибка! Введи число еще раз!")
        bot.register_next_step_handler_by_chat_id(message.chat.id,giveTeaBagFunctionSecondStep,description)
        


@bot.message_handler(content_types=["location"])
def location(message):
    print(message.location)

bot.polling()