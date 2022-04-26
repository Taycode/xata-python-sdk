# swagger_client.UsersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_api_key**](UsersApi.md#create_user_api_key) | **POST** /user/keys/{key_name} | Create and return new API key
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /user | Delete user
[**delete_user_api_key**](UsersApi.md#delete_user_api_key) | **DELETE** /user/keys/{key_name} | Delete an existing API key
[**get_user**](UsersApi.md#get_user) | **GET** /user | Get user details
[**get_user_api_keys**](UsersApi.md#get_user_api_keys) | **GET** /user/keys | Get the list of user API keys
[**update_user**](UsersApi.md#update_user) | **PUT** /user | Update user info

# **create_user_api_key**
> InlineResponse201 create_user_api_key(key_name)

Create and return new API key

Create and return new API key

### Example

```python
from __future__ import print_function
import time
import XataClient
from XataClient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = XataClient.UsersApi()
key_name = XataClient.APIKeyName() # APIKeyName | API Key name

try:
    # Create and return new API key
    api_response = api_instance.create_user_api_key(key_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_name** | [**APIKeyName**](.md)| API Key name | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user()

Delete user

Delete the user making the request

### Example

```python
from __future__ import print_function
import time
import XataClient
from XataClient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = XataClient.UsersApi()

try:
    # Delete user
    api_instance.delete_user()
except ApiException as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_api_key**
> delete_user_api_key(key_name)

Delete an existing API key

Delete an existing API key

### Example

```python
from __future__ import print_function
import time
import XataClient
from XataClient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = XataClient.UsersApi()
key_name = XataClient.APIKeyName() # APIKeyName | API Key name

try:
    # Delete an existing API key
    api_instance.delete_user_api_key(key_name)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_name** | [**APIKeyName**](.md)| API Key name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserWithID get_user()

Get user details

Return details of the user making the request

### Example

```python
from __future__ import print_function
import time
import XataClient
from XataClient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = XataClient.UsersApi()

try:
    # Get user details
    api_response = api_instance.get_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserWithID**](UserWithID.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_api_keys**
> InlineResponse200 get_user_api_keys()

Get the list of user API keys

Retrieve a list of existing user API keys

### Example

```python
from __future__ import print_function
import time
import XataClient
from XataClient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = XataClient.UsersApi()

try:
    # Get the list of user API keys
    api_response = api_instance.get_user_api_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_api_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> UserWithID update_user(body=body)

Update user info

Update user info

### Example

```python
from __future__ import print_function
import time
import XataClient
from XataClient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = XataClient.UsersApi()
body = XataClient.User() # User |  (optional)

try:
    # Update user info
    api_response = api_instance.update_user(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)|  | [optional] 

### Return type

[**UserWithID**](UserWithID.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

