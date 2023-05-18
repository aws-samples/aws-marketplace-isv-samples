import boto3

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
    