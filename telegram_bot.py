token=''
import telebot
from urllib.request import urlretrieve
import os
import random

    
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=["text"])
def handle(message, i=0): 
    try:
      print('request recieved')
      bot.send_message(chat_id=message.chat.id, text=generate_horo())
    except:
      bot.send_message(chat_id=message.chat.id, text='error')
