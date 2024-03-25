from noco_db_python_sdk.paths.api_v2_meta_bases_base_id_shared.get import ApiForget
from noco_db_python_sdk.paths.api_v2_meta_bases_base_id_shared.post import ApiForpost
from noco_db_python_sdk.paths.api_v2_meta_bases_base_id_shared.delete import ApiFordelete
from noco_db_python_sdk.paths.api_v2_meta_bases_base_id_shared.patch import ApiForpatch


class ApiV2MetaBasesBaseIdShared(
    ApiForget,
    ApiForpost,
    ApiFordelete,
    ApiForpatch,
):
    pass
