#!/usr/bin/python3

from telegram.ext import *
import requests
import logging

updater = Updater(token='', use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#start bot

def start(updater, context):
	context.bot.send_message(chat_id=updater.effective_chat.id, text='first request!')
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
