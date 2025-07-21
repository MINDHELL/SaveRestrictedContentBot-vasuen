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

API_ID = config("API_ID", cast=int)
API_HASH = config("API_HASH")
BOT_TOKEN = config("BOT_TOKEN")
SESSION = config("SESSION", default=None)

userbot = None
Bot = Client(
    "SaveRestricted",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

def run_main():
    asyncio.run(start_bot())

async def start_bot():
    global userbot

    try:
        await Bot.start()
        logging.warning("Pyrogram bot started successfully.")
    except Exception as e:
        logging.error(f"Failed to start Pyrogram bot: {e}")
        sys.exit(1)

    # Start userbot if SESSION is available
    if SESSION:
        try:
            userbot = TelegramClient(StringSession(SESSION), API_ID, API_HASH)
            await userbot.start()
            logging.warning("Telethon userbot started successfully.")
        except Exception as e:
            logging.warning(f"Userbot Error: {e}")
            userbot = None

    await idle()

    await Bot.stop()
    if userbot:
        await userbot.disconnect()
