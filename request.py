import json

import requests


def send_request_to_combot():
    raw_chats = []
    limit, offset = 10, 10
    for _ in range(0, 1030):
        try:
            url = f"https://combot.org/api/chart/ru?limit={limit}&offset={offset}"
            response = requests.get(url)
            response_json = json.loads(response.text)
            for chat in response_json:
                raw_chats.append(chat)
            offset += limit
        except:
            print("Pages ended")
            break
    return raw_chats


def send_request_to_tgram():
    raw_pages = []
    for page in range(0, 5):
        url = f"https://tgram.io/ru/topic/23/unsorted?lang=ru&page={page}"
        response = requests.get(url)
        raw_pages.append(response.text)
    return raw_pages
