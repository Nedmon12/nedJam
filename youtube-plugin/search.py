import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

load_dotenv()
DEVERLOPER_KEY = os.getenv('YOUTUBE_API')
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_SERVICE_NAME, developerKey=DEVERLOPER_KEY)


    search_response = youtube.search().list(
        q= options.q,
        part='id,snippet',
        maxResults=options.max_results
    ).execute()

    videos = []
    playlists = []
    channels = []
    leVideoCount = 0
    for search_result in search_response.get('items', []):
        if search_result['id']['kind']=='youtube#video':
            videos.append(search_result['snippet']['title'], search_result['id']['videoid'])
            if(leVideoCount==0):
                leVideo = (search_result['snippet']['title'], search_result['id']['videoid'])
                return leVideo
        elif search_result['id']['kind'] == 'youtube#channel':
            print("\n ________\skipping because search result is a channel")
        elif search_result['id']['kind'] == 'youtube#playlist':
            print("\n ________\skipping because search result is a playlist")
    return ()

    