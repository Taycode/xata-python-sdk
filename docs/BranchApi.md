# swagger_client.BranchApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_branch**](BranchApi.md#create_branch) | **PUT** /db/{db_branch_name} | Create Database branch
[**delete_branch**](BranchApi.md#delete_branch) | **DELETE** /db/{db_branch_name} | Delete Database branch
[**execute_branch_migration_plan**](BranchApi.md#execute_branch_migration_plan) | **POST** /db/{db_branch_name}/migrations/execute | Migrate branch
[**get_branch_details**](BranchApi.md#get_branch_details) | **GET** /db/{db_branch_name} | Get branch schema and metadata
[**get_branch_list**](BranchApi.md#get_branch_list) | **GET** /dbs/{db_name} | List branches
[**get_branch_metadata**](BranchApi.md#get_branch_metadata) | **GET** /db/{db_branch_name}/metadata | Get Branch Metadata
[**get_branch_migration_history**](BranchApi.md#get_branch_migration_history) | **GET** /db/{db_branch_name}/migrations | Get branch migration history
[**get_branch_migration_plan**](BranchApi.md#get_branch_migration_plan) | **POST** /db/{db_branch_name}/migrations/plan | Compute migration plan
[**get_branch_stats**](BranchApi.md#get_branch_stats) | **GET** /db/{db_branch_name}/stats | Branch stats
[**update_branch_metadata**](BranchApi.md#update_branch_metadata) | **PUT** /db/{db_branch_name}/metadata | Update branch metadata

# **create_branch**
> create_branch(db_branch_name, body=body, _from=_from)

Create Database branch

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BranchApi(swagger_client.ApiClient(configuration))
db_branch_name = swagger_client.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
body = swagger_client.DbDbBranchNameBody() # DbDbBranchNameBody |  (optional)
_from = '_from_example' # str | Name of source branch to branch the new schema from (optional)

try:
    # Create Database branch
    api_instance.create_branch(db_branch_name, body=body, _from=_from)
except ApiException as e:
    print("Exception when calling BranchApi->create_branch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **body** | [**DbDbBranchNameBody**](DbDbBranchNameBody.md)|  | [optional] 
 **_from** | **str**| Name of source branch to branch the new schema from | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_branch**
> delete_branch(db_branch_name)

Delete Database branch

Delete the branch in the database and all its resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BranchApi(swagger_client.ApiClient(configuration))
db_branch_name = swagger_client.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 

try:
    # Delete Database branch
    api_instance.delete_branch(db_branch_name)
except ApiException as e:
    print("Exception when calling BranchApi->delete_branch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_branch_migration_plan**
> execute_branch_migration_plan(db_branch_name, body=body)

Migrate branch

Apply a migration plan to the branch

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BranchApi(swagger_client.ApiClient(configuration))
db_branch_name = swagger_client.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
body = swagger_client.MigrationsExecuteBody() # MigrationsExecuteBody |  (optional)

try:
    # Migrate branch
    api_instance.execute_branch_migration_plan(db_branch_name, body=body)
except ApiException as e:
    print("Exception when calling BranchApi->execute_branch_migration_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **body** | [**MigrationsExecuteBody**](MigrationsExecuteBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branch_details**
> DBBranch get_branch_details(db_branch_name)

Get branch schema and metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BranchApi(swagger_client.ApiClient(configuration))
db_branch_name = swagger_client.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 

try:
    # Get branch schema and metadata
    api_response = api_instance.get_branch_details(db_branch_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BranchApi->get_branch_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 

### Return type

[**DBBranch**](DBBranch.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branch_list**
> ListBranchesResponse get_branch_list(db_name)

List branches

List all available Branches

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BranchApi(swagger_client.ApiClient(configuration))
db_name = swagger_client.DBName() # DBName | The Database Name

try:
    # List branches
    api_response = api_instance.get_branch_list(db_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BranchApi->get_branch_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_name** | [**DBName**](.md)| The Database Name | 

### Return type

[**ListBranchesResponse**](ListBranchesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branch_metadata**
> BranchMetadata get_branch_metadata(db_branch_name)

Get Branch Metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BranchApi(swagger_client.ApiClient(configuration))
db_branch_name = swagger_client.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 

try:
    # Get Branch Metadata
    api_response = api_instance.get_branch_metadata(db_branch_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BranchApi->get_branch_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 

### Return type

[**BranchMetadata**](BranchMetadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branch_migration_history**
> InlineResponse2002 get_branch_migration_history(db_branch_name)

Get branch migration history

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BranchApi(swagger_client.ApiClient(configuration))
db_branch_name = swagger_client.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 

try:
    # Get branch migration history
    api_response = api_instance.get_branch_migration_history(db_branch_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BranchApi->get_branch_migration_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branch_migration_plan**
> MigrationsExecuteBody get_branch_migration_plan(db_branch_name, body=body)

Compute migration plan

Compute a migration plan from a target schema the branch should be migrated too.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BranchApi(swagger_client.ApiClient(configuration))
db_branch_name = swagger_client.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
body = swagger_client.Schema() # Schema |  (optional)

try:
    # Compute migration plan
    api_response = api_instance.get_branch_migration_plan(db_branch_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BranchApi->get_branch_migration_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **body** | [**Schema**](Schema.md)|  | [optional] 

### Return type

[**MigrationsExecuteBody**](MigrationsExecuteBody.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branch_stats**
> InlineResponse2003 get_branch_stats(db_branch_name)

Branch stats

Get branch usage metrics.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BranchApi(swagger_client.ApiClient(configuration))
db_branch_name = swagger_client.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 

try:
    # Branch stats
    api_response = api_instance.get_branch_stats(db_branch_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BranchApi->get_branch_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_branch_metadata**
> update_branch_metadata(db_branch_name, body=body)

Update branch metadata

Update the branch metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BranchApi(swagger_client.ApiClient(configuration))
db_branch_name = swagger_client.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
body = swagger_client.BranchMetadata() # BranchMetadata |  (optional)

try:
    # Update branch metadata
    api_instance.update_branch_metadata(db_branch_name, body=body)
except ApiException as e:
    print("Exception when calling BranchApi->update_branch_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **body** | [**BranchMetadata**](BranchMetadata.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

