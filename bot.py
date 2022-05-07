from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json
import requests
import time

# list of quotes
quotes = [
    'First, solve the problem. Then, write the code. – John Johnson',
    'Experience is the name everyone gives to their mistakes. – Oscar Wilde',
    'Code is like humor. When you have to explain it, it’s bad. – Cory House',
    'Before software can be reusable it first has to be usable. – Ralph Johnson',
    'Optimism is an occupational hazard of programming: feedback is the treatment. - Kent Beck'
]

# loop through the quotes
for quote in quotes:
    url = 'https://api.telegram.org/bot5287913028:AAGI38rcE0pxJFgwl1jUt3M3nqrhwuE7N8Y/sendMessage?chat_id=CHAT_ID&text="{}"'.format(quote)
    requests.get(url)
    # sends new quotes every 20seconds
    time.sleep(20)