# DbBranchNameSearchBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tables** | **list[str]** | An array with the tables in which to search. By default, all tables are included. | [optional] 
**query** | **str** | The query string. | 
**fuzziness** | **int** | Maximum [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) for the search terms. The Levenshtein distance is the number of one charcter changes needed to make two strings equal. The default is 1, meaning that single character typos per word are tollerated by search. You can set it to 0 to remove the typo tollerance or set it to 2  to allow two typos in a word.  | [optional] [default to 1]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

