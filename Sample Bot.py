from setuptools import Command
import telegram
import Constants as keys
from telegram.ext import *
import responses as R
from datetime import datetime
import requests

bot = telegram.Bot(token='5287913028:AAGI38rcE0pxJFgwl1jUt3M3nqrhwuE7N8Y')

print("Bot started!!")

updates = bot.get_updates()

def start_command(update, context):
    update.message.reply_text('Type something random to get started')

def help_command(update, context):
    update.message.reply_text('Help Text Goes here')

def tyme(update, context):
    update.message.reply_text(str((datetime.now()).strftime("%d/%m/%y %H:%M:%S")))

def timetable(update, context):
  bot.send_photo(update.message.chat.id, 'https://pict-tt-bot.vercel.app/FE%20(4).jpg')

#Command for Timetable
# def timetable(update, context):
#     files = {'photo':open('D:\Visual Studio Code Projects\Telegram Bot\Bot\image1.png','rb')}
#     resp = requests.post('https://api.telegram.org/bot5287913028:AAGI38rcE0pxJFgwl1jUt3M3nqrhwuE7N8Y/sendPhoto?chat_id=-1001255506203&caption={}',files=files)
#     print(resp.status_code)

    # chat_id = update.message.chat_id
    # document =  open('image1.png','rb')
    # context.bot.send_document(chat_id,document)
    
    # bot.send_document(chat_id = chat_id, document='https://i.ibb.co/F0Lk4v3/image-2022-05-03-17-33-36.png')

def handle_message(update, context):
    text = str(update.message.text).lower()
    
    if text in ("tt","timetable"):
        files = {'photo':open('D:\Visual Studio Code Projects\Telegram Bot\Bot\image1.png','rb')}
        resp = requests.post('https://api.telegram.org/bot5287913028:AAGI38rcE0pxJFgwl1jUt3M3nqrhwuE7N8Y/sendPhoto?chat_id=-1001255506203&caption=FE5 Timetable Sem 2',files=files)
        print(resp.status_code)
    else:
        response = R.sample_responses(text)
        update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    
    # Commands
    
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("time", tyme))
    dp.add_handler(CommandHandler("tt", timetable))
    
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()