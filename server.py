from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"status": "ok", "message": "Render Flask server running"})

@app.route("/season/<int:year>")
def season_data(year):
    try:
        # Simple test request
        url = f"https://api.openf1.org/v1/sessions?year={year}"
        r = requests.get(url)
        return jsonify({"success": True, "data": r.json()})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run()
