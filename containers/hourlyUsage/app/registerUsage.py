import boto3
import os
import logging

logging.basicConfig(level=logging.INFO)
client = boto3.client('meteringmarketplace', region_name='us-east-1')

def registerUsage():
    try:
        response = client.register_usage(
            ProductCode=os.environ["PROD_CODE"],
            PublicKeyVersion=1
        )
        logging.info('Response from RegisterUsage API call '+str(response))
        return True
    except Exception as e:
        logging.error("Error could not call registerusage api **" + str(e))
        return False