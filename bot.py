import config
import telebot
import time
#import oauth2
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(messages):
    bot.send_message(messages.chat.id, 'hello')

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)
     while True:
         time.sleep(200)