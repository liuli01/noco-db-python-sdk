from noco_db_python_sdk.paths.api_v2_meta_views_view_id_share.post import ApiForpost
from noco_db_python_sdk.paths.api_v2_meta_views_view_id_share.delete import ApiFordelete
from noco_db_python_sdk.paths.api_v2_meta_views_view_id_share.patch import ApiForpatch


class ApiV2MetaViewsViewIdShare(
    ApiForpost,
    ApiFordelete,
    ApiForpatch,
):
    pass
