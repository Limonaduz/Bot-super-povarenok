'''Библиотека aiogram для разработки ботов'''
import sqlite3
import telebot
from telebot import types

token1 = '5864816054:AAFmevmUky_hvyOeKS6W93b6StKy4kH3J3Q'

bot = telebot.TeleBot(token1)
####################

####################
#ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ УЧАСТКОВ
####################
# №1
# №2
# №3
index_value = None
item_value = None
# №4
newrec_name = None
newrec_portions = None
newrec_time = None
newrec_kcal = None
newrec_country = None
newrec_category = None
newrec_ingredients = None
newrec_recipe_text = None
####################

"""№1 СТАPT, СТАРТОВЫЕ КНОПКИ!!!"""
@bot.message_handler(commands=['start'])
#стартовая фунция приветствия пользователя
def start(message):
    bot.send_message(message.chat.id, 'Приветству вас, ваш поварской помошник MetroplexAsterix\n'
                         'Чем я могу вас помочь ?\n'
                         'Напишите любое сообщение, чтобы продолжить!')

    #активация базы данных base1.sql
    db = sqlite3.connect('megtron.sql')
    c = db.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS recep (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                portions INTEGER,
                time TEXT,
                kcal INTEGER,
                country TEXT,
                category TEXT,
                ingredients TEXT,
                recipe TEXT
    )""")

    db.commit()
    c.close()
    db.close()

@bot.message_handler(commands=['startbtns'])
def start_btns(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('кухни мира')
    btn2 = types.KeyboardButton('категории')
    btn3 = types.KeyboardButton('искать рецепт')
    btn4 = types.KeyboardButton('запись рецепта')
    btn5 = types.KeyboardButton('отключение бота')
    markup.row(btn1, btn2)
    markup.row(btn3, btn5, btn4)

    bot.register_next_step_handler(message, on_click)

    bot.send_message(message.chat.id,'Активация', reply_markup=markup)

###############################################################################
def on_click(message):
    '''КЛИК - АКТИВАЦИЯ 4 КАТЕГОРИЙ ВЫБОРА В БОТЕ'''
    if message.text == 'кухни мира':
        world_recipes(message)
    elif message.text == 'категории':
        categories(message)
    elif message.text == 'искать рецепт':
        pass
    elif message.text == 'отключение бота':
        disconnect_bot(message)
###'''@bot.callback_query_handlers(func=lambda message:True)
@bot.message_handler(commands=['countries'])
def world_recipes(message):
    '''КУХНИ МИРА'''
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton('Русская', callback_data='russia')
    btn2 = types.InlineKeyboardButton('Индийская', callback_data='india')
    btn3 = types.InlineKeyboardButton('Итальянска', callback_data='italy')
    btn4 = types.InlineKeyboardButton('Французская', callback_data='france')
    btn5 = types.InlineKeyboardButton('Японская', callback_data='japan')
    btn6 = types.InlineKeyboardButton('❤️Вернуться в главное меню❤️', callback_data='main_menu')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id, 'Выберите кухню: ', reply_markup=markup)
#############################
#############################
#############################
@bot.callback_query_handler(func=lambda call:call.data == "russia")
def country_handle_btn1(call):
    ccc = 'Русская'
    country_search_recipe(call.message, ccc)

@bot.callback_query_handler(func=lambda call:call.data == "india")
def country_handle_btn2(call):
    ccc = 'Индийская'
    country_search_recipe(call.message, ccc)

@bot.callback_query_handler(func=lambda call:call.data == "italy")
def country_handle_btn3(call):
    ccc = 'Итальянская'
    country_search_recipe(call.message, ccc)

@bot.callback_query_handler(func=lambda call:call.data == "france")
def country_handle_btn4(call):
    ccc = 'Французская'
    country_search_recipe(call.message, ccc)

@bot.callback_query_handler(func=lambda call:call.data == "japan")
def country_handle_btn5(call):
    ccc = 'Японская'
    country_search_recipe(call.message, ccc)


def country_search_recipe(message, ccc):
    #ПОИСК РЕЦЕПТА ИЗ БАЗЫ ДАННЫХ по категории отнажатия кнопки btn2 закуски
    chat_id = message.chat.id
    country = ccc
    country_search_vivod_zakus(message, country)

def country_search_vivod_zakus(message, country):
    #вывод всех рецептов с фильтром на закуски
    chat_id = message.chat.id
    #получение локального фильтра на закуски
    coun = country

    db = sqlite3.connect('megtron.sql')
    c = db.cursor()

    c.execute("SELECT * FROM recep WHERE country=?", (coun,))

    recipe = c.fetchall()
    if recipe:
        # Распаковка элементов записи рецепта
        for rec in recipe:
            recipe_id, name, portions, time, kcal, country, category, ingredients, recipe_text = rec
            bot.send_message(chat_id, "🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁")
            bot.send_message(chat_id, f"ID: {id}")
            bot.send_message(chat_id, f"Название: {name}")
            bot.send_message(chat_id, f"Число порций: {portions}")
            bot.send_message(chat_id, f"Время готовки мин: {time}")
            bot.send_message(chat_id, f"Калорийность в ккал: {kcal}")
            bot.send_message(chat_id, f"Родина блюда: {country}")
            bot.send_message(chat_id, f"Родина блюда: {category}")
            bot.send_message(chat_id, f"Родина блюда: {ingredients}")
            bot.send_message(chat_id, f"Родина блюда: {recipe_text}")
            bot.send_message(chat_id, "🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁")

        # закрытие базы данных
        db.commit()
        c.close()
        db.close()
    else:
        bot.send_message(chat_id, f"Нет в наличии страны {coun}")
        # закрытие базы данных
        db.commit()
        c.close()
        db.close()
#######################
#############################
#############################
#############################
#ГЛАВНАЯ ФУНКЦИЯ КАТЕГОРИЙ
@bot.message_handler(commands=['categories'])
def categories(message):
    '''КАТЕГОРИИ☘️'''
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('Выпечка, десерты', callback_data='выпечка')
    btn2 = types.InlineKeyboardButton('Закуски', callback_data='закуски')
    btn3 = types.InlineKeyboardButton('Завтраки', callback_data='завтраки')
    btn4 = types.InlineKeyboardButton('Основные блюда', callback_data='основные_блюда')
    btn5 = types.InlineKeyboardButton('Салаты', callback_data='салаты')
    btn6 = types.InlineKeyboardButton('❤️Вернуться в главное меню❤️', callback_data='main_menu')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id, 'Выберите Категорию ', reply_markup=markup)
#поиск рецептов по категориям 2
#вспомогательные функции поиска рецептов по категориям
@bot.callback_query_handler(func=lambda call:call.data == "выпечка")
def bakery_category_handle_btn1(call):
    bakery_category_search_recipe(call.message)

def bakery_category_search_recipe(message):
    #ПОИСК РЕЦЕПТА ИЗ БАЗЫ ДАННЫХ по категории отнажатия кнопки btn1 выпечка
    chat_id = message.chat.id
    categ = "Мучное"
    bakery_category_search_vivod(message, categ)

def bakery_category_search_vivod(message, categ):
    #вывод всех рецептов с фильтром на выпечку
    chat_id = message.chat.id
    #получение локального фильтра на мучное
    muchnoe = categ

    db = sqlite3.connect('megtron.sql')
    c = db.cursor()

    c.execute("SELECT * FROM recep WHERE category=?", (muchnoe,))

    recipe = c.fetchall()
    if recipe:
        # Распаковка элементов записи рецепта
        for rec in recipe:
            recipe_id, name, portions, time, kcal, country, category, ingredients, recipe_text = rec
            bot.send_message(chat_id, "🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞")
            bot.send_message(chat_id, f"ID: {id}")
            bot.send_message(chat_id, f"Название: {name}")
            bot.send_message(chat_id, f"Число порций: {portions}")
            bot.send_message(chat_id, f"Время готовки мин: {time}")
            bot.send_message(chat_id, f"Калорийность в ккал: {kcal}")
            bot.send_message(chat_id, f"Родина блюда: {country}")
            bot.send_message(chat_id, f"Родина блюда: {category}")
            bot.send_message(chat_id, f"Родина блюда: {ingredients}")
            bot.send_message(chat_id, f"Родина блюда: {recipe_text}")
            bot.send_message(chat_id, "🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞")

        # закрытие базы данных
        db.commit()
        c.close()
        db.close()
    else:
        bot.send_message(chat_id, "Нет в наличии")
        # закрытие базы данных
        db.commit()
        c.close()
        db.close()
#######################
@bot.callback_query_handler(func=lambda call:call.data == "закуски")
def snack_category_handle_btn2(call):
    snack_category_search_recipe(call.message)

def snack_category_search_recipe(message):
    #ПОИСК РЕЦЕПТА ИЗ БАЗЫ ДАННЫХ по категории отнажатия кнопки btn2 закуски
    chat_id = message.chat.id
    categ = "закуски"
    snack_category_search_vivod(message, categ)

def snack_category_search_vivod(message, categ):
    #вывод всех рецептов с фильтром на закуски
    chat_id = message.chat.id
    #получение локального фильтра на закуски
    zakus = categ

    db = sqlite3.connect('megtron.sql')
    c = db.cursor()

    c.execute("SELECT * FROM recep WHERE category=?", (zakus,))

    recipe = c.fetchall()
    if recipe:
        # Распаковка элементов записи рецепта
        for rec in recipe:
            recipe_id, name, portions, time, kcal, country, category, ingredients, recipe_text = rec
            bot.send_message(chat_id, "🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿")
            bot.send_message(chat_id, f"ID: {id}")
            bot.send_message(chat_id, f"Название: {name}")
            bot.send_message(chat_id, f"Число порций: {portions}")
            bot.send_message(chat_id, f"Время готовки мин: {time}")
            bot.send_message(chat_id, f"Калорийность в ккал: {kcal}")
            bot.send_message(chat_id, f"Родина блюда: {country}")
            bot.send_message(chat_id, f"Родина блюда: {category}")
            bot.send_message(chat_id, f"Родина блюда: {ingredients}")
            bot.send_message(chat_id, f"Родина блюда: {recipe_text}")
            bot.send_message(chat_id, "🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿🍿")

        # закрытие базы данных
        db.commit()
        c.close()
        db.close()
    else:
        bot.send_message(chat_id, "Нет в наличии")
        # закрытие базы данных
        db.commit()
        c.close()
        db.close()
#######################
@bot.callback_query_handler(func=lambda call:call.data == "завтраки")
def breakfast_category_handle_btn3(call):
    breakfast_category_search_recipe(call.message)

def breakfast_category_search_recipe(message):
    #ПОИСК РЕЦЕПТА ИЗ БАЗЫ ДАННЫХ по категории отнажатия кнопки btn3 завтраки
    chat_id = message.chat.id
    categ = "завтраки"
    breakfast_category_search_vivod(message, categ)

def breakfast_category_search_vivod(message, categ):
    #вывод всех рецептов с фильтром на выпечку
    chat_id = message.chat.id
    #получение локального фильтра на мучное
    zavtrak = categ

    db = sqlite3.connect('megtron.sql')
    c = db.cursor()

    c.execute("SELECT * FROM recep WHERE category=?", (zavtrak,))

    recipe = c.fetchall()
    if recipe:
        # Распаковка элементов записи рецепта
        for rec in recipe:
            recipe_id, name, portions, time, kcal, country, category, ingredients, recipe_text = rec
            bot.send_message(chat_id, "🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚")
            bot.send_message(chat_id, f"ID: {id}")
            bot.send_message(chat_id, f"Название: {name}")
            bot.send_message(chat_id, f"Число порций: {portions}")
            bot.send_message(chat_id, f"Время готовки мин: {time}")
            bot.send_message(chat_id, f"Калорийность в ккал: {kcal}")
            bot.send_message(chat_id, f"Родина блюда: {country}")
            bot.send_message(chat_id, f"Родина блюда: {category}")
            bot.send_message(chat_id, f"Родина блюда: {ingredients}")
            bot.send_message(chat_id, f"Родина блюда: {recipe_text}")
            bot.send_message(chat_id, "🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚")

        # закрытие базы данных
        db.commit()
        c.close()
        db.close()
    else:
        bot.send_message(chat_id, "Нет в наличии")
        # закрытие базы данных
        db.commit()
        c.close()
        db.close()
#######################
@bot.callback_query_handler(func=lambda call:call.data == "основные_блюда")
def important_dish_category_handle_btn4(call):
    important_dish_category_search_recipe(call.message)

def important_dish_category_search_recipe(message):
    #ПОИСК РЕЦЕПТА ИЗ БАЗЫ ДАННЫХ по категории отнажатия кнопки btn3 завтраки
    chat_id = message.chat.id
    categ = "основные_блюда"
    important_dish_category_search_vivod(message, categ)

def important_dish_category_search_vivod(message, categ):
    #вывод всех рецептов с фильтром на выпечку
    chat_id = message.chat.id
    #получение локального фильтра на мучное
    important_dish = categ

    db = sqlite3.connect('megtron.sql')
    c = db.cursor()

    c.execute("SELECT * FROM recep WHERE category=?", (important_dish,))

    recipe = c.fetchall()
    if recipe:
        # Распаковка элементов записи рецепта
        for rec in recipe:
            recipe_id, name, portions, time, kcal, country, category, ingredients, recipe_text = rec
            bot.send_message(chat_id, "🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜")
            bot.send_message(chat_id, f"ID: {id}")
            bot.send_message(chat_id, f"Название: {name}")
            bot.send_message(chat_id, f"Число порций: {portions}")
            bot.send_message(chat_id, f"Время готовки мин: {time}")
            bot.send_message(chat_id, f"Калорийность в ккал: {kcal}")
            bot.send_message(chat_id, f"Родина блюда: {country}")
            bot.send_message(chat_id, f"Родина блюда: {category}")
            bot.send_message(chat_id, f"Родина блюда: {ingredients}")
            bot.send_message(chat_id, f"Родина блюда: {recipe_text}")
            bot.send_message(chat_id, "🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜")
    else:
        bot.send_message(chat_id, "Нет в наличии")
        # закрытие базы данных
        db.commit()
        c.close()
        db.close()
#######################
@bot.callback_query_handler(func=lambda call:call.data == "салаты")
def salad_category_handle_btn5(call):
    salad_category_search_recipe(call.message)

def salad_category_search_recipe(message):
    #ПОИСК РЕЦЕПТА ИЗ БАЗЫ ДАННЫХ по категории отнажатия кнопки btn3 завтраки
    chat_id = message.chat.id
    categ = "салаты"
    salad_category_search_vivod(message, categ)

def salad_category_search_vivod(message, categ):
    #вывод всех рецептов с фильтром на выпечку
    chat_id = message.chat.id
    #получение локального фильтра на мучное
    salad = categ

    db = sqlite3.connect('megtron.sql')
    c = db.cursor()

    c.execute("SELECT * FROM recep WHERE category=?", (salad,))

    recipe = c.fetchall()
    if recipe:
        print(recipe)
        # Распаковка элементов записи рецепта
        for rec in recipe:
            recipe_id, name, portions, time, kcal, country, category, ingredients, recipe_text = rec
            bot.send_message(chat_id, "🥬🥬🥬🥬🥬🥬🥬🥬🥬🥬🥬🥬🥬🥬🥬🥬🥬🥬🥬")
            bot.send_message(chat_id, f"ID: {id}")
            bot.send_message(chat_id, f"Название: {name}")
            bot.send_message(chat_id, f"Число порций: {portions}")
            bot.send_message(chat_id, f"Время готовки мин: {time}")
            bot.send_message(chat_id, f"Калорийность в ккал: {kcal}")
            bot.send_message(chat_id, f"Родина блюда: {country}")
            bot.send_message(chat_id, f"Родина блюда: {category}")
            bot.send_message(chat_id, f"Родина блюда: {ingredients}")
            bot.send_message(chat_id, f"Родина блюда: {recipe_text}")
            bot.send_message(chat_id, "🥬🥬🥬🥬🥬🥬🥬🥬🥬🥬🥬🥬🥬🥬🥬🥬🥬🥬🥬")

        # закрытие базы данных
        db.commit()
        c.close()
        db.close()
    else:
        bot.send_message(chat_id, "Нет в наличии")
        # закрытие базы данных
        db.commit()
        c.close()
        db.close()
#######################


def disconnect_bot(message):
    '''РЕСТАРТ(ОТКЛЮЧЕНИЕ) БОТА'''
    start(message)
###############################################################################
###############################################################################


@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    '''_Категроии'''
    if callback.data == 'выпечка':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)

    if callback.data == 'закуски':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    if callback.data == 'завтраки':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    if callback.data == 'основные_блюда':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    if callback.data == 'салаты':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    if callback.data == 'main_menu':
        #tart(callback)
        #bot.reply_to(callback.message)
       # webbrowser.open('https://limonaduz.github.io/indxer-test1.github.io/')
        pass
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    #################
    #УЧАСТОК СОЗДАНИЯ РЕЦЕПТОВ И ВНУТРЕННЕГО ВЗАИМОДЕЙСТВИЯ С НИМИ
    #################
    call = callback
    chat_id = call.message.chat.id
    # message_id = call.message.message_id
    if call.data == 'btn1':
        # переход нв
        bot.send_message(chat_id, 'Вы нажали на кнопку 1')
        save_recipe_name(call.message)
    elif call.data == 'btn2':
        # переход на
        bot.send_message(chat_id, 'Вы нажали на кнопку 2')
        save_recipe_portions(call.message)
    elif call.data == 'btn3':
        # переход на
        bot.send_message(chat_id, 'Вы нажали на кнопку 3')
        save_recipe_time(call.message)
    elif call.data == 'btn4':
        # переход на
        bot.send_message(chat_id, 'Вы нажали на кнопку 4')
        save_recipe_kcal(call.message)
    elif call.data == 'btn5':
        # переход на
        bot.send_message(chat_id, 'Вы нажали на кнопку 5')
        save_recipe_country(call.message)
    elif call.data == 'btn6':
        # переход на
        bot.send_message(chat_id, 'Вы нажали на кнопку 6')
        save_recipe_category(call.message)
    elif call.data == 'btn7':
        # переход на
        bot.send_message(chat_id, 'Вы нажали на кнопку 7')
        save_recipe_ingredients(call.message)
    elif call.data == 'btn8':
        # переход на
        bot.send_message(chat_id, 'Вы нажали на кнопку 8')
        save_recipe_text_description(call.message)
    # Добавьте дополнительные условия для остальных кнопок

    # Отправьте ответное сообщение в чат
    bot.answer_callback_query(callback_query_id=call.id, text='Кнопка обработана')


'''№2 УЧАСТОК СОЗДАНИЯ РЕЦЕПТОВ И ВНУТРЕННЕГО ВЗАИМОДЕЙСТВИЯ С НИМИ'''
'''СОХРАНЕНИЕ ОТДЕЛЬНЫХ КОМПОНЕНТОВ РЕЦЕПТА'''
@bot.message_handler(commands=['createrecipe'])
def create_recipe(message):
    #СОЗДАНИЕ НОВОГО РЕЦЕПТА
    get_recipe_data(message)


def get_recipe_data(message):
    chat_id = message.chat.id

    # Запрос инфы(какой-то одной) о новом рицепте у пользователя
    #bot.send_message(chat_id, 'Введите пожалуйста, что вы хотите сделать с рецептом ?: ')


    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Название блюда', callback_data= 'btn1')
    btn2 = types.InlineKeyboardButton('Число порций', callback_data= 'btn2')
    btn3 = types.InlineKeyboardButton('Время готовки', callback_data= 'btn3')
    btn4 = types.InlineKeyboardButton('Килокалории', callback_data= 'btn4')
    btn5 = types.InlineKeyboardButton('Страна', callback_data= 'btn5')
    btn6 = types.InlineKeyboardButton('Категория блюда', callback_data= 'btn6')
    btn7 = types.InlineKeyboardButton('Ингредиенты', callback_data= 'btn7')
    btn8 = types.InlineKeyboardButton('Текст рецепта', callback_data= 'btn8')

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(chat_id, 'Введите пожалуйста, что вы хотите сделать с рецептом ?: ', reply_markup=markup)


    #bot.register_next_step_handler(message, save_recipe_name)


def save_recipe_name(message):
    chat_id = message.chat.id
    recipe_name = message.text

    # Сохраните название рецепта в базу данных
    db = sqlite3.connect('megtron.sql')
    c = db.cursor()
    c.execute("INSERT INTO recep (name) VALUES (?)", (recipe_name,))

    bot.send_message(message.chat.id, str(c.fetchall()))

    recipe_id = c.lastrowid

    db.commit()
    c.close()
    db.close()

    #сообщение о сохранении данных
    bot.send_message(message.chat.id, 'Данные успешно сохранены в таблицу')
    #DELETE THIS STUFF
    bot.send_message(message.chat.id, f'Репепт сохранен с id: {recipe_id}')

def save_recipe_portions(message):
    chat_id = message.chat.id
    r_portions = message.text

    # Сохраните название рецепта в базу данных
    db = sqlite3.connect('megtron.sql')
    c = db.cursor()
    c.execute("INSERT INTO recep (portions) VALUES (?)", (r_portions,))

    bot.send_message(message.chat.id, str(c.fetchall()))

    recipe_id = c.lastrowid

    db.commit()
    c.close()
    db.close()

    # сообщение о сохранении данных
    bot.send_message(message.chat.id, 'Данные успешно сохранены в таблицу')
    # DELETE THIS STUFF
    bot.send_message(message.chat.id, f'Репепт сохранен с id: {recipe_id}')

def save_recipe_time(message):
    chat_id = message.chat.id
    r_time = message.text

    # Сохраните название рецепта в базу данных
    db = sqlite3.connect('megtron.sql')
    c = db.cursor()
    c.execute("INSERT INTO recep (time) VALUES (?)", (r_time,))

    bot.send_message(message.chat.id, str(c.fetchall()))

    recipe_id = c.lastrowid

    db.commit()
    c.close()
    db.close()

    # сообщение о сохранении данных
    bot.send_message(message.chat.id, 'Данные успешно сохранены в таблицу')
    # DELETE THIS STUFF
    bot.send_message(message.chat.id, f'Репепт сохранен с id: {recipe_id}')

def save_recipe_kcal(message):
    chat_id = message.chat.id
    r_kcal = message.text

    # Сохраните название рецепта в базу данных
    db = sqlite3.connect('megtron.sql')
    c = db.cursor()
    c.execute("INSERT INTO recep (kcal) VALUES (?)", (r_kcal,))

    bot.send_message(message.chat.id, str(c.fetchall()))

    recipe_id = c.lastrowid

    db.commit()
    c.close()
    db.close()

    # сообщение о сохранении данных
    bot.send_message(message.chat.id, 'Данные успешно сохранены в таблицу')
    # DELETE THIS STUFF
    bot.send_message(message.chat.id, f'Репепт сохранен с id: {recipe_id}')

def save_recipe_country(message):
    chat_id = message.chat.id
    r_country = message.text

    # Сохраните название рецепта в базу данных
    db = sqlite3.connect('megtron.sql')
    c = db.cursor()
    c.execute("INSERT INTO recep (country) VALUES (?)", (r_country,))

    bot.send_message(message.chat.id, str(c.fetchall()))

    recipe_id = c.lastrowid

    db.commit()
    c.close()
    db.close()

    # сообщение о сохранении данных
    bot.send_message(message.chat.id, 'Данные успешно сохранены в таблицу')
    # DELETE THIS STUFF
    bot.send_message(message.chat.id, f'Репепт сохранен с id: {recipe_id}')

def save_recipe_category(message):
    chat_id = message.chat.id
    r_category = message.text

    # Сохраните название рецепта в базу данных
    db = sqlite3.connect('megtron.sql')
    c = db.cursor()
    c.execute("INSERT INTO recep (category) VALUES (?)", (r_category,))

    bot.send_message(message.chat.id, str(c.fetchall()))

    recipe_id = c.lastrowid

    db.commit()
    c.close()
    db.close()

    # сообщение о сохранении данных
    bot.send_message(message.chat.id, 'Данные успешно сохранены в таблицу')
    # DELETE THIS STUFF
    bot.send_message(message.chat.id, f'Репепт сохранен с id: {recipe_id}')

def save_recipe_ingredients(message):
    chat_id = message.chat.id
    r_ingredients = message.text

    # Сохраните название рецепта в базу данных
    db = sqlite3.connect('megtron.sql')
    c = db.cursor()
    c.execute("INSERT INTO recep (ingredients) VALUES (?)", (r_ingredients,))

    bot.send_message(message.chat.id, str(c.fetchall()))

    recipe_id = c.lastrowid

    db.commit()
    c.close()
    db.close()

    # сообщение о сохранении данных
    bot.send_message(message.chat.id, 'Данные успешно сохранены в таблицу')
    # DELETE THIS STUFF
    bot.send_message(message.chat.id, f'Репепт сохранен с id: {recipe_id}')


def save_recipe_text_description(message):
    '''СОЗДАНИЕ ОПИСАНИЯ(ИНСТРУКЦИИ) РЕЦЕАТА'''
    chat_id = message.chat.id
    r_text = message.text

    # Сохраните название рецепта в базу данных
    db = sqlite3.connect('megtron.sql')
    c = db.cursor()
    c.execute("INSERT INTO recep (recipe) VALUES (?)", (r_text,))

    bot.send_message(message.chat.id, str(c.fetchall()))

    recipe_id = c.lastrowid

    db.commit()
    c.close()
    db.close()

    # сообщение о сохранении данных
    bot.send_message(message.chat.id, 'Данные успешно сохранены в таблицу')
    # DELETE THIS STUFF
    bot.send_message(message.chat.id, f'Репепт сохранен с id: {recipe_id}')

#################
#################
#################

@bot.message_handler(commands=['1234'])
def vivod(message):
    #полный вывод всех таблиц и их элементов
    db = sqlite3.connect('megtron.sql')
    c = db.cursor()

    c.execute("SELECT * FROM recep")
    items = c.fetchall()
    bot.send_message(message.chat.id, str(items))


    db.commit()
    c.close()
    db.close()


'''№3 УЧАСТОК СВЕРХТОЧНОГО ВЫВОДА КОНКРЕТНЫХ ЗНАЧЕНИЙ ИЗ ТАБЛИЦ'''
@bot.message_handler(commands=['idsearch'])
def get_inputline_idindex(message):
    #введите в чилсовой форме индекс таблици
    chat_id = message.chat.id
    bot.send_message(chat_id, 'введите индекс таблици: ')
    bot.register_next_step_handler(message, _get_inputline_idindex)


def _get_inputline_idindex(message):
    global index_value
    chat_id = message.chat.id

    index_value = message.text
    bot.send_message(chat_id, index_value)

    get_inputline_itemnum(message)
    #удаление ненужного сообщения
    bot.delete_message(chat_id, message.message_id + 1)

def get_inputline_itemnum(message):
    #введите в чиловой форме номер ячейки интерисуемой таблици
    chat_id = message.chat.id
    bot.send_message(chat_id, 'введите номер ячейки от 1 до 8')
    bot.register_next_step_handler(message, _get_inputline_itemnum)


def _get_inputline_itemnum(message):
    global item_value
    chat_id = message.chat.id

    item_value = message.text
    bot.send_message(chat_id, item_value)

    sup_idsearch(message)
    #удаление ненужного сообщения
    bot.delete_message(chat_id, message.message_id + 1)


def sup_idsearch(message):
    global index_value
    global item_value
    chat_id = message.chat.id
    #ф-я сборщик индекса и itema для принудительного нахождения элемента
    db = sqlite3.connect('megtron.sql')
    c = db.cursor()
    #индекс элемента
    try:
        ind = int(index_value)
    except ValueError:
        bot.send_message(message.chat.id, "Некорректный индекс")
        return


    c.execute("SELECT * FROM recep WHERE id=?",(ind,))
    item = c.fetchone()
    if item:
        #Если есть элемент, то он выведется в соответствии индексу
        path = item[int(item_value)]
        bot.send_message(chat_id, 'Получен элемент: ')
        bot.send_message(message.chat.id, path)
    else:
        bot.send_message(message.chat.id, "Нет элемента с указанным индексом")

    #обнуление глоб переменных
    index_value = None
    item_value = None

    db.commit()
    c.close()
    db.close()

'''№4 УЧАСТОК РЕЖИМА ЗАПИСИ ПОЛНОСТЬЮ НОВОГО РИЦЕПТА, ЕГО ДОБАВЛЕНИЯ И ВЫВОДА'''
@bot.message_handler(commands=['createfullrecipe'])
def new_recept(message):
    get_new_recipe_data(message)

def get_new_recipe_data(message):
    #активация режима записи и добавления полного нового рецепта
    chat_id = message.chat.id
    bot.send_message(chat_id, "Запущен режим создания полного  рецепта, пожалуйста, \n"
                              "вводите данные по порядку.\n"
                              "Введите название рецепта (блюда)")

    bot.register_next_step_handler(message, new_recipe_name)


def new_recipe_name(message):
    global newrec_name
    newrec_name = message.text

    chat_id = message.chat.id
    bot.send_message(chat_id, newrec_name)
    bot.send_message(chat_id, 'Введите число порций')
    bot.register_next_step_handler(message, new_recipe_portions)
    #удаление побочного сообщения
    bot.delete_message(chat_id, message.message_id - 1)


def new_recipe_portions(message):
    global newrec_portions
    newrec_portions = message.text

    chat_id = message.chat.id
    bot.send_message(chat_id, newrec_portions)
    bot.send_message(chat_id, 'Введите среднее время готовки')
    bot.register_next_step_handler(message, new_recipe_time)
    # удаление побочного сообщения
    bot.delete_message(chat_id, message.message_id - 1)
    bot.delete_message(chat_id, message.message_id - 2)


def new_recipe_time(message):
    global newrec_time
    newrec_time = message.text

    chat_id = message.chat.id
    bot.send_message(chat_id, newrec_time)
    bot.send_message(chat_id, 'Введите среднее количество кикакалорий на порцию')
    bot.register_next_step_handler(message, new_recipe_kcal)
    # удаление побочного сообщения
    bot.delete_message(chat_id, message.message_id - 1)
    bot.delete_message(chat_id, message.message_id - 2)


def new_recipe_kcal(message):
    global newrec_kcal
    newrec_kcal = message.text

    chat_id = message.chat.id
    bot.send_message(chat_id, newrec_kcal)
    bot.send_message(chat_id, 'Введите страну Родину блюда')
    bot.register_next_step_handler(message, new_recipe_country)
    # удаление побочного сообщения
    bot.delete_message(chat_id, message.message_id - 1)
    bot.delete_message(chat_id, message.message_id - 2)


def new_recipe_country(message):
    global  newrec_country
    newrec_country = message.text

    chat_id = message.chat.id
    bot.send_message(chat_id, newrec_country)
    bot.send_message(chat_id, 'Введите категорию/разновидность блюда')
    bot.register_next_step_handler(message, new_recipe_category)
    # удаление побочного сообщения
    bot.delete_message(chat_id, message.message_id - 1)
    bot.delete_message(chat_id, message.message_id - 2)


def new_recipe_category(message):
    global newrec_category
    newrec_category = message.text

    chat_id = message.chat.id
    bot.send_message(chat_id, newrec_category)
    bot.send_message(chat_id, 'Введите список ингредиентов через запятую')
    bot.register_next_step_handler(message, new_recipe_ingredients)
    # удаление побочного сообщения
    bot.delete_message(chat_id, message.message_id - 1)
    bot.delete_message(chat_id, message.message_id - 2)


def new_recipe_ingredients(message):
    global newrec_ingredients
    newrec_ingredients = message.text

    chat_id = message.chat.id
    bot.send_message(chat_id, newrec_ingredients)
    bot.send_message(chat_id, 'Введите пошаговое описание рецепта')
    bot.register_next_step_handler(message, opent_entry_close_database_full_recipe)
    # удаление побочного сообщения
    bot.delete_message(chat_id, message.message_id - 1)
    bot.delete_message(chat_id, message.message_id - 2)


def opent_entry_close_database_full_recipe(message):
    # создание имени новому рецепту
    global newrec_name
    global newrec_portions
    global newrec_time
    global newrec_kcal
    global newrec_country
    global newrec_category
    global newrec_ingredients
    global newrec_recipe_text
    #присвоение глобальной переменной текста значение из сообщения
    newrec_recipe_text = message.text
    #перевод глобальных переменных в локальные
    name = newrec_name
    portions = newrec_portions
    time = newrec_time
    kcal = newrec_kcal
    country = newrec_country
    category = newrec_category
    ingredients = newrec_ingredients
    text = newrec_recipe_text


    chat_id = message.chat.id
    bot.send_message(chat_id, message.text)


    # Сохраните название рецепта в базу данных
    db = sqlite3.connect('megtron.sql')
    c = db.cursor()
    # обработка значений в функциях под каждое значение таблици с последующим заполнением таблици
    c.execute("INSERT INTO recep (name, portions, time, kcal, country, category, ingredients, recipe) VALUES (?,?,?,?,?,?,?,?)",
              (name, portions, time, kcal, country, category, ingredients, text))

    # вывод id готового рецепта и всего остального
    bot.send_message(message.chat.id, str(c.fetchall()))
    recipe_id = c.lastrowid

    # закрытие базы данных
    db.commit()
    c.close()
    db.close()

    # сообщение о сохранении данных
    bot.send_message(message.chat.id, 'Данные успешно сохранены в таблицу')
    # DELETE THIS STUFF
    bot.send_message(message.chat.id, f'Репепт сохранен с id: {recipe_id}')

    #анулирование глобальных переменных
    newrec_name = None
    newrec_portions = None
    newrec_time = None
    newrec_kcal = None
    newrec_country = None
    newrec_category = None
    newrec_ingredients = None
    newrec_recipe_text = None

'''№5 УЧАССТОК ГРАФИЧЕСКИ ЦЕЛОСТНОГО ВЫВОДА РЕЦЕПТА ИЗ ТАБЛИЦИ'''
@bot.message_handler(commands=['recipegraph'])
def recipe_graph_start(message):
    chat_id = message.chat.id

    bot.send_message(chat_id, "Запущен режим вывода графически целостного рецепта")
    bot.send_message(chat_id, "Введите id для выбора по id или name по названию")
    bot.register_next_step_handler(message, get_vibor)


def get_vibor(message):
    chat_id = message.chat.id
    if message.text == 'id':
        bot.send_message(chat_id, "введите id (номер) рецепта в виде числа")
        enter_id(message)
    elif message.text == 'name':
        bot.send_message(chat_id,"введите name (название) блюда")
        enter_name(message)

def enter_id(message):
    chat_id = message.chat.id
    bot.delete_message(chat_id, message.message_id -1)
    bot.delete_message(chat_id, message.message_id -2)
    bot.register_next_step_handler(message, get_recipe_by_id)


def enter_name(message):
    chat_id = message.chat.id
    bot.delete_message(chat_id, message.message_id -1)
    bot.delete_message(chat_id, message.message_id -2)
    bot.register_next_step_handler(message, get_recipe_by_name)


def get_recipe_by_id(message):
    #получения графически целостного рецепта по id
    chat_id = message.chat.id
    #удаление предыдущих сообщений
    bot.delete_message(chat_id, message.message_id - 1)
    bot.delete_message(chat_id, message.message_id - 2)

    recipe_id = int(message.text)

    db = sqlite3.connect('megtron.sql')
    c = db.cursor()

    c.execute("SELECT * FROM recep WHERE id=?", (recipe_id,))

    recipe = c.fetchone()
    print(recipe)
    # Распаковка элементов записи рецепта
    recipe_id, name, portions, time, kcal, country, category, ingredients, recipe_text = recipe
    bot.send_message(chat_id, "🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏")
    bot.send_message(chat_id, f"ID: {id}")
    bot.send_message(chat_id, f"Название: {name}")
    bot.send_message(chat_id, f"Число порций: {portions}")
    bot.send_message(chat_id, f"Время готовки мин: {time}")
    bot.send_message(chat_id, f"Калорийность в ккал: {kcal}")
    bot.send_message(chat_id, f"Родина блюда: {country}")
    bot.send_message(chat_id, f"Родина блюда: {category}")
    bot.send_message(chat_id, f"Родина блюда: {ingredients}")
    bot.send_message(chat_id, f"Родина блюда: {recipe_text}")
    bot.send_message(chat_id, "🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏")

    # закрытие базы данных
    db.commit()
    c.close()
    db.close()

def get_recipe_by_name(message):
    #вывод графически целостного рецепта по названиб блюда
    chat_id = message.chat.id
    # удаление предыдущих сообщений
    bot.delete_message(chat_id, message.message_id - 1)
    bot.delete_message(chat_id, message.message_id - 2)

    name_r = message.text

    db = sqlite3.connect('megtron.sql')
    c = db.cursor()

    c.execute("SELECT * FROM recep WHERE name=?", (name_r,))

    recipe = c.fetchone()
    print(recipe)
    # Распаковка элементов записи рецепта
    recipe_id, name, portions, time, kcal, country, category, ingredients, recipe_text = recipe
    bot.send_message(chat_id, "🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎")
    bot.send_message(chat_id, f"ID: {id}")
    bot.send_message(chat_id, f"Название: {name}")
    bot.send_message(chat_id, f"Число порций: {portions}")
    bot.send_message(chat_id, f"Время готовки мин: {time}")
    bot.send_message(chat_id, f"Калорийность в ккал: {kcal}")
    bot.send_message(chat_id, f"Родина блюда: {country}")
    bot.send_message(chat_id, f"Родина блюда: {category}")
    bot.send_message(chat_id, f"Родина блюда: {ingredients}")
    bot.send_message(chat_id, f"Родина блюда: {recipe_text}")
    bot.send_message(chat_id, "🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎")

    # закрытие базы данных
    db.commit()
    c.close()
    db.close()


if __name__ == "__main__":
    bot.polling(none_stop=True)
