from noco_db_python_sdk.paths.api_v2_meta_cache.get import ApiForget
from noco_db_python_sdk.paths.api_v2_meta_cache.delete import ApiFordelete


class ApiV2MetaCache(
    ApiForget,
    ApiFordelete,
):
    pass
