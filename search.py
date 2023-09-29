import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
import argparse
import asyncio
load_dotenv()
DEVERLOPER_KEY = os.getenv('YOUTUBE_API')
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVERLOPER_KEY)


    search_response = youtube.search().list(
        q= options['q'],
        part='id,snippet',
        maxResults=options.max_results
    ).execute()

    videos = []
    playlists = []
    channels = []
    leVideoCount = 0
    for search_result in search_response.get('items', []):
        if search_result['id']['kind']=='youtube#video':
            videos.append((search_result['snippet']['title'], search_result['id']['videoId']))
            if(leVideoCount==0):
                leVideo = (search_result['snippet']['title'], search_result['id']['videoId'])
                print(leVideo)
                return leVideo
        elif search_result['id']['kind'] == 'youtube#channel':
            print("\n ________\skipping because search result is a channel")
        elif search_result['id']['kind'] == 'youtube#playlist':
            print("\n ________\skipping because search result is a playlist")
    return ()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--q', help='Search term', default='Google')
    parser.add_argument('--max-results',help='Max results', default=5)
    args = parser.parse_args()
    print(args)
    try:
        youtube_search(args)
    except HttpError:
        print ('An HTTP error occured:\n')
    

def sendTitleandId(searchString,options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVERLOPER_KEY)


    search_response = youtube.search().list(
        q= options['q'],
        part='id,snippet',
        maxResults=options['max_results']
    ).execute()

    videos = []
    leVideoCount = 0

    for search_result in search_response.get('items', []):
        if search_result['id']['kind']=='youtube#video':
            videos.append((search_result['snippet']['title'], search_result['id']['videoId']))
            if(leVideoCount==0):
                leVideo = (search_result['snippet']['title'], search_result['id']['videoId'])
                print(leVideo)
                return search_result['id']['videoId']
        elif search_result['id']['kind'] == 'youtube#channel':
            print("\n ________\skipping because search result is a channel")
        elif search_result['id']['kind'] == 'youtube#playlist':
            print("\n ________\skipping because search result is a playlist")
        return ()
    
    