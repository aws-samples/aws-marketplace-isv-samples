import boto3
import os
from datetime import datetime
import uuid

client = boto3.client('license-manager', region_name='us-east-1')

def checkoutLic():
    try:
        response = client.checkout_license(
            ProductSKU=os.environ["PROD_ID"],
            CheckoutType='PROVISIONAL',
            KeyFingerprint=os.environ["ISSUER_FT"],
            Entitlements=[
                {
                    'Name': 'ReadOnly',
                    'Value': '1',
                    'Unit': 'Count'
                },
            ],
            ClientToken=str(uuid.uuid4())
        )
        print('Check out license successful '+str(response))
        if(len(response['EntitlementsAllowed'])>0 and int(response['EntitlementsAllowed'][0]['Value'])>0):
            return True
        else:
            print('Insufficient or expired license')
            return False
    except Exception as e:
        print("Error could not call LM checkout api **" + str(e))
        return False