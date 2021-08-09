import requests
from bs4 import BeautifulSoup
import spotipy


input_date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: (For example: '2021-04-10') "
)

# Using Billboard to obtain top 100 songs for a specific date.


def get_100_songs():
    response = requests.get(f"https://www.billboard.com/charts/hot-100/{input_date}")
    billboard_hot = response.text
    soup = BeautifulSoup(billboard_hot, "html.parser")
    song_data = soup.findAll(
        name="span",
        class_="chart-element__information__song text--truncate color--primary",
    )
    top_100 = [song.get_text() for song in song_data]
    return top_100


# Manages spotify auth and returns the spotify object.
def spotify_auth():
    oauth2 = spotipy.oauth2.SpotifyOAuth(
        client_id="",
        client_secret="",
        redirect_uri="",
        scope="",
        show_dialog=True,
        cache_path="token.txt",
    )
    spotify = spotipy.Spotify(oauth_manager=oauth2)
    return spotify


# Get the user id from Spotify


def get_spotify_user_id():
    user_id = spotify.current_user()["id"]
    return user_id


# Gets the song uris obtained from Billboard website.
def spotify_get_song_uris():
    uris = []
    for song in top_100:
        results = spotify.search(
            q=f"track:{song} year:{input_date.split('-')[0]}", type="track"
        )
        try:
            uri = results["tracks"]["items"][0]["uri"]
            uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")
    return uris


# Creates a spotify playlist and returns a playlist id.
def spotify_create_playlist_and_get_playlist_id():
    playlist_id = spotify.user_playlist_create(
        user=user_id,
        name=f"{input_date} Billboard 100",
        public=False,
        description="Custom Playlist created using Billboard 100 and Spotify API",
    )["id"]
    return playlist_id


# Adds items to the spotify playlist
def spotify_add_items_to_playlist():
    add_tracks = spotify.playlist_add_items(playlist_id=playlist_id, items=uris)
    print(add_tracks)


# Main file
try:
    with open(f"top_songs_of_{input_date}.txt") as data:
        print("File already exists!")

except FileNotFoundError:
    top_100 = get_100_songs()
    with open(f"top_songs_of_{input_date}.txt", mode="w") as data:
        data.write(f"Top 100 songs of {input_date}\n\n")
        for song in top_100:
            data.write(f"{song}\n")
    spotify = spotify_auth()
    user_id = get_spotify_user_id()
    uris = spotify_get_song_uris()
    playlist_id = spotify_create_playlist_and_get_playlist_id()
    spotify_add_items_to_playlist()
