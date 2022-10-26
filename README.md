# lambdaREST

## 1 Insfraestructura:

- A DynamoDB table named “Prode” with a `Partition key` named `id`.
- An IAM Role that grants a Lambda function with **permissions** to:
  - Write and read from the “Prode” table (`AmazonDynamoDBFullAccess`).
  - Create log groups, a log stream and write log events.
- Two Lambda functions, one for the GET operation, and one for the POST operation.
  - Set the runtime to Python 3.7
  - Configure the function to use the IAM role you created.
  
## 2 Codeamos las lambdas:

### POST:

Creamos la lambda:

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

Podemos probarla, vamos a  Test tab, creamos un nuevo test del template `hello-world` y usamos:

```json
{
  "id": "d290f1ee-6c54-4b01-90e6-d701748f0851",

  "name": "Hansie",

  "breed": "Dachshund",

  "gender": "Male",

  "owner": "Mike",

  "birthday": "2012-05-15"
}
```
Si todo sale  bien deberiamos ver el mensaje:

```json
{
  "statusCode": 200,

  "body": "Record d290f1ee-6c54-4b01-90e6-d701748f0851 added"
}
```
### GET:

Creamos la lambda:

```python
import boto3

def lambda_handler(event, context):
   client = boto3.resource('dynamodb')
   table = client.Table('prode')
   response = table.get_item(Key={'id': event['id']})
   if 'Item' in response:
       return response['Item']
   else:
       return {
           'statusCode': '404',
           'body': 'Not found'
    }
```
Podemos probarla, vamos a  Test tab, creamos un nuevo test del template `hello-world` y usamos:
```json
{
  "id": "d290f1ee-6c54-4b01-90e6-d701748f0851"
}
```
## 3 Seteamos las conexiones de la API:

## 4 Deploy & Testing

  
