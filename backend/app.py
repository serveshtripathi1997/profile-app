from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder="frontend", static_url_path="")

# --------- API ENDPOINT ---------
@app.route("/profile")
def profile():
    return jsonify({
        "name": "SERVESH",
        "role": "Adobe Commerce Cloud | DevOps | SRE Engineer",
        "primary": [
            "Azure", "AWS", "Adobe Commerce Cloud",
            "Linux", "Docker", "Jenkins", "Windows Server"
        ],
        "secondary": ["Terraform"],
        "tertiary": [
            "CI/CD Pipelines",
            "Monitoring (New Relic)",
            "Container Security",
            "Cloud Optimization"
        ]
    })

# --------- FRONTEND ROOT ROUTE ---------
@app.route("/")
def serve_home():
    return send_from_directory("frontend", "index.html")

