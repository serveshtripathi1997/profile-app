from flask import Flask, send_from_directory, jsonify
import os

# Backend directory = /Python/backend
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Frontend directory = /Python/frontend
FRONTEND_FOLDER = os.path.join(BASE_DIR, "..", "frontend")

# Media directory = /Python/backend/Media
MEDIA_FOLDER = os.path.join(BASE_DIR, "Media")

app = Flask(
    __name__,
    static_folder=FRONTEND_FOLDER,     # Serve CSS/JS
    static_url_path=""
)


# ------------ API ------------
@app.route("/profile")
def profile():
    return jsonify({
        "brand": "DEPT APPAREL",
        "tagline": "Worldwide Collections",
        "release_date": "01.12.2025"
    })


# ---------- Serve Media ----------
@app.route("/media/<path:filename>")
def media_files(filename):
    return send_from_directory(MEDIA_FOLDER, filename)


# ---------- Serve Frontend ----------
@app.route("/")
def home():
    return send_from_directory(FRONTEND_FOLDER, "index.html")


# ---------- Run Server ----------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
