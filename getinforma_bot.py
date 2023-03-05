import telebot
from config import currency, TOKEN

bot = telebot.TeleBot(TOKEN)  # создать новый объект Telegram Bot

# команды боту /start, /help
@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
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

bot.polling()