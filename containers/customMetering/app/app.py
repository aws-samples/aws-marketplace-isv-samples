import customMetering
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/meter")
def meterUsage():
    meterrecord = {
        'name':'customDimension1',
        'quantity':'1'
    }
    if customMetering.reportUsage(meterrecord):
        print('Reported usaeg successfully!')
        return "Report usage successful!"
    else:
        print('Failed to call reportUsage')
        return "Report usage failed!"

def init():
    app.run(host='0.0.0.0', port=80)

if __name__ == '__main__':
    init()