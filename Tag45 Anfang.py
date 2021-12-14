from bs4 import BeautifulSoup
import requests
import os

result = requests.get("https://www.edreams.com/blog/the-best-world-christmas-songs-playlist-ever/")
content = result.text

soup = BeautifulSoup(content, "html.parser")
entry_content = soup.find(class_='entry-content')
songs = entry_content.findAll('h2')
with open('songs.txt', 'w', encoding='utf-8') as file:
    for song in songs:
        print(song.get_text())
        file.write(song.get_text() + os.linesep)
