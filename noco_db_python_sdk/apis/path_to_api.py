import typing_extensions

from noco_db_python_sdk.paths import PathValues
from noco_db_python_sdk.apis.paths.api_v2_meta_bases_base_id_users import ApiV2MetaBasesBaseIdUsers
from noco_db_python_sdk.apis.paths.api_v2_meta_bases_base_id_info import ApiV2MetaBasesBaseIdInfo
from noco_db_python_sdk.apis.paths.api_v2_meta_bases_base_id_users_user_id import ApiV2MetaBasesBaseIdUsersUserId
from noco_db_python_sdk.apis.paths.api_v2_meta_bases_base_id_visibility_rules import ApiV2MetaBasesBaseIdVisibilityRules
from noco_db_python_sdk.apis.paths.api_v2_meta_duplicate_base_id_source_id import ApiV2MetaDuplicateBaseIdSourceId
from noco_db_python_sdk.apis.paths.api_v2_meta_duplicate_base_id import ApiV2MetaDuplicateBaseId
from noco_db_python_sdk.apis.paths.api_v2_meta_bases_base_id import ApiV2MetaBasesBaseId
from noco_db_python_sdk.apis.paths.api_v2_meta_bases_base_id_user import ApiV2MetaBasesBaseIdUser
from noco_db_python_sdk.apis.paths.api_v2_meta_bases_base_id_sources_source_id import ApiV2MetaBasesBaseIdSourcesSourceId
from noco_db_python_sdk.apis.paths.api_v2_meta_bases_base_id_sources_source_id_sql_view import ApiV2MetaBasesBaseIdSourcesSourceIdSqlView
from noco_db_python_sdk.apis.paths.api_v2_meta_bases_base_id_sources_source_id_share_erd import ApiV2MetaBasesBaseIdSourcesSourceIdShareErd
from noco_db_python_sdk.apis.paths.api_v2_meta_bases_base_id_shared import ApiV2MetaBasesBaseIdShared
from noco_db_python_sdk.apis.paths.api_v2_meta_bases_base_id_cost import ApiV2MetaBasesBaseIdCost
from noco_db_python_sdk.apis.paths.api_v2_meta_bases_base_id_tables import ApiV2MetaBasesBaseIdTables
from noco_db_python_sdk.apis.paths.api_v2_meta_tables_table_id import ApiV2MetaTablesTableId
from noco_db_python_sdk.apis.paths.api_v2_meta_duplicate_base_id_table_table_id import ApiV2MetaDuplicateBaseIdTableTableId
from noco_db_python_sdk.apis.paths.api_v2_meta_bases_base_id_source_id_tables import ApiV2MetaBasesBaseIdSourceIdTables
from noco_db_python_sdk.apis.paths.api_v2_meta_tables_table_id_reorder import ApiV2MetaTablesTableIdReorder
from noco_db_python_sdk.apis.paths.api_v2_meta_tables_table_id_columns import ApiV2MetaTablesTableIdColumns
from noco_db_python_sdk.apis.paths.api_v2_meta_columns_column_id import ApiV2MetaColumnsColumnId
from noco_db_python_sdk.apis.paths.api_v2_meta_columns_column_id_primary import ApiV2MetaColumnsColumnIdPrimary
from noco_db_python_sdk.apis.paths.api_v2_meta_tables_table_id_views import ApiV2MetaTablesTableIdViews
from noco_db_python_sdk.apis.paths.api_v2_meta_views_view_id import ApiV2MetaViewsViewId
from noco_db_python_sdk.apis.paths.api_v2_meta_views_view_id_show_all import ApiV2MetaViewsViewIdShowAll
from noco_db_python_sdk.apis.paths.api_v2_meta_views_view_id_hide_all import ApiV2MetaViewsViewIdHideAll
from noco_db_python_sdk.apis.paths.api_v2_meta_tables_table_id_share import ApiV2MetaTablesTableIdShare
from noco_db_python_sdk.apis.paths.api_v2_meta_views_view_id_share import ApiV2MetaViewsViewIdShare
from noco_db_python_sdk.apis.paths.api_v2_meta_views_view_id_columns import ApiV2MetaViewsViewIdColumns
from noco_db_python_sdk.apis.paths.api_v2_meta_views_view_id_columns_column_id import ApiV2MetaViewsViewIdColumnsColumnId
from noco_db_python_sdk.apis.paths.api_v2_meta_views_view_id_sorts import ApiV2MetaViewsViewIdSorts
from noco_db_python_sdk.apis.paths.api_v2_meta_sorts_sort_id import ApiV2MetaSortsSortId
from noco_db_python_sdk.apis.paths.api_v2_meta_views_view_id_filters import ApiV2MetaViewsViewIdFilters
from noco_db_python_sdk.apis.paths.api_v2_meta_hooks_hook_id_filters import ApiV2MetaHooksHookIdFilters
from noco_db_python_sdk.apis.paths.api_v2_meta_hooks_hook_id_logs import ApiV2MetaHooksHookIdLogs
from noco_db_python_sdk.apis.paths.api_v2_meta_filters_filter_id import ApiV2MetaFiltersFilterId
from noco_db_python_sdk.apis.paths.api_v2_meta_filters_filter_group_id_children import ApiV2MetaFiltersFilterGroupIdChildren
from noco_db_python_sdk.apis.paths.api_v2_meta_tables_table_id_grids import ApiV2MetaTablesTableIdGrids
from noco_db_python_sdk.apis.paths.api_v2_meta_tables_table_id_forms import ApiV2MetaTablesTableIdForms
from noco_db_python_sdk.apis.paths.api_v2_meta_forms_form_view_id import ApiV2MetaFormsFormViewId
from noco_db_python_sdk.apis.paths.api_v2_meta_form_columns_form_view_column_id import ApiV2MetaFormColumnsFormViewColumnId
from noco_db_python_sdk.apis.paths.api_v2_meta_grids_view_id import ApiV2MetaGridsViewId
from noco_db_python_sdk.apis.paths.api_v2_meta_grids_grid_id_grid_columns import ApiV2MetaGridsGridIdGridColumns
from noco_db_python_sdk.apis.paths.api_v2_meta_grid_columns_column_id import ApiV2MetaGridColumnsColumnId
from noco_db_python_sdk.apis.paths.api_v2_meta_tables_table_id_galleries import ApiV2MetaTablesTableIdGalleries
from noco_db_python_sdk.apis.paths.api_v2_meta_galleries_gallery_view_id import ApiV2MetaGalleriesGalleryViewId
from noco_db_python_sdk.apis.paths.api_v2_meta_tables_table_id_kanbans import ApiV2MetaTablesTableIdKanbans
from noco_db_python_sdk.apis.paths.api_v2_meta_kanbans_kanban_view_id import ApiV2MetaKanbansKanbanViewId
from noco_db_python_sdk.apis.paths.api_v2_meta_tables_table_id_maps import ApiV2MetaTablesTableIdMaps
from noco_db_python_sdk.apis.paths.api_v2_meta_maps_map_view_id import ApiV2MetaMapsMapViewId
from noco_db_python_sdk.apis.paths.api_v2_meta_bases_base_id_meta_diff import ApiV2MetaBasesBaseIdMetaDiff
from noco_db_python_sdk.apis.paths.api_v2_meta_bases_base_id_meta_diff_source_id import ApiV2MetaBasesBaseIdMetaDiffSourceId
from noco_db_python_sdk.apis.paths.api_v2_meta_bases_base_id_has_empty_or_null_filters import ApiV2MetaBasesBaseIdHasEmptyOrNullFilters
from noco_db_python_sdk.apis.paths.api_v2_public_shared_view_shared_view_uuid_group_column_id import ApiV2PublicSharedViewSharedViewUuidGroupColumnId
from noco_db_python_sdk.apis.paths.api_v2_public_calendar_view_shared_view_uuid_count_by_date import ApiV2PublicCalendarViewSharedViewUuidCountByDate
from noco_db_python_sdk.apis.paths.api_v2_public_shared_view_shared_view_uuid_rows import ApiV2PublicSharedViewSharedViewUuidRows
from noco_db_python_sdk.apis.paths.api_v2_public_shared_view_shared_view_uuid_groupby import ApiV2PublicSharedViewSharedViewUuidGroupby
from noco_db_python_sdk.apis.paths.api_v2_public_shared_view_shared_view_uuid_rows_row_id_relation_type_column_name import ApiV2PublicSharedViewSharedViewUuidRowsRowIdRelationTypeColumnName
from noco_db_python_sdk.apis.paths.api_v2_public_shared_view_shared_view_uuid_rows_export_type import ApiV2PublicSharedViewSharedViewUuidRowsExportType
from noco_db_python_sdk.apis.paths.api_v2_public_shared_view_shared_view_uuid_nested_column_name import ApiV2PublicSharedViewSharedViewUuidNestedColumnName
from noco_db_python_sdk.apis.paths.api_v2_public_shared_base_shared_base_uuid_meta import ApiV2PublicSharedBaseSharedBaseUuidMeta
from noco_db_python_sdk.apis.paths.api_v2_public_shared_view_shared_view_uuid_meta import ApiV2PublicSharedViewSharedViewUuidMeta
from noco_db_python_sdk.apis.paths.api_v2_public_shared_erd_shared_erd_uuid_meta import ApiV2PublicSharedErdSharedErdUuidMeta
from noco_db_python_sdk.apis.paths.api_v2_meta_audits_comments import ApiV2MetaAuditsComments
from noco_db_python_sdk.apis.paths.api_v2_meta_audits_audit_id_comment import ApiV2MetaAuditsAuditIdComment
from noco_db_python_sdk.apis.paths.api_v2_meta_audits_comments_count import ApiV2MetaAuditsCommentsCount
from noco_db_python_sdk.apis.paths.api_v2_meta_bases_base_id_audits import ApiV2MetaBasesBaseIdAudits
from noco_db_python_sdk.apis.paths.api_v2_meta_audits_rows_row_id_update import ApiV2MetaAuditsRowsRowIdUpdate
from noco_db_python_sdk.apis.paths.api_v2_meta_tables_table_id_hooks import ApiV2MetaTablesTableIdHooks
from noco_db_python_sdk.apis.paths.api_v2_meta_tables_table_id_hooks_test import ApiV2MetaTablesTableIdHooksTest
from noco_db_python_sdk.apis.paths.api_v2_meta_tables_table_id_hooks_sample_payload_operation_version import ApiV2MetaTablesTableIdHooksSamplePayloadOperationVersion
from noco_db_python_sdk.apis.paths.api_v2_meta_hooks_hook_id import ApiV2MetaHooksHookId
from noco_db_python_sdk.apis.paths.api_v2_meta_plugins import ApiV2MetaPlugins
from noco_db_python_sdk.apis.paths.api_v2_meta_plugins_webhook import ApiV2MetaPluginsWebhook
from noco_db_python_sdk.apis.paths.api_v2_meta_plugins_plugin_title_status import ApiV2MetaPluginsPluginTitleStatus
from noco_db_python_sdk.apis.paths.api_v2_meta_plugins_test import ApiV2MetaPluginsTest
from noco_db_python_sdk.apis.paths.api_v2_meta_plugins_plugin_id import ApiV2MetaPluginsPluginId
from noco_db_python_sdk.apis.paths.api_v2_meta_connection_test import ApiV2MetaConnectionTest
from noco_db_python_sdk.apis.paths.api_v2_meta_connection_select import ApiV2MetaConnectionSelect
from noco_db_python_sdk.apis.paths.api_v2_meta_nocodb_info import ApiV2MetaNocodbInfo
from noco_db_python_sdk.apis.paths.api_v2_meta_axios_request_make import ApiV2MetaAxiosRequestMake
from noco_db_python_sdk.apis.paths.api_v2_meta_cache import ApiV2MetaCache
from noco_db_python_sdk.apis.paths.api_v2_meta_bases_base_id_api_tokens import ApiV2MetaBasesBaseIdApiTokens
from noco_db_python_sdk.apis.paths.api_v2_meta_bases_base_id_api_tokens_token import ApiV2MetaBasesBaseIdApiTokensToken
from noco_db_python_sdk.apis.paths.api_v2_storage_upload import ApiV2StorageUpload
from noco_db_python_sdk.apis.paths.api_v2_storage_upload_by_url import ApiV2StorageUploadByUrl
from noco_db_python_sdk.apis.paths.api_v2_meta_bases_base_id_users_user_id_resend_invite import ApiV2MetaBasesBaseIdUsersUserIdResendInvite
from noco_db_python_sdk.apis.paths.api_v2_meta_tables_table_id_columns_hash import ApiV2MetaTablesTableIdColumnsHash
from noco_db_python_sdk.apis.paths.api_v2_meta_tables_table_id_columns_bulk import ApiV2MetaTablesTableIdColumnsBulk
from noco_db_python_sdk.apis.paths.api_v2_tables_table_id_records import ApiV2TablesTableIdRecords
from noco_db_python_sdk.apis.paths.api_v2_tables_table_id_records_record_id import ApiV2TablesTableIdRecordsRecordId
from noco_db_python_sdk.apis.paths.api_v2_tables_table_id_records_count import ApiV2TablesTableIdRecordsCount
from noco_db_python_sdk.apis.paths.api_v2_tables_table_id_links_link_field_id_records_record_id import ApiV2TablesTableIdLinksLinkFieldIdRecordsRecordId
from noco_db_python_sdk.apis.paths.api_v2_meta_bases import ApiV2MetaBases
from noco_db_python_sdk.apis.paths.api_v2_meta_bases_base_id_sources import ApiV2MetaBasesBaseIdSources
from noco_db_python_sdk.apis.paths.api_v2_public_calendar_view_shared_view_uuid import ApiV2PublicCalendarViewSharedViewUuid

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_V2_META_BASES_BASE_ID_USERS: ApiV2MetaBasesBaseIdUsers,
        PathValues.API_V2_META_BASES_BASE_ID_INFO: ApiV2MetaBasesBaseIdInfo,
        PathValues.API_V2_META_BASES_BASE_ID_USERS_USER_ID: ApiV2MetaBasesBaseIdUsersUserId,
        PathValues.API_V2_META_BASES_BASE_ID_VISIBILITYRULES: ApiV2MetaBasesBaseIdVisibilityRules,
        PathValues.API_V2_META_DUPLICATE_BASE_ID_SOURCE_ID: ApiV2MetaDuplicateBaseIdSourceId,
        PathValues.API_V2_META_DUPLICATE_BASE_ID: ApiV2MetaDuplicateBaseId,
        PathValues.API_V2_META_BASES_BASE_ID: ApiV2MetaBasesBaseId,
        PathValues.API_V2_META_BASES_BASE_ID_USER: ApiV2MetaBasesBaseIdUser,
        PathValues.API_V2_META_BASES_BASE_ID_SOURCES_SOURCE_ID: ApiV2MetaBasesBaseIdSourcesSourceId,
        PathValues.API_V2_META_BASES_BASE_ID_SOURCES_SOURCE_ID_SQL_VIEW: ApiV2MetaBasesBaseIdSourcesSourceIdSqlView,
        PathValues.API_V2_META_BASES_BASE_ID_SOURCES_SOURCE_ID_SHARE_ERD: ApiV2MetaBasesBaseIdSourcesSourceIdShareErd,
        PathValues.API_V2_META_BASES_BASE_ID_SHARED: ApiV2MetaBasesBaseIdShared,
        PathValues.API_V2_META_BASES_BASE_ID_COST: ApiV2MetaBasesBaseIdCost,
        PathValues.API_V2_META_BASES_BASE_ID_TABLES: ApiV2MetaBasesBaseIdTables,
        PathValues.API_V2_META_TABLES_TABLE_ID: ApiV2MetaTablesTableId,
        PathValues.API_V2_META_DUPLICATE_BASE_ID_TABLE_TABLE_ID: ApiV2MetaDuplicateBaseIdTableTableId,
        PathValues.API_V2_META_BASES_BASE_ID_SOURCE_ID_TABLES: ApiV2MetaBasesBaseIdSourceIdTables,
        PathValues.API_V2_META_TABLES_TABLE_ID_REORDER: ApiV2MetaTablesTableIdReorder,
        PathValues.API_V2_META_TABLES_TABLE_ID_COLUMNS: ApiV2MetaTablesTableIdColumns,
        PathValues.API_V2_META_COLUMNS_COLUMN_ID: ApiV2MetaColumnsColumnId,
        PathValues.API_V2_META_COLUMNS_COLUMN_ID_PRIMARY: ApiV2MetaColumnsColumnIdPrimary,
        PathValues.API_V2_META_TABLES_TABLE_ID_VIEWS: ApiV2MetaTablesTableIdViews,
        PathValues.API_V2_META_VIEWS_VIEW_ID: ApiV2MetaViewsViewId,
        PathValues.API_V2_META_VIEWS_VIEW_ID_SHOWALL: ApiV2MetaViewsViewIdShowAll,
        PathValues.API_V2_META_VIEWS_VIEW_ID_HIDEALL: ApiV2MetaViewsViewIdHideAll,
        PathValues.API_V2_META_TABLES_TABLE_ID_SHARE: ApiV2MetaTablesTableIdShare,
        PathValues.API_V2_META_VIEWS_VIEW_ID_SHARE: ApiV2MetaViewsViewIdShare,
        PathValues.API_V2_META_VIEWS_VIEW_ID_COLUMNS: ApiV2MetaViewsViewIdColumns,
        PathValues.API_V2_META_VIEWS_VIEW_ID_COLUMNS_COLUMN_ID: ApiV2MetaViewsViewIdColumnsColumnId,
        PathValues.API_V2_META_VIEWS_VIEW_ID_SORTS: ApiV2MetaViewsViewIdSorts,
        PathValues.API_V2_META_SORTS_SORT_ID: ApiV2MetaSortsSortId,
        PathValues.API_V2_META_VIEWS_VIEW_ID_FILTERS: ApiV2MetaViewsViewIdFilters,
        PathValues.API_V2_META_HOOKS_HOOK_ID_FILTERS: ApiV2MetaHooksHookIdFilters,
        PathValues.API_V2_META_HOOKS_HOOK_ID_LOGS: ApiV2MetaHooksHookIdLogs,
        PathValues.API_V2_META_FILTERS_FILTER_ID: ApiV2MetaFiltersFilterId,
        PathValues.API_V2_META_FILTERS_FILTER_GROUP_ID_CHILDREN: ApiV2MetaFiltersFilterGroupIdChildren,
        PathValues.API_V2_META_TABLES_TABLE_ID_GRIDS: ApiV2MetaTablesTableIdGrids,
        PathValues.API_V2_META_TABLES_TABLE_ID_FORMS: ApiV2MetaTablesTableIdForms,
        PathValues.API_V2_META_FORMS_FORM_VIEW_ID: ApiV2MetaFormsFormViewId,
        PathValues.API_V2_META_FORMCOLUMNS_FORM_VIEW_COLUMN_ID: ApiV2MetaFormColumnsFormViewColumnId,
        PathValues.API_V2_META_GRIDS_VIEW_ID: ApiV2MetaGridsViewId,
        PathValues.API_V2_META_GRIDS_GRID_ID_GRIDCOLUMNS: ApiV2MetaGridsGridIdGridColumns,
        PathValues.API_V2_META_GRIDCOLUMNS_COLUMN_ID: ApiV2MetaGridColumnsColumnId,
        PathValues.API_V2_META_TABLES_TABLE_ID_GALLERIES: ApiV2MetaTablesTableIdGalleries,
        PathValues.API_V2_META_GALLERIES_GALLERY_VIEW_ID: ApiV2MetaGalleriesGalleryViewId,
        PathValues.API_V2_META_TABLES_TABLE_ID_KANBANS: ApiV2MetaTablesTableIdKanbans,
        PathValues.API_V2_META_KANBANS_KANBAN_VIEW_ID: ApiV2MetaKanbansKanbanViewId,
        PathValues.API_V2_META_TABLES_TABLE_ID_MAPS: ApiV2MetaTablesTableIdMaps,
        PathValues.API_V2_META_MAPS_MAP_VIEW_ID: ApiV2MetaMapsMapViewId,
        PathValues.API_V2_META_BASES_BASE_ID_METADIFF: ApiV2MetaBasesBaseIdMetaDiff,
        PathValues.API_V2_META_BASES_BASE_ID_METADIFF_SOURCE_ID: ApiV2MetaBasesBaseIdMetaDiffSourceId,
        PathValues.API_V2_META_BASES_BASE_ID_HASEMPTYORNULLFILTERS: ApiV2MetaBasesBaseIdHasEmptyOrNullFilters,
        PathValues.API_V2_PUBLIC_SHAREDVIEW_SHARED_VIEW_UUID_GROUP_COLUMN_ID: ApiV2PublicSharedViewSharedViewUuidGroupColumnId,
        PathValues.API_V2_PUBLIC_CALENDARVIEW_SHARED_VIEW_UUID_COUNT_BY_DATE: ApiV2PublicCalendarViewSharedViewUuidCountByDate,
        PathValues.API_V2_PUBLIC_SHAREDVIEW_SHARED_VIEW_UUID_ROWS: ApiV2PublicSharedViewSharedViewUuidRows,
        PathValues.API_V2_PUBLIC_SHAREDVIEW_SHARED_VIEW_UUID_GROUPBY: ApiV2PublicSharedViewSharedViewUuidGroupby,
        PathValues.API_V2_PUBLIC_SHAREDVIEW_SHARED_VIEW_UUID_ROWS_ROW_ID_RELATION_TYPE_COLUMN_NAME: ApiV2PublicSharedViewSharedViewUuidRowsRowIdRelationTypeColumnName,
        PathValues.API_V2_PUBLIC_SHAREDVIEW_SHARED_VIEW_UUID_ROWS_EXPORT_TYPE: ApiV2PublicSharedViewSharedViewUuidRowsExportType,
        PathValues.API_V2_PUBLIC_SHAREDVIEW_SHARED_VIEW_UUID_NESTED_COLUMN_NAME: ApiV2PublicSharedViewSharedViewUuidNestedColumnName,
        PathValues.API_V2_PUBLIC_SHAREDBASE_SHARED_BASE_UUID_META: ApiV2PublicSharedBaseSharedBaseUuidMeta,
        PathValues.API_V2_PUBLIC_SHAREDVIEW_SHARED_VIEW_UUID_META: ApiV2PublicSharedViewSharedViewUuidMeta,
        PathValues.API_V2_PUBLIC_SHAREDERD_SHARED_ERD_UUID_META: ApiV2PublicSharedErdSharedErdUuidMeta,
        PathValues.API_V2_META_AUDITS_COMMENTS: ApiV2MetaAuditsComments,
        PathValues.API_V2_META_AUDITS_AUDIT_ID_COMMENT: ApiV2MetaAuditsAuditIdComment,
        PathValues.API_V2_META_AUDITS_COMMENTS_COUNT: ApiV2MetaAuditsCommentsCount,
        PathValues.API_V2_META_BASES_BASE_ID_AUDITS: ApiV2MetaBasesBaseIdAudits,
        PathValues.API_V2_META_AUDITS_ROWS_ROW_ID_UPDATE: ApiV2MetaAuditsRowsRowIdUpdate,
        PathValues.API_V2_META_TABLES_TABLE_ID_HOOKS: ApiV2MetaTablesTableIdHooks,
        PathValues.API_V2_META_TABLES_TABLE_ID_HOOKS_TEST: ApiV2MetaTablesTableIdHooksTest,
        PathValues.API_V2_META_TABLES_TABLE_ID_HOOKS_SAMPLE_PAYLOAD_OPERATION_VERSION: ApiV2MetaTablesTableIdHooksSamplePayloadOperationVersion,
        PathValues.API_V2_META_HOOKS_HOOK_ID: ApiV2MetaHooksHookId,
        PathValues.API_V2_META_PLUGINS: ApiV2MetaPlugins,
        PathValues.API_V2_META_PLUGINS_WEBHOOK: ApiV2MetaPluginsWebhook,
        PathValues.API_V2_META_PLUGINS_PLUGIN_TITLE_STATUS: ApiV2MetaPluginsPluginTitleStatus,
        PathValues.API_V2_META_PLUGINS_TEST: ApiV2MetaPluginsTest,
        PathValues.API_V2_META_PLUGINS_PLUGIN_ID: ApiV2MetaPluginsPluginId,
        PathValues.API_V2_META_CONNECTION_TEST: ApiV2MetaConnectionTest,
        PathValues.API_V2_META_CONNECTION_SELECT: ApiV2MetaConnectionSelect,
        PathValues.API_V2_META_NOCODB_INFO: ApiV2MetaNocodbInfo,
        PathValues.API_V2_META_AXIOS_REQUEST_MAKE: ApiV2MetaAxiosRequestMake,
        PathValues.API_V2_META_CACHE: ApiV2MetaCache,
        PathValues.API_V2_META_BASES_BASE_ID_APITOKENS: ApiV2MetaBasesBaseIdApiTokens,
        PathValues.API_V2_META_BASES_BASE_ID_APITOKENS_TOKEN: ApiV2MetaBasesBaseIdApiTokensToken,
        PathValues.API_V2_STORAGE_UPLOAD: ApiV2StorageUpload,
        PathValues.API_V2_STORAGE_UPLOADBYURL: ApiV2StorageUploadByUrl,
        PathValues.API_V2_META_BASES_BASE_ID_USERS_USER_ID_RESENDINVITE: ApiV2MetaBasesBaseIdUsersUserIdResendInvite,
        PathValues.API_V2_META_TABLES_TABLE_ID_COLUMNS_HASH: ApiV2MetaTablesTableIdColumnsHash,
        PathValues.API_V2_META_TABLES_TABLE_ID_COLUMNS_BULK: ApiV2MetaTablesTableIdColumnsBulk,
        PathValues.API_V2_TABLES_TABLE_ID_RECORDS: ApiV2TablesTableIdRecords,
        PathValues.API_V2_TABLES_TABLE_ID_RECORDS_RECORD_ID: ApiV2TablesTableIdRecordsRecordId,
        PathValues.API_V2_TABLES_TABLE_ID_RECORDS_COUNT: ApiV2TablesTableIdRecordsCount,
        PathValues.API_V2_TABLES_TABLE_ID_LINKS_LINK_FIELD_ID_RECORDS_RECORD_ID: ApiV2TablesTableIdLinksLinkFieldIdRecordsRecordId,
        PathValues.API_V2_META_BASES: ApiV2MetaBases,
        PathValues.API_V2_META_BASES_BASE_ID_SOURCES: ApiV2MetaBasesBaseIdSources,
        PathValues.API_V2_PUBLIC_CALENDARVIEW_SHARED_VIEW_UUID: ApiV2PublicCalendarViewSharedViewUuid,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_V2_META_BASES_BASE_ID_USERS: ApiV2MetaBasesBaseIdUsers,
        PathValues.API_V2_META_BASES_BASE_ID_INFO: ApiV2MetaBasesBaseIdInfo,
        PathValues.API_V2_META_BASES_BASE_ID_USERS_USER_ID: ApiV2MetaBasesBaseIdUsersUserId,
        PathValues.API_V2_META_BASES_BASE_ID_VISIBILITYRULES: ApiV2MetaBasesBaseIdVisibilityRules,
        PathValues.API_V2_META_DUPLICATE_BASE_ID_SOURCE_ID: ApiV2MetaDuplicateBaseIdSourceId,
        PathValues.API_V2_META_DUPLICATE_BASE_ID: ApiV2MetaDuplicateBaseId,
        PathValues.API_V2_META_BASES_BASE_ID: ApiV2MetaBasesBaseId,
        PathValues.API_V2_META_BASES_BASE_ID_USER: ApiV2MetaBasesBaseIdUser,
        PathValues.API_V2_META_BASES_BASE_ID_SOURCES_SOURCE_ID: ApiV2MetaBasesBaseIdSourcesSourceId,
        PathValues.API_V2_META_BASES_BASE_ID_SOURCES_SOURCE_ID_SQL_VIEW: ApiV2MetaBasesBaseIdSourcesSourceIdSqlView,
        PathValues.API_V2_META_BASES_BASE_ID_SOURCES_SOURCE_ID_SHARE_ERD: ApiV2MetaBasesBaseIdSourcesSourceIdShareErd,
        PathValues.API_V2_META_BASES_BASE_ID_SHARED: ApiV2MetaBasesBaseIdShared,
        PathValues.API_V2_META_BASES_BASE_ID_COST: ApiV2MetaBasesBaseIdCost,
        PathValues.API_V2_META_BASES_BASE_ID_TABLES: ApiV2MetaBasesBaseIdTables,
        PathValues.API_V2_META_TABLES_TABLE_ID: ApiV2MetaTablesTableId,
        PathValues.API_V2_META_DUPLICATE_BASE_ID_TABLE_TABLE_ID: ApiV2MetaDuplicateBaseIdTableTableId,
        PathValues.API_V2_META_BASES_BASE_ID_SOURCE_ID_TABLES: ApiV2MetaBasesBaseIdSourceIdTables,
        PathValues.API_V2_META_TABLES_TABLE_ID_REORDER: ApiV2MetaTablesTableIdReorder,
        PathValues.API_V2_META_TABLES_TABLE_ID_COLUMNS: ApiV2MetaTablesTableIdColumns,
        PathValues.API_V2_META_COLUMNS_COLUMN_ID: ApiV2MetaColumnsColumnId,
        PathValues.API_V2_META_COLUMNS_COLUMN_ID_PRIMARY: ApiV2MetaColumnsColumnIdPrimary,
        PathValues.API_V2_META_TABLES_TABLE_ID_VIEWS: ApiV2MetaTablesTableIdViews,
        PathValues.API_V2_META_VIEWS_VIEW_ID: ApiV2MetaViewsViewId,
        PathValues.API_V2_META_VIEWS_VIEW_ID_SHOWALL: ApiV2MetaViewsViewIdShowAll,
        PathValues.API_V2_META_VIEWS_VIEW_ID_HIDEALL: ApiV2MetaViewsViewIdHideAll,
        PathValues.API_V2_META_TABLES_TABLE_ID_SHARE: ApiV2MetaTablesTableIdShare,
        PathValues.API_V2_META_VIEWS_VIEW_ID_SHARE: ApiV2MetaViewsViewIdShare,
        PathValues.API_V2_META_VIEWS_VIEW_ID_COLUMNS: ApiV2MetaViewsViewIdColumns,
        PathValues.API_V2_META_VIEWS_VIEW_ID_COLUMNS_COLUMN_ID: ApiV2MetaViewsViewIdColumnsColumnId,
        PathValues.API_V2_META_VIEWS_VIEW_ID_SORTS: ApiV2MetaViewsViewIdSorts,
        PathValues.API_V2_META_SORTS_SORT_ID: ApiV2MetaSortsSortId,
        PathValues.API_V2_META_VIEWS_VIEW_ID_FILTERS: ApiV2MetaViewsViewIdFilters,
        PathValues.API_V2_META_HOOKS_HOOK_ID_FILTERS: ApiV2MetaHooksHookIdFilters,
        PathValues.API_V2_META_HOOKS_HOOK_ID_LOGS: ApiV2MetaHooksHookIdLogs,
        PathValues.API_V2_META_FILTERS_FILTER_ID: ApiV2MetaFiltersFilterId,
        PathValues.API_V2_META_FILTERS_FILTER_GROUP_ID_CHILDREN: ApiV2MetaFiltersFilterGroupIdChildren,
        PathValues.API_V2_META_TABLES_TABLE_ID_GRIDS: ApiV2MetaTablesTableIdGrids,
        PathValues.API_V2_META_TABLES_TABLE_ID_FORMS: ApiV2MetaTablesTableIdForms,
        PathValues.API_V2_META_FORMS_FORM_VIEW_ID: ApiV2MetaFormsFormViewId,
        PathValues.API_V2_META_FORMCOLUMNS_FORM_VIEW_COLUMN_ID: ApiV2MetaFormColumnsFormViewColumnId,
        PathValues.API_V2_META_GRIDS_VIEW_ID: ApiV2MetaGridsViewId,
        PathValues.API_V2_META_GRIDS_GRID_ID_GRIDCOLUMNS: ApiV2MetaGridsGridIdGridColumns,
        PathValues.API_V2_META_GRIDCOLUMNS_COLUMN_ID: ApiV2MetaGridColumnsColumnId,
        PathValues.API_V2_META_TABLES_TABLE_ID_GALLERIES: ApiV2MetaTablesTableIdGalleries,
        PathValues.API_V2_META_GALLERIES_GALLERY_VIEW_ID: ApiV2MetaGalleriesGalleryViewId,
        PathValues.API_V2_META_TABLES_TABLE_ID_KANBANS: ApiV2MetaTablesTableIdKanbans,
        PathValues.API_V2_META_KANBANS_KANBAN_VIEW_ID: ApiV2MetaKanbansKanbanViewId,
        PathValues.API_V2_META_TABLES_TABLE_ID_MAPS: ApiV2MetaTablesTableIdMaps,
        PathValues.API_V2_META_MAPS_MAP_VIEW_ID: ApiV2MetaMapsMapViewId,
        PathValues.API_V2_META_BASES_BASE_ID_METADIFF: ApiV2MetaBasesBaseIdMetaDiff,
        PathValues.API_V2_META_BASES_BASE_ID_METADIFF_SOURCE_ID: ApiV2MetaBasesBaseIdMetaDiffSourceId,
        PathValues.API_V2_META_BASES_BASE_ID_HASEMPTYORNULLFILTERS: ApiV2MetaBasesBaseIdHasEmptyOrNullFilters,
        PathValues.API_V2_PUBLIC_SHAREDVIEW_SHARED_VIEW_UUID_GROUP_COLUMN_ID: ApiV2PublicSharedViewSharedViewUuidGroupColumnId,
        PathValues.API_V2_PUBLIC_CALENDARVIEW_SHARED_VIEW_UUID_COUNT_BY_DATE: ApiV2PublicCalendarViewSharedViewUuidCountByDate,
        PathValues.API_V2_PUBLIC_SHAREDVIEW_SHARED_VIEW_UUID_ROWS: ApiV2PublicSharedViewSharedViewUuidRows,
        PathValues.API_V2_PUBLIC_SHAREDVIEW_SHARED_VIEW_UUID_GROUPBY: ApiV2PublicSharedViewSharedViewUuidGroupby,
        PathValues.API_V2_PUBLIC_SHAREDVIEW_SHARED_VIEW_UUID_ROWS_ROW_ID_RELATION_TYPE_COLUMN_NAME: ApiV2PublicSharedViewSharedViewUuidRowsRowIdRelationTypeColumnName,
        PathValues.API_V2_PUBLIC_SHAREDVIEW_SHARED_VIEW_UUID_ROWS_EXPORT_TYPE: ApiV2PublicSharedViewSharedViewUuidRowsExportType,
        PathValues.API_V2_PUBLIC_SHAREDVIEW_SHARED_VIEW_UUID_NESTED_COLUMN_NAME: ApiV2PublicSharedViewSharedViewUuidNestedColumnName,
        PathValues.API_V2_PUBLIC_SHAREDBASE_SHARED_BASE_UUID_META: ApiV2PublicSharedBaseSharedBaseUuidMeta,
        PathValues.API_V2_PUBLIC_SHAREDVIEW_SHARED_VIEW_UUID_META: ApiV2PublicSharedViewSharedViewUuidMeta,
        PathValues.API_V2_PUBLIC_SHAREDERD_SHARED_ERD_UUID_META: ApiV2PublicSharedErdSharedErdUuidMeta,
        PathValues.API_V2_META_AUDITS_COMMENTS: ApiV2MetaAuditsComments,
        PathValues.API_V2_META_AUDITS_AUDIT_ID_COMMENT: ApiV2MetaAuditsAuditIdComment,
        PathValues.API_V2_META_AUDITS_COMMENTS_COUNT: ApiV2MetaAuditsCommentsCount,
        PathValues.API_V2_META_BASES_BASE_ID_AUDITS: ApiV2MetaBasesBaseIdAudits,
        PathValues.API_V2_META_AUDITS_ROWS_ROW_ID_UPDATE: ApiV2MetaAuditsRowsRowIdUpdate,
        PathValues.API_V2_META_TABLES_TABLE_ID_HOOKS: ApiV2MetaTablesTableIdHooks,
        PathValues.API_V2_META_TABLES_TABLE_ID_HOOKS_TEST: ApiV2MetaTablesTableIdHooksTest,
        PathValues.API_V2_META_TABLES_TABLE_ID_HOOKS_SAMPLE_PAYLOAD_OPERATION_VERSION: ApiV2MetaTablesTableIdHooksSamplePayloadOperationVersion,
        PathValues.API_V2_META_HOOKS_HOOK_ID: ApiV2MetaHooksHookId,
        PathValues.API_V2_META_PLUGINS: ApiV2MetaPlugins,
        PathValues.API_V2_META_PLUGINS_WEBHOOK: ApiV2MetaPluginsWebhook,
        PathValues.API_V2_META_PLUGINS_PLUGIN_TITLE_STATUS: ApiV2MetaPluginsPluginTitleStatus,
        PathValues.API_V2_META_PLUGINS_TEST: ApiV2MetaPluginsTest,
        PathValues.API_V2_META_PLUGINS_PLUGIN_ID: ApiV2MetaPluginsPluginId,
        PathValues.API_V2_META_CONNECTION_TEST: ApiV2MetaConnectionTest,
        PathValues.API_V2_META_CONNECTION_SELECT: ApiV2MetaConnectionSelect,
        PathValues.API_V2_META_NOCODB_INFO: ApiV2MetaNocodbInfo,
        PathValues.API_V2_META_AXIOS_REQUEST_MAKE: ApiV2MetaAxiosRequestMake,
        PathValues.API_V2_META_CACHE: ApiV2MetaCache,
        PathValues.API_V2_META_BASES_BASE_ID_APITOKENS: ApiV2MetaBasesBaseIdApiTokens,
        PathValues.API_V2_META_BASES_BASE_ID_APITOKENS_TOKEN: ApiV2MetaBasesBaseIdApiTokensToken,
        PathValues.API_V2_STORAGE_UPLOAD: ApiV2StorageUpload,
        PathValues.API_V2_STORAGE_UPLOADBYURL: ApiV2StorageUploadByUrl,
        PathValues.API_V2_META_BASES_BASE_ID_USERS_USER_ID_RESENDINVITE: ApiV2MetaBasesBaseIdUsersUserIdResendInvite,
        PathValues.API_V2_META_TABLES_TABLE_ID_COLUMNS_HASH: ApiV2MetaTablesTableIdColumnsHash,
        PathValues.API_V2_META_TABLES_TABLE_ID_COLUMNS_BULK: ApiV2MetaTablesTableIdColumnsBulk,
        PathValues.API_V2_TABLES_TABLE_ID_RECORDS: ApiV2TablesTableIdRecords,
        PathValues.API_V2_TABLES_TABLE_ID_RECORDS_RECORD_ID: ApiV2TablesTableIdRecordsRecordId,
        PathValues.API_V2_TABLES_TABLE_ID_RECORDS_COUNT: ApiV2TablesTableIdRecordsCount,
        PathValues.API_V2_TABLES_TABLE_ID_LINKS_LINK_FIELD_ID_RECORDS_RECORD_ID: ApiV2TablesTableIdLinksLinkFieldIdRecordsRecordId,
        PathValues.API_V2_META_BASES: ApiV2MetaBases,
        PathValues.API_V2_META_BASES_BASE_ID_SOURCES: ApiV2MetaBasesBaseIdSources,
        PathValues.API_V2_PUBLIC_CALENDARVIEW_SHARED_VIEW_UUID: ApiV2PublicCalendarViewSharedViewUuid,
    }
)
