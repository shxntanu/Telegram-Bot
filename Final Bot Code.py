from setuptools import Command
import telegram
import Constants as keys
from telegram.ext import *
import responses as R
from datetime import datetime

bot = telegram.Bot(token='5287913028:AAGI38rcE0pxJFgwl1jUt3M3nqrhwuE7N8Y')

print("\n\n------------------------------------------------------------------------------------------------------------------\n\nBot started!!")

updates = bot.get_updates()

def start_command(update, context):
    update.message.reply_text('Type something random to get started')

def help_command(update, context):
    update.message.reply_text('Help Text Goes here')

def time(update, context):
    update.message.reply_text(str((datetime.now()).strftime("%d/%m/%y %H:%M:%S")))

def timetable(update, context):
    update.message.reply_text('''Hey there PICTian 🌊,
    To get the timetable for the required division, type a command in the following manner.
    Syntax:

                        tt <space> x

        where x: Number of the division whose timetable you want to fetch.

    Enjoy!
    ''')


def handle_message(update, context):
    text = str(update.message.text).lower()
    
    if text in ("tt 1","tt 2","tt 3","tt 4","tt 5","tt 6","tt 7","tt 8","tt 9","tt 10","tt 11"):
        sl = list(text.split(" "))
        bot.send_photo(update.message.chat.id, 'https://pict-tt-bot.vercel.app/FE%20({}).jpg'.format(str(sl[1])))
    
    else:
        response = R.sample_responses(text)
        update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    
    # Command Handlers
    
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("time", time))
    dp.add_handler(CommandHandler("timetable",timetable))

    # Message Handlers

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()