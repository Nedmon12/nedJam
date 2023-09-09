import os
import ffmpeg
from pytgcalls import GroupCallFactory
import pyrogram
from pyrogram import filters
from dotenv import load_dotenv
from .search import youtube_search
from .download import downloadLink
import redis
load_dotenv()

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

API_HASH = os.getenv('API_HASH')
API_ID = os.getenv('API_ID')
CHAT_ID = os.getenv('CHAT_ID')
INPUT_FILENAME = "Never_gonna_give_you_up.mp3" # maybe replace  
OUTPUT_FILENAME = "rick_roll.mp3"              # with env
SESSION = os.getenv('SESSION')

app = pyrogram.Client(SESSION, int(API_ID), API_HASH)

# parse message.text
@app.on_message(filters.command("play"))
async def handler(client, message):
    result = youtube_search({'q':message.text,'maxResults':5})
    downloadFile = downloadLink(result[1])
    # r.hset(result)
    # if (result):
        # download results
        # 

app.run()


# def main():
#     main_client = pyrogram.Client(SESSION,
#                                   int(API_ID), API_HASH)
    