# coding: utf-8

"""
    NocoDB v2

    NocoDB API Documentation

    Generated by: https://konfigthis.com
"""

from noco_db_python_sdk.paths.api_v2_meta_bases_base_id_api_tokens.post import CreateInBase
from noco_db_python_sdk.paths.api_v2_meta_bases_base_id_api_tokens_token.delete import DeleteInBase
from noco_db_python_sdk.paths.api_v2_meta_bases_base_id_api_tokens.get import ListInBase
from noco_db_python_sdk.apis.tags.api_token_api_raw import APITokenApiRaw


class APITokenApi(
    CreateInBase,
    DeleteInBase,
    ListInBase,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: APITokenApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = APITokenApiRaw(api_client)
