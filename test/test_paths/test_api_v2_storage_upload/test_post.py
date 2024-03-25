# coding: utf-8

"""
    NocoDB v2

    NocoDB API Documentation

    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import noco_db_python_sdk
from noco_db_python_sdk.paths.api_v2_storage_upload import post
from noco_db_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV2StorageUpload(ApiTestMixin, unittest.TestCase):
    """
    ApiV2StorageUpload unit test stubs
        Attachment Upload
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()