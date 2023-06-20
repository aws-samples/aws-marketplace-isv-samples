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