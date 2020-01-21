import requests
import subprocess
import re



SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

def setWallPaper():
    apiURL = 'https://api.nasa.gov/planetary/apod?api_key=2wsUBSMoZz0gI6yDBDXXCIrcgjzlwkd5EA5vQ1XM'
    apiReq= requests.get(apiURL)
    imgTitle = ''

    if apiReq:
        imgURL = apiReq.json()['url']
        imgReq = requests.get(imgURL)
        imgTitle = 'NASSSA.jpg'
        downloadImg(imgReq, imgTitle)
    else:
        imgTitle = '716buffalo.jpg'
    imgPath = '/Users/michaelspagna/programming/python/NASSSSA/' + imgTitle
    subprocess.Popen(SCRIPT%imgPath, shell=True)

def downloadImg(req, title):
    with open(title, 'wb') as f:
        f.write(req.content)

setWallPaper()
