from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Hello from Flask!"})

@app.route("/api")
def home():
    return jsonify({"message": "Found Api"})

if __name__ == "__main__":
    app.run()