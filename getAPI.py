import boto3
import json

def lambda_handler(event, context):
   cuerpo=json.loads(event["body"])
   client = boto3.resource('dynamodb')
   table = client.Table('prode')
   response = table.get_item(Key={'id': cuerpo['id']})
   
   if 'Item' in response:
      return {
        
         'statusCode' :'200',
         'body' : json.dumps(response['Item'])
      }
   else:
       return {
           'statusCode': '404',
           'body': 'Not found'
    }
    