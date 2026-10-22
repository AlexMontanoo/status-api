from flask import Flask, jsonify
from datetime import datetime
import socket

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })

@app.route("/info")
def info():
    return jsonify({
        "service": "Network Status API",
        "hostname": socket.gethostname(),
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route("/version")
def version():
    return jsonify({
        "version": "1.0"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
