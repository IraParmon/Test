import telebot

from telebot import types


from register import create_table_inc, get_sum2, get_sum1, get_sum, create_table_exp, get_sum_ex, \
    get_sum_ex2, get_sum_August, get_sum_September, get_sum_ех_August

from datetime import datetime

bot = telebot.TeleBot('5248756848:AAENL3NfNeNJWnHthybUTGYkK5aPD-7reAo')


@bot.message_handler(commands=['all'])
def all_inc(message):
    income_sum = get_sum()
    income_sum1 = get_sum1()
    income_sum2 = get_sum2()
    bot.send_message(message.chat.id, f'Сумма доходов ⬆: {income_sum[0][0]} руб.')
    bot.send_message(message.chat.id, f' Зарплата: {income_sum1[0][0]} руб. Переводы: {income_sum2[0][0]} руб.')
    return start(message)


def all_inc_month(message):
    income_sum3 = get_sum_August()
    bot.send_message(message.chat.id, f' Доходы за август: {income_sum3[0][0]} руб.')
    income_sum4 = get_sum_September()
    bot.send_message(message.chat.id, f' Доходы за сентябрь: {income_sum4[0][0]} руб.')
    return start(message)

def all_exp_month(message):
    income_sum5 = get_sum_ех_August()
    bot.send_message(message.chat.id, f' Расходы за август: {income_sum5[0][0]} руб.')

    return start(message)


def all_exp(message):
    expense_sum = get_sum_ex()
    expense_sum2 = get_sum_ex2()
    bot.send_message(message.chat.id, f'Сумма расходов ⬇: {expense_sum[0][0]} руб.')
    bot.send_message(message.chat.id, f'  {expense_sum2}  руб.')
                                      # f'{expense_sum2[1][0]}: {expense_sum2[1][1]} руб.'
                                      # f'{expense_sum2[2][0]}: {expense_sum2[2][1]} руб.'
                                      # f'{expense_sum2[3][0]}: {expense_sum2[3][1]} руб.')
                                      # f'{expense_sum2[4][0]}: {expense_sum2[4][1]} руб.'
                                      # f'{expense_sum2[5][0]}: {expense_sum2[5][1]} руб.'
                                      # f'{expense_sum2[6][0]}: {expense_sum2[6][1]} руб.'
                                      # f'{expense_sum2[7][0]}: {expense_sum2[7][1]} руб.'
                                      # f'{expense_sum2[8][0]}: {expense_sum2[8][1]} руб.' )
    return start(message)

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    keyboard_menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    btn_one = types.KeyboardButton('Расходы ⬇')
    btn_two = types.KeyboardButton('Доходы ⬆')
    btn_three = types.KeyboardButton('Все расходы')
    btn_four = types.KeyboardButton('Все доходы')
    btn_five = types.KeyboardButton('Расходы за месяц')
    btn_six = types.KeyboardButton('Доходы за месяц')


    keyboard_menu.add(btn_one, btn_two, btn_three, btn_four, btn_five, btn_six)
    msg = bot.send_message(chat_id, 'Главное меню: ',
                           reply_markup=keyboard_menu)
    bot.register_next_step_handler(msg, on_select_menu_button)



def on_select_menu_button(message):
    if message.text == "Доходы ⬆":
        button_income(message)
    elif message.text == "Все доходы":
        all_inc(message)
    elif message.text == "Доходы за месяц":
        all_inc_month(message)
    elif message.text == "Расходы ⬇":
        button_expenses(message)
    elif message.text == "Все расходы":
        all_exp(message)
    elif message.text == "Расходы за месяц":
        all_exp_month(message)

def button_income(message):
    chat_id = message.chat.id
    keyboard_menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    btn_one = types.KeyboardButton('Зарплата')
    btn_two = types.KeyboardButton('Перевод')
    btn_three = types.KeyboardButton('Назад')

    keyboard_menu.add(btn_one, btn_two, btn_three)
    msg = bot.send_message(chat_id, 'Укажи вид дохода:',
                           reply_markup=keyboard_menu)
    bot.register_next_step_handler(msg, read_type_inc)

def read_type_inc(message):
    if message.text == "Назад":
        start(message)
    elif message.text == "Зарплата":
        read_inc(message)
    elif message.text == "Перевод":
        read_inc(message)

def read_inc(message):
    INCOME = message.text
    bot.send_message(message.chat.id, f"Введите сумму:")
    bot.register_next_step_handler(message, read_SUM, INCOME)

def read_SUM(message, INCOME):
    SUM = message.text
    DATE = datetime.now().date()
    bot.send_message(message.chat.id, f"Доход записан")
    create_table_inc(DATE, INCOME, SUM)
    return start(message)


def button_expenses(message):
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
    msg = bot.send_message(chat_id, 'Укажи вид расхода:',
                           reply_markup=keyboard_menu)
    bot.register_next_step_handler(msg, read_type_exp)

def read_type_exp(message):
    if message.text == "Назад":
        start(message)
    else:
        read_exp(message)

def read_exp(message):
    EXPENSE = message.text
    bot.send_message(message.chat.id, f"Введите сумму:")
    bot.register_next_step_handler(message, read_SUM_exp, EXPENSE)

def read_SUM_exp(message, EXPENSE):
    SUM = message.text
    if SUM.isdigit():
        DATE = datetime.now().date()
        bot.send_message(message.chat.id, f"Доход записан")
        create_table_exp(DATE, EXPENSE, SUM)
        return start(message)
    else:
        try:
            float(SUM)
            DATE = datetime.now().date()
            bot.send_message(message.chat.id, f"Доход записан")
            create_table_exp(DATE, EXPENSE, SUM)
            return start(message)
        except ValueError:
            bot.send_message(message.chat.id, f"Cумма должна быть числом!")
            return button_expenses(message)



bot.infinity_polling()
