import youtube_dl

def downloadLink(link):
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
        ydl.download([mystring])

    # youtube_dl.YoutubeDL.download()