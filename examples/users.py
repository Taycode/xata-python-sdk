import os

import XataClient
from dotenv import load_dotenv

load_dotenv()

client = XataClient.ApiClient()
client.set_default_header('Authorization', f'Bearer {os.getenv("XATA_API_KEY")}')
user_api_instance = XataClient.UsersApi(client)
user = user_api_instance.get_user()

