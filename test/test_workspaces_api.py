# coding: utf-8

"""
    xata

    xata.io API  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import XataClient
from XataClient.api.workspaces_api import WorkspacesApi  # noqa: E501
from XataClient.rest import ApiException


class TestWorkspacesApi(unittest.TestCase):
    """WorkspacesApi unit test stubs"""

    def setUp(self):
        self.api = WorkspacesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_accept_workspace_member_invite(self):
        """Test case for accept_workspace_member_invite

        Accept the invitation to join a workspace  # noqa: E501
        """
        pass

    def test_cancel_workspace_member_invite(self):
        """Test case for cancel_workspace_member_invite

        Deletes an invite  # noqa: E501
        """
        pass

    def test_create_workspace(self):
        """Test case for create_workspace

        Create a new workspace  # noqa: E501
        """
        pass

    def test_delete_workspace(self):
        """Test case for delete_workspace

        Delete an existing workspace  # noqa: E501
        """
        pass

    def test_get_workspace(self):
        """Test case for get_workspace

        Get an existing workspace  # noqa: E501
        """
        pass

    def test_get_workspace_members_list(self):
        """Test case for get_workspace_members_list

        Get the list members of a workspace  # noqa: E501
        """
        pass

    def test_get_workspaces_list(self):
        """Test case for get_workspaces_list

        Get workspaces  # noqa: E501
        """
        pass

    def test_invite_workspace_member(self):
        """Test case for invite_workspace_member

        Invite a user to join the workspace  # noqa: E501
        """
        pass

    def test_remove_workspace_member(self):
        """Test case for remove_workspace_member

        Remove a member from the workspace  # noqa: E501
        """
        pass

    def test_resend_workspace_member_invite(self):
        """Test case for resend_workspace_member_invite

        Resend Invite notification  # noqa: E501
        """
        pass

    def test_update_workspace(self):
        """Test case for update_workspace

        Update an existing workspace  # noqa: E501
        """
        pass

    def test_update_workspace_member_role(self):
        """Test case for update_workspace_member_role

        Update workspace member role  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
