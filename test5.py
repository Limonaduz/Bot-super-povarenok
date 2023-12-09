'''Библиотека aiogram для разработки ботов'''
from aiogram import Bot, Dispatcher, executor, types

bot = Bot('6767871779:AAHkGzY8z3_CML0IxUmW-Z7ec5D4D-nu-Rc')
db = Dispatcher(bot)

image = 'dark.jpg'

@db.message_handler(commands=['photo'])
async def start(message: types.Message):
    await message.answer('здарова')
    await message.reply('2sd')

    file = open('./' + image, 'rb')
    await message.answer_photo(file)


@db.message_handler(commands=['inline'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('utube', url = 'https://youtube.com')
    btn2 = types.InlineKeyboardButton('sdsds', callback_data= 'hello')
    markup.row(btn1, btn2)
    await message.reply('Good morning', reply_markup= markup)

@db.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)

@db.message_handler(commands=['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton('utube')
    btn2 = types.KeyboardButton('vk')
    markup.add(btn1)
    markup.add(btn2)
    await message.answer('FFFFFF', reply_markup=markup)


executor.start_polling(db)