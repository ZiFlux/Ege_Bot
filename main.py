import telebot
from telebot import types
import json
import openpyxl
import time
from dotenv import load_dotenv
import os

load_dotenv()

bot = telebot.TeleBot(os.getenv('TOKEN'))


# ADMIN_CHAT_ID = 712386884


@bot.message_handler(commands=['start'])
def start(message):
    global answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9, answer10, answer11, answer12
    global answer13, answer14, answer15, answer16, answer17, answer18, answer19, answer20, answer21, answer22, answer23
    global answer26, answer27, answer24, ranswer5, answer25, sumka, user_id
    answer1 = answer2 = answer3 = answer4 = answer5 = answer6 = answer7 = answer8 = answer9 = answer10 = answer11 = answer12 = 0
    answer13 = answer14 = answer15 = answer16 = answer17 = answer18 = answer19 = answer20 = answer21 = answer22 = answer23 = 0
    answer26 = answer27 = answer24 = answer25 = ranswer5 = sumka = 0
    global var5_, var10_, var15_
    var5_ = 0
    var10_ = 0
    var15_ = 0
    with open("data.json", "r") as f_o:
        datas = json.load(f_o)
    user_id = message.from_user.id
    username1 = message.from_user.username

    if str(user_id) not in datas:
        datas[user_id] = {
            "username": username1,
            "var5": 0,
            "percentage5": 0,
            "var10": 0,
            "percentage10": 0,
            "var15": 0,
            "percentage15": 0
        }
        time.sleep(2)
        bot.send_message(message.chat.id, text=str(f"✅Вы зарегестрированы под {user_id}, {username1}.\nВаша статистика "
                                                   f"будет сохранена!"))

    else:
        bot.send_message(message.chat.id,
                         text=str(f"✅Вы вошли как {user_id}, {username1}.\nВаша статистика будет сохранена!"))
    with open("data.json", "w") as f_o:
        json.dump(datas, f_o, indent=4, ensure_ascii=False)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/Bapuant5")
    btn2 = types.KeyboardButton("/Bapuant10")
    btn3 = types.KeyboardButton("/Bapuant15")
    btn4 = types.KeyboardButton("/statistic")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id,
                     text="👋 Привет, {0.first_name}! Это тренировочный бот ЕГЭ по информатике!\n"
                          "Выбери один из вариантов!↘️".format(
                           message.from_user), reply_markup=markup)


@bot.message_handler(commands=['statistic'])
def stat(message):
    global ranswer5, ranswer10, ranswer15, percentage5, percentage10, percentage15, username
    with open('data.json', 'r') as f:
        datas = json.load(f)
    user_id1 = message.from_user.id
    inf1 = datas[str(user_id1)]["var5"]
    inf1_ = datas[str(user_id1)]["percentage5"]
    inf2 = datas[str(user_id1)]["var10"]
    inf2_ = datas[str(user_id1)]["percentage10"]
    inf3 = datas[str(user_id1)]["var15"]
    inf3_ = datas[str(user_id1)]["percentage15"]
    if str(user_id1) not in datas:
        datas[user_id1] = {
            "username": username,
            "var5": 0,
            "percentage5": 0,
            "var10": 0,
            "percentage10": 0,
            "var15": 0,
            "percentage15": 0
        }
        bot.send_message(message.chat.id, text="Вас нет в базе данных!\nСейчас вы будете зарегестрированны...")
        time.sleep(2)
        bot.send_message(message.chat.id, text=str(f"✅Вы зарегестрированы под {user_id}, {username}.\nВаша статистика "
                                                   f"будет сохранена!"))
    else:
        bot.send_message(message.chat.id,
                         text=f"Ваша статистика:\n5 Вариант: {inf1} из 27 - {inf1_}%\n"
                              f"10 Вариант: {inf2} из 27 - {inf2_}%\n"
                              f"15 Вариант: {inf3} из 27 - {inf3_}%")


@bot.message_handler(commands=['Bapuant5'])
def var5(message):
    global var5_
    var5_ = 1
    bot.send_message(message.chat.id, text="Держи задания! Ответы вводи один номер - одно сообщение(искл. 25)\n"
                                           "Например так:\n 1) 123\n 2) zywx\n"
                                           "❗ Ответ на задания принимается только 1 раз!\n"
                                           "‼ Примечание: в заданиях 17, 20, 25, 26 и 27, если потребуется,"
                                           "ответ выводить через нижнее подчёркивание(_)!\n"
                                           "25-ое задание вводить так:\n"
                                           "25) 124567_8990124/12456_8990/и т.д.\n"
                                           "Ссылка на файлы для заданий:"
                                           "\nhttps://drive.google.com/file/d/1qSA1ndSgB7jqcZlGNQtM5M3u1SmrVJpQ/view")
    f = open("E:\\Bot\\vars\\5var.pdf", "rb")
    bot.send_document(message.chat.id, f)
    bot.send_message(message.chat.id, text="Приступай к выполнению!😊")


@bot.message_handler(commands=['Bapuant10'])
def var10(message):
    global var10_
    var10_ = 1
    bot.send_message(message.chat.id, text="Держи задания! Ответы вводи один номер - одно сообщение(искл. 25)\n"
                                           "Например так:\n 1) 123\n 2) zywx\n"
                                           "❗ Ответ на задания принимается только 1 раз!\n"
                                           "‼ Примечание: в заданиях 17, 20, 25, 26 и 27, если потребуется,"
                                           "ответ выводить через нижнее подчёркивание(_)!\n"
                                           "25-ое задание вводить так:\n"
                                           "25) 124567_8990124/12456_8990/и т.д.\n"
                                           "Ссылка на файлы для заданий:\n"
                                           "https://drive.google.com/file/d/1hvg5vnMbyK7U6l-Qo2ph8AZs0a5IvXof/view?usp=sharing")
    f = open("E:\\Bot\\vars\\10var.pdf", "rb")
    bot.send_document(message.chat.id, f)
    bot.send_message(message.chat.id, text="Приступай к выполнению!😊")


@bot.message_handler(commands=['Bapuant15'])
def var15(message):
    global var15_
    var15_ = 1
    bot.send_message(message.chat.id, text="Держи задания! Ответы вводи один номер - одно сообщение(искл. 25)\n"
                                           "Например так:\n 1) 123\n 2) zywx\n"
                                           "❗ Ответ на задания принимается только 1 раз!\n"
                                           "‼ Примечание: в заданиях 17, 20, 25, 26 и 27, если потребуется,"
                                           "ответ выводить через нижнее подчёркивание(_)!\n"
                                           "25-ое задание вводить так:\n"
                                           "25) 124567_8990124/12456_8990/и т.д.\n"
                                           "Ссылки на задания:\n<url>\n<url>\n<url>")
    f = open("E:\\Bot\\vars\\15var.pdf", "rb")
    bot.send_document(message.chat.id, f)
    bot.send_message(message.chat.id, text="Приступай к выполнению!😊")


@bot.message_handler(content_types='text')
def check_var(message):
    global answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9, answer10, answer11, answer12
    global answer13, answer14, answer15, answer16, answer17, answer18, answer19, answer20, answer21, answer22, answer23
    global answer26, answer27, answer24, answer25, ranswer5, sumka, percentage5
    book = openpyxl.open("otv5var.xlsx")
    book2 = openpyxl.open("otv10var.xlsx")
    book3 = openpyxl.open("otv15var.xlsx")
    sheet2 = book2.active
    sheet3 = book3.active
    sheet = book.active
    if var5_ == 1:
        if message.text[:2] == "1)":
            if answer1 != 1:
                if str(sheet[1][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer1 += 1
                    ranswer5 += 1
                    sumka = sumka + answer1
                else:
                    answer1 += 1
                    sumka = sumka + answer1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос.")
        if message.text[:2] == "2)":
            if answer2 != 1:
                if str(sheet[2][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer2 += 1
                    ranswer5 += 1
                    sumka = sumka + answer2
                else:
                    answer2 += 1
                    sumka = sumka + answer2
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "3)":
            if answer3 != 1:
                if str(sheet[3][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer3 += 1
                    ranswer5 += 1
                    sumka = sumka + answer3
                else:
                    answer3 += 1
                    sumka = sumka + answer3
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "4)":
            if answer4 != 1:
                if str(sheet[4][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer4 += 1
                    ranswer5 += 1
                    sumka = sumka + answer4
                else:
                    answer4 += 1
                    sumka = sumka + answer4
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "5)":
            if answer5 != 1:
                if str(sheet[5][0].value) == message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer5 += 1
                    ranswer5 += 1
                    sumka = sumka + answer5
                else:
                    answer5 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer5
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "6)":
            if answer6 != 1:
                if str(sheet[6][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer6 += 1
                    ranswer5 += 1
                    sumka = sumka + answer6
                else:
                    answer6 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer6
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "7)":
            if answer7 != 1:
                if str(sheet[7][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer7 += 1
                    ranswer5 += 1
                    sumka = sumka + answer7
                else:
                    answer7 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer7
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "8)":
            if answer8 != 1:
                if str(sheet[8][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer8 += 1
                    ranswer5 += 1
                    sumka = sumka + answer8
                else:
                    answer8 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer8
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "9)":
            if answer9 != 1:
                if str(sheet[9][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer9 += 1
                    ranswer5 += 1
                    sumka = sumka + answer9
                else:
                    answer9 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer9
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "10":
            if answer10 != 1:
                if str(sheet[10][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer10 += 1
                    ranswer5 += 1
                    sumka = sumka + answer10
                else:
                    answer10 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer10
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "11":
            if answer11 != 1:
                if str(sheet[11][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer11 += 1
                    ranswer5 += 1
                    sumka = sumka + answer11
                else:
                    answer11 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer11
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "12":
            if answer12 != 1:
                if str(sheet[12][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer12 += 1
                    ranswer5 += 1
                    sumka = sumka + answer12
                else:
                    answer12 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer12
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "13":
            if answer13 != 1:
                if str(sheet[13][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer13 += 1
                    ranswer5 += 1
                    sumka = sumka + answer13
                else:
                    answer13 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer13
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "14":
            if answer14 != 1:
                if str(sheet[14][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer14 += 1
                    ranswer5 += 1
                    sumka = sumka + answer14
                else:
                    answer14 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer14
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "15":
            if answer15 != 1:
                if str(sheet[15][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer15 += 1
                    ranswer5 += 1
                    sumka = sumka + answer15
                else:
                    answer15 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer15
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "16":
            if answer16 != 1:
                if str(sheet[16][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer16 += 1
                    ranswer5 += 1
                    sumka = sumka + answer16
                else:
                    answer16 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer16
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "17":
            if answer17 != 1:
                if str(sheet[17][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer17 += 1
                    ranswer5 += 1
                    sumka = sumka + answer17
                else:
                    answer17 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer17
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "18":
            if answer18 != 1:
                if str(sheet[18][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer18 += 1
                    ranswer5 += 1
                    sumka = sumka + answer18
                else:
                    answer18 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer18
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "19":
            if answer19 != 1:
                if str(sheet[19][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer19 += 1
                    ranswer5 += 1
                    sumka = sumka + answer19
                else:
                    answer19 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer19
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "20":
            if answer20 != 1:
                if str(sheet[20][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer20 += 1
                    ranswer5 += 1
                    sumka = sumka + answer20
                else:
                    answer20 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer20
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "21":
            if answer21 != 1:
                if str(sheet[21][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer21 += 1
                    ranswer5 += 1
                    sumka = sumka + answer21
                else:
                    answer21 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer21
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "22":
            if answer22 != 1:
                if str(sheet[22][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer22 += 1
                    ranswer5 += 1
                    sumka = sumka + answer22
                else:
                    answer22 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer22
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "23":
            if answer23 != 1:
                if str(sheet[23][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer23 += 1
                    ranswer5 += 1
                    sumka = sumka + answer23
                else:
                    answer23 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer23
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "24":
            if answer24 != 1:
                if str(sheet[24][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer24 += 1
                    ranswer5 += 1
                    sumka = sumka + answer24
                else:
                    answer24 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer24
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "25":
            if answer25 != 1:
                if str(sheet[25][1].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer25 += 1
                    ranswer5 += 1
                    sumka = sumka + answer25
                else:
                    answer25 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer25
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "26":
            if answer26 != 1:
                if str(sheet[26][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer26 += 1
                    ranswer5 += 1
                    sumka = sumka + answer26
                else:
                    answer26 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer26
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
        if message.text[:2] == "27":
            if answer27 != 1:
                if str(sheet[27][0].value) in message.text:
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    answer27 += 1
                    ranswer5 += 1
                    sumka = sumka + answer27
                else:
                    answer27 += 1
                    bot.send_message(message.chat.id, text="Ответ принят!✅")
                    sumka = sumka + answer27
            else:
                bot.send_message(message.chat.id, text="⚠Вы уже дали ответ на данный вопрос")
    if message.text == "Стоп":
        sumka = 27
        answer1 = answer2 = answer3 = answer4 = answer5 = answer6 = answer7 = answer8 = answer9 = answer10 = answer11 = answer12 = answer13 = answer14 = answer15 = answer16 = answer17 = answer18 = answer19 = answer20 = answer21 = answer22 = answer23 = answer26 = answer27 = answer24 = answer25 = 1
    if sumka >= 27:
        percentage5 = int((ranswer5 / 27) * 100)
        with open('data.json', 'r') as f:
            datas = json.load(f)
            user_id1 = message.from_user.id
            last_attemp = datas[str(user_id1)]["var5"]
        if ranswer5 < last_attemp:
            bot.send_message(message.chat.id,
                             text=f"Тест окончен!\nВаша статистика:\nВерно решено - {ranswer5} из 27\nВы завершили вариант на {percentage5}%")
            bot.send_message(message.chat.id,
                             text=f"Эта попытка была хуже предыдущей. Она не будет записана в статистику.")
        else:

            bot.send_message(message.chat.id,
                             text=f"Тест окончен!\nВаша статистика:\nВерно решено - {ranswer5} из 27\nВы завершили вариант на {percentage5}%")
            time.sleep(2)

            with open('data.json', 'r') as f:
                datas = json.load(f)
                datas[str(user_id1)]["var5"] = ranswer5
                datas[str(user_id1)]["percentage5"] = percentage5

            with open('data.json', 'w') as f:
                f.write(json.dumps(datas, indent=4, ensure_ascii=False))


bot.polling(none_stop=True)
