import telebot

bot = telebot.TeleBot("6690746593:AAE2UrO5rS16Smt08EiygUB__yE_BgmvSQo")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()