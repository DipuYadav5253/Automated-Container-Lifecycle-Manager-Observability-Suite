from flask import Flask
import os
import signal
import time

app = Flask(__name__)

# This is the "Heartbeat" endpoint
@app.route('/health')
def health():
    return {"status": "ok", "message": "I am alive!"}, 200

# This is a "Suicide" endpoint to help us test self-healing later
@app.route('/kill')
def kill():
    print("Received kill signal...")
    os.kill(os.getpid(), signal.SIGTERM)
    return "Shutting down..."

if __name__ == "__main__":
    # We run on port 5000
    app.run(host="0.0.0.0", port=5000)