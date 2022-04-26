# swagger_client.TableApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_table_column**](TableApi.md#add_table_column) | **POST** /db/{db_branch_name}/tables/{table_name}/columns | Creates a new column
[**create_table**](TableApi.md#create_table) | **PUT** /db/{db_branch_name}/tables/{table_name} | Create table
[**delete_column**](TableApi.md#delete_column) | **DELETE** /db/{db_branch_name}/tables/{table_name}/columns/{column_name} | Deletes a column
[**delete_table**](TableApi.md#delete_table) | **DELETE** /db/{db_branch_name}/tables/{table_name} | Delete table
[**get_column**](TableApi.md#get_column) | **GET** /db/{db_branch_name}/tables/{table_name}/columns/{column_name} | Get column information
[**get_table_columns**](TableApi.md#get_table_columns) | **GET** /db/{db_branch_name}/tables/{table_name}/columns | Get the columns
[**get_table_schema**](TableApi.md#get_table_schema) | **GET** /db/{db_branch_name}/tables/{table_name}/schema | Get table schema
[**set_table_schema**](TableApi.md#set_table_schema) | **PUT** /db/{db_branch_name}/tables/{table_name}/schema | Update table schema
[**update_column**](TableApi.md#update_column) | **PATCH** /db/{db_branch_name}/tables/{table_name}/columns/{column_name} | Updates a column
[**update_table**](TableApi.md#update_table) | **PATCH** /db/{db_branch_name}/tables/{table_name} | Update table

# **add_table_column**
> InlineResponse2006 add_table_column(db_branch_name, table_name, body=body)

Creates a new column

Adds a new column to the table. The body of the request should contain the column definition. In the column definition, the 'name' field should contain the full path separated by dots. If the parent objects do not exists, they will be automatically created. For example, passing `\"name\": \"address.city\"` will auto-create the `address` object if it doesn't exist. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TableApi(swagger_client.ApiClient(configuration))
db_branch_name = swagger_client.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
table_name = swagger_client.TableName() # TableName | The Table name
body = swagger_client.Column() # Column | The column definition. (optional)

try:
    # Creates a new column
    api_response = api_instance.add_table_column(db_branch_name, table_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TableApi->add_table_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **table_name** | [**TableName**](.md)| The Table name | 
 **body** | [**Column**](Column.md)| The column definition. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_table**
> create_table(db_branch_name, table_name)

Create table

Creates a new table with the given name. Returns 422 if a table with the same name already exists.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TableApi(swagger_client.ApiClient(configuration))
db_branch_name = swagger_client.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
table_name = swagger_client.TableName() # TableName | The Table name

try:
    # Create table
    api_instance.create_table(db_branch_name, table_name)
except ApiException as e:
    print("Exception when calling TableApi->create_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **table_name** | [**TableName**](.md)| The Table name | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_column**
> InlineResponse2006 delete_column(db_branch_name, table_name, column_name)

Deletes a column

Deletes the specified column. To refer to sub-objects, the column name can contain dots. For example `address.country`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TableApi(swagger_client.ApiClient(configuration))
db_branch_name = swagger_client.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
table_name = swagger_client.TableName() # TableName | The Table name
column_name = swagger_client.ColumnName() # ColumnName | The Column name

try:
    # Deletes a column
    api_response = api_instance.delete_column(db_branch_name, table_name, column_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TableApi->delete_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **table_name** | [**TableName**](.md)| The Table name | 
 **column_name** | [**ColumnName**](.md)| The Column name | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_table**
> delete_table(db_branch_name, table_name)

Delete table

Deletes the table with the given name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TableApi(swagger_client.ApiClient(configuration))
db_branch_name = swagger_client.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
table_name = swagger_client.TableName() # TableName | The Table name

try:
    # Delete table
    api_instance.delete_table(db_branch_name, table_name)
except ApiException as e:
    print("Exception when calling TableApi->delete_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **table_name** | [**TableName**](.md)| The Table name | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_column**
> Column get_column(db_branch_name, table_name, column_name)

Get column information

Get the definition of a single column. To refer to sub-objects, the column name can contain dots. For example `address.country`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TableApi(swagger_client.ApiClient(configuration))
db_branch_name = swagger_client.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
table_name = swagger_client.TableName() # TableName | The Table name
column_name = swagger_client.ColumnName() # ColumnName | The Column name

try:
    # Get column information
    api_response = api_instance.get_column(db_branch_name, table_name, column_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TableApi->get_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **table_name** | [**TableName**](.md)| The Table name | 
 **column_name** | [**ColumnName**](.md)| The Column name | 

### Return type

[**Column**](Column.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table_columns**
> InlineResponse2005 get_table_columns(db_branch_name, table_name)

Get the columns

Retrieves the list of table columns and their definition. This endpoint returns the column list with object columns being reported with their full dot-separated path (flattened). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TableApi(swagger_client.ApiClient(configuration))
db_branch_name = swagger_client.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
table_name = swagger_client.TableName() # TableName | The Table name

try:
    # Get the columns
    api_response = api_instance.get_table_columns(db_branch_name, table_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TableApi->get_table_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **table_name** | [**TableName**](.md)| The Table name | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table_schema**
> InlineResponse2004 get_table_schema(db_branch_name, table_name)

Get table schema

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TableApi(swagger_client.ApiClient(configuration))
db_branch_name = swagger_client.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
table_name = swagger_client.TableName() # TableName | The Table name

try:
    # Get table schema
    api_response = api_instance.get_table_schema(db_branch_name, table_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TableApi->get_table_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **table_name** | [**TableName**](.md)| The Table name | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_table_schema**
> set_table_schema(db_branch_name, table_name, body=body)

Update table schema

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TableApi(swagger_client.ApiClient(configuration))
db_branch_name = swagger_client.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
table_name = swagger_client.TableName() # TableName | The Table name
body = swagger_client.TableNameSchemaBody() # TableNameSchemaBody |  (optional)

try:
    # Update table schema
    api_instance.set_table_schema(db_branch_name, table_name, body=body)
except ApiException as e:
    print("Exception when calling TableApi->set_table_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **table_name** | [**TableName**](.md)| The Table name | 
 **body** | [**TableNameSchemaBody**](TableNameSchemaBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_column**
> InlineResponse2006 update_column(db_branch_name, table_name, column_name, body=body)

Updates a column

Update column with partial data. Can be used for renaming the column by providing a new \"name\" field. To refer to sub-objects, the column name can contain dots. For example `address.country`. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TableApi(swagger_client.ApiClient(configuration))
db_branch_name = swagger_client.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
table_name = swagger_client.TableName() # TableName | The Table name
column_name = swagger_client.ColumnName() # ColumnName | The Column name
body = swagger_client.ColumnsColumnNameBody() # ColumnsColumnNameBody |  (optional)

try:
    # Updates a column
    api_response = api_instance.update_column(db_branch_name, table_name, column_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TableApi->update_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **table_name** | [**TableName**](.md)| The Table name | 
 **column_name** | [**ColumnName**](.md)| The Column name | 
 **body** | [**ColumnsColumnNameBody**](ColumnsColumnNameBody.md)|  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_table**
> update_table(db_branch_name, table_name, body=body)

Update table

Update table. Currently there is only one update operation supported: renaming the table by providing a new name.  In the example below, we rename a table from â€œusersâ€ to â€œpeopleâ€:  ```jsx PATCH /db/test:main/tables/users {   \"name\": \"people\" } ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TableApi(swagger_client.ApiClient(configuration))
db_branch_name = swagger_client.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
table_name = swagger_client.TableName() # TableName | The Table name
body = swagger_client.TablesTableNameBody() # TablesTableNameBody |  (optional)

try:
    # Update table
    api_instance.update_table(db_branch_name, table_name, body=body)
except ApiException as e:
    print("Exception when calling TableApi->update_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **table_name** | [**TableName**](.md)| The Table name | 
 **body** | [**TablesTableNameBody**](TablesTableNameBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

