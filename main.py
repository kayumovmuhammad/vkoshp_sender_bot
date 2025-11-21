from os import getenv
from time import sleep

import requests
from dotenv import load_dotenv

load_dotenv()

timer = 0

BOT_TOKEN = getenv("BOT_TOKEN")
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

WEBSITE_URLS = [
    "https://neerc.ifmo.ru/school/russia-team/",
    "https://neerc.ifmo.ru/school/archive/2025-2026/ru-olymp-team-internet-2025-standings.html",
    "https://neerc.ifmo.ru/school/information/index.html",
    "https://neerc.ifmo.ru/school/archive/2025-2026.html",
    "https://neerc.ifmo.ru/school/russia-team/listTeamsFinal.jsp",
]
ADMIN_ID = getenv("KAYUMOVMUHAMMAD_ID")
USERS_ID = [ADMIN_ID, 1982459265, 1351195326, 775472748]


def send_message(chat_id, message):
    data = {"chat_id": chat_id, "text": message}
    response = requests.post(URL, data=data)
    print(response.text, chat_id)
    return response


def logger(message: str):
    print(f"LOGGER: {message}")


oldHTMLs = []
for url in WEBSITE_URLS:
    oldHTMLs.append(requests.get(url).text)

logger("Start polling")

while True:
    if timer % 120 == 0:
        send_message(ADMIN_ID, "Все работает ✅")
    timer += 1

    for index in range(len(oldHTMLs)):
        newHTML = requests.get(WEBSITE_URLS[index]).text

        if newHTML != oldHTMLs[index]:
            for chat_id in USERS_ID:
                send_message(
                    chat_id, f"Что то изменилось на сайте: {WEBSITE_URLS[index]}"
                )
            oldHTMLs[index] = newHTML

    sleep(60)
