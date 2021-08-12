import telebot

bot = telebot.TeleBot('')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text == "Hello":
		bot.send_message(message.from_user.id, "Hi, Can I help You?")
	elif message.text == "/help":
		bot.send_message(message.from_user.id, "Text Hello please")
	else:
		bot.send_message(message.from_user.id, "I don't understand You. Text please /help")

bot.polling(none_stop=True, interval=0)
