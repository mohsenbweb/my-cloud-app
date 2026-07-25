from flask import Flask, jsonify
from datetime import datetime
import platform
import socket
import os

app = Flask(__name__)

APP_NAME = "My Cloud App"
VERSION = "1.0.0"


@app.route("/")
def home():
    return jsonify({
        "application": APP_NAME,
        "message": "Application is running successfully.",
        "version": VERSION
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "Healthy",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })


@app.route("/version")
def version():
    return jsonify({
        "version": VERSION
    })


@app.route("/info")
def info():
    return jsonify({
        "application": APP_NAME,
        "framework": "Flask",
        "python": platform.python_version(),
        "platform": "Azure Container Apps",
        "container_registry": "Azure Container Registry",
        "ci_cd": "GitHub Actions"
    })


@app.route("/system")
def system():
    return jsonify({
        "hostname": socket.gethostname(),
        "python_version": platform.python_version(),
        "operating_system": platform.system(),
        "os_release": platform.release(),
        "container_revision": os.getenv("CONTAINER_APP_REVISION", "unknown"),
        "environment": os.getenv("ENVIRONMENT", "development"),
        "utc_time": datetime.utcnow().isoformat() + "Z"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)