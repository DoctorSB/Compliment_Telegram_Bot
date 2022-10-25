#Бот присылает сообщения с рандомным промежутком
import telebot
import random
import time
from datetime import datetime

bot = telebot.TeleBot('BOT_TOKEN')
member_id = 'CHAT_ID'

compliments = ['это массив комплиментов']
timer = [3600, 7200, 5400, 14400]

bot.send_message(member_id, "Текст который отправиться при запуске бота")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print('Мы запустились в ' + current_time)

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    bot.send_message(member_id, random.choice(compliments))
    print('Комплимент отправлен в ' + current_time)
    time.sleep(random.choice(timer))

bot.infinity_polling()
