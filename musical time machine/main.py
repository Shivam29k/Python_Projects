import requests
import spotipy
from bs4 import BeautifulSoup
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv('client_id')          # client id of spotify
SPOTIFY_SECRET_KEY = os.getenv("client_secret")     # secret key of spotify
REDIRECT_URI = os.getenv("redirect_uri")            # redirect uri of spotify
SPOTIFY_USERNAME = os.getenv('Spotify_username')

BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/"
OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'


# --------------> getting list of songs from billboard website using web scrapping <--------

date = input("What year would you want to travel to? Type the date in this format YYYY-MM-DD: ")

token = requests.get(url=f"{BILLBOARD_URL}{date}/")

soup = BeautifulSoup(token.text, "html.parser")

song_names = [' '.join(tag.find(name="h3", id="title-of-a-story").string.split()) for tag in soup.find_all(name="div", class_="o-chart-results-list-row-container")]

pprint(song_names)


# ------------------------------------> spotify <-------------------------------------

token = spotipy.oauth2.SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_SECRET_KEY, redirect_uri=REDIRECT_URI, scope="playlist-modify-private", cache_path="token.txt")

sp = spotipy.Spotify(auth_manager=token)

# finding track uri's
track_uri_list = []
for song in song_names:
    result = sp.search(q=song, type="track")
    name = result['tracks']['items'][0]['name']
    # track_id = result['tracks']['items'][0]['id']
    print(name)
    track_uri = result['tracks']['items'][0]['uri']
    print('uri:',track_uri)
    track_uri_list.append(track_uri)

# creating playlist
name = f"{date} Top 100"
description = f"Top 100 songs on {date} according to Billboard."
playlist = sp.user_playlist_create(user=SPOTIFY_USERNAME,name=name, public=False, collaborative=False, description=description)
playlist_id = playlist['uri']
print(f"Playlist created: {playlist_id}")

# adding songs on playlist
sp.user_playlist_add_tracks(user=SPOTIFY_USERNAME, playlist_id= playlist_id, tracks=track_uri_list, position=None)