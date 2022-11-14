import telebot
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

bot = telebot.TeleBot(config["BOT_CONFIG"]["BOT_TOKEN"])

bot.send_message(config["BOT_CONFIG"]["ADM_ID"], "Пока")
