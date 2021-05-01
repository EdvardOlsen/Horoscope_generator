token=''
import telebot
from urllib.request import urlretrieve
import os
import random
from generate import generateHoro

    
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=["text"])
def handle(message, i=0): 
    try:
      print('request recieved')
      bot.send_message(chat_id=message.chat.id, text=generateHoro(message.text))
    except ValueError:
      bot.send_message(chat_id=message.chat.id, text='error')
