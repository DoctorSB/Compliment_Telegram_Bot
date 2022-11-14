# Бот присылает сообщения при нажати на кнопку
import telebot
import random
import time

bot = telebot.TeleBot('BOT_TOKEN')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Приветики', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'комплимент':
        bot.send_message(message.chat.id, random.choice(compliments))
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю. Напиши /start.')


keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Комплимент')


compliments = ['это массив комплиментов']

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        time.sleep(15)
