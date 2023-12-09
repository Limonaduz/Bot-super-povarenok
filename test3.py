'''БОТ ДЛЯ ИЗУЧЕНИЯ ПОГОДЫ'''

import telebot
import requests
import json



bot = telebot.TeleBot('6767871779:AAHkGzY8z3_CML0IxUmW-Z7ec5D4D-nu-Rc')
API = 'ce8cb71bef4d32de3e887a0ad1e4b98c'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Бот-погодник активирован')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()

    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if not (res.status_code == 200):
        bot.reply_to(message, 'Город указан неверно')
    data = json.loads(res.text)
    temp = data["main"]["temp"]

    bot.send_message(message.chat.id, f'Температура в городе сейчас: {temp}')

    image = 'sun.jpg' if temp > 5.0 else 'dark.jpg'
    file = open('./'+image, 'rb')

    bot.reply_to(message, file)
    #else:
    #    bot.send_message(message.chat.id, "Город указан неверно")

bot.polling(none_stop = True)