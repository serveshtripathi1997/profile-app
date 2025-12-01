from flask import Flask, send_from_directory, jsonify
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND = os.path.abspath(os.path.join(BASE_DIR, "..", "frontend"))
MEDIA = os.path.join(BASE_DIR, "Media")

print("BASE_DIR:", BASE_DIR)
print("FRONTEND:", FRONTEND)
print("MEDIA:", MEDIA)

app = Flask(__name__, static_folder=FRONTEND, static_url_path="")

@app.route("/profile")
def profile():
    return jsonify({"name": "Servesh", "role": "DevOps / SRE / Commerce Cloud"})

@app.route("/media/<path:filename>")
def media_files(filename):
    return send_from_directory(MEDIA, filename)

@app.route("/")
def home():
    return send_from_directory(FRONTEND, "index.html")

app.run(host="0.0.0.0", port=9000)
