# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from noco_db_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_V2_META_BASES_BASE_ID_USERS = "/api/v2/meta/bases/{baseId}/users"
    API_V2_META_BASES_BASE_ID_INFO = "/api/v2/meta/bases/{baseId}/info"
    API_V2_META_BASES_BASE_ID_USERS_USER_ID = "/api/v2/meta/bases/{baseId}/users/{userId}"
    API_V2_META_BASES_BASE_ID_VISIBILITYRULES = "/api/v2/meta/bases/{baseId}/visibility-rules"
    API_V2_META_DUPLICATE_BASE_ID_SOURCE_ID = "/api/v2/meta/duplicate/{baseId}/{sourceId}"
    API_V2_META_DUPLICATE_BASE_ID = "/api/v2/meta/duplicate/{baseId}"
    API_V2_META_BASES_BASE_ID = "/api/v2/meta/bases/{baseId}"
    API_V2_META_BASES_BASE_ID_USER = "/api/v2/meta/bases/{baseId}/user"
    API_V2_META_BASES_BASE_ID_SOURCES_SOURCE_ID = "/api/v2/meta/bases/{baseId}/sources/{sourceId}"
    API_V2_META_BASES_BASE_ID_SOURCES_SOURCE_ID_SQL_VIEW = "/api/v2/meta/bases/:baseId/sources/:sourceId/sqlView"
    API_V2_META_BASES_BASE_ID_SOURCES_SOURCE_ID_SHARE_ERD = "/api/v2/meta/bases/{baseId}/sources/{sourceId}/share/erd"
    API_V2_META_BASES_BASE_ID_SHARED = "/api/v2/meta/bases/{baseId}/shared"
    API_V2_META_BASES_BASE_ID_COST = "/api/v2/meta/bases/{baseId}/cost"
    API_V2_META_BASES_BASE_ID_TABLES = "/api/v2/meta/bases/{baseId}/tables"
    API_V2_META_TABLES_TABLE_ID = "/api/v2/meta/tables/{tableId}"
    API_V2_META_DUPLICATE_BASE_ID_TABLE_TABLE_ID = "/api/v2/meta/duplicate/{baseId}/table/{tableId}"
    API_V2_META_BASES_BASE_ID_SOURCE_ID_TABLES = "/api/v2/meta/bases/{baseId}/{sourceId}/tables"
    API_V2_META_TABLES_TABLE_ID_REORDER = "/api/v2/meta/tables/{tableId}/reorder"
    API_V2_META_TABLES_TABLE_ID_COLUMNS = "/api/v2/meta/tables/{tableId}/columns"
    API_V2_META_COLUMNS_COLUMN_ID = "/api/v2/meta/columns/{columnId}"
    API_V2_META_COLUMNS_COLUMN_ID_PRIMARY = "/api/v2/meta/columns/{columnId}/primary"
    API_V2_META_TABLES_TABLE_ID_VIEWS = "/api/v2/meta/tables/{tableId}/views"
    API_V2_META_VIEWS_VIEW_ID = "/api/v2/meta/views/{viewId}"
    API_V2_META_VIEWS_VIEW_ID_SHOWALL = "/api/v2/meta/views/{viewId}/show-all"
    API_V2_META_VIEWS_VIEW_ID_HIDEALL = "/api/v2/meta/views/{viewId}/hide-all"
    API_V2_META_TABLES_TABLE_ID_SHARE = "/api/v2/meta/tables/{tableId}/share"
    API_V2_META_VIEWS_VIEW_ID_SHARE = "/api/v2/meta/views/{viewId}/share"
    API_V2_META_VIEWS_VIEW_ID_COLUMNS = "/api/v2/meta/views/{viewId}/columns"
    API_V2_META_VIEWS_VIEW_ID_COLUMNS_COLUMN_ID = "/api/v2/meta/views/{viewId}/columns/{columnId}"
    API_V2_META_VIEWS_VIEW_ID_SORTS = "/api/v2/meta/views/{viewId}/sorts"
    API_V2_META_SORTS_SORT_ID = "/api/v2/meta/sorts/{sortId}"
    API_V2_META_VIEWS_VIEW_ID_FILTERS = "/api/v2/meta/views/{viewId}/filters"
    API_V2_META_HOOKS_HOOK_ID_FILTERS = "/api/v2/meta/hooks/{hookId}/filters"
    API_V2_META_HOOKS_HOOK_ID_LOGS = "/api/v2/meta/hooks/{hookId}/logs"
    API_V2_META_FILTERS_FILTER_ID = "/api/v2/meta/filters/{filterId}"
    API_V2_META_FILTERS_FILTER_GROUP_ID_CHILDREN = "/api/v2/meta/filters/{filterGroupId}/children"
    API_V2_META_TABLES_TABLE_ID_GRIDS = "/api/v2/meta/tables/{tableId}/grids"
    API_V2_META_TABLES_TABLE_ID_FORMS = "/api/v2/meta/tables/{tableId}/forms"
    API_V2_META_FORMS_FORM_VIEW_ID = "/api/v2/meta/forms/{formViewId}"
    API_V2_META_FORMCOLUMNS_FORM_VIEW_COLUMN_ID = "/api/v2/meta/form-columns/{formViewColumnId}"
    API_V2_META_GRIDS_VIEW_ID = "/api/v2/meta/grids/{viewId}"
    API_V2_META_GRIDS_GRID_ID_GRIDCOLUMNS = "/api/v2/meta/grids/{gridId}/grid-columns"
    API_V2_META_GRIDCOLUMNS_COLUMN_ID = "/api/v2/meta/grid-columns/{columnId}"
    API_V2_META_TABLES_TABLE_ID_GALLERIES = "/api/v2/meta/tables/{tableId}/galleries"
    API_V2_META_GALLERIES_GALLERY_VIEW_ID = "/api/v2/meta/galleries/{galleryViewId}"
    API_V2_META_TABLES_TABLE_ID_KANBANS = "/api/v2/meta/tables/{tableId}/kanbans"
    API_V2_META_KANBANS_KANBAN_VIEW_ID = "/api/v2/meta/kanbans/{kanbanViewId}"
    API_V2_META_TABLES_TABLE_ID_MAPS = "/api/v2/meta/tables/{tableId}/maps"
    API_V2_META_MAPS_MAP_VIEW_ID = "/api/v2/meta/maps/{mapViewId}"
    API_V2_META_BASES_BASE_ID_METADIFF = "/api/v2/meta/bases/{baseId}/meta-diff"
    API_V2_META_BASES_BASE_ID_METADIFF_SOURCE_ID = "/api/v2/meta/bases/{baseId}/meta-diff/{sourceId}"
    API_V2_META_BASES_BASE_ID_HASEMPTYORNULLFILTERS = "/api/v2/meta/bases/{baseId}/has-empty-or-null-filters"
    API_V2_PUBLIC_SHAREDVIEW_SHARED_VIEW_UUID_GROUP_COLUMN_ID = "/api/v2/public/shared-view/{sharedViewUuid}/group/{columnId}"
    API_V2_PUBLIC_CALENDARVIEW_SHARED_VIEW_UUID_COUNT_BY_DATE = "/api/v2/public/calendar-view/{sharedViewUuid}/countByDate"
    API_V2_PUBLIC_SHAREDVIEW_SHARED_VIEW_UUID_ROWS = "/api/v2/public/shared-view/{sharedViewUuid}/rows"
    API_V2_PUBLIC_SHAREDVIEW_SHARED_VIEW_UUID_GROUPBY = "/api/v2/public/shared-view/{sharedViewUuid}/groupby"
    API_V2_PUBLIC_SHAREDVIEW_SHARED_VIEW_UUID_ROWS_ROW_ID_RELATION_TYPE_COLUMN_NAME = "/api/v2/public/shared-view/{sharedViewUuid}/rows/{rowId}/{relationType}/{columnName}"
    API_V2_PUBLIC_SHAREDVIEW_SHARED_VIEW_UUID_ROWS_EXPORT_TYPE = "/api/v2/public/shared-view/{sharedViewUuid}/rows/export/{type}"
    API_V2_PUBLIC_SHAREDVIEW_SHARED_VIEW_UUID_NESTED_COLUMN_NAME = "/api/v2/public/shared-view/{sharedViewUuid}/nested/{columnName}"
    API_V2_PUBLIC_SHAREDBASE_SHARED_BASE_UUID_META = "/api/v2/public/shared-base/{sharedBaseUuid}/meta"
    API_V2_PUBLIC_SHAREDVIEW_SHARED_VIEW_UUID_META = "/api/v2/public/shared-view/{sharedViewUuid}/meta"
    API_V2_PUBLIC_SHAREDERD_SHARED_ERD_UUID_META = "/api/v2/public/shared-erd/{sharedErdUuid}/meta"
    API_V2_META_AUDITS_COMMENTS = "/api/v2/meta/audits/comments"
    API_V2_META_AUDITS_AUDIT_ID_COMMENT = "/api/v2/meta/audits/{auditId}/comment"
    API_V2_META_AUDITS_COMMENTS_COUNT = "/api/v2/meta/audits/comments/count"
    API_V2_META_BASES_BASE_ID_AUDITS = "/api/v2/meta/bases/{baseId}/audits"
    API_V2_META_AUDITS_ROWS_ROW_ID_UPDATE = "/api/v2/meta/audits/rows/{rowId}/update"
    API_V2_META_TABLES_TABLE_ID_HOOKS = "/api/v2/meta/tables/{tableId}/hooks"
    API_V2_META_TABLES_TABLE_ID_HOOKS_TEST = "/api/v2/meta/tables/{tableId}/hooks/test"
    API_V2_META_TABLES_TABLE_ID_HOOKS_SAMPLE_PAYLOAD_OPERATION_VERSION = "/api/v2/meta/tables/{tableId}/hooks/samplePayload/{operation}/{version}"
    API_V2_META_HOOKS_HOOK_ID = "/api/v2/meta/hooks/{hookId}"
    API_V2_META_PLUGINS = "/api/v2/meta/plugins"
    API_V2_META_PLUGINS_WEBHOOK = "/api/v2/meta/plugins/webhook"
    API_V2_META_PLUGINS_PLUGIN_TITLE_STATUS = "/api/v2/meta/plugins/{pluginTitle}/status"
    API_V2_META_PLUGINS_TEST = "/api/v2/meta/plugins/test"
    API_V2_META_PLUGINS_PLUGIN_ID = "/api/v2/meta/plugins/{pluginId}"
    API_V2_META_CONNECTION_TEST = "/api/v2/meta/connection/test"
    API_V2_META_CONNECTION_SELECT = "/api/v2/meta/connection/select"
    API_V2_META_NOCODB_INFO = "/api/v2/meta/nocodb/info"
    API_V2_META_AXIOS_REQUEST_MAKE = "/api/v2/meta/axiosRequestMake"
    API_V2_META_CACHE = "/api/v2/meta/cache"
    API_V2_META_BASES_BASE_ID_APITOKENS = "/api/v2/meta/bases/{baseId}/api-tokens"
    API_V2_META_BASES_BASE_ID_APITOKENS_TOKEN = "/api/v2/meta/bases/{baseId}/api-tokens/{token}"
    API_V2_STORAGE_UPLOAD = "/api/v2/storage/upload"
    API_V2_STORAGE_UPLOADBYURL = "/api/v2/storage/upload-by-url"
    API_V2_META_BASES_BASE_ID_USERS_USER_ID_RESENDINVITE = "/api/v2/meta/bases/{baseId}/users/{userId}/resend-invite"
    API_V2_META_TABLES_TABLE_ID_COLUMNS_HASH = "/api/v2/meta/tables/{tableId}/columns/hash"
    API_V2_META_TABLES_TABLE_ID_COLUMNS_BULK = "/api/v2/meta/tables/{tableId}/columns/bulk"
    API_V2_TABLES_TABLE_ID_RECORDS = "/api/v2/tables/{tableId}/records"
    API_V2_TABLES_TABLE_ID_RECORDS_RECORD_ID = "/api/v2/tables/{tableId}/records/{recordId}"
    API_V2_TABLES_TABLE_ID_RECORDS_COUNT = "/api/v2/tables/{tableId}/records/count"
    API_V2_TABLES_TABLE_ID_LINKS_LINK_FIELD_ID_RECORDS_RECORD_ID = "/api/v2/tables/{tableId}/links/{linkFieldId}/records/{recordId}"
    API_V2_META_BASES = "/api/v2/meta/bases"
    API_V2_META_BASES_BASE_ID_SOURCES = "/api/v2/meta/bases/{baseId}/sources"
    API_V2_PUBLIC_CALENDARVIEW_SHARED_VIEW_UUID = "/api/v2/public/calendar-view/{sharedViewUuid}"
