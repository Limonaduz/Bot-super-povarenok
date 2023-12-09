import telebot
import webbrowser
from telebot import  types

bot = telebot.TeleBot('6767871779:AAHkGzY8z3_CML0IxUmW-Z7ec5D4D-nu-Rc')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()

    btn1 = types.KeyboardButton('Переход на ютуб')
    btn2 = types.KeyboardButton('Delete photo ?')
    markup.row(btn1, btn2)
    btn3 = types.KeyboardButton('eVhange text ?')
    markup.row(btn3)

    #file = open('./photo1.jpg', 'rb')
    #bot.send_photo(message.chat.id, file, reply_markup=markup)
    file = open('./song.mp3', 'rb')
    bot.send_audio(message.chat.id, file, reply_markup=markup)
    #bot.send_message(message.chat.id, 'Здарова', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
def on_click(message):
    if message.text == 'Переход на ютуб':
        bot.send_message(message.chat.id, "переходим на сайт !")
    elif message.text == 'Delete photo ?':
        bot.send_message(message.chat.id, "Delete phot")
    elif message.text == 'eVhange text ?':
        bot.send_message(message.chat.id, "editing ytqag")
    bot.register_next_step_handler(message, start)

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    #добавление кнопки
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton('Переход на ютуб', url = 'https://youtube.com')
    btn2 = types.InlineKeyboardButton('Delete photo ?', callback_data='delete')
    markup.row(btn1, btn2)

    btn3 = types.InlineKeyboardButton('eVhange text ?', callback_data='edit')
    markup.row(btn3)

    bot.reply_to(message, 'do you wanna delete &', reply_markup = markup)

@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('This text edited',callback.message.chat.id, callback.message.message_id)

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://youtube.com')

@bot.message_handler(commands = ['start', 'attacki2'])
def main(message):
    bot.send_message(message.chat.id, 'Привеasdьчик, ')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, f'<b>Help info</b> <em><u>{message.from_user.last_name}, {message.from_user.first_name}</u></em>', parse_mode='html')

'''@bot.message_handler()
def info(message):
    if message.text.lower() == 'dsf':
        bot.send_message(message.chat.id, 'DSF WRITTEN АБЛБА')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    #elif message.text.lower() == 'armout':
       # bot.send_massage()
    else:
        bot.send_message(message.chat.id, 'Uncknown command')
'''
bot.polling(none_stop=True)
#bot.infinity_polling()