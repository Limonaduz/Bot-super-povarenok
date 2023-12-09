'''Web Apps. Полноценные веб приложения в Телеграм'''
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6767871779:AAHkGzY8z3_CML0IxUmW-Z7ec5D4D-nu-Rc')
db = Dispatcher(bot)

@db.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('website', web_app=WebAppInfo(url = "https://youtube.com") )
    markup.add(btn1)
    await message.answer('Hello', reply_markup=markup)



executor.start_polling(db)