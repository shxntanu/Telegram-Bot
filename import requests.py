import requests

files = {'photo':open('D:\Visual Studio Code Projects\Telegram Bot\Bot\image1.png','rb')}
resp = requests.post('https://api.telegram.org/bot5287913028:AAGI38rcE0pxJFgwl1jUt3M3nqrhwuE7N8Y/sendPhoto?chat_id=-1001255506203&caption={}',files=files)
print(resp.status_code)