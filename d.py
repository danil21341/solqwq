
import telebot 
from telebot import types 
import json

def get_token():
    with open('token.json') as file:
        json_answer = json.load(file)
        token = json_answer['config']
    return token

bot = telebot.TeleBot(get_token())         
@bot.message_handler(content_types=['text']) 
def get_text_messages(message): 
    if message.text == "Привет": 
        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.") 
        keyboard = types.InlineKeyboardMarkup() 
        print_key = types.InlineKeyboardButton(text='print',callback_data='python1' ) 
        keyboard.add(print_key) 
        if_key = types.InlineKeyboardButton(text='if', callback_data='python2') 
        keyboard.add(if_key) 
        else_key = types.InlineKeyboardButton(text='list', callback_data='python3') 
        keyboard.add(else_key) 
        while_key = types.InlineKeyboardButton(text='while', callback_data='python4') 
        keyboard.add(while_key ) 
        input_key = types.InlineKeyboardButton(text='input', callback_data='python5') 
        keyboard.add(input_key) 
        def_key = types.InlineKeyboardButton(text='def', callback_data='python6') 
        keyboard.add(def_key) 
        len_key = types.InlineKeyboardButton(text='len', callback_data='python7') 
        keyboard.add(len_key) 
        class_key = types.InlineKeyboardButton(text='class', callback_data='python8') 
        keyboard.add(class_key) 
        import_key = types.InlineKeyboardButton(text='find', callback_data='python9') 
        keyboard.add(import_key) 
        for_key = types.InlineKeyboardButton(text='for', callback_data='python0') 
        keyboard.add(for_key) 
        bot.send_message(message.from_user.id, text='Выбери о какой команде хочешь узнать ', reply_markup=keyboard) 
    elif message.text == "/help": 
        bot.send_message(message.from_user.id, "Напиши Привет") 
    else: 
        bot.send_message(message.from_user.id, "Напиши /help.") 
@bot.callback_query_handler(func=lambda call: True) 
def callback_worker(call): 
    if call.data == "python1": 
        bot.send_message(call.from_user.id, "Команда для печати сообщений на экране или другом стандартном устройстве вывода. Команда print может использоваться для печати любого типа объекта — целого числа, строки, списка, кортежа и других.") 
    elif call.data == "python2": 
        bot.send_message(call.from_user.id, "Команда if оценивает выражение и, если оно истинно (true), выполняет операторы под ним.") 
    elif call.data == "python3": 
        bot.send_message(call.from_user.id, "Функция Python list() принимает любую итерацию (объект, который можно перебирать) в качестве параметра и возвращает список") 
    elif call.data == "python4": 
        bot.send_message(call.from_user.id, "Команда while используется для выполнения набора операторов, если заданное условие истинно") 
    elif call.data == "python5": 
        bot.send_message(call.from_user.id, "Команда для получения ввода от пользователя. Исполнение программы будет остановлено до тех пор, пока пользователь не введет какое-либо значение, которое будет преобразовано функцией input() в строку") 
    elif call.data == "python6": 
        bot.send_message(call.from_user.id, "Команда определения функции Python дает возможность оборачивать повторно используемый код внутри функций, чтобы вызваны его позже, когда это необходимо") 
    elif call.data == "python7": 
        bot.send_message(call.from_user.id, "Команда len или функция len() используются для подсчёта количества элементов в объекте. Если объект является строкой, то функция len() возвращает количество присутствующих в ней символов") 
    elif call.data == "python8": 
        bot.send_message(call.from_user.id, "Команда для создания классов. Python поддерживает объектно-ориентированное программирование и позволяет пользователям создавать классы и инициализировать объекты") 
    elif call.data == "python9": 
        bot.send_message(call.from_user.id, "Команда find() используется для поиска подстроки в строке. Если таковая найдена,find() возвращает индекс первого вхождения подстроки, в противном случае возвращает -1.") 
    elif call.data == "python0": 
        bot.send_message(call.from_user.id, "Команда цикла for используется для выполнения набора операторов путем повторения последовательности. Эта последовательность может быть списком, кортежем, строкой, словарем и т. д.") 
 
bot.polling(none_stop=True, interval=0)

