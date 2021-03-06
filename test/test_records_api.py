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
from XataClient.api.records_api import RecordsApi  # noqa: E501
from XataClient.rest import ApiException


class TestRecordsApi(unittest.TestCase):
    """RecordsApi unit test stubs"""

    def setUp(self):
        self.api = RecordsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_bulk_insert_table_records(self):
        """Test case for bulk_insert_table_records

        Bulk insert records  # noqa: E501
        """
        pass

    def test_delete_record(self):
        """Test case for delete_record

        Delete record from table  # noqa: E501
        """
        pass

    def test_get_record(self):
        """Test case for get_record

        Get record by ID  # noqa: E501
        """
        pass

    def test_insert_record(self):
        """Test case for insert_record

        Insert record  # noqa: E501
        """
        pass

    def test_insert_record_with_id(self):
        """Test case for insert_record_with_id

        Insert record with ID  # noqa: E501
        """
        pass

    def test_query_table(self):
        """Test case for query_table

        Query table  # noqa: E501
        """
        pass

    def test_search_branch(self):
        """Test case for search_branch

        Free text search  # noqa: E501
        """
        pass

    def test_update_record_with_id(self):
        """Test case for update_record_with_id

        Update record with ID  # noqa: E501
        """
        pass

    def test_upsert_record_with_id(self):
        """Test case for upsert_record_with_id

        Upsert record with ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
