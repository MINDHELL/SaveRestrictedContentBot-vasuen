# __init__.py

import logging
import sys
import asyncio
from pyrogram import Client, idle
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from decouple import config

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)

API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SESSION = config("SESSION", default=None)

# Start Telethon userbot if SESSION is provided
userbot = None
if SESSION:
    try:
        userbot = TelegramClient(StringSession(SESSION), API_ID, API_HASH)
        userbot.start()
        logging.warning("Userbot started successfully.")
    except Exception as e:
        logging.warning(f"Userbot Error: {e}")
        sys.exit(1)
else:
    logging.warning("No SESSION provided. Skipping userbot.")

# Start Pyrogram bot
Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

async def main():
    await Bot.start()
    logging.warning("Pyrogram bot started successfully.")

    # Run idle loop to keep the bot alive
    await idle()

    await Bot.stop()
    if userbot:
        await userbot.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
