import telebot
from telebot import types
import Currency

bot = telebot.TeleBot('5538346660:AAHHtRZONJfnywFqUAEXa3oIusQ037u8THM')

message_first_currency = ''
message_second_currency = ''
message_amount = 0.0


@bot.message_handler(commands=['start'])
def start_func(message):
    mess = f'Hello, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['help'])
def help_func(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    usd = types.KeyboardButton('USD')
    eur = types.KeyboardButton('EUR')
    byn = types.KeyboardButton('BYN')
    rub = types.KeyboardButton('RUB')
    btc = types.KeyboardButton('BTC')
    pln = types.KeyboardButton('PLN')
    markup.add(usd, eur, byn, rub, btc, pln)
    msg = bot.send_message(message.chat.id, f'Enter the currency you want to change:', reply_markup=markup)
    bot.register_next_step_handler(msg, first_currency)


currencies_list = ['USD', 'EUR', 'BYN', 'RUB', 'BTC', 'PLN']


def first_currency(message):
    if message.text in currencies_list:
        msg = bot.send_message(message.chat.id, f'Enter the currency you want to get: ')
        global message_first_currency
        message_first_currency = message.text
        bot.register_next_step_handler(msg, second_currency)
        return message.text
    else:
        bot.send_message(message.chat.id, f'Sorry, i do not understand you ')


def second_currency(message):
    if message.text in currencies_list:
        msg = bot.send_message(message.chat.id, f'How much do you want to change? ')
        global message_second_currency
        message_second_currency = message.text
        bot.register_next_step_handler(msg, currency_amount)
        return message.text
    else:
        bot.send_message(message.chat.id, f'Sorry, i do not understand you ')


def currency_amount(message):
    global message_amount
    message_amount = message.text
    bot.send_message(message.chat.id, f'{Currency.convert_currency(message_first_currency, message_second_currency, message_amount)}')
    return message.text


bot.infinity_polling(none_stop=True)
