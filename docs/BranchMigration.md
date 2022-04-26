# BranchMigration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**status** | **str** |  | 
**title** | **str** |  | [optional] 
**last_git_revision** | **str** |  | [optional] 
**local_changes** | **bool** |  | 
**created_at** | **datetime** |  | [optional] 
**new_tables** | [**dict(str, Table)**](Table.md) |  | [optional] 
**removed_tables** | **list[str]** |  | [optional] 
**table_migrations** | [**dict(str, TableMigration)**](TableMigration.md) |  | [optional] 
**new_table_order** | **list[str]** |  | 
**renamed_tables** | [**list[TableRename]**](TableRename.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

