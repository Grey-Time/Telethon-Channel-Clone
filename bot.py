from telethon.sync import TelegramClient
from telethon.tl.types import MessageService
from config import Config as BOT_SETTING
import time

with TelegramClient(BOT_SETTING.NAME, BOT_SETTING.API_ID, BOT_SETTING.API_HASH) as client:
    amount_forwarded = 0
    for message in client.iter_messages(BOT_SETTING.SRC_CHAT_ID, reverse=True):
        if isinstance(message, MessageService):
            continue
        try:
            client.send_message(BOT_SETTING.DEST_CHAT_ID, message)
            amount_forwarded += 1
            if amount_forwarded >= 48:
                amount_forwarded = 0
                time.sleep(2)
        except Exception as e:
            print(e)
            time.sleep(5)