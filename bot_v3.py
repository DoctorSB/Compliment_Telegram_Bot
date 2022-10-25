import telebot
import random
import time
from datetime import datetime
from random import randrange

bot = telebot.TeleBot('BOT_TOKEN')
member_id = 'CHAT_ID'

compliments = []
stickers = []
stickers_mini = []
timer = [7200, 9000, 10800, 12600, 14400]
#требуется создать файл с названием "compliments.txt" и вставить в него массив комплиментов
file = open('compliments.txt', 'r')
st = file.readline()
while True:
    line = file.readline()
    if not line:
        break
    compliments.append(line.strip())
file.close
#требуется создать файл с названием "stickers.txt" и вставить в него массив стикеров
file = open('stickers_mini.txt', 'r')
st = file.readline()
while True:
    line = file.readline()
    if not line:
        break
    stickers_mini.append(line.strip())
file.close
#требуется создать файл с названием "stickers_mini.txt" и вставить в него массив стикеров
file = open('stickers.txt', 'r')
st = file.readline()
while True:
    line = file.readline()
    if not line:
        break
    stickers.append(line.strip())
file.close

bot.send_message(member_id, "Текст который отправиться при запуске бота")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print('Мы запустились в ' + current_time)

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    randomer = randrange(3)
    if randomer == 1:
        bot.send_sticker(member_id, random.choice(stickers))
        print('Отправлено в ' + current_time)
    else:
        randomer = randrange(3)
        bot.send_message(member_id, random.choice(compliments))
        if randomer == 1:
            bot.send_sticker(member_id, random.choice(stickers_mini))
        print('Комплимент отправлен в ' + current_time)
    time.sleep(random.choice(timer))

bot.infinity_polling()