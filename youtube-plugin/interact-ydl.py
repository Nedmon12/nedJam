import subprocess

def downloadByTitle(title):
    process = subprocess.Popen([], #youtube-dl command goes here
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    process.communicate() #I am not sure :p