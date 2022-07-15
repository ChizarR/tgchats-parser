import csv


def write_to_csv(data):
    with open("tg_chats.csv", "w", encoding="utf-8") as file:
        headers = ["ID", "CHAT_NAME", "LINK", "LANG"]
        writer = csv.writer(file)
        writer.writerow(headers)
        counter = 0
        for chat in data:
            row = [counter, chat.chat_name, chat.telegram_link, chat.lang]
            writer.writerow(row)
            counter += 1
    print("Done!")
