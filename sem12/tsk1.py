import time

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

with open('bot.token', 'r') as f:
    token = f.read()
app = telebot.TeleBot(token=token, parse_mode=None)

answers = dict()
call_data = None


def added_ans(id, ans):
    if id in answers.keys():
        answers[id].append(ans)
    else:
        answers[id] = [ans]


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"),
               InlineKeyboardButton("No", callback_data="cb_no"))
    return markup


@app.message_handler(commands=['start'])
def welcome(message):
    app.send_message(message.chat.id, 'Starting')
    for _ in range(3):
        app.send_message(message.chat.id, "Yes/no?", reply_markup=gen_markup())
        time.sleep(3)
    app.send_message(message.chat.id, f'Your answers: {answers[message.chat.id]}')


@app.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        app.answer_callback_query(call.id, "Answer is Yes")
        added_ans(call.from_user.id, 'Yes')
    elif call.data == "cb_no":
        app.answer_callback_query(call.id, "Answer is No")
        added_ans(call.from_user.id, 'No')
    elif call.data == "cb_unknown":
        app.answer_callback_query(call.id, "Answer is Unknown")
        added_ans(call.from_user.id, 'Unknown')


app.infinity_polling()
