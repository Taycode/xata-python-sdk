import os

import XataClient
from dotenv import load_dotenv
load_dotenv()


class UserExample(object):
    def __init__(self):
        self.client = XataClient.ApiClient()
        self.client.set_default_header('Authorization', f'Bearer {os.getenv("XATA_API_KEY")}')
        self.api = XataClient.UsersApi(self.client)

    def get_user_details(self):
        """
        path: GET /user
        Returns User Details
        """
        user = self.api.get_user()
        return user

    def update_user_info(self):
        """
        path: PUT /user
        Updates User Info
        """
        updated_user = self.api.update_user(body={
            'email': 'test@example.io',
            'fullname': 'John Doe'
        })
        return updated_user

    def delete_user(self):
        """
        path: DELETE /user
        Deletes the User making the request
        """
        return self.api.delete_user()

    def get_list_of_user_api_keys(self):
        """
        path: GET /user/keys
        Retrieves a list of existing user API keys
        """
        return self.api.get_user_api_keys()

    def create_and_return_new_api_key(self, key_name: str):
        """
        path: POST /user/keys/{key}
        Creates and return new API key
        """
        return self.api.create_user_api_key(key_name)

    def delete_existing_api_key(self, key_name: str):
        """
        path: DELETE /user/keys/{key}
        Deletes an existing API key
        """
        return self.api.delete_user_api_key(key_name)


Example = UserExample()
print(Example.get_user_details())
