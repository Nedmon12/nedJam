import os

import ffmpeg
from pyrogram import Client, filters
from pyrogram.types import Message
import download
import search
import asyncio
import pyrogram
import pytgcalls

from pytgcalls import GroupCallFactory

SESSION = os.getenv('SESSION')
API_HASH = os.getenv('API_HASH')
API_ID = os.getenv('API_ID')
DEFAULT_SONG = '' #default song to play on start
OUTPUT_FILENAME = 'output.mp3' # does it really matter?
CLIENT_TYPE = GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM

CHAT_ID = os.getenv('CHAT_ID')

main_filter = filters.text & filters.outgoing
cmd_filter = lambda cmd: filters.command(cmd, prefixes='!')

group_call = None

def init_client_and_delete_message(func):
    async def wrapper (client, message):
        global group_call
        if not group_call:
            group_call = GroupCallFactory(client).get_file_group_call()

        await message.delete()

        return await func(client, message)
    
    return wrapper

def convertFileToRaw(filepath):
    input_filename = 'input.raw' # filename.raw
    ffmpeg.input(filepath).output(
        input_filename,
        format='s16le',
        acodec='pcm_s16le',
        ac=2,
        ar='48k'
    ).overwrite_output().run()

@Client.on_message(filters.command("start"))
async def start_playout(client, message: Message):
    print("does this get called?????")
    # if not message.reply_to_message or not message.reply_to_message.audio:
    #     return await message.delete()
    
    # if not group_call:
    #     return await message.reply_text('You are not in a voice chat')
    
    # input_filename = 'input.raw'
    
    status = '-....\n'
    input_filename = 'input.raw'
    # await message.edit_text(status)
    print(f"this is message.text {message.text}")
    temp = message.text.split()[1]
    print(temp)
    options = {'q':temp, 'part':'id,snippet', 'max_results':5}

    print(options['q'])
    # audio_original = await search.sendTitleandId(message.text, options)
    ytsearch = search.sendTitleandId(message.text, options)
    audio_original = download.downloadLink(ytsearch[1])
    # tobedownloaded = search.sendTitleandId(message.text,options)
    # audio_original = 
    filename = ytsearch[0]+"-"+ytsearch[1]+".mp3"
    convertFileToRaw(filename)
    global group_call
    if not group_call:
        group_call = GroupCallFactory(client, CLIENT_TYPE).get_file_group_call(input_filename)
        await group_call.start(CHAT_ID)
    else : 
        group_call.input_filename = input_filename
