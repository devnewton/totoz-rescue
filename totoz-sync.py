#!/usr/bin/env python3
import requests
import urllib.parse
import os.path
from bs4 import BeautifulSoup

TOTOZ_SERVER = "https://nsfw.totoz.eu/"

def saveImage(totoz):
    src = totoz.select("img")[0]["src"]
    imgUrl = urllib.parse.urljoin(TOTOZ_SERVER, src)
    name = os.path.basename(imgUrl)
    imgFilename = f"img/{name}"
    if not os.path.exists(imgFilename):
        print(f"Download {name}")
        with open(imgFilename, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=65536):
                fd.write(chunk)

print(f"Retrieve totozes from {TOTOZ_SERVER}")
r = requests.get(TOTOZ_SERVER)
soup = BeautifulSoup(r.content, features="lxml")

totozes = soup.select('.totoz')
for totoz in totozes:
    saveImage(totoz)

print("Done")
