print("fre nggrs be able well")
a = "ne strelyai"
b = "strelyai"
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "zodiac": 
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
        bot.send_message(call.message.chat.id, msg)