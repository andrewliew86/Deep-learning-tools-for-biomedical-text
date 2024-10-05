# Create a sagemaker inference endpoint for a HuggingFace model. See here: https://github.com/huggingface/notebooks/blob/main/sagemaker/10_deploy_model_from_s3/deploy_transformer_model_from_s3.ipynb
from sagemaker.huggingface import HuggingFaceModel
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Now you can access the variables
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_default_region = os.getenv('AWS_DEFAULT_REGION')
aws_role = os.getenv('AWS_ROLE')
# Example of using the credentials with boto3
import boto3

session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_default_region
)
sagemaker = session.client('sagemaker')

role =  aws_role  # Example: "arn:aws:iam::18022222:role/service-role/AmazonSageMaker-ExecutionRole-202231321"

# create Hugging Face Model Class
huggingface_model = HuggingFaceModel(
   model_data="s3://test-finetuning-bucket/fined-tuned-model/model.tar.gz",  # path to your trained sagemaker model
   role=role, # iam role with permissions to create an Endpoint
   transformers_version="4.26", # transformers version used
   pytorch_version="1.13", # pytorch version used
   py_version="py39", # python version of the DLC
)

# deploy model to SageMaker Inference
predictor = huggingface_model.deploy(
   initial_instance_count=1,
   instance_type="ml.g4dn.2xlarge",
   endpoint_name='huggingface-endpoint'
   )

# example request, you always need to define "inputs"
data = {
   "inputs": "Alpelisib plus fulvestrant in PIK3CA-mutated, hormone receptor-positive advanced breast cancer after a CDK4/6 inhibitor (BYLieve): one cohort of a phase 2, multicentre, open-label, non-comparative study"
}

# request
predictor.predict(data)