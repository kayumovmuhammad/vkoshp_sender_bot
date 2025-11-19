from time import sleep
from dotenv import load_dotenv
from os import getenv
import requests

load_dotenv()

timer = 0

BOT_TOKEN = getenv("BOT_TOKEN")
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

WEBSITE_URL = "https://neerc.ifmo.ru/school/russia-team/"
ADMIN_ID = getenv("KAYUMOVMUHAMMAD_ID")
USERS_ID = [ADMIN_ID, getenv("MAHDI_ID"), getenv("AKAI_SUHROB_ID")]
print(ADMIN_ID)

def send_message(chat_id, message):
    data = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(URL, data=data)
    print(response.text, chat_id)
    return response

oldHTML = requests.get(WEBSITE_URL).text

while True:
    if timer % 12 == 0:
        send_message(ADMIN_ID, "Все работает✅")
    timer += 1

    newHTML = requests.get(WEBSITE_URL).text
    
    if (newHTML != oldHTML):
        for chat_id in USERS_ID:
            send_message(chat_id, f"Что то изменилось на сайте: {WEBSITE_URL}")
        oldHTML = newHTML

    sleep(60*10)