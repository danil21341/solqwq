
import telebot 
from telebot import types 
import json

def get_token():
    with open('token.json') as file:
        json_answer = json.load(file)
        token = json_answer['config']
    return token

def get_words():
    with open('questions.json') as file:
        data = json.loads(file)         
        return data['questions']       

a = get_words()

bot = telebot.TeleBot(get_token())         
@bot.message_handler(content_types=['text']) 
def get_text_messages(message): 
    if message.text == "Привет": 
        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе о функциях питона!.") 
        keyboard = types.InlineKeyboardMarkup() 
        for i in a.keys():
            keyboard.add(types.InlineKeyboardButton(text=i,callback_data=i) ) 
        
        bot.send_message(message.from_user.id, text='Выбери о какой команде хочешь узнать ', reply_markup=keyboard) 
    elif message.text == "/help": 
        bot.send_message(message.from_user.id, "Напиши Привет") 
    else: 
        bot.send_message(message.from_user.id, "Напиши /help.") 
@bot.callback_query_handler(func=lambda call: True) 
def callback_worker(call): 
    bot.send_message(call.from_user.id, a[call.data]) 

bot.polling(none_stop=True, interval=0)


