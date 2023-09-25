import os

import ffmpeg
from pyrogram import Client, filters
from pyrogram.types import Message
import download
import search

from pytgcalls import GroupCallFactory

main_filter = filters.text & filters.outgoing & ~filters.edited
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

@Client.on_message(main_filer & cmd_filter('play'))
async def start_playout(_, message: Message):
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