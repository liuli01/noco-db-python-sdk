from noco_db_python_sdk.paths.api_v2_meta_bases_base_id.get import ApiForget
from noco_db_python_sdk.paths.api_v2_meta_bases_base_id.delete import ApiFordelete
from noco_db_python_sdk.paths.api_v2_meta_bases_base_id.patch import ApiForpatch


class ApiV2MetaBasesBaseId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
