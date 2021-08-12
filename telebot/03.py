# bot.py

import telebot
import config
import privatbank
import datetime
import pytz
import json
import traceback


P_TIMEZONE = pytz.timezone(config.TIMEZONE)

TIMEZONE_COMMON_NAME = config.TIMEZONE_COMMON_NAME


bot = telebot.TeleBot(config.TOKEN)

# обработчик команды /help с помощью встроенной кнопки со ссылкой на ваш аккаунт в Telegram. 

@bot.message_handler(commands=['start'])
def start_command(message):
	bot.send_message(
		message.chat.id,  
        'Greetings! I can show you exchange rates.\n' + 
        'To get the exchange rates press /exchange.\n' + 
        'To get help press /help.'
        )

@bot.message_handler(commands=['help'])
def help_command(message):
	keyboard = telebot.types.InlineKeyboardMarkup()
	keyboard.add(telebot.types.InlineKeyboardButton('Message the developer', url='telegram.me/januspy'))
	bot.send_message(
        message.chat.id,
        '1) To receive a list of available currencies press /exchange.\n' + 
        '2) Click on the currency you are interested in.\n' + 
        '3) You will receive a message containing information regarding the source and the target currencies, ' + 
        'buying rates and selling rates.\n' + 
        '4) Click “Update” to receive the current information regarding the request. ' + 
        'The bot will also show the difference between the previous and the current exchange rates.\n' + 
        '5) The bot supports inline. Type @<botusername> in any chat and the first letters of a currency.',
        reply_markup=keyboard
    )

# Обработчик команды /exchange отображает меню выбора валюты 
# и встроенную клавиатуру с 3 кнопками: USD, EUR и RUR (это валюты, поддерживаемые API банка).

@bot.message_handler(commands=['exchange'])
def exchange_command(message):
	keyboard = telebot.types.InlineKeyboardMarkup()
	keyboard.row(telebot.types.InlineKeyboardButton('USD', callback_data='get-USD'))
	keyboard.row(telebot.types.InlineKeyboardButton('EUR', callback_data='get-EUR'), telebot.types.InlineKeyboardButton('RUR', callback_data='get-RUR'))
	bot.send_message(message.chat.id, 'Click on the currency of choice:', reply_markup=keyboard)

bot.polling(none_stop=True)

# как работает InlineKeyboardButton.
# Когда пользователь нажимает на кнопку, вы получаете CallbackQuery 
# (в параметре data содержится callback-data) в getUpdates. 
# Таким образом вы знаете, какую именно кнопку нажал пользователь, и как ее правильно обработать.
