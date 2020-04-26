import telebot

#main variables
TOKEN = "1082686208:AAHplV16bZjst_CrCbmDZ_Sy1cP2XVjqCvA"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, я буду парсить заголовки с Хабра')


bot.polling()