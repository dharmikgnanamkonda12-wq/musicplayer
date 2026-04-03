from flask import Flask, render_template, request, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

# 🔑 Replace these with your real credentials from Spotify Developer Dashboard
CLIENT_ID = "38847e54e3a8a929a2240369557"
CLIENT_SECRET = "f753c6306c34447eabf2e18c3b5bee0"

# Authentication
auth_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

sp = spotipy.Spotify(auth_manager=auth_manager)

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# Search route
@app.route("/search")
def search():
    query = request.args.get("q")

    if not query:
        return jsonify([])

    results = sp.search(q=query, type="track", limit=10)

    tracks = []

    for item in results["tracks"]["items"]:
        tracks.append({
            "name": item["name"],
            "artist": item["artists"][0]["name"],
            "image": item["album"]["images"][0]["url"] if item["album"]["images"] else None,
            "preview": item["preview_url"]
        })

    return jsonify(tracks)

# Run app
if __name__ == "__main__":
    app.run(debug=True)
