# lambdaREST

## 1 Insfraestructura:

- A DynamoDB table named “Prode” with a `Partition key` named `id`.
- An IAM Role that grants a Lambda function with **permissions** to:
  - Write and read from the “Prode” table.
  - Create log groups, a log stream and write log events.
- Two Lambda functions, one for the GET operation, and one for the POST operation.
  - Set the runtime to Python 3.7
  - Configure the function to use the IAM role you created.
  
## 2 Codeamos las lambdas:

### POST:

```python
import boto3
def lambda_handler(event, context):
   client = boto3.resource('dynamodb')
   table = client.Table('prode')
   response = table.put_item(
       Item={
           'id': event['id'],
           'name': event['name'],
           'breed': event['breed'],
           'gender': event['gender'],
           'owner': event['owner'],
          'birthday': event['birthday']
       })
   return {'statusCode': response['ResponseMetadata']['HTTPStatusCode'], 'body': 'Record ' + event['id'] + ' added'}
```

## 3 Seteamos las conexiones de la API:

## 4 Deploy & Testing

  
