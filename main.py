from parse_response import parse_combot, parse_tgram
from request import send_request_to_combot, send_request_to_tgram
from writer import write_to_csv


def main():
    response_combot = send_request_to_combot()
    response_tgram = send_request_to_tgram()
    chats = [
        *parse_combot(response_combot),
        *parse_tgram(response_tgram)
    ]
    write_to_csv(chats, "combot")


if __name__ == "__main__":
    main()



