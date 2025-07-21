from pyrogram import Client
from decouple import config
import logging
import sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

API_ID = config("API_ID", cast=int)
API_HASH = config("API_HASH")
BOT_TOKEN = config("BOT_TOKEN")
SESSION = config("SESSION", default=None)  # Optional Userbot session
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", default=None, cast=int)

# Bot client
bot = Client(
    "SaveRestrictedBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Optional userbot client
userbot = None
if SESSION:
    try:
        userbot = Client(
            "SaveRestrictedUser",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION
        )
        userbot.start()
        print("✅ Userbot started successfully.")
    except Exception as e:
        print("⚠️ Failed to start userbot session:")
        print(e)
        print("🔁 Continuing without userbot.")
else:
    print("ℹ️ SESSION not provided. Userbot is disabled.")
