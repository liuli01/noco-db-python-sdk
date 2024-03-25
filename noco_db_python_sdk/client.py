# coding: utf-8
"""
    NocoDB v2

    NocoDB API Documentation

    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from noco_db_python_sdk.client_custom import ClientCustom
from noco_db_python_sdk.configuration import Configuration
from noco_db_python_sdk.api_client import ApiClient
from noco_db_python_sdk.type_util import copy_signature
from noco_db_python_sdk.apis.tags.api_token_api import APITokenApi
from noco_db_python_sdk.apis.tags.auth_api import AuthApi
from noco_db_python_sdk.apis.tags.base_api import BaseApi
from noco_db_python_sdk.apis.tags.db_table_api import DBTableApi
from noco_db_python_sdk.apis.tags.db_table_column_api import DBTableColumnApi
from noco_db_python_sdk.apis.tags.db_table_filter_api import DBTableFilterApi
from noco_db_python_sdk.apis.tags.db_table_sort_api import DBTableSortApi
from noco_db_python_sdk.apis.tags.db_table_webhook_api import DBTableWebhookApi
from noco_db_python_sdk.apis.tags.db_table_webhook_filter_api import DBTableWebhookFilterApi
from noco_db_python_sdk.apis.tags.db_table_webhook_logs_api import DBTableWebhookLogsApi
from noco_db_python_sdk.apis.tags.db_view_api import DBViewApi
from noco_db_python_sdk.apis.tags.db_view_column_api import DBViewColumnApi
from noco_db_python_sdk.apis.tags.db_view_share_api import DBViewShareApi
from noco_db_python_sdk.apis.tags.plugin_api import PluginApi
from noco_db_python_sdk.apis.tags.public_api import PublicApi
from noco_db_python_sdk.apis.tags.source_api import SourceApi
from noco_db_python_sdk.apis.tags.storage_api import StorageApi
from noco_db_python_sdk.apis.tags.table_records_api import TableRecordsApi
from noco_db_python_sdk.apis.tags.utils_api import UtilsApi



class NocoDb(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.api_token: APITokenApi = APITokenApi(api_client)
        self.auth: AuthApi = AuthApi(api_client)
        self.base: BaseApi = BaseApi(api_client)
        self.db_table: DBTableApi = DBTableApi(api_client)
        self.db_table_column: DBTableColumnApi = DBTableColumnApi(api_client)
        self.db_table_filter: DBTableFilterApi = DBTableFilterApi(api_client)
        self.db_table_sort: DBTableSortApi = DBTableSortApi(api_client)
        self.db_table_webhook: DBTableWebhookApi = DBTableWebhookApi(api_client)
        self.db_table_webhook_filter: DBTableWebhookFilterApi = DBTableWebhookFilterApi(api_client)
        self.db_table_webhook_logs: DBTableWebhookLogsApi = DBTableWebhookLogsApi(api_client)
        self.db_view: DBViewApi = DBViewApi(api_client)
        self.db_view_column: DBViewColumnApi = DBViewColumnApi(api_client)
        self.db_view_share: DBViewShareApi = DBViewShareApi(api_client)
        self.plugin: PluginApi = PluginApi(api_client)
        self.public: PublicApi = PublicApi(api_client)
        self.source: SourceApi = SourceApi(api_client)
        self.storage: StorageApi = StorageApi(api_client)
        self.table_records: TableRecordsApi = TableRecordsApi(api_client)
        self.utils: UtilsApi = UtilsApi(api_client)