import registerUsage
from flask import Flask
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

def init():
    if registerUsage.registerUsage():
        app.run(host='0.0.0.0', port=80)
    else:
        logging.error('Failed to call registerusage so cannot start api server')

if __name__ == '__main__':
    init()


