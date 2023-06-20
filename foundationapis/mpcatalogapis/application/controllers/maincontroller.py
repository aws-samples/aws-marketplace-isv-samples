from flask import Flask, Blueprint, render_template, request
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from application.services.catalogservice import CatalogService
from application.models.changerequests.ChangeSet import ChangeSet
from application.models.changerequests.ChangeSetDetails import ChangeSetDetails
import secrets
import application.templates
import logging 
import json
import traceback

""" This is the main controller which contains the various Routes used to invoke the MP Catalog service."""
app = Flask(__name__)

# Need blueprint for modularization of controllers. 
main_blueprint = Blueprint('main', __name__)

logging.basicConfig(level=logging.INFO)
secret_key = secrets.token_hex(16)
print('secret key is: %s', secret_key)
app.config['SECRET_KEY'] = secret_key
csrf = CSRFProtect(app)

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

# To get list of products (ami, containers, saas)
@main_blueprint.route("/getallproducts")
def get_all_products():
    logging.info('Calling Get All Products from MP Catalog.')
    catalog_service = app.config['catalog_service'] 
    result = 'Invalid Input'
    try:
        result = catalog_service.get_all_products() 
        print("*" * 80)
        logging.info('The result from the get all products')  
        print("*" * 80)
    except Exception as ex:
        logging.error(f'Exception occured while getting all products')
        traceback.print_exc()
        result= str(ex)

    logging.info(result)
    return render_template('display_all_products.html', title='Marketplace Catalog - Product List Page', json_data=result)


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


def get_tags(arn):
    logging.info('Listing Tags.')
    logging.info('ARN after concatenation is: %s', arn)
    catalog_service = app.config['catalog_service'] 

    result = ''
    try:
        result = catalog_service.list_tags(arn) 
        logging.info('Response from Listing tags');
        logging.info(result)
    except Exception as ex:
        logging.error(f'Exception occured while listing tags for arn: ', arn)
        result= str(ex)

    return result

@main_blueprint.route("/managetags/<op>/<part>/<type>/<id>")
def redirect_managetags_page(op, part, type, id):
    arn=part + '/' + type + '/' + id
    result = get_tags(arn)

    return render_template('manage_tags.html', title='Marketplace Catalog - Product Tagging Status Page', tags_list_json = result['Tags'], entity_arn=arn, operation = op)

@main_blueprint.route("/processtag", methods=['POST'])
def apply_tag():
    logging.info('Initiating Tag operation for the product.')
    catalog_service = app.config['catalog_service'] 
    tag_name = request.form['tagname']
    tag_value = request.form['tagvalue']
    entity_arn = request.form.get('entity_arn')
    result = ''
    new_result_set = []

    logging.info('Input tag name is: %s', tag_name)
    logging.info('Input tag value is: %s', tag_value)
    logging.info('Input ARN is: %s', entity_arn)
    

    try:
        result = catalog_service.tag_resource(entity_arn, tag_name, tag_value) 
        print("Result of adding Tag is: %s" , result['ResponseMetadata']['HTTPStatusCode'])
        if result['ResponseMetadata']['HTTPStatusCode'] == 200: 
            new_result_set = get_tags(entity_arn)

    except Exception as ex:
        logging.error(f'Exception occured while tagging for ARN: ', entity_arn)
        result= str(ex)

    return render_template('manage_tags.html', title='Marketplace Catalog - Product Tagging Status Page', tags_list_json = new_result_set['Tags'], entity_arn = entity_arn, operation = 'process_results')

# To remove Tag from a given resource. 
@main_blueprint.route("/removetag/<part>/<type>/<id>/<tagkey>", methods=['GET','POST'])
def remove_tag(part, type, id, tagkey):
    
    catalog_service = app.config['catalog_service']  
    entity_arn = part + '/' + type + '/' + id
    logging.info('Input tag key is: %s', tagkey)
    logging.info('Input entity arn is: %s', entity_arn)
    
    result = ''
    new_result_set = []
    try:
        result = catalog_service.untag_resource(entity_arn, tagkey) 
        if result['ResponseMetadata']['HTTPStatusCode'] == 200: 
            new_result_set = get_tags(entity_arn)

    except Exception as ex:
        logging.error(f'Exception occured while untagging for arn: ', entity_arn)
        result= str(ex)
        

    return render_template('manage_tags.html', title='Marketplace Catalog - Manage Tag resources', tags_list_json = new_result_set['Tags'], entity_arn = entity_arn)

@main_blueprint.route("/getproductform/<part>/<type>/<id>", methods=['GET'])
def get_update_product_form(part,type,id):
    logging.info('Initiating Update operation for the product.')
    catalog_service = app.config['catalog_service'] 
    entity_arn = part + '/' + type + '/' + id
    result = ''
    details_str = ''
    details_json = ''
   
    try:
        result = catalog_service.getProductDetails(id) 
        logging.info('Product response from catalog: %s', result)
        if result['ResponseMetadata']['HTTPStatusCode'] == 200: 
            details_str = result['Details']
            details_json = json.loads(details_str)

    except Exception as ex:
        logging.error(f'Exception occured while tagging for ARN: ', entity_arn)
        result= str(ex)

    return render_template('update_product.html', title='Marketplace Catalog - Update Product Page', result_json=details_json, entity_arn = entity_arn, entity_id = id)


@main_blueprint.route("/updateproduct", methods=['POST'])
def update_product():
    logging.info('Initiating Update operation for the product.')
    catalog_service = app.config['catalog_service'] 
    entity_arn = request.form['entity_arn']
    entity_id = request.form['entity_id']
    product_title = request.form['product_title']
    result1 = ''
    result2 = ''
    details_str = ''
    details_json = ''
  
    logging.info('Value of arn is: %s', entity_arn)
    logging.info('Value of product title is: %s', product_title)
    try:
        cs = populate_change_set(request)
        result1 = catalog_service.update_product(cs) 
        if result1['ResponseMetadata']['HTTPStatusCode'] == 200:
            print('Change set operation was successful. Now, retrieve product details.')
            result2 = catalog_service.getProductDetails(entity_id) 

        print(result1)
        if result2['ResponseMetadata']['HTTPStatusCode'] == 200: 
            details_str = result2['Details']
            details_json = json.loads(details_str)

    except Exception as ex:
        logging.error(f'Exception occured while tagging for ARN: ', entity_arn)
        result= str(ex)

    return render_template('update_product.html', title='Marketplace Catalog - Update Product Page', result_json=details_json, entity_arn = entity_arn)

def populate_change_set(request): 
    cs = ChangeSet() 
    details = ChangeSetDetails()

    details.set_title(request.form['product_title'])
    details.set_short_description(request.form['short_description']) 
    details.set_long_description(request.form['long_description']) 
    details.set_categories(request.form['categories'])
    details.set_highlights(request.form['highlights'])
    details.set_keywords(request.form['keywords'])
    details.set_logo_url(request.form['logo_url'])
    details.set_sku(request.form['sku'])
    cs.set_details(details)
    cs.set_entityid(request.form['entity_id'])
    
    return cs