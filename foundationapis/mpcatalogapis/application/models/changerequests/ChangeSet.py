import json
from application.models.changerequests.ChangeSetDetails import ChangeSetDetails 

class ChangeSet:

    def __init__(self): 
        pass

    def set_details(self, details):
        self.details = details

    def get_details(self):
        return self.details
    
    def get_entityid(self):
        return self.entity_id
    
    def set_entityid(self, entity_id):
        self.entity_id = entity_id

    def set_change_request_name(self, cr_name):
        self.change_request_name = cr_name 

    def get_change_request_name(self):
        return self.change_request_name
    
    def get_product_type(self):
        return self.product_type
    
    def set_product_type(self, type):
        self.product_type = type