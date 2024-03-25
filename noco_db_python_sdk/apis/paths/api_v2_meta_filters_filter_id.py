from noco_db_python_sdk.paths.api_v2_meta_filters_filter_id.get import ApiForget
from noco_db_python_sdk.paths.api_v2_meta_filters_filter_id.delete import ApiFordelete
from noco_db_python_sdk.paths.api_v2_meta_filters_filter_id.patch import ApiForpatch


class ApiV2MetaFiltersFilterId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
