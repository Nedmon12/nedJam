from pyrogram import Client
import os
plugins = dict(root="plugins")

SESSION = os.getenv('SESSION')
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
print(SESSION)
print(API_HASH)
print(API_ID)
Client('accountsession',plugins=plugins).run()