import logging
from config import APP_NAME, VERSION, ENVIRONMENT
from flask import Flask, jsonify
from datetime import datetime
import platform
import socket
import os


app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)


@app.route("/")
def home():
    logger.info("Home endpoint called")

    return jsonify({
        "application": APP_NAME,
        "message": "Application is running successfully.",
        "version": VERSION
    })


@app.route("/health")
def health():
    logger.info("Health endpoint called")

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
    logger.info("System endpoint called")

    return jsonify({
        "hostname": socket.gethostname(),
        "python_version": platform.python_version(),
        "operating_system": platform.system(),
        "os_release": platform.release(),
        "container_revision": os.getenv("CONTAINER_APP_REVISION", "unknown"),
        "environment": ENVIRONMENT,
        "utc_time": datetime.utcnow().isoformat() + "Z"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)