import telebot

API_TOKEN = '7482301429:AAGqW25r7oGert4wmqEYWGwcN5qrvgjmaMc'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm your bot.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
