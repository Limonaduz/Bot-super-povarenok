'''БОТ ДЛЯ КОНВЕРТАЦИИ ВАЛЮТ'''
from currency_converter import  CurrencyConverter
import telebot
from telebot import types


bot = telebot.TeleBot('6767871779:AAHkGzY8z3_CML0IxUmW-Z7ec5D4D-nu-Rc')
currency = CurrencyConverter()
amount = 0


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Конвертер-бот активирован')
    bot.register_next_step_handler(message, summa)

def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Валюта указана не целочисленно, повторите попытку')
        bot.register_next_step_handler(message, summa)
        return

    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn_2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn_3 = types.InlineKeyboardButton('RUB/EUR', callback_data='rub/eur')
        btn_4 = types.InlineKeyboardButton('Пустое значение', callback_data='else')

        markup.add(btn_1, btn_2, btn_3, btn_4)
        bot.send_message(message.chat.id,'Введите сумму валюты', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Число должно быть больше 0, повторите попытку')
        bot.register_next_step_handler(message, summa)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id,f'Текущая конвертация 1 валюты в другую дает {round(res, 4)}\nМожете написать сумму заново')
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'Введите пару значений через слэщ (прим ***/***): ')
        bot.register_next_step_handler(call.message, my_currency)

def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'Получим {round(res, 4)}\nМожете написать сумму заново')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, 'Что-то не так, введите сумму заново')
        bot.register_next_step_handler(message, my_currency)


bot.polling(none_stop=True)