import os
from dotenv import load_dotenv
from azure.identity import ClientSecretCredential
from openai import AzureOpenAI
 
load_dotenv()
 
tenant_id = os.getenv("AZURE_TENANT_ID")
client_id = os.getenv("AZURE_CLIENT_ID")
client_secret = os.getenv("AZURE_CLIENT_SECRET")
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
api_client_id = f"api://" + client_id + "/.default"
api_key = os.getenv("API_KEY")
 
credential = ClientSecretCredential(
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=client_secret
)
 
# client = AzureOpenAI(
#   api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
#   api_version = "2024-10-21",
#   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
# )
 

client = AzureOpenAI(
    api_version="",    # required API version
    azure_endpoint=azure_endpoint,
    azure_ad_token_provider=lambda: credential.get_token(api_client_id).token, # newly added
    default_headers={
        "api-key": api_key
    }
)
 
response = client.chat.completions.create(
    model=azure_deployment_name,  
    messages=[
        {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
        {"role": "user", "content": "Who were the founders of Amazon?"}
    ]
)

# print(response.model_dump_json(indent=2))
print(response.choices[0].message.content)