import youtube_dl
import asyncio

async def downloadLink(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec':'mp3',
            'preferredquality': '192',
        }],
        
    }
    mystring = f"https://www.youtube.com/watch?v={link}"
    print(mystring)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
       donwloadable = await ydl.download([mystring])
    return (donwloadable)
    # youtube_dl.YoutubeDL.download()