import sqlite3

connection = sqlite3.connect("songs.db")


def searchSong(song):
    #Construct a string prior to this
    result = connection.execute("SELECT path FROM songs where songTitle = {var}")
   
    # Implement a way of checking similarity between audio files
    result.fetchone()
