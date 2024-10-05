import boto3
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Now you can access the variables
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_default_region = os.getenv('AWS_DEFAULT_REGION')

# Specify endpoint
ENDPOINT_NAME = 'huggingface-endpoint'  # Replace with your endpoint name

# Initialize the SageMaker runtime client
runtime = boto3.client(
    'sagemaker-runtime',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_default_region
)

# Prepare the payload
payload = {
    "inputs": "Alpelisib plus fulvestrant in PIK3CA-mutated, hormone receptor-positive advanced breast cancer after a CDK4/6 inhibitor (BYLieve): one cohort of a phase 2, multicentre, open-label, non-comparative study"
}

# Invoke the endpoint
response = runtime.invoke_endpoint(
    EndpointName=ENDPOINT_NAME,
    ContentType='application/json',
    Body=json.dumps(payload)
)
result = json.loads(response['Body'].read().decode())
print(result)