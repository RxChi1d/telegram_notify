from telethon import TelegramClient


def sent_message(text: str, api_id: int, api_hash: str, bot_token: str, chat_id: int):
    with TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token) as client:
        client.send_message(chat_id, text)


if __name__ == '__main__':
    api_id = 1234567890
    api_hash = 'your api hash'
    bot_token = 'your bot token'
    chat_id = 1234567890

    sent_message('the message you want to send',
                 api_id, api_hash, bot_token, chat_id)
