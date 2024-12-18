# coding: utf-8

"""
    NocoDB v2

    NocoDB API Documentation

    Generated by: https://konfigthis.com
"""

from noco_db_python_sdk.paths.api_v2_meta_cache.delete import ClearNocoCache
from noco_db_python_sdk.paths.api_v2_meta_audits_comments_count.get import CountComments
from noco_db_python_sdk.paths.api_v2_meta_audits_comments.post import CreateNewCommentRow
from noco_db_python_sdk.paths.api_v2_meta_cache.get import GetAllNocoCache
from noco_db_python_sdk.paths.api_v2_meta_nocodb_info.get import GetAppInfo
from noco_db_python_sdk.paths.api_v2_meta_audits_comments.get import ListComments
from noco_db_python_sdk.paths.api_v2_meta_axios_request_make.post import MakeAxiosRequest
from noco_db_python_sdk.paths.api_v2_meta_connection_select.post import SelectConnectionPost
from noco_db_python_sdk.paths.api_v2_meta_connection_test.post import TestDbConnection
from noco_db_python_sdk.paths.api_v2_meta_audits_audit_id_comment.patch import UpdateAuditComment
from noco_db_python_sdk.paths.api_v2_meta_audits_rows_row_id_update.post import UpdateAuditRow
from noco_db_python_sdk.apis.tags.utils_api_raw import UtilsApiRaw


class UtilsApi(
    ClearNocoCache,
    CountComments,
    CreateNewCommentRow,
    GetAllNocoCache,
    GetAppInfo,
    ListComments,
    MakeAxiosRequest,
    SelectConnectionPost,
    TestDbConnection,
    UpdateAuditComment,
    UpdateAuditRow,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: UtilsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = UtilsApiRaw(api_client)
