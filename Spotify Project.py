# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qF2SwUl0cacfQezwonIgwO2wITxxRnCO
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import sys
import pprint
import requests

Date = input('Enter Date: in YYY-MM-DD Format: ')

link = "https://www.billboard.com/charts/hot-100/" + Date + "/"

page = requests.get(link)

soup = BeautifulSoup(page.content, 'html.parser')

tags = soup.select("li ul li h3 ")

song_titles = []

for tag in tags:
    song_titles.append(tag.get_text())


for i in range(len(song_titles)):
    song_titles[i] = song_titles[i].strip()

print(song_titles)

clinet_id = '078ec2df54124132b289cbd46261c43d'
client_secret = '7dc04f6af56349c3bdefa914e96e7f56'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth( scope="playlist-modify-private",
                                                redirect_uri="http://example.com",
                                                client_id=clinet_id ,
                                                client_secret=client_secret,
                                                show_dialog=True,
                                                cache_path="token.txt" ,
                                                username='22ij6jwtxfi6pwj3obml3dvra',)
)
user_id = sp.current_user()["id"]

song_uris = []
year = Date.split('-')[0]

for song in song_titles:
    result = sp.search(q= f"track {song}  year: {year}", type = "track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user_id, name = f"{Date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)