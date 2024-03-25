# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from noco_db_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    DB_VIEW = "DB View"
    BASE = "Base"
    SOURCE = "Source"
    PUBLIC = "Public"
    UTILS = "Utils"
    TABLE_RECORDS = "Table Records"
    DB_TABLE = "DB Table"
    DB_TABLE_COLUMN = "DB Table Column"
    DB_TABLE_FILTER = "DB Table Filter"
    DB_TABLE_WEBHOOK = "DB Table Webhook"
    PLUGIN = "Plugin"
    AUTH = "Auth"
    DB_TABLE_SORT = "DB Table Sort"
    DB_VIEW_SHARE = "DB View Share"
    DB_VIEW_COLUMN = "DB View Column"
    API_TOKEN = "API Token"
    DB_TABLE_WEBHOOK_FILTER = "DB Table Webhook Filter"
    STORAGE = "Storage"
    DB_TABLE_WEBHOOK_LOGS = "DB Table Webhook Logs"
