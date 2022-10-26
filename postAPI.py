import boto3
import json

def lambda_handler(event, context):
   client = boto3.resource('dynamodb')
   table = client.Table('prode')
   cuerpo=json.loads(event["body"])
   response = table.put_item(
       Item=cuerpo)
   return {'statusCode': response['ResponseMetadata']['HTTPStatusCode'], 'body': 'Record ' + event['id'] + ' added'}