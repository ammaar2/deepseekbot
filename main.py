import requests
import telebot
from telebot.types import InlineKeyboardMarkup as mk
from telebot.types import InlineKeyboardButton as btn

tok = "7868827627:AAEUd9DdKLOFbVNVfkrX44xRTy_UlN6lZvk"
s1 = telebot.TeleBot(tok)

@s1.message_handler(commands=["start"])
def rr(mes):
    ui = btn("Def", url="https://t.me/jokerpython3")
    yu = btn("بدا مضرطه مع ذكاء اصطناعي", callback_data="st")
    rip=btn("Def For Api deepseek",url="https://t.me/PyCodz")
    qw = mk(row_width=1)
    qw.add(ui, yu,rip)
    s1.send_message(mes.chat.id, "ها هذا بوت تحدث مع ذكاء اصطناعي deepseek", reply_markup=qw)

@s1.callback_query_handler(func=lambda call: True)
def uy(call):
    if call.data == "st":

        s1.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="دز شتريد")


        @s1.message_handler(func=lambda msg: True)
        def handle_user_message(msg):
            es = msg.text
            url = f"https://dev-pycodz-blackbox.pantheonsite.io/DEvZ44d/deepseek.php?text={es}"
            r = requests.get(url).json()["response"]
            s1.send_message(msg.chat.id, r)

s1.infinity_polling()
