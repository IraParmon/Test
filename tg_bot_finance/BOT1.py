import telebot

from telebot import types

from register import create_user, get_all_users, get_sum2, get_sum1, get_sum

from datetime import datetime

bot = telebot.TeleBot('5248756848:AAENL3NfNeNJWnHthybUTGYkK5aPD-7reAo')


@bot.message_handler(commands=['start'])
def menu(message):
    chat_id = message.chat.id
    keyboard_menu = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)

    btn_one = types.KeyboardButton('Расходы ⬇')
    btn_two = types.KeyboardButton('Доходы ⬆')
    btn_three = types.KeyboardButton('Кнопка3')

    keyboard_menu.add(btn_one, btn_two, btn_three)
    msg = bot.send_message(chat_id, 'Выберите категорию:',
                           reply_markup=keyboard_menu)
    bot.register_next_step_handler(msg, on_select_menu_button)


def on_select_menu_button(message):
    if message.text == "Расходы ⬇":
        button1_action(message)
    elif message.text == "Доходы ⬆":
        chat_id = message.chat.id
        keyboard_menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn_one = types.KeyboardButton('Зарплата')
        btn_two = types.KeyboardButton('Перевод')
        keyboard_menu.add(btn_one, btn_two)
        msg = bot.send_message(chat_id, 'Выберите категорию дохода:',
                               reply_markup=keyboard_menu)
        bot.register_next_step_handler(msg, on_select_menu_button)

        button2_action(message)


    elif message.text == "Кнопка3":
        button3_action(message)
    else:
        bot.send_message(message.chat.id, 'Что то пошло не так')


def button1_action(message):
    bot.send_message(message.chat.id, 'Вы нажали Кнопка1')


def button2_action(message):
    bot.send_message(message.chat.id, 'Вы нажали Кнопка2')


def button3_action(message):
    bot.send_message(message.chat.id, 'Вы нажали Кнопка3')


# bot.send_message(chat_id, text=f' Я знаю команды: /start для начала работы, /all для вывода суммы Доходов')

# @bot.message_handler(commands=['all'])
# def register(message):
#     income_sum = get_sum()
#     income_sum1 = get_sum1()
#     income_sum2 = get_sum2()
#     bot.send_message(message.chat.id, f'Сумма доходов ⬆: {income_sum[0][0]} руб.')
#     bot.send_message(message.chat.id, f' Зарплата: {income_sum1[0][0]} руб. Переводы: {income_sum2[0][0]} руб.')
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     keyboard = types.InlineKeyboardMarkup()
#     keyboard.add(types.InlineKeyboardButton(text="Расходы ⬇", callback_data='minus'))
#     keyboard.add(types.InlineKeyboardButton(text="Доходы ⬆", callback_data='plus'))
#     bot.send_message(message.chat.id, "Категории:", reply_markup=keyboard)
#
#     @bot.callback_query_handler(func=lambda call: True)
#     def button_callback(call):
#         if call.data == 'plus':
#
#             keyboard = types.InlineKeyboardMarkup()
#             keyboard.add(types.InlineKeyboardButton(text="Зарплата", callback_data="Зарплата"))
#             keyboard.add(types.InlineKeyboardButton(text="Перевод", callback_data="Перевод"))
#             keyboard.add(types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data="back"))
#             bot.send_message(message.chat.id, "Укажи вид дохода ", reply_markup=keyboard)
#
#             @bot.callback_query_handler(func=lambda call: True)
#             def button_callback(call):
#                 if call.data == 'Зарплата' or 'Перевод':
#                     INCOME = call.data
#                     print(INCOME)
#                     bot.send_message(message.chat.id, f"Введите сумму:")
#                     bot.register_next_step_handler(message, read_SUM, INCOME)
#
#                 else:
#                     bot.send_message(call.message.chat.id, f"Конец!!!")


#
# @bot.message_handler(content_types=['text'])
# def func(message):
#     if (message.text == "☝ Нажми для выбора категории"):
#         keyboard  = types.InlineKeyboardMarkup()
#         keyboard.add(types.InlineKeyboardButton(text="Расходы ⬇"))
#         keyboard.add(types.InlineKeyboardButton(text="Доходы ⬆"))
#         bot.send_message(message.chat.id, "＄", reply_markup=keyboard)


#
# elif (message.text == "Доходы ⬆"):
#     # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     # btn1 = types.KeyboardButton("Зарплата")
#     # btn2 = types.KeyboardButton("Перевод")
#     # back = types.KeyboardButton("Вернуться в главное меню")
#     # markup.add(btn1, btn2, back)
#     # bot.send_message(message.chat.id, text="Укажи вид дохода", reply_markup=markup)
#     # bot.register_next_step_handler(message, read_inc)
#
#
#
#     keyboard  = types.InlineKeyboardMarkup()
#     keyboard.add(types.InlineKeyboardButton(text="Зарплата", callback_data="Зарплата"))
#     keyboard.add(types.InlineKeyboardButton(text="Перевод", callback_data="Перевод"))
#     keyboard.add(types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data="back"))
#     bot.send_message(message.chat.id, "Укажи вид дохода ", reply_markup=keyboard)
#
# @bot.callback_query_handler(func=lambda call: True)
# def button_callback(call):
#     if call.data == 'Зарплата' or 'Перевод':
#         INCOME = call.data
#         print(INCOME)
#         bot.send_message(message.chat.id, f"Введите сумму:")
#         bot.register_next_step_handler(message, read_SUM, INCOME)
#
#     else:
#         bot.send_message(call.message.chat.id, f"Конец!!!")
#
#


# def read_inc(message):
#     INCOME = message.text
#     bot.send_message(message.chat.id, f"Введите сумму:")
#     bot.register_next_step_handler(message, read_SUM, INCOME)


# @bot.message_handler(content_types=['text'])
# def read_SUM(message, INCOME):
#     SUM = message.text
#     DATE = datetime.now().date()
#     bot.send_message(message.chat.id, f"Доход записан")
#     create_user(DATE, INCOME, SUM)
#
#     keyboard  = types.InlineKeyboardMarkup()
#     keyboard.add(types.InlineKeyboardButton(text="ДА", callback_data="yes"))
#     keyboard.add(types.InlineKeyboardButton(text="НЕТ", callback_data="no"))
#     bot.send_message(message.chat.id, "Вернуться в главное меню? ", reply_markup=keyboard)
#
#     @bot.callback_query_handler(func=lambda call: True)
#     def button_callback(call):
#         if call.data == 'yes':
#             return func
#         elif call.data == 'no':
#             bot.send_message(call.message.chat.id, f"Конец")
#


# def callback_inline(call):
#     if call.data == 'text':
#        print('press button "text"')
#     elif call.data == 'menu':
#        print('"press button menu"')


# @bot.message_handler(commands=['start'])
# def start_message(message):
#     print(f"Мне написал пользователь {message.chat.id}")
#     bot.send_message(message.chat.id, 'Выбери:  /income или /expenses')


# def read_name(message):
#             name = message.text
#             bot.send_message(message.chat.id, f"Введи пожалуйста свою почту")
#             bot.register_next_step_handler(message, read_email, name)
#             print(name)


#


# def read_name(message):
#     name = message.text
#     bot.send_message(message.chat.id, f"Напиши сумму:")
#     bot.register_next_step_handler(message, read_email, name)

#
# bot.send_message(message.chat.id, "У меня нет имени..")


#
# @bot.message_handler(commands=['income'])
# def income(message):
#     income = message.text
#     bot.send_message(message.chat.id, f"Выбери категорию:")
#     bot.register_next_step_handler(message, read_name, income)
#
#
# def read_name(message):
#     name = message.text
#     bot.send_message(message.chat.id, f"Введи пожалуйста свою почту")
#     bot.register_next_step_handler(message, read_email, name)
#
#     # user_id = message.chat.id
#     # if is_user_exists(user_id):
#     #     bot.send_message(user_id, 'Ты уже регистрировался!')
#     # else:
#     #     bot.send_message(message.chat.id, 'Введи пожалуйста свое имя и фамилию')
#     #     bot.register_next_step_handler(message, read_name)
#
#
# def read_name(message):
#     name = message.text
#     bot.send_message(message.chat.id, f"Введи пожалуйста свою почту")
#     bot.register_next_step_handler(message, read_email, name)
#
#
# def read_email(message, name):
#     email = message.text
#     bot.send_message(message.chat.id, f"Спасибо за регистрацию")
#     create_user(message.chat.id, name, email)
#
#


#
# bot.infinity_polling()
#
# # @bot.message_handler(commands=['start'])
# # def start_message(message):
# #     print(message)
# #     bot.send_message(message.chat.id, 'Введи, пожалуйста, свое имя')
# #     bot.register_next_step_handler(message, read_name)
# #
# #
# # def read_name(message):
# #     name = message.text
# #     bot.send_message(message.chat.id, f'Введи свою фамилию')
# #     bot.register_next_step_handler(message, read_sname, name)
# #
# #
# # def read_sname(message, name):
# #     sname = message.text
# #     bot.send_message(message.chat.id, f'Привет {name} {sname}')
#
#
bot.infinity_polling()


        button_expenses(message)

def button_expense(message):
    chat_id = message.chat.id
    keyboard_menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    btn_1 = types.KeyboardButton('Еда')
    btn_2 = types.KeyboardButton('Транспорт')
    btn_3 = types.KeyboardButton('Спорт')
    btn_4 = types.KeyboardButton('Образование')
    btn_5 = types.KeyboardButton('Одежда')
    btn_6 = types.KeyboardButton('Здоровье')
    btn_7 = types.KeyboardButton('Путешествия')
    btn_8 = types.KeyboardButton('Развлечения')
    btn_9 = types.KeyboardButton('Коммунальные')
    btn_10 = types.KeyboardButton('Назад')

    keyboard_menu.add(btn_1, btn_2, btn_3, btn_4,btn_5,btn_6,btn_7,btn_8, btn_9,btn_10)
    msg = bot.send_message(chat_id, 'Укажи вид дохода',
                           reply_markup=keyboard_menu)
    bot.register_next_step_handler(msg, read_type_exp)

def read_type_exp(message):
    if message.text == "Назад":
        start(message)
    else:
        read_exp(message)

def read_exp(message):
    INCOME = message.text
    bot.send_message(message.chat.id, f"Введите сумму:")
    bot.register_next_step_handler(message, read_SUM_exp, INCOME)

def read_SUM_exp(message, INCOME):
    SUM = message.text
    DATE = datetime.now().date()
    bot.send_message(message.chat.id, f"Доход записан")
    create_table_exp(DATE, INCOME, SUM)