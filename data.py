import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas
from service import spotify_api_client


sp = spotify_api_client()
artist = 'davido'
track = 'if'
q = 'artist:{} track: {}'.format(artist, track)
results = sp.search(q=q, limit=1, type='track')
print(results['tracks']['items'][0]['uri'])