import os
import asyncio
import pytgcalls
import pyrogram
from dotenv import load_dotenv
import ffmpeg
import json
load_dotenv()

API_HASH = os.getenv('API_HASH')
API_ID = os.getenv('API_ID')
CHAT_ID = os.getenv('CHAT_ID')
INPUT_FILENAME = "Never_gonna_give_you_up.mp3" # maybe replace  
OUTPUT_FILENAME = "rick_roll.mp3"              # with env
SESSION = os.getenv('SESSION')


with open("songlist.json", "r")as file:
    songList = json.load(file)

playlist = {}

def populatePlaylist():
    #value songList read from db
    """
     {
      song: {
       title: "",
       filepath: "",
      },
      metadata: {
      duration: "",
      artist: "",
      album: "",
      }
     }
    """
    
    for song in songList:
        playlist[song.title] = song.filepath

def convertFileToRaw(filepath):
    # result = subprocess.run(["ffpmeg"], ["-i"], ["filepath"])
    input_filename = 'input.raw'
    ffmpeg.input(filepath).output(
        input_filename,
        format='s16le',
        acodec='pcm_s16le',
        ac=2,
        ar='48k'
    ).overwrite_output().run()

CLIENT_TYPE = pytgcalls.GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM
async def main(client):
    await client.start()
    while not client.is_connected:
        await asyncio.sleep(1)

    group_call = pytgcalls.GroupCallFactory(client, CLIENT_TYPE)\
        .get_file_group_call(INPUT_FILENAME, OUTPUT_FILENAME)
    
    await group_call.start(int(CHAT_ID))

    await pyrogram.idle()

if __name__ == '__main__':
    main_client = pyrogram.Client(SESSION,
                                  int(API_ID), API_HASH)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(main_client))
