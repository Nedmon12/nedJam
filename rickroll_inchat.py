import os
import asyncio
import pytgcalls
import pyrogram
from dotenv import load_dotenv

API_HASH = os.getenv('API_HASH')
API_ID = os.getenv('API_ID')
CHAT_ID = os.getenv('CHAT_ID')
INPUT_FILENAME = ""
OUTPUT_FILENAME = ""
CLIENT_TYPE = pytgcalls.GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM
async def main(client):
    await client.start()
    while not client.is_connected:
        await asyncio.sleep(1)

    group_call = pytgcalls.GroupCallFactory(client, CLIENT_TYPE).get_file_group_call(INPUT_FILENAME, OUTPUT_FILENAME)
    
    await group_call.start(CHAT_ID)

    await pyrogram.idlle()

if __name__ == '__main__':
    main_client = pyrogram.Client(os.environ.get('SESSION_NAME', 'pytgcalls'),
                                  int(os.environ['API_ID']),
                                  os.environ['API_HASH'])
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(main_client))
