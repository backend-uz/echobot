import requests
from pprint import pprint
from time import sleep
TOKEN = '1950937652:AAEKFVSEwjT55RYro5X-3ILwKXnh_s6ThPU'

def get_updates():
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    response = requests.get(url)
    data = response.json() 
    return data['result']
##getting last updates
def get_last_updates(result):
    message = result[-1]
    update_id = message['update_id']
    chat_id = message['message']['chat']['id']
    msg = message['message']

    if 'text' in msg:
        text = msg['text']
        return chat_id, text, update_id
    
    if 'photo' in msg:
        photo = msg['photo'][-1]['file_id']
        return chat_id, photo, update_id
    
    if 'sticker' in msg:
        sticker = msg['sticker']['file_id']
        return chat_id, sticker, update_id

## sending functions
def send_message(chat_id, text):
    params = {'chat_id': chat_id, 'text': text}
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    r = requests.post(url, params=params)
    return r.json()

def send_photo(chat_id, photo):
    params = {'chat_id': chat_id, 'photo':photo}
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    r = requests.post(url, params=params)
    return r.json()

def send_sticker(chat_id, sticker):
    params = {'chat_id': chat_id, 'sticker': sticker}
    url = f"https://api.telegram.org/bot{TOKEN}/sendSticker"
    r = requests.post(url, params=params)
    return r.json()
## ending send functions 

last_update_id = -1

while True:
    result = get_updates()
    
    chat_id, tis, update_id = get_last_updates(result)
    if update_id != last_update_id:
        print(update_id, last_update_id)

        if 'text' in result[-1]['message']:
            send_message(chat_id, tis)
        if 'photo' in result[-1]['message']:
            send_photo(chat_id, tis)
            print('photo')
        if 'sticker' in result[-1]['message']:
            send_sticker(chat_id, tis)
            print('stik')
        last_update_id = update_id
        print(last_update_id)
    sleep(2)