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
async def start_playout(_, message: Message):
    print("does this get called?????")
    if not message.reply_to_message or not message.reply_to_message.audio:
        return await message.delete()
    
    if not group_call:
        return await message.reply_text('You are not in a voice chat')
    
    input_filename = 'input.raw'

    status = '-....\n'
    await message.edit_text(status)
    print(f"this is message.text {message.text}")
    audio_original = await download.sendTitleandId(search.sendTitleandId(message.text))
    print(audio_original)

CLIENT_TYPE = pytgcalls.GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM
async def main(client):
    await client.start()
    # while not client.is_connected:
    #     await asyncio.sleep(1)

    input_filename = 'input.raw'
    ffmpeg.input("Heat_waves.mp3").output(input_filename, format='s16le', acodec='pcm_s16le', ac=2, ar='48k').overwrite_output().run()
    # convertFileToRaw(DEFAULT_SONG)
    global group_call
    if not group_call:
            group_call = GroupCallFactory(client).get_file_group_call()
    # group_call = pytgcalls.GroupCallFactory(client, CLIENT_TYPE)\
    #     .get_file_group_call('input.raw',OUTPUT_FILENAME)
    
    # group_call.input_filename = ''
    await group_call.start(int(CHAT_ID))

    # client.run()

    await pyrogram.idle()

if __name__ == '__main__':
    main_client = pyrogram.Client(SESSION, int(API_ID), API_HASH)
    main_client.run(main(main_client))


    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main(main_client))