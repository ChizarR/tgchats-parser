from tg_types import TelegramChatData

from bs4 import BeautifulSoup

def parse_combot(response):
    chats = []
    for chat in response:
        chat_name = chat["t"]
        telegram_link = "@" + chat["u"]
        lang = chat["l"]
        chat_data = TelegramChatData(chat_name, telegram_link, lang)
        chats.append(chat_data)
    return chats


def parse_tgram(pages):
    chats = []
    counter = 0
    for page in pages:
        soup = BeautifulSoup(page, "lxml")
        raw_cards = soup.find_all("div", class_="col-12 col-sm-6 col-md-4")
        for card_soup in raw_cards:
            counter += 1
            chat_name = card_soup.find("a")
            telegram_link = card_soup.find("span", class_="text-success small2")
            lang = "RU"
            chat_data = TelegramChatData(
                chat_name.text,
                telegram_link.text,
                lang
            )
            chats.append(chat_data)
    return chats




