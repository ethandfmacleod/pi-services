from flask import Flask
import os

app = Flask(__name__)


@app.route("/wake")
def wake():
    mac_address = os.environ.get("WAKE_MAC_ADDRESS")
    if not mac_address:
        return "MAC address not set", 500

    os.system(f"wakeonlan {mac_address}")
    return f"Sent magic packet to {mac_address}!", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
