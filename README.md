# lambdaREST

## Primeros pasos:

- A DynamoDB table named “Prode” with a primary key named `id`.
- An IAM Role that grants a Lambda function with permission to:
  - Write and read from the “Prode” table.
  - Create log groups, a log stream and write log events.
- Two Lambda functions, one for the GET operation, and one for the POST operation.
  - Set the runtime to Python 3.7
  - Configure the function to use the IAM role you created.
  
  
