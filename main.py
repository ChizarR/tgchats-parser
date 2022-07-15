from parse_response import parse_json, parse_html
from request import send_request_to_combot, send_request_to_tgram
from writer import write_to_csv


def main():
    response_combot = send_request_to_combot()
    response_tgram = send_request_to_tgram()
    chats = [
        *parse_json(response_combot),
        *parse_html(response_tgram)
    ]
    write_to_csv(chats)


if __name__ == "__main__":
    main()



