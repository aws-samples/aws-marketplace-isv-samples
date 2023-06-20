import boto3
import json 

from application.models.changerequests.ChangeSet import ChangeSet
from application.models.changerequests.ChangeSetDetails import ChangeSetDetails
from application.models.changerequests.ChangeSetEncoder import ChangeSetEncoder

class CatalogService:
    """This is Class for invoking the Marketplace Catalog APIs using the Python SDK."""
    
    def __init__(self):
        self.client = boto3.client('marketplace-catalog', region_name='us-east-1')
        self.catalog = 'AWSMarketplace'
        
    # To get list of Marketplace Catalog Entities or products. 
    def getProducts(self, productType):
        response = self.client.list_entities (
            Catalog= self.catalog,
            EntityType=productType       
        ) 
        return response 
    
    # To get list of all Marketplace Catalog Entities or products. 
    def get_all_products(self):
        result =  []

        # get all ami entities. 
        response = self.getProducts('AmiProduct'),
        json_data = response[0]
        ami_list = json_data["EntitySummaryList"]
        result.append(ami_list)
        

        # get all container entities. 
        response = self.getProducts('ContainerProduct'),
        json_data = response[0]
        container_list = json_data["EntitySummaryList"]
        result.append(container_list)
       
         

        # get all saas entities. 
        response = self.getProducts('SaaSProduct'),
        json_data = response[0]
        saas_list = json_data["EntitySummaryList"]
        result.append(saas_list)

        return result

    # To get details of a Marketplace Catalog Product. 
    def getProductDetails(self, id): 
        response = self.client.describe_entity (
            Catalog=self.catalog,
            EntityId=id,
        )
        return response
    
    # To get list of Marketplace Catalog Change Sets. 
    def getchangesets(self, statustype='FAILED'): 
        response = self.client.list_change_sets (
            Catalog=self.catalog,
            FilterList=[
                {
                    'Name': 'Status',
                    'ValueList': [
                        statustype,
                    ]
                },
            ]
        )
        return response
    
    # To get details of a specific Change Set given the ID. 
    def retrievechangeset(self, changesetid):
        response = self.client.describe_change_set (
            Catalog=self.catalog,
            ChangeSetId=changesetid, # change to changeset id. 
        )
        return response
    
    # To Cancel a specific Change Set given the ID. 
    def cancelchangeset(self, changesetid):
        '''Must be sent before the status of the 
           request changes to APPLYING, 
           the final stage of completing your change request''' 
        response = self.client.cancel_change_set (
            Catalog=self.catalog,
            ChangeSetId=changesetid
        ) 
        return response
    
    # To tag a resource 
    def tag_resource(self, entity_arn, tag_name, tag_value):

        response = self.client.tag_resource(
            ResourceArn=entity_arn, 
            Tags=[
                {
                    'Key': tag_name,
                    'Value': tag_value
                },
            ]
        )

        return response

    # To tag a resource 
    def untag_resource(self, entity_arn, tag_key):

        response = self.client.untag_resource(
            ResourceArn=entity_arn, 
            TagKeys=[tag_key]
        )

        return response
    
    # To list tags for a given resource ARN
    def list_tags(self, entity_arn):

        response = self.client.list_tags_for_resource(
            ResourceArn=entity_arn
        )

        return response 
    
    # To update product information...
    def update_product(self, changeSet):
        
        changesetDetails = changeSet.get_details()
        details = json.dumps(changesetDetails, cls=ChangeSetEncoder)
        print('Value of change set details: ', details)
        response = self.client.start_change_set(
            Catalog=self.catalog,
            ChangeSetName=changeSet.get_change_request_name(),
            ChangeSet=[
                {
                    'ChangeType':'UpdateInformation',
                    'Entity': {
                        'Type':changeSet.get_product_type(),
                        'Identifier': changeSet.entity_id
                    },
                    'Details': details,
                },
            ]
        )

        #print('Response from update_product after calling start change set.')
        print(response)
        return response 