from noco_db_python_sdk.paths.api_v2_tables_table_id_records.get import ApiForget
from noco_db_python_sdk.paths.api_v2_tables_table_id_records.post import ApiForpost
from noco_db_python_sdk.paths.api_v2_tables_table_id_records.delete import ApiFordelete
from noco_db_python_sdk.paths.api_v2_tables_table_id_records.patch import ApiForpatch


class ApiV2TablesTableIdRecords(
    ApiForget,
    ApiForpost,
    ApiFordelete,
    ApiForpatch,
):
    pass
