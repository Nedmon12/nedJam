import subprocess
import youtube_dl
# def downloadByTitle(title):
    


def downloadLink(ytlink):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([ytlink])

        