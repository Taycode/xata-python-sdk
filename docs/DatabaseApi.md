# swagger_client.DatabaseApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_database**](DatabaseApi.md#create_database) | **PUT** /dbs/{db_name} | Create Database
[**delete_database**](DatabaseApi.md#delete_database) | **DELETE** /dbs/{db_name} | Delete Database
[**get_database_list**](DatabaseApi.md#get_database_list) | **GET** /dbs | List databases

# **create_database**
> InlineResponse2011 create_database(db_name, body=body)

Create Database

Create Database with identifier name

### Example

```python
from __future__ import print_function
import time
import XataClient
from XataClient.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = XataClient.DatabaseApi(XataClient.ApiClient(configuration))
db_name = XataClient.DBName() # DBName | The Database Name
body = XataClient.DbsDbNameBody() # DbsDbNameBody |  (optional)

try:
    # Create Database
    api_response = api_instance.create_database(db_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseApi->create_database: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_name** | [**DBName**](.md)| The Database Name | 
 **body** | [**DbsDbNameBody**](DbsDbNameBody.md)|  | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_database**
> delete_database(db_name)

Delete Database

Delete a database and all of its branches and tables permanently.

### Example

```python
from __future__ import print_function
import time
import XataClient
from XataClient.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = XataClient.DatabaseApi(XataClient.ApiClient(configuration))
db_name = XataClient.DBName() # DBName | The Database Name

try:
    # Delete Database
    api_instance.delete_database(db_name)
except ApiException as e:
    print("Exception when calling DatabaseApi->delete_database: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_name** | [**DBName**](.md)| The Database Name | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_list**
> ListDatabasesResponse get_database_list()

List databases

List all databases available in your Workspace.

### Example

```python
from __future__ import print_function
import time
import XataClient
from XataClient.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = XataClient.DatabaseApi(XataClient.ApiClient(configuration))

try:
    # List databases
    api_response = api_instance.get_database_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseApi->get_database_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListDatabasesResponse**](ListDatabasesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

