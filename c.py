import telebot
from random import *

Token = "7072798631:AAHgPocsl536-VtAb2-LZ-tWqC9zfsYzLNk"
bot = telebot.TeleBot(Token)
d = ["+","-","*","/"]
c = d[randint(0, len(d)-1)]
a = randint(1,100)
b = randint(1,100)

@bot.message_handler(content_types=['text'])
def send_start(message):
    global a
    global b
    global c
    
    bot.send_message(message.from_user.id, f"{a}{c}{b}")





bot.polling(none_stop=True, interval=0, timeout=120)