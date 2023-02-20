from datetime import datetime
import os
import boto3

client = boto3.client('meteringmarketplace', region_name='us-east-1')

def reportUsage(dimension):
    try:
        response = client.meter_usage(
            ProductCode= os.environ["PROD_CODE"],
            UsageDimension=dimension['name'],
            UsageQuantity=int(dimension['quantity']),
            Timestamp=datetime.now()
        )
        print('Response from Marketplace Metering API call ' + str(response))
        return True
    except Exception as e:
        print("Error could not report usage using Marketplace metering api **" + str(e))
        return False
