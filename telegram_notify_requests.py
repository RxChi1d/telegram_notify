import requests


def send_msg(msg: str, token: str, chatID: str):
    assert type(msg) == str, "the type of msg must be str"
    url = f'https://api.telegram.org/{token}/sendMessage?chat_id={chatID}&text={msg}'
    requests.get(url)


if __name__ == '__main__':
    bot_token = 'your bot token'
    chat_id = 1234567890
    send_msg('the message you want to send', bot_token, chat_id)
