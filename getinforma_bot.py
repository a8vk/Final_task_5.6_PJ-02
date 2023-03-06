import telebot
from config import *
from extensions import ConvertionException, CurrencyConverter

bot = telebot.TeleBot(TOKEN)  # создать новый объект Telegram Bot


# команды боту /start, /help
@bot.message_handler(commands=['start', 'help'])
def command_help(message: telebot.types.Message):
    text = 'Введите команду боту в следующем формате:\n \
<имя валюты> <в какую валюту перевести> <сколько>.\n \
Отделяйте команды пробелом. Например, доллар рубль 1500. \n \
Список валют: /currency'
    bot.reply_to(message, text)


# команда боту /currency
@bot.message_handler(commands=['currency'])
def values(message: telebot.types.Message):
    text = 'Список валют:'
    for key in currency.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


# обработка ввода от пользователя
@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        accept = message.text.lower().split()  # переводим строку в нижний регистр и разбиваем

        if len(accept) != 3:  # если нет трёх параметров
            raise ConvertionException('Параметры указаны неверно. Правильно, например, юань доллар 100.')
        quote, base, amount = accept
        total_base = CurrencyConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()
