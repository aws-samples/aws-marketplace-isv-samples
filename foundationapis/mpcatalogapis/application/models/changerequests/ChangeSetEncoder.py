import json
from application.models.changerequests.ChangeSetDetails import ChangeSetDetails


class ChangeSetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ChangeSetDetails):
            return {
                    'ProductTitle': obj.title, 
                    'ShortDescription': obj.short_description,
                    'LongDescription': obj.long_description,
                    'Categories': [obj.categories],
                    'LogoUrl': obj.logo_url,
                    'SearchKeywords': [obj.keywords],
                    'Highlights': [obj.highlights],
                    'Sku': obj.sku

                   }
        return super().default(obj)