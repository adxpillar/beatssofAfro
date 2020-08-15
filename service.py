import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

CID = os.getenv("CLIENT_ID")
SECRET = os.getenv("CLIENT_SECRET")

def spotify_api_client():
    """
    args: none
    returns: spotify-spotipy connection
    """
    # credential manager pointing to dotenv file
    client_credentials_manager = SpotifyClientCredentials(client_id=CID, client_secret=SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp
spotify_api_client()

if __name__ == "__main__":
    



