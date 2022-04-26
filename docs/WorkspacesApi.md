# swagger_client.WorkspacesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_workspace_member_invite**](WorkspacesApi.md#accept_workspace_member_invite) | **POST** /workspaces/{workspace_id}/invites/{invite_key}/accept | Accept the invitation to join a workspace
[**cancel_workspace_member_invite**](WorkspacesApi.md#cancel_workspace_member_invite) | **DELETE** /workspaces/{workspace_id}/invites/{invite_id} | Deletes an invite
[**create_workspace**](WorkspacesApi.md#create_workspace) | **POST** /workspaces | Create a new workspace
[**delete_workspace**](WorkspacesApi.md#delete_workspace) | **DELETE** /workspaces/{workspace_id} | Delete an existing workspace
[**get_workspace**](WorkspacesApi.md#get_workspace) | **GET** /workspaces/{workspace_id} | Get an existing workspace
[**get_workspace_members_list**](WorkspacesApi.md#get_workspace_members_list) | **GET** /workspaces/{workspace_id}/members | Get the list members of a workspace
[**get_workspaces_list**](WorkspacesApi.md#get_workspaces_list) | **GET** /workspaces | Get workspaces
[**invite_workspace_member**](WorkspacesApi.md#invite_workspace_member) | **POST** /workspaces/{workspace_id}/invites | Invite a user to join the workspace
[**remove_workspace_member**](WorkspacesApi.md#remove_workspace_member) | **DELETE** /workspaces/{workspace_id}/members/{user_id} | Remove a member from the workspace
[**resend_workspace_member_invite**](WorkspacesApi.md#resend_workspace_member_invite) | **POST** /workspaces/{workspace_id}/invites/{invite_id}/resend | Resend Invite notification
[**update_workspace**](WorkspacesApi.md#update_workspace) | **PUT** /workspaces/{workspace_id} | Update an existing workspace
[**update_workspace_member_role**](WorkspacesApi.md#update_workspace_member_role) | **PUT** /workspaces/{workspace_id}/members/{user_id} | Update workspace member role

# **accept_workspace_member_invite**
> accept_workspace_member_invite(workspace_id, invite_key)

Accept the invitation to join a workspace

Accept the invitation to join a workspace. If the operation succeeds the user will be a member of the workspace 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()
workspace_id = swagger_client.WorkspaceID() # WorkspaceID | Workspace name
invite_key = swagger_client.InviteKey() # InviteKey | Invite Key (secret) for the invited user

try:
    # Accept the invitation to join a workspace
    api_instance.accept_workspace_member_invite(workspace_id, invite_key)
except ApiException as e:
    print("Exception when calling WorkspacesApi->accept_workspace_member_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | [**WorkspaceID**](.md)| Workspace name | 
 **invite_key** | [**InviteKey**](.md)| Invite Key (secret) for the invited user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_workspace_member_invite**
> cancel_workspace_member_invite(workspace_id, invite_id)

Deletes an invite

This operation provides a way to cancel invites by deleting them. Already accepted invites cannot be deleted.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()
workspace_id = swagger_client.WorkspaceID() # WorkspaceID | Workspace name
invite_id = swagger_client.InviteID() # InviteID | Invite identifier

try:
    # Deletes an invite
    api_instance.cancel_workspace_member_invite(workspace_id, invite_id)
except ApiException as e:
    print("Exception when calling WorkspacesApi->cancel_workspace_member_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | [**WorkspaceID**](.md)| Workspace name | 
 **invite_id** | [**InviteID**](.md)| Invite identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workspace**
> Workspace create_workspace(body=body)

Create a new workspace

Creates a new workspace with the user requesting it as its single owner.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()
body = swagger_client.WorkspaceMeta() # WorkspaceMeta |  (optional)

try:
    # Create a new workspace
    api_response = api_instance.create_workspace(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->create_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkspaceMeta**](WorkspaceMeta.md)|  | [optional] 

### Return type

[**Workspace**](Workspace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace**
> delete_workspace(workspace_id)

Delete an existing workspace

Delete the workspace with the provided ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()
workspace_id = swagger_client.WorkspaceID() # WorkspaceID | Workspace name

try:
    # Delete an existing workspace
    api_instance.delete_workspace(workspace_id)
except ApiException as e:
    print("Exception when calling WorkspacesApi->delete_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | [**WorkspaceID**](.md)| Workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace**
> Workspace get_workspace(workspace_id)

Get an existing workspace

Retrieve workspace info from a workspace ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()
workspace_id = swagger_client.WorkspaceID() # WorkspaceID | Workspace name

try:
    # Get an existing workspace
    api_response = api_instance.get_workspace(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | [**WorkspaceID**](.md)| Workspace name | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_members_list**
> WorkspaceMembers get_workspace_members_list(workspace_id)

Get the list members of a workspace

Retrieve the list of members of the given workspace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()
workspace_id = swagger_client.WorkspaceID() # WorkspaceID | Workspace name

try:
    # Get the list members of a workspace
    api_response = api_instance.get_workspace_members_list(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspace_members_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | [**WorkspaceID**](.md)| Workspace name | 

### Return type

[**WorkspaceMembers**](WorkspaceMembers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspaces_list**
> InlineResponse2001 get_workspaces_list()

Get workspaces

Retrieve the list of workspaces the user belongs to

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()

try:
    # Get workspaces
    api_response = api_instance.get_workspaces_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspaces_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_workspace_member**
> WorkspaceInvite invite_workspace_member(workspace_id, body=body)

Invite a user to join the workspace

Invite some user to join the workspace with the given role

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()
workspace_id = swagger_client.WorkspaceID() # WorkspaceID | Workspace name
body = swagger_client.WorkspaceIdInvitesBody() # WorkspaceIdInvitesBody |  (optional)

try:
    # Invite a user to join the workspace
    api_response = api_instance.invite_workspace_member(workspace_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->invite_workspace_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | [**WorkspaceID**](.md)| Workspace name | 
 **body** | [**WorkspaceIdInvitesBody**](WorkspaceIdInvitesBody.md)|  | [optional] 

### Return type

[**WorkspaceInvite**](WorkspaceInvite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_workspace_member**
> remove_workspace_member(workspace_id, user_id)

Remove a member from the workspace

Remove the member from the workspace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()
workspace_id = swagger_client.WorkspaceID() # WorkspaceID | Workspace name
user_id = swagger_client.UserID() # UserID | UserID

try:
    # Remove a member from the workspace
    api_instance.remove_workspace_member(workspace_id, user_id)
except ApiException as e:
    print("Exception when calling WorkspacesApi->remove_workspace_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | [**WorkspaceID**](.md)| Workspace name | 
 **user_id** | [**UserID**](.md)| UserID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_workspace_member_invite**
> resend_workspace_member_invite(workspace_id, invite_id)

Resend Invite notification

This operation provides a way to resend an Invite notification. Invite notifications can only be sent for Invites not yet accepted.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()
workspace_id = swagger_client.WorkspaceID() # WorkspaceID | Workspace name
invite_id = swagger_client.InviteID() # InviteID | Invite identifier

try:
    # Resend Invite notification
    api_instance.resend_workspace_member_invite(workspace_id, invite_id)
except ApiException as e:
    print("Exception when calling WorkspacesApi->resend_workspace_member_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | [**WorkspaceID**](.md)| Workspace name | 
 **invite_id** | [**InviteID**](.md)| Invite identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace**
> Workspace update_workspace(workspace_id, body=body)

Update an existing workspace

Update workspace info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()
workspace_id = swagger_client.WorkspaceID() # WorkspaceID | Workspace name
body = swagger_client.WorkspaceMeta() # WorkspaceMeta |  (optional)

try:
    # Update an existing workspace
    api_response = api_instance.update_workspace(workspace_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->update_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | [**WorkspaceID**](.md)| Workspace name | 
 **body** | [**WorkspaceMeta**](WorkspaceMeta.md)|  | [optional] 

### Return type

[**Workspace**](Workspace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace_member_role**
> update_workspace_member_role(workspace_id, user_id, body=body)

Update workspace member role

Update a workspace member role. Workspaces must always have at least one owner, so this operation will fail if trying to remove owner role from the last owner in the workspace. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()
workspace_id = swagger_client.WorkspaceID() # WorkspaceID | Workspace name
user_id = swagger_client.UserID() # UserID | UserID
body = swagger_client.MembersUserIdBody() # MembersUserIdBody |  (optional)

try:
    # Update workspace member role
    api_instance.update_workspace_member_role(workspace_id, user_id, body=body)
except ApiException as e:
    print("Exception when calling WorkspacesApi->update_workspace_member_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | [**WorkspaceID**](.md)| Workspace name | 
 **user_id** | [**UserID**](.md)| UserID | 
 **body** | [**MembersUserIdBody**](MembersUserIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

