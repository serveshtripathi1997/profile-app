from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder="../frontend", static_url_path="")

# ---------- API ----------
@app.route("/profile")
def profile():
    return jsonify({
        "brand": "DEPT APPAREL",
        "tagline": "Worldwide Collections",
        "release_date": "01.12.2025"
    })

# ---------- SERVE IMAGES ----------
@app.route('/media/<path:filename>')
def media(filename):
    media_folder = os.path.join(os.getcwd(), "Media")
    return send_from_directory(media_folder, filename)

# ---------- SERVE FRONTEND ----------
@app.route("/")
def home():
    return send_from_directory("../frontend", "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
