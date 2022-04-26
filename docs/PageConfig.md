# PageConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **str** | Query the next page that follow the cursor. | [optional] 
**before** | **str** | Query the previous page before the cursor. | [optional] 
**first** | **str** | Query the first page from the cursor. | [optional] 
**last** | **str** | Query the last page from the cursor. | [optional] 
**size** | **int** | Set page size. If the size is missing it is read from the cursor. If no cursor is given xata will choose the default page size. | [optional] [default to 20]
**offset** | **int** | Use offset to skip entries. To skip pages set offset to a multiple of size. | [optional] [default to 0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

