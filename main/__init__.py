#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("10000844", default=None, cast=int)
API_HASH = config("776f257fc1d1f8aa4aea9dd35d10a45b", default=None)
BOT_TOKEN = config("7346846250:AAFSrWYPO7t8IaJ4f9SX6j-b4_ziZTe4aJ8", default=None)
SESSION = config("AQCUKpYPlvNDeRJe_rzI76PW60zHvPX3fgGM8hs8_TjB_8Fm1DR9tQrWrOwb6OCQ93J7SPOPJm_8LRBJ9dBxDbMvqL_WmdmTk8lSYcnODREzWaQptYFcSaAtK5Ou0v_VtZuzF_0LQOoZkfYQRIGSEz40w5JuJ52htVC75sJA9Kn-unxB0mmT6gGxFg7uaT3UclbSgcG7D-LrlLIK0i1HWYS4depqM7HA9HYxD8Y_G1yaWBmh4ZMKPcnDc9BLDerK_h078kUsDjUUNR4e33eLtjngXkWHNblJElXXknT6xfzb4RgbpdE7KxtVl1i4QifE4Q-fs-4ApC6YQoabjvUDGH6NAAAAAamsXEEA", default=None)
FORCESUB = config("Restricted_content_bot1", default=None)
AUTH = config("7141612609", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
