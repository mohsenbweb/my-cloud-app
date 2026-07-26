from flask import Flask, jsonify, request, g, abort
from datetime import datetime, UTC
from config import APP_NAME, VERSION, ENVIRONMENT

import platform
import socket
import os
import time
import logging

app = Flask(__name__)

# ----------------------------------------------------
# Logging
# ----------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


@app.before_request
def before_request():
    g.start_time = time.time()

    logger.info(
        "Request started | %s %s",
        request.method,
        request.path
    )


@app.after_request
def after_request(response):
    duration = round((time.time() - g.start_time) * 1000, 2)

    logger.info(
        "Request finished | %s %s | Status: %s | %.2f ms",
        request.method,
        request.path,
        response.status_code,
        duration
    )

    return response


@app.errorhandler(404)
def not_found(error):

    logger.warning(
        "404 Not Found | %s %s",
        request.method,
        request.path
    )

    return jsonify({
        "error": "Not Found",
        "status": 404,
        "path": request.path,
        "timestamp": datetime.now(UTC).isoformat()
    }), 404


@app.errorhandler(500)
def internal_server_error(error):

    logger.exception("Internal Server Error")

    return jsonify({
        "error": "Internal Server Error",
        "status": 500,
        "path": request.path,
        "timestamp": datetime.now(UTC).isoformat()
    }), 500

# ----------------------------------------------------
# Routes
# ----------------------------------------------------

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
        "timestamp": datetime.now(UTC).isoformat()
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
        "environment": ENVIRONMENT,
        "utc_time": datetime.now(UTC).isoformat()
    })

@app.route("/test-error")
def test_error():
    raise Exception("This is a test exception")

# ----------------------------------------------------
# Start Application
# ----------------------------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
