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

    if 'text' in message:
        text = message['message']['text']
        return chat_id, text, update_id
    
    if 'photo' in message:
        photo = message['photo'][-1]['file_id']
        return chat_id, photo, update_id
    
    if 'sticker' in message:
        sticker = message['sticker']['file_id']
        return chat_id, sticker, update_id
print(get_last_updates(get_updates()))
# ## sending functions
# def send_message(chat_id, text):
#     params = {'chat_id': chat_id, 'text': text}
#     url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
#     response = requests.get(url, params=params)
#     data = response.json()
#     return data

# def send_photo(chat_id, photo):
#     params = {'chat_id': chat_id, 'photo':photo}
#     url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
#     response = requests.get(url, params=params)
#     data = response.json()
#     return data

# def send_sticker(chat_id, sticker):
#     params = {'chat_id': chat_id, 'sticker': sticker}
#     url = f"https://api.telegram.org/bot{TOKEN}/sendSticker"
#     response = requests.get(url, params=params)
#     data = response.json()
#     return data
# ## ending send functions 

# last_update_id = -1

# while True:
#     # result = get_updates()
#     chat_id, tis, update_id = get_last_updates(get_updates())
    
#     print(chat_id)
#     if update_id != last_update_id:
#         if get_last_updates()[1] == 'text':
#             send_message(chat_id, tis)

#         if get_last_updates()[1] == 'photo':
#             send_photo(chat_id, tis)

#         if get_last_updates()[1] == 'sticker':
#             send_sticker(chat_id, tis)
            
#         print('printed')
#         last_update_id = update_id
#     sleep(2)