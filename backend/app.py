from flask import Flask, send_from_directory, jsonify
import os

# Resolve absolute paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FRONTEND_FOLDER = os.path.abspath(os.path.join(BASE_DIR, "..", "frontend"))
MEDIA_FOLDER = os.path.join(BASE_DIR, "Media")

print("BASE_DIR:", BASE_DIR)
print("FRONTEND_FOLDER:", FRONTEND_FOLDER)
print("MEDIA_FOLDER:", MEDIA_FOLDER)

app = Flask(
    __name__,
    static_folder=FRONTEND_FOLDER,  # load style.css, script.js
    static_url_path=""
)

# ---------------- API ----------------
@app.route("/profile")
def profile():
    return jsonify({
        "brand": "DEPT APPAREL",
        "tagline": "Worldwide Collections",
        "release_date": "01.12.2025",
    })

# ----------- MEDIA ROUTE -----------
@app.route("/media/<path:filename>")
def media_files(filename):
    return send_from_directory(MEDIA_FOLDER, filename)

# -------- FRONTEND ROUTE ----------
@app.route("/")
def home():
    return send_from_directory(FRONTEND_FOLDER, "index.html")

# -----------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
