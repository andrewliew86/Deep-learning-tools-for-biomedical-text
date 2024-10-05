import streamlit as st
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

st.title("🧬Fine-tuned BioBERT model for medical text classification🧬")
st.write("Enter a publication title from PubMed that is related to CDK4/6 or bacterial cell division in the box below to start the analysis")

# User input
user_input = st.text_area("")

# Analyze button
if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        with st.spinner("Analyzing..."):
            try:
                # Prepare the payload
                payload = {
                    "inputs": user_input
                }

                # Invoke the endpoint
                response = runtime.invoke_endpoint(
                    EndpointName=ENDPOINT_NAME,
                    ContentType='application/json',
                    Body=json.dumps(payload)
                )

                # Parse the response
                result = json.loads(response['Body'].read().decode())
                
                st.success("Analysis Complete:")
                st.json(result)
            except Exception as e:
                st.error(f"An error occurred: {e}")