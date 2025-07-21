# Github.com/Vasusen-code

import logging
import sys
from pyrogram import Client
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from decouple import config

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)

# Config variables
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SESSION = config("SESSION", default=None)
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", default=None, cast=int)

# Start Telethon userbot (only if SESSION is provided)
if SESSION:
    try:
        userbot = TelegramClient(StringSession(SESSION), API_ID, API_HASH)
        userbot.start()
        logging.warning("Userbot started successfully.")
    except Exception as e:
        logging.warning(f"Userbot Error: {e}")
        sys.exit(1)
else:
    userbot = None
    logging.warning("SESSION not provided. Userbot will not start.")

# Start Pyrogram bot
try:
    Bot = Client(
        "SaveRestricted",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH
    )
    Bot.start()
    logging.warning("Pyrogram bot started successfully.")
except Exception as e:
    logging.error(f"Pyrogram Bot Error: {e}")
    sys.exit(1)
