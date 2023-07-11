from pyrogram import Client
from dotenv import load_dotenv
import os

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')

app = Client ("mybotsess", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

app.run()