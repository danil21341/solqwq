import telebot
from telebot import types
import json
def get_token():
    token = ''
    with open('token.jsons') as file:
        json_answer = json.load(file)
        token = json_answer['config']
    return token

bot = telebot.TeleBot(get_token())
first = ["Функция (оператор) print() выводит на экран данные. Внутри круглых скобок записываются выражения, которые нужно вывести на экран."]
second = ["Если ни одно из условий не истинно, используют else, чтобы выполнить код по умолчанию. В языке Python выражение считается истинным (true), если его результат — не ноль или выражение не является пустым объектом. А ложным (false) оно считается, если результат — ноль или пустой объект, в том числе значение none."]
second_add = ["Оператор if является началом условной конструкции. Далее идёт условие, которое возвращает логическое значение True (истина) или False (ложь). Завершается условие символом «двоеточие». Затем — обязательный отступ в четыре пробела, он показывает, что строки объединяются в один блок."]
third = ["Цикл while (“пока”) позволяет выполнить одну и ту же последовательность действий, пока проверяемое условие истинно. Условие записывается до тела цикла и проверяется до выполнения тела цикла. Как правило, цикл while используется, когда невозможно определить точное значение количества проходов исполнения цикла."]
four = ["В языке Python имеется встроенная функция input(), с помощью которой можно читать ввод пользователя. Эта функция принимает необязательный строковый аргумент (который выводится в консоли как строка приглашения к вводу) и ожидает, пока пользователь введет ответ и завершит ввод клавишей Enter (или Return)."]
five = ["Ключевое слово def сообщает Python, что вы определяете функцию. После def вы указываете имя функции; оно должно отвечать тем же правилам, что и имена переменных. Согласно конвенции, в имени функции нельзя использовать заглавные буквы, а слова должны быть разделены подчеркиванием вот_так ."]
six = ["Цикл for является одним из основных инструментов контроля потока выполнения программы в языке Python. Он позволяет итерировать по последовательности элементов, таких как списки, кортежи, строки и другие итерируемые объекты."]
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе о функциях питона")
        keyboard = types.InlineKeyboardMarkup()
        print_key = types.InlineKeyboardButton(text='print', callback_data='wqr' )
        keyboard.add(print_key)
        if_key = types.InlineKeyboardButton(text='if', callback_data='qwe')
        keyboard.add(if_key)
        else_key = types.InlineKeyboardButton(text='else', callback_data='qwq')
        keyboard.add(else_key)
        while_key = types.InlineKeyboardButton(text='while', callback_data='www')
        keyboard.add(while_key )
        input_key = types.InlineKeyboardButton(text='input', callback_data='qqq')
        keyboard.add(input_key)
        def_key = types.InlineKeyboardButton(text='def', callback_data='eee')
        keyboard.add(def_key)
        for_key = types.InlineKeyboardButton(text='for', callback_data='ewq')
        keyboard.add(for_key)
        bot.send_message(message.from_user.id, text='Выбери о какой команде хочешь узнать ', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Напиши /help.")
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "qwe": 
        msg = (second_add)
    if call.data == "qwq": 
        msg = (second)
    if call.data == "wqr": 
        msg = (first)
    if call.data == "www": 
        msg = (third)
    if call.data == "qqq": 
        msg = (four)
    if call.data == "eee": 
        msg = (five)
    if call.data == "ewq": 
        msg = (six)
    
    bot.send_message(call.message.chat.id, msg)
bot.polling(none_stop=True, interval=0)
