from flask import Flask
import logging

logging.basicConfig(level=logging.ERROR)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

def init():
    app.run(host='0.0.0.0', port=80)

if __name__ == '__main__':
    init()



