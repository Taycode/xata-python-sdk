# swagger_client.RecordsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_insert_table_records**](RecordsApi.md#bulk_insert_table_records) | **POST** /db/{db_branch_name}/tables/{table_name}/bulk | Bulk insert records
[**delete_record**](RecordsApi.md#delete_record) | **DELETE** /db/{db_branch_name}/tables/{table_name}/data/{record_id} | Delete record from table
[**get_record**](RecordsApi.md#get_record) | **GET** /db/{db_branch_name}/tables/{table_name}/data/{record_id} | Get record by ID
[**insert_record**](RecordsApi.md#insert_record) | **POST** /db/{db_branch_name}/tables/{table_name}/data | Insert record
[**insert_record_with_id**](RecordsApi.md#insert_record_with_id) | **PUT** /db/{db_branch_name}/tables/{table_name}/data/{record_id} | Insert record with ID
[**query_table**](RecordsApi.md#query_table) | **POST** /db/{db_branch_name}/tables/{table_name}/query | Query table
[**search_branch**](RecordsApi.md#search_branch) | **POST** /db/{db_branch_name}/search | Free text search
[**update_record_with_id**](RecordsApi.md#update_record_with_id) | **PATCH** /db/{db_branch_name}/tables/{table_name}/data/{record_id} | Update record with ID
[**upsert_record_with_id**](RecordsApi.md#upsert_record_with_id) | **POST** /db/{db_branch_name}/tables/{table_name}/data/{record_id} | Upsert record with ID

# **bulk_insert_table_records**
> InlineResponse2007 bulk_insert_table_records(db_branch_name, table_name, body=body)

Bulk insert records

Bulk insert records

### Example

```python
from __future__ import print_function
import time
import XataClient
from XataClient.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = XataClient.RecordsApi(XataClient.ApiClient(configuration))
db_branch_name = XataClient.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
table_name = XataClient.TableName() # TableName | The Table name
body = XataClient.TableNameBulkBody() # TableNameBulkBody |  (optional)

try:
    # Bulk insert records
    api_response = api_instance.bulk_insert_table_records(db_branch_name, table_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsApi->bulk_insert_table_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **table_name** | [**TableName**](.md)| The Table name | 
 **body** | [**TableNameBulkBody**](TableNameBulkBody.md)|  | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_record**
> delete_record(db_branch_name, table_name, record_id)

Delete record from table

### Example

```python
from __future__ import print_function
import time
import XataClient
from XataClient.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = XataClient.RecordsApi(XataClient.ApiClient(configuration))
db_branch_name = XataClient.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
table_name = XataClient.TableName() # TableName | The Table name
record_id = XataClient.RecordID() # RecordID | The Record name

try:
    # Delete record from table
    api_instance.delete_record(db_branch_name, table_name, record_id)
except ApiException as e:
    print("Exception when calling RecordsApi->delete_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **table_name** | [**TableName**](.md)| The Table name | 
 **record_id** | [**RecordID**](.md)| The Record name | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_record**
> Record get_record(db_branch_name, table_name, record_id)

Get record by ID

Retrieve record by ID

### Example

```python
from __future__ import print_function
import time
import XataClient
from XataClient.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = XataClient.RecordsApi(XataClient.ApiClient(configuration))
db_branch_name = XataClient.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
table_name = XataClient.TableName() # TableName | The Table name
record_id = XataClient.RecordID() # RecordID | The Record name

try:
    # Get record by ID
    api_response = api_instance.get_record(db_branch_name, table_name, record_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsApi->get_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **table_name** | [**TableName**](.md)| The Table name | 
 **record_id** | [**RecordID**](.md)| The Record name | 

### Return type

[**Record**](Record.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_record**
> InlineResponse2012 insert_record(db_branch_name, table_name, body=body)

Insert record

Insert a new Record into the Table

### Example

```python
from __future__ import print_function
import time
import XataClient
from XataClient.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = XataClient.RecordsApi(XataClient.ApiClient(configuration))
db_branch_name = XataClient.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
table_name = XataClient.TableName() # TableName | The Table name
body = NULL # object |  (optional)

try:
    # Insert record
    api_response = api_instance.insert_record(db_branch_name, table_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsApi->insert_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **table_name** | [**TableName**](.md)| The Table name | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_record_with_id**
> InlineResponse2012 insert_record_with_id(db_branch_name, table_name, record_id, body=body, create_only=create_only, if_version=if_version)

Insert record with ID

By default, IDs are auto-generated when data is insterted into Xata. Sending a request to this endpoint allows us to insert a record with a pre-existing ID, bypassing the default automatic ID generation.

### Example

```python
from __future__ import print_function
import time
import XataClient
from XataClient.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = XataClient.RecordsApi(XataClient.ApiClient(configuration))
db_branch_name = XataClient.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
table_name = XataClient.TableName() # TableName | The Table name
record_id = XataClient.RecordID() # RecordID | The Record name
body = NULL # object |  (optional)
create_only = true # bool |  (optional)
if_version = 56 # int |  (optional)

try:
    # Insert record with ID
    api_response = api_instance.insert_record_with_id(db_branch_name, table_name, record_id, body=body, create_only=create_only, if_version=if_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsApi->insert_record_with_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **table_name** | [**TableName**](.md)| The Table name | 
 **record_id** | [**RecordID**](.md)| The Record name | 
 **body** | [**object**](object.md)|  | [optional] 
 **create_only** | **bool**|  | [optional] 
 **if_version** | **int**|  | [optional] 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_table**
> InlineResponse2008 query_table(db_branch_name, table_name, body=body)

Query table

The Query Table API can be used to retrieve all records in a table. The API support filtering, sorting, selecting a subset of columns, and pagination.  The overall structure of the request looks like this:  ```json // POST /db/<dbname>:<branch>/tables/<table>/query {   \"columns\": [...],   \"filter\": {     \"$all\": [...]     \"$any\": [...]     ...   },   \"sort\": {     \"multiple\": [...]     ...   },   \"page\": {     ...   } } ```  ### Column selection  If the `columns` array is not specified, all columns are included. For link fields, only the ID column of the linked records is included in the response.  If the `columns` array is specified, only the selected columns are included. The `*` wildcard can be used to select all columns of the given array  For objects and link fields, if the column name of the object is specified, we include all of its sub-keys. If only some sub-keys are specified (via dotted notation, e.g. `\"settings.plan\"` ), then only those sub-keys from the object are included.  By the way of example, assuming two tables like this:  ```json {\"truncate\": true} {   \"formatVersion\": \"1.0\",   \"tables\": [     {       \"name\": \"teams\",       \"columns\": [         {           \"name\": \"name\",           \"type\": \"string\"         },         {           \"name\": \"owner\",           \"type\": \"link\",           \"link\": {             \"table\": \"users\"           }         }       ]     },     {       \"name\": \"users\",       \"columns\": [         {           \"name\": \"email\",           \"type\": \"email\"         },         {           \"name\": \"full_name\",           \"type\": \"string\"         },         {           \"name\": \"address\",           \"type\": \"object\",           \"columns\": [             {               \"name\": \"street\",               \"type\": \"string\"             },             {               \"name\": \"number\",               \"type\": \"int\"             },             {               \"name\": \"zipcode\",               \"type\": \"int\"             }           ]         },         {           \"name\": \"team\",           \"type\": \"link\",           \"link\": {             \"table\": \"teams\"           }         }       ]     }   ] } ```  A query like this:  ```json POST /db/<dbname>:<branch>/tables/<table>/query {   \"columns\": [     \"name\",     \"address.*\"   ] } ```  returns objects like:  ```json {   \"name\": \"Kilian\",   \"address\": {     \"street\": \"New street\",     \"number\": 41,     \"zipcode\": 10407   } } ```  while a query like this:  ```json POST /db/<dbname>:<branch>/tables/<table>/query {   \"columns\": [     \"name\",     \"address.street\"   ] } ```  returns objects like:  ```json {   \"name\": \"Kilian\",   \"address\": {     \"street\": \"New street\",   } } ```  If you want to return all columns from the main table and selected columns from the linked table, you can do it like this:  ```json {   \"columns\": [     \"*\",     \"team.name\"   ] } ```  The `\"*\"` in the above means all columns, including columns of objects. This returns data like:  ```json {   \"name\": \"Kilian\",   \"email\": \"kilian@gmail.com\",   \"address\": {     \"street\": \"New street\",     \"number\": 41,     \"zipcode\": 10407   },   \"team\": {     \"id\": \"XX\",     \"xata\": {       \"version\": 0,     },     \"name\": \"first team\"   } } ```  If you want all columns of the linked table, you can do:  ```json {   \"columns\": [     \"*\",     \"team.*\"   ] } ```  This returns, for example:  ```json {   \"name\": \"Kilian\",   \"email\": \"kilian@gmail.com\",   \"address\": {     \"street\": \"New street\",     \"number\": 41,     \"zipcode\": 10407   },   \"team\": {     \"id\": \"XX\",     \"xata\": {       \"version\": 0,     },     \"name\": \"first team\",     \"code\": \"A1\"   } } ```  ### Filtering  There are two types of operators:  - Operators that work on a single column: `$is`, `$contains`, `$pattern`,   `$includes`, `$gt`, etc. - Control operators that combine multiple conditions: `$any`, `$all`, `$not` ,   `$none`, etc.  All operators start with an `$` to differentiate them from column names (which are not allowed to start with an dollar sign).  #### Exact matching and control operators  Filter by one column:  ```json {   \"filter\": {     \"<column_name>\": \"value\"   } } ```  This is equivalent to using the `$is` operator:  ```json {   \"filter\": {     \"<column_name>\": {       \"$is\": \"value\"     }   } } ```  For example:  ```json {   \"filter\": {       \"name\": \"r2\",   } } ```  Or:  ```json {   \"filter\": {     \"name\": {       \"$is\": \"r2\"     }   } } ```  For objects, both dots and nested versions work:  ```json {   \"filter\": {       \"settings.plan\": \"free\",   } } ```  ```json {   \"filter\": {     \"settings\": {       \"plan\": \"free\"     },   }, } ```  If you want to OR together multiple values, you can use the `$any` operator with an array of values:  ```json {   \"filter\": {     \"settings.plan\": {\"$any\": [\"free\", \"paid\"]}   }, } ```  If you specify multiple columns in the same filter, they are logically AND'ed together:  ```json {   \"filter\": {       \"settings.dark\": true,       \"settings.plan\": \"free\",   }, } ```  The above matches if both conditions are met.  To be more explicit about it, you can use `$all` or `$any`:  ```json {   \"filter\": {       \"$any\": {         \"settings.dark\": true,         \"settings.plan\": \"free\"       }   }, } ```  The `$all` and `$any` operators can also receive an array of objects, which allows for repeating column names:  ```json {   \"filter\": {     \"$any\": [       {         \"name\": \"r1\",       },       {         \"name\": \"r2\",       },     ], } ```  You can check for a value being not-null with `$exists`:  ```json {   \"filter\": {     \"$exists\": \"settings\",   }, } ```  This can be combined with `$all` or `$any` :  ```json {   \"filter\": {     \"$all\": [       {         \"$exists\": \"settings\",       },       {         \"$exists\": \"name\",       },     ],   } } ```  Or you can use the inverse operator `$notExists`:  ```json {   \"filter\": {     \"$notExists\": \"settings\",   }, } ```  #### Partial match  `$contains` is the simplest operator for partial matching. We should generally discourage overusing `$contains` because it typically can't make use of indices.  ```json {   \"filter\": {     \"<column_name>\": {       \"$contains\": \"value\"     }   } } ```  Wildcards are supported via the `$pattern` operator:  ```json {   \"filter\": {     \"<column_name>\": {         \"$pattern\": \"v*alue*\"     }   } } ```  We could also have `$endsWith` and `$startsWith` operators:  ```json {   \"filter\": {     \"<column_name>\": {         \"$endsWith\": \".gz\"     },     \"<column_name>\": {         \"$startsWith\": \"tmp-\"     }   } } ```  #### Numeric ranges  ```json {   \"filter\": {       \"<column_name>\": {         \"$ge\": 0,         \"$lt\": 100       }   } } ```  The supported operators are `$gt`, `$lt`, `$ge`, `$le`.   #### Negations  A general `$not` operator can inverse any operation.  ```json {   \"filter\": {     \"$not\": {       \"<column_name1>\": \"value1\",       \"<column_name2>\": \"value1\"     }   } } ```  Note: in the above the two condition are AND together, so this does (NOT ( ... AND ...))  Or more complex:  ```json {   \"filter\": {     \"$not\": {       \"$any\": [{         \"<column_name1>\": \"value1\"       }, {         \"$all\": [{           \"<column_name2>\": \"value2\"         }, {           \"<column_name3>\": \"value3\"         }]       }]     }   } } ```  The `$not: { $any: {}}` can be shorted using the `$none` operator:  ```json {   \"filter\": {     \"$none\": {       \"<column_name1>\": \"value1\",       \"<column_name2>\": \"value1\"     }   } } ```  In addition, you can use operators like `$isNot` or `$notExists` to simplify expressions:  ```json {   \"filter\": {     \"<column_name>\": {       \"$isNot\": \"2019-10-12T07:20:50.52Z\"     }   } } ```  #### Working with arrays  To test that an array contains a value, use `$includes`.  ```json {   \"filter\": {     \"<array_name>\": {       \"$includes\": \"value\"     }   } } ```  The `$includes` operator accepts a custom predicate that will check if any array values matches the predicate. For example a complex predicate can include the `$all` , `$contains` and `$endsWith` operators:  ```json {   \"filter\": {     \"<array name>\": {       \"$includes\": {         \"$all\": [           {\"$contains\": \"label\"},           {\"$not\": {\"$endsWith\": \"-debug\"}}         ]       }     }   } } ```  The `$includes` all operator succeeds if any column in the array matches the predicate. The `$includesAll` operator succeeds if all array items match the predicate. The `$includesNone` operator succeeds if no array item matches the predicate. The `$includes` operator is a synonym for the `$includesAny` operator.  Here is an example of using the `$includesAll` operator:  ```json {   \"filter\": {     \"settings.labels\": {       \"$includesAll\": [         {\"$contains\": \"label\"},       ]     }   } } ```  The above matches if all label values contain the string \"labels\".  ### Sorting  Sorting by one element:  ```json POST /db/demo:main/tables/table/query {   \"sort\": {     \"index\": \"asc\"   } } ```  or descendently:  ```json POST /db/demo:main/tables/table/query {   \"sort\": {     \"index\": \"desc\"   } } ```  Sorting by multiple fields:  ```json POST /db/demo:main/tables/table/query {   \"sort\": [     {       \"index\": \"desc\"     },     {       \"createdAt\": \"desc\"     }   ] } ```   ### Pagination  We offer cursor pagination and offset pagination. The offset pagination is limited in the amount of data it can retrieve, so we recommend the cursor pagination if you have more than 1000 records.  Example of size + offset pagination:  ```json POST /db/demo:main/tables/table/query {   \"page\": {     \"size\": 100,     \"offset\": 200   } } ```  The `page.size` parameter represents the maximum number of records returned by this query. It has a default value of 20 and a maximum value of 200. The `page.offset` parameter represents the number of matching records to skip. It has a default value of 0 and a maximum value of 800.  Example of cursor pagination:  ```json POST /db/demo:main/tables/table/query {   \"page\": {     \"after\":\"fMoxCsIwFIDh3WP8c4amDai5hO5SJCRNfaVSeC9b6d1FD\"   } } ```  In the above example, the value of the `page.after` parameter is the cursor returned by the previous query. A sample response is shown below:  ```json {   \"meta\": {     \"page\": {       \"cursor\": \"fMoxCsIwFIDh3WP8c4amDai5hO5SJCRNfaVSeC9b6d1FD\",       \"more\": true     }   },   \"records\": [...] } ```  The `page` object might contain the follow keys, in addition to `size` and `offset` that were introduced before:  - `after`: Return the next page 'after' the current cursor - `before`: Return the previous page 'before' the current cursor. - `first`: Return the first page in the table from a cursor. - `last`: Return the last N records in the table from a cursor, where N is the `page.size` parameter.  The request will fail if an invalid cursor value is given to `page.before`, `page.after`, `page.first` , or `page.last`. No other cursor setting can be used if `page.first` or `page.last` is set in a query.  If both `page.before` and `page.after` parameters are present we treat the request as a range query. The range query will return all entries after `page.after`, but before `page.before`, up to `page.size` or the maximum page size. This query requires both cursors to use the same filters and sort settings, plus we require `page.after < page.before`. The range query returns a new cursor. If the range encompass multiple pages the next page in the range can be queried by update `page.after` to the returned cursor while keeping the `page.before` cursor from the first range query.  The `filter` , `columns`,  `sort` , and `page.size` configuration will be encoded with the cursor.  The pagination request will be invalid if `filter` or `sort` is set. The columns returned and page size can be changed anytime by passing the `columns` or `page.size` settings to the next query.  **Special cursors:**  - `page.after=end`: Result points past the last entry. The list of records   returned is empty, but `page.meta.cursor` will include a cursor that can be   used to \"tail\" the table from the end waiting for new data to be inserted. - `page.before=end`: This cursor returns the last page. - `page.first=<cursor>`: Go to first page. This is equivalent to querying the   first page without a cursor but `filter` and `sort` . Yet the `page.first`   cursor can be convenient at times as user code does not need to remember the   filter, sort, columns or page size configuration. All these information are   read from the cursor. - `page.last=<cursor>`: Go to the end of the table. This is equivalent to querying the   last page with `page.before=end`, `filter`, and `sort` . Yet the   `page.last` cursor can be more convenient at times as user code does not   need to remember the filter, sort, columns or page size configuration. All   these information are read from the cursor.  When using special cursors like `page.after=\"end\"` or `page.before=\"end\"`, we still allow `filter` and `sort` to be set.  Example of getting the last page:  ```json POST /db/demo:main/tables/table/query {   \"page\": {     \"size\": 10,     \"before\": \"end\"   } } ```

### Example

```python
from __future__ import print_function
import time
import XataClient
from XataClient.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = XataClient.RecordsApi(XataClient.ApiClient(configuration))
db_branch_name = XataClient.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
table_name = XataClient.TableName() # TableName | The Table name
body = XataClient.TableNameQueryBody() # TableNameQueryBody |  (optional)

try:
    # Query table
    api_response = api_instance.query_table(db_branch_name, table_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsApi->query_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **table_name** | [**TableName**](.md)| The Table name | 
 **body** | [**TableNameQueryBody**](TableNameQueryBody.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_branch**
> InlineResponse2009 search_branch(db_branch_name, body=body)

Free text search

Run a free text search operation across the database branch.

### Example

```python
from __future__ import print_function
import time
import XataClient
from XataClient.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = XataClient.RecordsApi(XataClient.ApiClient(configuration))
db_branch_name = XataClient.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
body = XataClient.DbBranchNameSearchBody() # DbBranchNameSearchBody |  (optional)

try:
    # Free text search
    api_response = api_instance.search_branch(db_branch_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsApi->search_branch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **body** | [**DbBranchNameSearchBody**](DbBranchNameSearchBody.md)|  | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_record_with_id**
> InlineResponse2012 update_record_with_id(db_branch_name, table_name, record_id, body=body, if_version=if_version)

Update record with ID

### Example

```python
from __future__ import print_function
import time
import XataClient
from XataClient.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = XataClient.RecordsApi(XataClient.ApiClient(configuration))
db_branch_name = XataClient.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
table_name = XataClient.TableName() # TableName | The Table name
record_id = XataClient.RecordID() # RecordID | The Record name
body = NULL # object |  (optional)
if_version = 56 # int |  (optional)

try:
    # Update record with ID
    api_response = api_instance.update_record_with_id(db_branch_name, table_name, record_id, body=body, if_version=if_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsApi->update_record_with_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **table_name** | [**TableName**](.md)| The Table name | 
 **record_id** | [**RecordID**](.md)| The Record name | 
 **body** | [**object**](object.md)|  | [optional] 
 **if_version** | **int**|  | [optional] 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_record_with_id**
> InlineResponse2012 upsert_record_with_id(db_branch_name, table_name, record_id, body=body, if_version=if_version)

Upsert record with ID

### Example

```python
from __future__ import print_function
import time
import XataClient
from XataClient.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = XataClient.RecordsApi(XataClient.ApiClient(configuration))
db_branch_name = XataClient.DBBranchName() # DBBranchName | The DBBranchName matches the pattern `{db_name}:{branch_name}`. 
table_name = XataClient.TableName() # TableName | The Table name
record_id = XataClient.RecordID() # RecordID | The Record name
body = NULL # object |  (optional)
if_version = 56 # int |  (optional)

try:
    # Upsert record with ID
    api_response = api_instance.upsert_record_with_id(db_branch_name, table_name, record_id, body=body, if_version=if_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsApi->upsert_record_with_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_branch_name** | [**DBBranchName**](.md)| The DBBranchName matches the pattern &#x60;{db_name}:{branch_name}&#x60;.  | 
 **table_name** | [**TableName**](.md)| The Table name | 
 **record_id** | [**RecordID**](.md)| The Record name | 
 **body** | [**object**](object.md)|  | [optional] 
 **if_version** | **int**|  | [optional] 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

