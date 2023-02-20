import checkoutLicense
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

def init():
    if checkoutLicense.checkoutLic():
        app.run(host='0.0.0.0', port=80)
    else:
        print('Could not start api server because of invalid LM checkout api call')

if __name__ == '__main__':
    init()