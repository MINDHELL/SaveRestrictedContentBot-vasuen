# Github.com/Vasusen-code

import sys
import logging
from pyrogram import Client
from decouple import config

# Logging config
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.INFO
)

# Environment Variables
API_ID = config("API_ID", cast=int)
API_HASH = config("API_HASH")
BOT_TOKEN = config("BOT_TOKEN")
SESSION = config("SESSION", default=None)
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", cast=int, default=None)

# Main Bot (Pyrogram)
Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

# Optional Userbot (Pyrogram)
userbot = None
if SESSION:
    userbot = Client(
        "saverestricted_userbot",
        session_string=SESSION,
        api_id=API_ID,
        api_hash=API_HASH
    )
    try:
        userbot.start()
        logging.info("Userbot started successfully.")
    except Exception as e:
        logging.warning(f"Userbot failed to start: {e}")
        userbot = None

# Start main bot
try:
    Bot.start()
    logging.info("Main Bot started successfully.")
except Exception as e:
    logging.error(f"Failed to start Bot: {e}")
    sys.exit(1)
