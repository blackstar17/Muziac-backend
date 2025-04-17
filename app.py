import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7117))  # Use 7117 if no PORT environment variable is set
    app.run(host="0.0.0.0", port=port)
