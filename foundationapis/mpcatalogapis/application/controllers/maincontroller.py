from flask import Flask, Blueprint, render_template
from application.services.catalogservice import CatalogService
import application.templates
import logging 
import json

""" This is the main controller which contains the various Routes used to invoke the MP Catalog service."""
app = Flask(__name__)

# Need blueprint for modularization of controllers. 
main_blueprint = Blueprint('main', __name__)

logging.basicConfig(level=logging.INFO)

@main_blueprint.before_request
def initialize_catalogservice(): 
    
    logging.info('Initializing the Services...')
    app.config['catalog_service'] = CatalogService()
    app.config['container'] = 'ContainerProduct'
    app.config['ami'] = 'AmiProduct'
    app.config['saas'] = 'SaaSProduct'

# To get list of products (ami, containers, saas)
@main_blueprint.route("/getproducts/<type>")
def get_products(type):
    logging.info('Calling Get Products from MP Catalog.')
    catalog_service = app.config['catalog_service'] 
    result = 'Invalid Input'
    try:
        result = catalog_service.getProducts(app.config[type]) 
    except Exception as ex:
        logging.error(f'Exception occured while getting list of products for product type:', app.config['type'])
        logging.error(ex)
        result= str(ex)
    
    logging.info(result)
    return render_template('display.html', title='Marketplace Catalog - Product List Page', json_data=result['EntitySummaryList'])

#To get details of a given Product ID. 
@main_blueprint.route("/getproductdetail/<productid>")
def get_product_details(productid):
    logging.info('Calling Get Product details from MP Catalog.')
    logging.info('Input Product ID is: ', productid)
    catalog_service = app.config['catalog_service'] 
    result = 'Invalid Input'
    try:
        result = catalog_service.getProductDetails(productid) 
    except Exception as ex:
        logging.error(f'Exception occured while retrieving details for the product id:', productid)
        logging.error(ex)
        result= str(ex)

    result = json.loads(result['Details'])
    #logging.info(result)
    return render_template('product_details.html', title='Marketplace Catalog - Product Details Page', product_details_json= result)

# To get list of all change request sets performed on products. 
@main_blueprint.route("/getchangesets")
def get_changeset_list():
    logging.info('Getting list of ChangeSets from MP Catalog.')
    catalog_service = app.config['catalog_service'] 
    result = 'Invalid Input'
    try:
        result = catalog_service.getchangesets() 
    except Exception as ex:
         logging.error('Exception occured while retrieving change set list')
         logging.error(ex)
         result= str(ex)
    
    return render_template('changeset_display.html', title='Marketplace Catalog - Product Change Request Page', json_data=result['ChangeSetSummaryList'])

# To get details of a specific Change Request set given the ID. 
@main_blueprint.route("/retrievechangeset/<csid>")
def retrieve_changeset_details(csid):
    logging.info('Retrieve details of ChangeSet from MP Catalog.')
    logging.info('Input ChangeSet ID is: ', csid)
    catalog_service = app.config['catalog_service'] 
    result = 'Invalid Input'
    try:
        result = catalog_service.retrievechangeset(csid) 
    except Exception as ex:
        logging.error(f'Exception occured while retrieving change set details for id: ', csid)
        logging.error(ex)
        result= str(ex)

    return render_template('changeset_details.html', title='Marketplace Catalog - Product Change Request Details Page', product_details_json= result)

# To Cancel the given Change Request set by ID. 
@main_blueprint.route("/cancelchangeset/<csid>")
def get_cancel_changeset(csid):
    logging.info('Initiating Cancel operation for ChangeSet.')
    logging.info('Input ChangeSet ID is: ', csid)
    catalog_service = app.config['catalog_service'] 

    result = ''
    try:
        result = catalog_service.cancelchangeset(csid) 
    except Exception as ex:
        logging.error(f'Exception occured while cancelling change set details for id: ', csid)
        result= str(ex)

    return render_template('changeset_action.html', title='Marketplace Catalog - Product Change Request Status Page', changeset_details_json= result)
