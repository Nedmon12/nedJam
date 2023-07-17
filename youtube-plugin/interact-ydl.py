import subprocess

def downloadByTitle(title):
    process = subprocess.Popen([], #youtube-dl command goes here
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    process.communicate() #I am not sure :p


def downloadLink(ytlink):
    result = subprocess.run(["youtube-dl"], ["ytlink"])  #tune with parameters


        #this is just a placeholder idk what youtube-dl returns yet
    if (result=="success"):
        #add song title and file location tuple to db
        