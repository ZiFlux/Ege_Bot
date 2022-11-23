import telebot
from Token import token
from telebot import TeleBot
from telebot import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json
import xlrd

bot = telebot.TeleBot(token)
ADMIN_CHAT_ID = 712386884


@bot.message_handler(commands=['start'])
def start(message):
    with open("data.json", "r") as f_o:
        data_from_json = json.load(f_o)
    user_id = message.from_user.id
    username = message.from_user.username


    if str(user_id) not in data_from_json:
        data_from_json[user_id] = {"username": username}
    with open("data.json", "w") as f_o:
        json.dump(data_from_json, f_o, indent=4, ensure_ascii=False)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Вариант 5")
    btn2 = types.KeyboardButton("Вариант 10")
    btn3 = types.KeyboardButton("Вариант 15")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Это тренировочный бот Егэ по информатике!\n"
                          "Выбери один из вариантов!".format(
                         message.from_user), reply_markup=markup)
    bot.send_message(message.chat.id, text=str(f"Вы зарегестрированы под {user_id}, {username}"))


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Вариант 5"):
        bot.send_message(message.chat.id, text="Держи задания! Ответы вводи один номер - одно сообщение\n"
                                               "Например так:\n 1) 123\n 2) zywx\n"
                                               "Примечание: в заданиях 17, 20, 25, 26 и 27 ответ выводить "
                                               "через пробел!")
        f = open("C:\\Users\\irsha\\PycharmProjects\\pythonProject5\\vars\\5var.pdf", "rb")
        bot.send_document(message.chat.id, f)
        bot.send_message(message.chat.id, text="Приступай к выполнению!")



    elif (message.text == "Вариант 10"):
        bot.send_message(message.chat.id, text="Держи задания! Ответы вводи один номер - одно сообщение\n"
                                               "Например так:\n 1) 123\n 2) zywx\n"
                                               "Примечание: в заданиях 17, 20, 25, 26 и 27 ответ выводить "
                                               "через пробел!")
        f = open("C:\\Users\\irsha\\PycharmProjects\\pythonProject5\\vars\\10var.pdf", "rb")
        bot.send_document(message.chat.id, f)
    elif (message.text == "Вариант 15"):
        bot.send_message(message.chat.id, text="Держи задания! Ответы вводи один номер - одно сообщение\n"
                                               "Например так:\n 1) 123\n 2) zywx\n"
                                               "Примечание: в заданиях 17, 20, 25, 26 и 27 ответ выводить "
                                               "через пробел!")
        f = open("C:\\Users\\irsha\\PycharmProjects\\pythonProject5\\vars\\15var.pdf", "rb")
        bot.send_document(message.chat.id, f)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


bot.polling(none_stop=True)
