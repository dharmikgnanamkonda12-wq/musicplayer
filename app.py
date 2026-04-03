from flask import Flask, render_template, request, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CLIENT_ID = "SPOTIFY_CLIENT_ID"
CLIENT_SECRET ="SPOTIFY_CLIENT_SECRET"
auth_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

sp = spotipy.Spotify(auth_manager=auth_manager)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("q")

    results = sp.search(q=query, type="track", limit=10)

    tracks = []

    for item in results["tracks"]["items"]:
        tracks.append({
            "name": item["name"],
            "artist": item["artists"][0]["name"],
            "image": item["album"]["images"][0]["url"],
            "preview": item["preview_url"]
        })

    return jsonify(tracks)

if __name__ == "__main__":
    app.run(debug=True)
