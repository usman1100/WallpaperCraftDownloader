import urllib
import requests
import re
import os
from bs4 import BeautifulSoup

count = 0
path = 'jpgs/'
category = 'hi-tech'
resolution = "1366x768"
pages = 5


dirName = 'jpgs'

try:
    os.mkdir(dirName)
    print("Directory ", dirName, " Created ")
except FileExistsError:
    print("Directory ", dirName, " already exists")


for j in range(pages):

    url = "https://wallpaperscraft.com/catalog/" + category + "/page" + str(j)

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    links = soup.find_all(class_="wallpapers__link")

    sources = []

    for i in links:
        sources.append("https://wallpaperscraft.com" + i['href'])

    for i in sources:
        newPage1 = requests.get(i)

        newSoup1 = BeautifulSoup(newPage1.content, 'html.parser')

        temp = newSoup1.find('a', text=re.compile(resolution))

        newSoup2URL = 'https://wallpaperscraft.com' + temp['href']

        newPage2 = requests.get(newSoup2URL)

        newSoup2 = BeautifulSoup(newPage2.content, 'html.parser')

        className = "gui-button gui-button_full-height"

        downloadLink = newSoup2.find(class_=className)

        downloadLink = downloadLink['href']

        filePath = path + category + str(count) + '.jpg'

        urllib.request.urlretrieve(downloadLink, filePath)

        print("Wallpaper ", count+1, " Downloaded")

        count += 1
