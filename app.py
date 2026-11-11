from flask import Flask, request, jsonify, render_template
from datetime import datetime, timezone

app = Flask(__name__)

locations = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/location", methods=["POST"])
def location():
    data = request.get_json()

    record = {
        "latitude": data["latitude"],
        "longitude": data["longitude"],
        "accuracy": data["accuracy"],
        "time": datetime.now(timezone.utc).isoformat()
    }

    locations.append(record)

    return jsonify({"status": "success"})

@app.route("/dashboard")
def dashboard():
    return jsonify(locations)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

