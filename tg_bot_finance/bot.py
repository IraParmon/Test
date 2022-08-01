import telebot

from table import create

bot = telebot.TeleBot('5248756848:AAENL3NfNeNJWnHthybUTGYkK5aPD-7reAo')


@bot.message_handler(commands=['start'])
def start_message(message):
    print(message)
    bot.send_message(message.chat.id, 'Введи, пожалуйста, свое имя')
    bot.register_next_step_handler(message, read_name)


def read_name(message):
    name = message.text
    bot.send_message(message.chat.id, f'Введи свою фамилию')
    bot.register_next_step_handler(message, read_sname, name)


def read_sname(message, name):
    sname = message.text
    bot.send_message(message.chat.id, f'Привет {name} {sname}')


bot.infinity_polling()