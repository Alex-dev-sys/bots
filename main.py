import webbrowser
from telebot import types
import telebot
import sqlite3

bot = telebot.TeleBot("7559053523:AAGTyRCqMq6jRuEi1TEiXc204KFHmWv0Zng")

@bot.message_handler(commands=["start"])
def start(message):
  markup = types.ReplyKeyboardMarkup()
  btn1 = types. KeyboardButton('Go to site') 
  btn4 = types.  KeyboardButton('Tech Support')
  markup.row(btn1, btn4)
  btn2 = types. KeyboardButton('About macros')
  btn3 = types. KeyboardButton('How to use our macros')
  markup.row(btn2, btn3) 
  bot.send_message(message.chat.id, 'Welcome to the bot which help you about macros for minecraft', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
  if message.text == 'About macros':
    bot.send_message(message.chat.id, 'We are creating a program called a macross for server use.For instance, if you are playing on a server and require a substantial amount of money, but you do not wish to invest time in doing so due to your laziness, our macross can assist you. The computer will handle everything for you!')
  elif message.text == 'How to use our macros':
    bot.send_message(message.chat.id, 'How to use our Macross. You can contact us directly via telegram by clicking on the write to tech support, or you can go to our website and contact us via email by clicking on the "Write to me" button.We will coordinate the cost of our services.I will write to you and send you instructions on how to download and use our Macross.The computer will do everything for you, so you don not have to waste time making money if you are too lazy to do it.')
  elif message.text == 'Write me':
    bot.send_message(message.chat.id, "Write me: @g2lover")
bot.polling(non_stop=True)  