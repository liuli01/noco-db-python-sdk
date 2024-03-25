from noco_db_python_sdk.paths.api_v2_meta_columns_column_id.get import ApiForget
from noco_db_python_sdk.paths.api_v2_meta_columns_column_id.delete import ApiFordelete
from noco_db_python_sdk.paths.api_v2_meta_columns_column_id.patch import ApiForpatch


class ApiV2MetaColumnsColumnId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
