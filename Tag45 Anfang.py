from bs4 import BeautifulSoup
import requests
import os

result = requests.get("https://www.edreams.com/blog/the-best-world-christmas-songs-playlist-ever/")
content = result.text

#Schreibe deinen Code unter dieser Zeile 👇