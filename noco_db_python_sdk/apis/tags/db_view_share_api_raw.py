# coding: utf-8

"""
    NocoDB v2

    NocoDB API Documentation

    Generated by: https://konfigthis.com
"""

from noco_db_python_sdk.paths.api_v2_meta_views_view_id_share.post import CreateSharedViewRaw
from noco_db_python_sdk.paths.api_v2_meta_views_view_id_share.delete import DeleteSharedViewRaw
from noco_db_python_sdk.paths.api_v2_meta_tables_table_id_share.get import ListSharedViewsRaw
from noco_db_python_sdk.paths.api_v2_meta_views_view_id_share.patch import UpdateSharedViewRaw


class DBViewShareApiRaw(
    CreateSharedViewRaw,
    DeleteSharedViewRaw,
    ListSharedViewsRaw,
    UpdateSharedViewRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
