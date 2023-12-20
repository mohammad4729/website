import sqlite3
import telebot

bot = telebot.TeleBot("6772514038:AAEypTgXm1fds_OP5HbylPqmIag9h8WNBD4")

key = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
key.add("All", "Last")

@bot.message_handler(commands=['start'])
def send(messeage):
    bot.reply_to(messeage, "سلام و درود دوست عزیز و به ربات نمایش مشتری من خوش اومدید.", reply_markup=key)

@bot.message_handler()
def keyboard(messeage):
    if messeage.text == "All":
        con = sqlite3.connect("data.db")
        cur = con.cursor()
        res = cur.execute("SELECT Name,Number FROM Customers")
        for i in res:
            item1 = i[0]
            item2 = i[1]
            bot.send_message(messeage.chat.id, f"{item1}------>{item2}")
        con.close()
    elif messeage.text == "Last":
        con = sqlite3.connect("data.db")
        cur = con.cursor()
        res = cur.execute("SELECT Name,Number FROM Customers")
        for i in res:
            item1 = i[0]
            item2 = i[1]
        bot.send_message(messeage.chat.id, f"{item1}------>{item2}")
        con.close()
    else:
        bot.send_message(messeage.chat.id, "Invalid!")



bot.infinity_polling()

