import telebot
import random
import time
import os
from datetime import datetime
from random import randrange
import configparser


config = configparser.ConfigParser()
config.read("settings.ini")

bot = telebot.TeleBot(config["BOT_CONFIG"]["BOT_TOKEN"])
member_id = config["BOT_CONFIG"]["MEMBER_ID"]

compliments = []
stickers = []
stickers_mini = []
images = []
timer = [7200, 9000, 10800, 12600, 14400]

# требуется создать файл с названием "compliments.txt" и вставить в него массив комплиментов
file = open('data/compliments.txt', 'r')
st = file.readline()
while True:
    line = file.readline()
    if not line:
        break
    compliments.append(line.strip())
file.close
# требуется создать файл с названием "stickers.txt" и вставить в него массив стикеров
file = open('data/stickers_mini.txt', 'r')
st = file.readline()
while True:
    line = file.readline()
    if not line:
        break
    stickers_mini.append(line.strip())
file.close
# требуется создать файл с названием "stickers_mini.txt" и вставить в него массив стикеров
file = open('data/stickers.txt', 'r')
st = file.readline()
while True:
    line = file.readline()
    if not line:
        break
    stickers.append(line.strip())
file.close

files = os.listdir('img/')
for file in files:
    images.append('img/' + file)

print(images)

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
        img = open(random.choice(images), 'rb')
        print(img)
        bot.send_photo(member_id, img)
    else:
        randomer = randrange(3)
        bot.send_message(member_id, random.choice(compliments))
        if randomer == 1:
            bot.send_sticker(member_id, random.choice(stickers_mini))
        print('Комплимент отправлен в ' + current_time)
    time.sleep(random.choice(timer))

bot.infinity_polling()
