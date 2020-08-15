# Rough work script 

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas
import json
from service import spotify_api_client

Client_ID   = "xxxxxxxxxxxxxxxxxxxx"
Client_Secret = "xxxxxxxxxxxxxxxx"

client_credentials_manager = SpotifyClientCredentials(client_id=Client_ID,client_secret=Client_Secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# query a single artist 
# Just testing credentials here 
artist = 'davido'
track = 'if'
q = 'artist:{} track: {}'.format(artist, track)
results = sp.search(q=q, limit=1, type='track')
print(results['tracks']['items'][0]['uri'])


# First script to extract audio features
  
def get_spotify_uris(df):
    """
    args: dataframe of saved tracks
    returns: list of saved uris
    """
    saved_uris = []
    artist_names = df['artist'].values
    track_names = df['track'].values
    
    for i in range(len(artist_names)):
        artist = artist_names[i]
        track = track_names[i]
        q = 'artist:{} track: {}'.format(artist, track)
        results = sp.search(q=q, limit=1, type='track')
        uri = results['tracks']['items'][0]['uri']
        saved_uris.append(uri)
        
    return saved_uris

def get_audio_features(saved_uris):

    """
    args: list of saved uris
    returns: dataframe with audio features
    """
    artist = []
    track = []
    
    danceability = []
    energy = []
    key = []
    loudness = []
    mode = []
    speechiness = []
    acousticness = []
    instrumentalness = []
    liveness = []
    valence = []
    tempo = []
    duration_ms = []

    for uri in saved_uris:
        x = sp.audio_features(uri)
        y = sp.track(uri)
        for audio_features in x:
            danceability.append(audio_features['danceability'])
            energy.append(audio_features['energy'])
            key.append(audio_features['key'])
            loudness.append(audio_features['loudness'])
            mode.append(audio_features['mode'])
            speechiness.append(audio_features['speechiness'])
            acousticness.append(audio_features['acousticness'])
            instrumentalness.append(audio_features['instrumentalness'])
            liveness.append(audio_features['liveness'])
            valence.append(audio_features['valence'])
            tempo.append(audio_features['tempo'])
            duration_ms.append(audio_features['duration_ms'])
            print('append')
      
        artist.append(y['album']['artists'][0]['name'])
        track.append(y['name'])

    df = pd.DataFrame()
    df['artist'] = artist
    df['track'] = track
    df['danceability'] = danceability
    df['energy'] = energy
    df['key'] = key
    df['loudness'] = loudness
    df['mode'] = mode
    df['speechiness'] = speechiness
    df['acousticness'] = acousticness
    df['instrumentalness'] = instrumentalness
    df['liveness'] = liveness
    df['valence'] = valence
    df['tempo'] = tempo
    df['duration_ms'] = duration_ms
    
    df.to_csv('data/OnelateAudioFeatures.csv')
    
    return df