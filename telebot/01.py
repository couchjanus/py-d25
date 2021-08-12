# bot.py
# Создадим файл bot.py. 
# Нужно импортировать все необходимые библиотеки, файлы с настройками и предварительно созданный pb.py. 
# Если каких-то библиотек не хватает, их можно установить с помощью pip.

import telebot
import config
import privatbank
import datetime
import pytz
import json
import traceback


P_TIMEZONE = pytz.timezone(config.TIMEZONE)

TIMEZONE_COMMON_NAME = config.TIMEZONE_COMMON_NAME

# Создадим бота с помощью библиотеки pyTelegramBotAPI. Для этого конструктору нужно передать токен:

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
	bot.send_message(
		message.chat.id,  
        'Greetings! I can show you exchange rates.\n' + 
        'To get the exchange rates press /exchange.\n' + 
        'To get help press /help.'
        )

bot.polling(none_stop=True)
