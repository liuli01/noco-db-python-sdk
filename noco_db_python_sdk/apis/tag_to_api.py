import typing_extensions

from noco_db_python_sdk.apis.tags import TagValues
from noco_db_python_sdk.apis.tags.db_view_api import DBViewApi
from noco_db_python_sdk.apis.tags.base_api import BaseApi
from noco_db_python_sdk.apis.tags.source_api import SourceApi
from noco_db_python_sdk.apis.tags.public_api import PublicApi
from noco_db_python_sdk.apis.tags.utils_api import UtilsApi
from noco_db_python_sdk.apis.tags.table_records_api import TableRecordsApi
from noco_db_python_sdk.apis.tags.db_table_api import DBTableApi
from noco_db_python_sdk.apis.tags.db_table_column_api import DBTableColumnApi
from noco_db_python_sdk.apis.tags.db_table_filter_api import DBTableFilterApi
from noco_db_python_sdk.apis.tags.db_table_webhook_api import DBTableWebhookApi
from noco_db_python_sdk.apis.tags.plugin_api import PluginApi
from noco_db_python_sdk.apis.tags.auth_api import AuthApi
from noco_db_python_sdk.apis.tags.db_table_sort_api import DBTableSortApi
from noco_db_python_sdk.apis.tags.db_view_share_api import DBViewShareApi
from noco_db_python_sdk.apis.tags.db_view_column_api import DBViewColumnApi
from noco_db_python_sdk.apis.tags.api_token_api import APITokenApi
from noco_db_python_sdk.apis.tags.db_table_webhook_filter_api import DBTableWebhookFilterApi
from noco_db_python_sdk.apis.tags.storage_api import StorageApi
from noco_db_python_sdk.apis.tags.db_table_webhook_logs_api import DBTableWebhookLogsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DB_VIEW: DBViewApi,
        TagValues.BASE: BaseApi,
        TagValues.SOURCE: SourceApi,
        TagValues.PUBLIC: PublicApi,
        TagValues.UTILS: UtilsApi,
        TagValues.TABLE_RECORDS: TableRecordsApi,
        TagValues.DB_TABLE: DBTableApi,
        TagValues.DB_TABLE_COLUMN: DBTableColumnApi,
        TagValues.DB_TABLE_FILTER: DBTableFilterApi,
        TagValues.DB_TABLE_WEBHOOK: DBTableWebhookApi,
        TagValues.PLUGIN: PluginApi,
        TagValues.AUTH: AuthApi,
        TagValues.DB_TABLE_SORT: DBTableSortApi,
        TagValues.DB_VIEW_SHARE: DBViewShareApi,
        TagValues.DB_VIEW_COLUMN: DBViewColumnApi,
        TagValues.API_TOKEN: APITokenApi,
        TagValues.DB_TABLE_WEBHOOK_FILTER: DBTableWebhookFilterApi,
        TagValues.STORAGE: StorageApi,
        TagValues.DB_TABLE_WEBHOOK_LOGS: DBTableWebhookLogsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DB_VIEW: DBViewApi,
        TagValues.BASE: BaseApi,
        TagValues.SOURCE: SourceApi,
        TagValues.PUBLIC: PublicApi,
        TagValues.UTILS: UtilsApi,
        TagValues.TABLE_RECORDS: TableRecordsApi,
        TagValues.DB_TABLE: DBTableApi,
        TagValues.DB_TABLE_COLUMN: DBTableColumnApi,
        TagValues.DB_TABLE_FILTER: DBTableFilterApi,
        TagValues.DB_TABLE_WEBHOOK: DBTableWebhookApi,
        TagValues.PLUGIN: PluginApi,
        TagValues.AUTH: AuthApi,
        TagValues.DB_TABLE_SORT: DBTableSortApi,
        TagValues.DB_VIEW_SHARE: DBViewShareApi,
        TagValues.DB_VIEW_COLUMN: DBViewColumnApi,
        TagValues.API_TOKEN: APITokenApi,
        TagValues.DB_TABLE_WEBHOOK_FILTER: DBTableWebhookFilterApi,
        TagValues.STORAGE: StorageApi,
        TagValues.DB_TABLE_WEBHOOK_LOGS: DBTableWebhookLogsApi,
    }
)
