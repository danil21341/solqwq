
import telebot 
from telebot import types 
import json

def get_token():
    with open('token.json') as file:
        json_answer = json.load(file)
        token = json_answer['config']
    return token

def get_words():
    d = []
    with open('questions.json', encoding='UTF-8') as file:
        d = json.load(file)
    return d       
a = get_words()
users = {}

bot = telebot.TeleBot(get_token())         
@bot.message_handler(content_types=['text']) 
def get_text_messages(message): 
    if message.text == "Привет": 
        bot.send_message(message.from_user.id, "Привет, сейчас я тебе помогу узнать больше о программировании.") 
        keyboard = types.InlineKeyboardMarkup()
         
        for i in a.keys():
            keyboard.add(types.InlineKeyboardButton(text=i, callback_data="cat"+i) ) 
            
        
        bot.send_message(message.from_user.id, text='Выбери о какой категории хочешь узнать ', reply_markup=keyboard) 
    elif message.text == "/help": 
        bot.send_message(message.from_user.id, "Напиши Привет") 
    else: 
        bot.send_message(message.from_user.id, "Напиши /help.") 
@bot.callback_query_handler(func=lambda call: True) 
def callback_worker(call): 
    if call.data.find('cat') == 0:
        users[call.from_user.id] = call.data.replace('cat', '')
        keyboard = types.InlineKeyboardMarkup()
         
        for i in a[users[call.from_user.id]].keys():
            keyboard.add(types.InlineKeyboardButton(text=i, callback_data=i) ) 
            
        bot.send_message(call.from_user.id, text='Выбери о какой команде хочешь узнать ', reply_markup=keyboard) 
    else:
        bot.send_message(call.from_user.id, a[users[call.from_user.id]][call.data]) 

bot.polling(none_stop=True, interval=0)


