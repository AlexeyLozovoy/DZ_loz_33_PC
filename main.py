#!/usr/bin/env python
import telebot

# import random

TOKEN = "5879031351:AAH6NKM0x3c5NgH-qX5SjBOiYbbbLJRFHBY"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "beep!")


@bot.message_handler(func=lambda message: message.text == "a")
def send_welcome(message):
    bot.reply_to(message, "Я")


@bot.message_handler(func=lambda message: message.text == "b")
def send_welcome(message):
    bot.reply_to(message, "тебя")


@bot.message_handler(func=lambda message: message.text == "c")
def send_welcome(message):
    bot.reply_to(message, "люблю!")

@bot.message_handler(func=lambda message: message.text == "Key")
def echo_message(message):
    bot.reply_to(message, message.text)
    markup = telebot.types.ReplyKeyboardMarkup(row_width=3)
    itembtn1 = telebot.types.KeyboardButton('a')
    itembtn2 = telebot.types.KeyboardButton('b')
    itembtn3 = telebot.types.KeyboardButton('c')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
