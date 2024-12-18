# coding: utf-8

"""
    NocoDB v2

    NocoDB API Documentation

    Generated by: https://konfigthis.com
"""

from noco_db_python_sdk.paths.api_v2_meta_views_view_id_filters.post import CreateViewFilterRaw
from noco_db_python_sdk.paths.api_v2_meta_filters_filter_id.delete import DeleteByIdRaw
from noco_db_python_sdk.paths.api_v2_meta_filters_filter_id.get import GetByIdRaw
from noco_db_python_sdk.paths.api_v2_meta_filters_filter_group_id_children.get import GetChildrenRaw
from noco_db_python_sdk.paths.api_v2_meta_views_view_id_filters.get import GetViewDataRaw
from noco_db_python_sdk.paths.api_v2_meta_filters_filter_id.patch import UpdateByIdRaw


class DBTableFilterApiRaw(
    CreateViewFilterRaw,
    DeleteByIdRaw,
    GetByIdRaw,
    GetChildrenRaw,
    GetViewDataRaw,
    UpdateByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
