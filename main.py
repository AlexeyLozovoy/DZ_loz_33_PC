#!/usr/bin/env python
import telebot
# import random

TOKEN = "5879031351:AAH6NKM0x3c5NgH-qX5SjBOiYbbbLJRFHBY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "beep!")

@bot.message_handler(func=lambda message: message.text=="keyboard")
def echo_message(message):
    # bot.reply_to(message, message.text)
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = telebot.types.KeyboardButton('a')
    itembtn2 = telebot.types.KeyboardButton('v')
    itembtn3 = telebot.types.KeyboardButton('d')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     keyboard = telebot.types.InlineKeyboardMarkup()
#     keyboard_cities = telebot.types.InlineKeyboardButton(text='"Игра в города"', callback_data='cities')
#     keyboard.add(keyboard_cities)
#     bot.send_message(message.chat.id, 'Привет', reply_markup=keyboard)
# # клавиатура
#
# allcities = []
# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     if call.data == 'cities':
#         bot.send_message(call.message.chat.id, 'Напишите город')
#         user_city = call.text # пользователь начинает первый и вводит город
#         if user_city.lower() == 'стоп':
#             bot.send_message((call.message.chat.id, 'Вы выиграли')) # остановка игры
#         else:
#             for i in allcities:
#                 if i[0].lower() == user_city[-1].lower():
#                     b.append(i) # перебираем все города в списке, если первая буква города из списка равна последней букве введеного пользователем города мы добавляем этот город в список
#                 elif user_city[-1].lower() == 'ь' or user_city[-1].lower() == 'ъ' or user_city[-1].lower() == 'й' or user_city[-1].lower() == 'ы':
#                     if i[0].lower() == user_city[-2].lower():
#                         b.append(i) # если город заканчивается на ь,й,ъ,ы сравниваем первую букву с предпоследней
#         gorod = random.choice(b) # из полученного списка выбираем рандомом одно подходящее слово
#         bot.send_message((call.message.chat.id, gorod))
#         b.clear() # очищаем список
