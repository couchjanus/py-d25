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

@bot.message_handler(commands=['exchange'])
def exchange_command(message):
	keyboard = telebot.types.InlineKeyboardMarkup()
	keyboard.row(telebot.types.InlineKeyboardButton('USD', callback_data='get-USD'))
	keyboard.row(telebot.types.InlineKeyboardButton('EUR', callback_data='get-EUR'), telebot.types.InlineKeyboardButton('RUR', callback_data='get-RUR'))
	bot.send_message(message.chat.id, 'Click on the currency of choice:', reply_markup=keyboard)



# метод get_ex_callback:

def get_ex_callback(query):
	bot.answer_callback_query(query.id)
	send_exchange_result(query.message, query.data[4:])

# Метод answer_callback_query нужен, чтобы убрать состояние загрузки, 
# к которому переходит бот после нажатия кнопки. 
# Отправим сообщение send_exchange_query. 
# Ему нужно передать Message и код валюты 
# (получить ее можно из query.data. Если это, например, get-USD, передавайте USD).

# send_exchange_result:

def send_exchange_result(message, ex_code):
	bot.send_chat_action(message.chat.id, 'typing')
	ex = privatbank.get_exchange(ex_code)
	bot.send_message(message.chat.id, serialize_ex(ex), reply_markup=get_update_keyboard(ex), parse_mode='HTML')

# Сперва отправим состояние ввода в чат, 
# так чтобы бот показывал индикатор «набора текста», пока API банка получает запрос. 
# Теперь вызовем метод get_exchange из файла privatbank.py, 
# который получит код валюты (например, USD). 
# Также нужно вызвать два новых метода в send_message: serialize_ex, 
# сериализатор валюты и get_update_keyboard 
# (который возвращает клавиатуре кнопки “Update” и “Share”).

def get_update_keyboard(ex):
	keyboard = telebot.types.InlineKeyboardMarkup()
	keyboard.row(telebot.types.InlineKeyboardButton(
		'Update', callback_data=json.dumps(
		 {
		  't': 'u',
		  'e': {
			  'b': ex['buy'],
		      's': ex['sale'],
		      'c': ex['ccy']
		      }
		 }
	    ).replace(' ', '')
	), 
	telebot.types.InlineKeyboardButton('Share', switch_inline_query=ex['ccy']))
	return keyboard

# Запишем в get_update_keyboard текущий курс валют в callback_data в форме JSON. 
# JSON сжимается, потому что максимальный разрешенный размер файла равен 64 байтам.

# Кнопка t значит тип, а e — обмен. Остальное выполнено по тому же принципу.

# У кнопки Share есть параметр switch_inline_query. 
# После нажатия кнопки пользователю будет предложено выбрать один из чатов, 
# открыть этот чат и ввести имя бота и определенный запрос в поле ввода.

# Методы serialize_ex и дополнительный serialize_exchange_diff нужны, 
# чтобы показывать разницу между текущим и старыми курсами валют после нажатия кнопки Update.

def serialize_ex(ex_json, diff=None):
	result = '<b>' + ex_json['base_ccy'] + ' -> ' + ex_json['ccy'] + ':</b>\n\n' + 'Buy: ' + ex_json['buy']
	if diff:
		result += ' ' + serialize_exchange_diff(diff['buy_diff']) + '\n' + 'Sell: ' + ex_json['sale'] + ' ' + serialize_exchange_diff(diff['sale_diff']) + '\n'
	else:
		result += '\nSell: ' + ex_json['sale'] + '\n'
	return result

def serialize_exchange_diff(diff):
	result = ''
	if diff > 0:
		result = '(' + str(diff) + ' <img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="↗️" src="https://s.w.org/images/core/emoji/2.3/svg/2197.svg">" src="https://s.w.org/images/core/emoji/2.3/svg/2197.svg">" src="https://s.w.org/images/core/emoji/2.3/svg/2197.svg">" src="https://s.w.org/images/core/emoji/72x72/2197.png">" src="https://s.w.org/images/core/emoji/72x72/2197.png">)'
	elif diff < 0:
		result = '(' + str(diff)[1:] + ' <img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="<img draggable="false" data-mce-resize="false" data-mce-placeholder="1" data-wp-emoji="1" class="emoji" alt="↘️" src="https://s.w.org/images/core/emoji/2.3/svg/2198.svg">" src="https://s.w.org/images/core/emoji/2.3/svg/2198.svg">" src="https://s.w.org/images/core/emoji/2.3/svg/2198.svg">" src="https://s.w.org/images/core/emoji/72x72/2198.png">" src="https://s.w.org/images/core/emoji/72x72/2198.png">)'
	return result

# метод serialize_ex получает необязательный параметр diff. 
# Ему будет передаваться разница между курсами обмена 
# в формате {'buy_diff': <float>, 'sale_diff': <float>}. 
# Это будет происходить во время сериализации после нажатия кнопки Update. 
# Когда курсы валют отображаются первый раз, он нам не нужен.


# обработчик для кнопок встроенной клавиатуры
# В библиотеке pyTelegramBot Api есть декоратор @bot.callback_query_handler, 
# который передает объект CallbackQuery во вложенную функцию.

@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
	data = query.data
	if data.startswith('get-'):
		get_ex_callback(query)


# Если данные обратного вызова начинаются с get- (get-USD, get-EUR и так далее), 
# тогда нужно вызывать get_ex_callback, как раньше. 
# В противном случае стоит попробовать разобрать строку JSON и получить ее ключ t. 
# Если его значение равно u, тогда нужно вызвать метод edit_message_callback. Реализуем это:

def edit_message_callback(query):
	data = json.loads(query.data)['e']
	exchange_now = privatbank.get_exchange(data['c'])
	text = serialize_ex(
		exchange_now,
		get_exchange_diff(get_ex_from_iq_data(data), exchange_now)
		) + '\n' + get_edited_signature()
	if query.message:
		bot.edit_message_text(
			text,
			query.message.chat.id,
			query.message.message_id,
			reply_markup=get_update_keyboard(exchange_now),
			parse_mode='HTML'
			)
	elif query.inline_message_id:
		bot.edit_message_text(
			text,
			inline_message_id=query.inline_message_id,
			reply_markup=get_update_keyboard(exchange_now),
			parse_mode='HTML'
			)

# Загружаем текущий курс валюты (exchange_now = privatbank.get_exchange(data['c'])).

# Генерируем текст нового сообщения путем сериализации текущего курса валют с параметром diff, 
# который можно получить с помощью новых методов. 
# Также нужно добавить подпись — get_edited_signature.

# Вызываем метод edit_message_text, если оригинальное сообщение не изменилось. 
# Если это ответ на встроенный запрос, передаем другие параметры.

# Метод get_ex_from_iq_data разбирает JSON из callback_data:

def get_ex_from_iq_data(exc_json):
	return {
	       'buy': exc_json['b'],
	       'sale': exc_json['s']
	       }

# Метод get_exchange_diff получает старое и текущее значение курсов валют 
# и возвращает разницу в формате {'buy_diff': <float>, 'sale_diff': <float>}:

def get_exchange_diff(last, now):
	return {
		'sale_diff': float("%.6f" % (float(now['sale']) - float(last['sale']))),
		'buy_diff': float("%.6f" % (float(now['buy']) - float(last['buy'])))
		}


# get_edited_signature генерирует текст “Updated…”:

def get_edited_signature():
	return '<i>Updated ' + str(datetime.datetime.now(P_TIMEZONE).strftime('%H:%M:%S')) + ' (' + TIMEZONE_COMMON_NAME + ')</i>'

# обработчик кнопки обновления
# Теперь можно создать обработчик кнопки Update. 
# После дополнения метода iq_callback_method он будет выглядеть следующим образом:

@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
	data = query.data
	if data.startswith('get-'):
		get_ex_callback(query)
	else:
		try:
			if json.loads(data)['t'] == 'u':
				edit_message_callback(query)
		except ValueError:
			pass


bot.polling(none_stop=True)