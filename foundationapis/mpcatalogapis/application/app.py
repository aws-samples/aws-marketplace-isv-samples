from flask import Flask, render_template
import application.templates
import logging 
import json
import application.controllers
from .controllers.maincontroller import main_blueprint

""" This is the first point of entry for the Web application which will display the home page. """
app = Flask(__name__)

# Register the blueprint controller class which contains the various API routes used for catalog operations.
app.register_blueprint(main_blueprint)

@app.before_request
def initialize_catalogservice(): 
    logging.info('Initializing the Services...')
    app.config['container'] = 'ContainerProduct'
    app.config['ami'] = 'AmiProduct'
    app.config['saas'] = 'SaaSProduct'

@app.template_filter('json_loads')
def json_loads(value):
    return json.loads(value)

@app.route("/")
def main_page(): 
    return render_template('homepage.html', title='Marketplace Catalog API Reference', page='home')
if __name__ == "__main__":
    app.run()