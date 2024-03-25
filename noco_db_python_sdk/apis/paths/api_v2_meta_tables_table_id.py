from noco_db_python_sdk.paths.api_v2_meta_tables_table_id.get import ApiForget
from noco_db_python_sdk.paths.api_v2_meta_tables_table_id.delete import ApiFordelete
from noco_db_python_sdk.paths.api_v2_meta_tables_table_id.patch import ApiForpatch


class ApiV2MetaTablesTableId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
