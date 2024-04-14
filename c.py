import telebot 
from random import * 
import json 
import time 
token = '7072798631:AAHgPocsl536-VtAb2-LZ-tWqC9zfsYzLNk' 
 
bot = telebot.TeleBot(token)  
 
@bot.message_handler(content_types=['text']) 
def send_start(message): 
    d = ["+","-","*","/"] 
    c = d[randint(0, len(d)-1)] 
    a = randint(1,100) 
    b = randint(1,100) 
    if message.text == 'start':
        bot.send_message(message.from_user.id, 'Привет, я задам тебе 10 математических вопросов, а в конце скажу на сколько ты ответил правильно, и за какое время! Ты готов(Да/Нет)?') 
        if message.text == 'Да':
            for i in range(10):
                bot.send_message(message.from_user.id, f"{a}{c}{b}") 
        elif message.text == 'Нет':
            bot.send_message(message.from_user.id, 'Пока (start - чтобы наччать заново)')
 
 
 
bot.polling(none_stop=True, interval=0, timeout=120)