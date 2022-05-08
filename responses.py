from datetime import datetime
from telegram.ext import *
import telegram

bot = telegram.Bot(token='5287913028:AAGI38rcE0pxJFgwl1jUt3M3nqrhwuE7N8Y')

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup",):
        return "Hey there PICTian, how's it going?"

    if user_message in ("start", "run"):
        return "Bot has started"

    if user_message in ("about", "who are you", "who are you?"):
        return "I am a sample bot created for testing, by Shantanu"

    if user_message in ("yessir"):
        return "yessir"

    if user_message in ("rupya"):
        return "Baba Rupya ki Jai 🙏"
