<div align="center">

[![Visit Nocodb](./header.png)](https://nocodb.com)

# Nocodb<a id="nocodb"></a>

NocoDB API Documentation


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`nocodb.api_token.create_in_base`](#nocodbapi_tokencreate_in_base)
  * [`nocodb.api_token.delete_in_base`](#nocodbapi_tokendelete_in_base)
  * [`nocodb.api_token.list_in_base`](#nocodbapi_tokenlist_in_base)
  * [`nocodb.auth.add_base_user`](#nocodbauthadd_base_user)
  * [`nocodb.auth.delete_base_user`](#nocodbauthdelete_base_user)
  * [`nocodb.auth.list_base_users`](#nocodbauthlist_base_users)
  * [`nocodb.auth.resend_invite_user`](#nocodbauthresend_invite_user)
  * [`nocodb.auth.update_base_user`](#nocodbauthupdate_base_user)
  * [`nocodb.base.calculate_cost`](#nocodbbasecalculate_cost)
  * [`nocodb.base.check_empty_filters`](#nocodbbasecheck_empty_filters)
  * [`nocodb.base.create_new_base`](#nocodbbasecreate_new_base)
  * [`nocodb.base.create_shared_base`](#nocodbbasecreate_shared_base)
  * [`nocodb.base.create_ui_acl`](#nocodbbasecreate_ui_acl)
  * [`nocodb.base.delete_shared_base`](#nocodbbasedelete_shared_base)
  * [`nocodb.base.duplicate_base_post`](#nocodbbaseduplicate_base_post)
  * [`nocodb.base.duplicate_post`](#nocodbbaseduplicate_post)
  * [`nocodb.base.get_info`](#nocodbbaseget_info)
  * [`nocodb.base.get_info_by_id`](#nocodbbaseget_info_by_id)
  * [`nocodb.base.get_shared_base`](#nocodbbaseget_shared_base)
  * [`nocodb.base.get_ui_acl`](#nocodbbaseget_ui_acl)
  * [`nocodb.base.list_audits_in_base`](#nocodbbaselist_audits_in_base)
  * [`nocodb.base.list_bases`](#nocodbbaselist_bases)
  * [`nocodb.base.meta_diff_get`](#nocodbbasemeta_diff_get)
  * [`nocodb.base.remove_base`](#nocodbbaseremove_base)
  * [`nocodb.base.sync_meta_diff`](#nocodbbasesync_meta_diff)
  * [`nocodb.base.update_base_meta`](#nocodbbaseupdate_base_meta)
  * [`nocodb.base.update_meta_user`](#nocodbbaseupdate_meta_user)
  * [`nocodb.base.update_shared_base`](#nocodbbaseupdate_shared_base)
  * [`nocodb.db_table.create_new_table`](#nocodbdb_tablecreate_new_table)
  * [`nocodb.db_table.delete_by_table_id`](#nocodbdb_tabledelete_by_table_id)
  * [`nocodb.db_table.duplicate_table_post`](#nocodbdb_tableduplicate_table_post)
  * [`nocodb.db_table.list_tables`](#nocodbdb_tablelist_tables)
  * [`nocodb.db_table.read_by_table_id`](#nocodbdb_tableread_by_table_id)
  * [`nocodb.db_table.update_meta`](#nocodbdb_tableupdate_meta)
  * [`nocodb.db_table.update_table_order`](#nocodbdb_tableupdate_table_order)
  * [`nocodb.db_table_column.bulk_create_update`](#nocodbdb_table_columnbulk_create_update)
  * [`nocodb.db_table_column.create_new_column`](#nocodbdb_table_columncreate_new_column)
  * [`nocodb.db_table_column.delete_by_column_id`](#nocodbdb_table_columndelete_by_column_id)
  * [`nocodb.db_table_column.get_column_by_id`](#nocodbdb_table_columnget_column_by_id)
  * [`nocodb.db_table_column.get_table_columns_hash`](#nocodbdb_table_columnget_table_columns_hash)
  * [`nocodb.db_table_column.set_primary_value`](#nocodbdb_table_columnset_primary_value)
  * [`nocodb.db_table_column.update_by_column_id`](#nocodbdb_table_columnupdate_by_column_id)
  * [`nocodb.db_table_filter.create_view_filter`](#nocodbdb_table_filtercreate_view_filter)
  * [`nocodb.db_table_filter.delete_by_id`](#nocodbdb_table_filterdelete_by_id)
  * [`nocodb.db_table_filter.get_by_id`](#nocodbdb_table_filterget_by_id)
  * [`nocodb.db_table_filter.get_children`](#nocodbdb_table_filterget_children)
  * [`nocodb.db_table_filter.get_view_data`](#nocodbdb_table_filterget_view_data)
  * [`nocodb.db_table_filter.update_by_id`](#nocodbdb_table_filterupdate_by_id)
  * [`nocodb.db_table_sort.delete_by_id`](#nocodbdb_table_sortdelete_by_id)
  * [`nocodb.db_table_sort.get_all_sorts`](#nocodbdb_table_sortget_all_sorts)
  * [`nocodb.db_table_sort.get_sort_by_id`](#nocodbdb_table_sortget_sort_by_id)
  * [`nocodb.db_table_sort.update_sort_by_id`](#nocodbdb_table_sortupdate_sort_by_id)
  * [`nocodb.db_table_sort.update_view_sort`](#nocodbdb_table_sortupdate_view_sort)
  * [`nocodb.db_table_webhook.create_hook`](#nocodbdb_table_webhookcreate_hook)
  * [`nocodb.db_table_webhook.delete_by_id`](#nocodbdb_table_webhookdelete_by_id)
  * [`nocodb.db_table_webhook.get_sample_payload`](#nocodbdb_table_webhookget_sample_payload)
  * [`nocodb.db_table_webhook.list_table_hooks`](#nocodbdb_table_webhooklist_table_hooks)
  * [`nocodb.db_table_webhook.test_hook_create`](#nocodbdb_table_webhooktest_hook_create)
  * [`nocodb.db_table_webhook.update_by_id`](#nocodbdb_table_webhookupdate_by_id)
  * [`nocodb.db_table_webhook_filter.create_new_filter`](#nocodbdb_table_webhook_filtercreate_new_filter)
  * [`nocodb.db_table_webhook_filter.get_hook_filter`](#nocodbdb_table_webhook_filterget_hook_filter)
  * [`nocodb.db_table_webhook_logs.list`](#nocodbdb_table_webhook_logslist)
  * [`nocodb.db_view.create_form_view`](#nocodbdb_viewcreate_form_view)
  * [`nocodb.db_view.create_gallery_view`](#nocodbdb_viewcreate_gallery_view)
  * [`nocodb.db_view.create_grid_view`](#nocodbdb_viewcreate_grid_view)
  * [`nocodb.db_view.create_kanban_view`](#nocodbdb_viewcreate_kanban_view)
  * [`nocodb.db_view.create_map_view`](#nocodbdb_viewcreate_map_view)
  * [`nocodb.db_view.delete_view_by_id`](#nocodbdb_viewdelete_view_by_id)
  * [`nocodb.db_view.get_form_by_id`](#nocodbdb_viewget_form_by_id)
  * [`nocodb.db_view.get_gallery_view`](#nocodbdb_viewget_gallery_view)
  * [`nocodb.db_view.get_map_view_by_id`](#nocodbdb_viewget_map_view_by_id)
  * [`nocodb.db_view.hide_all_columns`](#nocodbdb_viewhide_all_columns)
  * [`nocodb.db_view.kanban_view_get`](#nocodbdb_viewkanban_view_get)
  * [`nocodb.db_view.list_grid_columns`](#nocodbdb_viewlist_grid_columns)
  * [`nocodb.db_view.list_table_views`](#nocodbdb_viewlist_table_views)
  * [`nocodb.db_view.show_all_columns`](#nocodbdb_viewshow_all_columns)
  * [`nocodb.db_view.update_by_id`](#nocodbdb_viewupdate_by_id)
  * [`nocodb.db_view.update_form_column`](#nocodbdb_viewupdate_form_column)
  * [`nocodb.db_view.update_form_view`](#nocodbdb_viewupdate_form_view)
  * [`nocodb.db_view.update_gallery_view_data`](#nocodbdb_viewupdate_gallery_view_data)
  * [`nocodb.db_view.update_grid_column_patch`](#nocodbdb_viewupdate_grid_column_patch)
  * [`nocodb.db_view.update_grid_view`](#nocodbdb_viewupdate_grid_view)
  * [`nocodb.db_view.update_kanban_view`](#nocodbdb_viewupdate_kanban_view)
  * [`nocodb.db_view.update_map_view_data`](#nocodbdb_viewupdate_map_view_data)
  * [`nocodb.db_view_column.create_new_column`](#nocodbdb_view_columncreate_new_column)
  * [`nocodb.db_view_column.list_by_view`](#nocodbdb_view_columnlist_by_view)
  * [`nocodb.db_view_column.update_column`](#nocodbdb_view_columnupdate_column)
  * [`nocodb.db_view_share.create_shared_view`](#nocodbdb_view_sharecreate_shared_view)
  * [`nocodb.db_view_share.delete_shared_view`](#nocodbdb_view_sharedelete_shared_view)
  * [`nocodb.db_view_share.list_shared_views`](#nocodbdb_view_sharelist_shared_views)
  * [`nocodb.db_view_share.update_shared_view`](#nocodbdb_view_shareupdate_shared_view)
  * [`nocodb.plugin.get_data_by_id`](#nocodbpluginget_data_by_id)
  * [`nocodb.plugin.get_status`](#nocodbpluginget_status)
  * [`nocodb.plugin.list_all_plugins`](#nocodbpluginlist_all_plugins)
  * [`nocodb.plugin.test_configuration_post`](#nocodbplugintest_configuration_post)
  * [`nocodb.plugin.update_by_id`](#nocodbpluginupdate_by_id)
  * [`nocodb.plugin.webhook_list_plugins`](#nocodbpluginwebhook_list_plugins)
  * [`nocodb.public.calendar_view_count_by_date`](#nocodbpubliccalendar_view_count_by_date)
  * [`nocodb.public.calendar_view_list_shared_rows`](#nocodbpubliccalendar_view_list_shared_rows)
  * [`nocodb.public.create_shared_view_row`](#nocodbpubliccreate_shared_view_row)
  * [`nocodb.public.list_nested_data`](#nocodbpubliclist_nested_data)
  * [`nocodb.public.list_shared_rows`](#nocodbpubliclist_shared_rows)
  * [`nocodb.public.list_shared_view_rows_group_by`](#nocodbpubliclist_shared_view_rows_group_by)
  * [`nocodb.public.nested_data_relation_list`](#nocodbpublicnested_data_relation_list)
  * [`nocodb.public.rows_export_type`](#nocodbpublicrows_export_type)
  * [`nocodb.public.shared_base_meta_get`](#nocodbpublicshared_base_meta_get)
  * [`nocodb.public.shared_erd_meta_get`](#nocodbpublicshared_erd_meta_get)
  * [`nocodb.public.shared_view_group_data_list`](#nocodbpublicshared_view_group_data_list)
  * [`nocodb.public.view_meta_get`](#nocodbpublicview_meta_get)
  * [`nocodb.source.base_id_sources_list`](#nocodbsourcebase_id_sources_list)
  * [`nocodb.source.create_erd_share`](#nocodbsourcecreate_erd_share)
  * [`nocodb.source.create_new_source`](#nocodbsourcecreate_new_source)
  * [`nocodb.source.create_sql_view`](#nocodbsourcecreate_sql_view)
  * [`nocodb.source.create_table`](#nocodbsourcecreate_table)
  * [`nocodb.source.delete_details`](#nocodbsourcedelete_details)
  * [`nocodb.source.delete_erd_share`](#nocodbsourcedelete_erd_share)
  * [`nocodb.source.get_details`](#nocodbsourceget_details)
  * [`nocodb.source.get_meta_diff`](#nocodbsourceget_meta_diff)
  * [`nocodb.source.get_tables`](#nocodbsourceget_tables)
  * [`nocodb.source.sync_meta_diff`](#nocodbsourcesync_meta_diff)
  * [`nocodb.source.update_details`](#nocodbsourceupdate_details)
  * [`nocodb.storage.upload_attachment`](#nocodbstorageupload_attachment)
  * [`nocodb.storage.upload_by_url`](#nocodbstorageupload_by_url)
  * [`nocodb.table_records.create_new_record`](#nocodbtable_recordscreate_new_record)
  * [`nocodb.table_records.delete_by_array`](#nocodbtable_recordsdelete_by_array)
  * [`nocodb.table_records.get_count`](#nocodbtable_recordsget_count)
  * [`nocodb.table_records.link_records_post`](#nocodbtable_recordslink_records_post)
  * [`nocodb.table_records.list`](#nocodbtable_recordslist)
  * [`nocodb.table_records.list_linked_records`](#nocodbtable_recordslist_linked_records)
  * [`nocodb.table_records.read_by_id`](#nocodbtable_recordsread_by_id)
  * [`nocodb.table_records.unlink_records`](#nocodbtable_recordsunlink_records)
  * [`nocodb.table_records.update_patch_table_records`](#nocodbtable_recordsupdate_patch_table_records)
  * [`nocodb.utils.clear_noco_cache`](#nocodbutilsclear_noco_cache)
  * [`nocodb.utils.count_comments`](#nocodbutilscount_comments)
  * [`nocodb.utils.create_new_comment_row`](#nocodbutilscreate_new_comment_row)
  * [`nocodb.utils.get_all_noco_cache`](#nocodbutilsget_all_noco_cache)
  * [`nocodb.utils.get_app_info`](#nocodbutilsget_app_info)
  * [`nocodb.utils.list_comments`](#nocodbutilslist_comments)
  * [`nocodb.utils.make_axios_request`](#nocodbutilsmake_axios_request)
  * [`nocodb.utils.select_connection_post`](#nocodbutilsselect_connection_post)
  * [`nocodb.utils.test_db_connection`](#nocodbutilstest_db_connection)
  * [`nocodb.utils.update_audit_comment`](#nocodbutilsupdate_audit_comment)
  * [`nocodb.utils.update_audit_row`](#nocodbutilsupdate_audit_row)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=NocoDB&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from noco_db_python_sdk import NocoDb, ApiException

nocodb = NocoDb(
)

try:
    # Create API Token
    create_in_base_response = nocodb.api_token.create_in_base(
        base_id="string",
        description="This API Token is for ABC application",
        xc_auth="string_example",
    )
    print(create_in_base_response)
except ApiException as e:
    print("Exception when calling APITokenApi.create_in_base: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["msg"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from noco_db_python_sdk import NocoDb, ApiException

nocodb = NocoDb(
)

async def main():
    try:
        # Create API Token
        create_in_base_response = await nocodb.api_token.acreate_in_base(
            base_id="string",
            description="This API Token is for ABC application",
            xc_auth="string_example",
        )
        print(create_in_base_response)
    except ApiException as e:
        print("Exception when calling APITokenApi.create_in_base: %s\n" % e)
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["msg"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from noco_db_python_sdk import NocoDb, ApiException

nocodb = NocoDb(
)

try:
    # Create API Token
    create_in_base_response = nocodb.api_token.raw.create_in_base(
        base_id="string",
        description="This API Token is for ABC application",
        xc_auth="string_example",
    )
    pprint(create_in_base_response.body)
    pprint(create_in_base_response.body["description"])
    pprint(create_in_base_response.body["id"])
    pprint(create_in_base_response.body["fk_user_id"])
    pprint(create_in_base_response.body["token"])
    pprint(create_in_base_response.headers)
    pprint(create_in_base_response.status)
    pprint(create_in_base_response.round_trip_time)
except ApiException as e:
    print("Exception when calling APITokenApi.create_in_base: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["msg"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `nocodb.api_token.create_in_base`<a id="nocodbapi_tokencreate_in_base"></a>

Create API Token in a base

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_in_base_response = nocodb.api_token.create_in_base(
    base_id="string",
    description="This API Token is for ABC application",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### description: `str`<a id="description-str"></a>

Description of the API token

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApiTokenReq`](./noco_db_python_sdk/type/api_token_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ApiToken`](./noco_db_python_sdk/pydantic/api_token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/api-tokens` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.api_token.delete_in_base`<a id="nocodbapi_tokendelete_in_base"></a>

Delete the given API Token in base

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_in_base_response = nocodb.api_token.delete_in_base(
    base_id="string",
    token="DYh540o8hbWpUGdarekECKLdN5OhlgCUWutVJYX2",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### token: `str`<a id="token-str"></a>

API Token

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/api-tokens/{token}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.api_token.list_in_base`<a id="nocodbapi_tokenlist_in_base"></a>

List API Tokens in the given base

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_in_base_response = nocodb.api_token.list_in_base(
    base_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`ApiTokenList`](./noco_db_python_sdk/pydantic/api_token_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/api-tokens` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.auth.add_base_user`<a id="nocodbauthadd_base_user"></a>

Create a user and add it to the given base

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_base_user_response = nocodb.auth.add_base_user(
    email="user@example.com",
    roles="owner",
    base_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

Base User Email

##### roles: `str`<a id="roles-str"></a>

Base User Role

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectUserReq`](./noco_db_python_sdk/type/project_user_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AuthAddBaseUserResponse`](./noco_db_python_sdk/pydantic/auth_add_base_user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/users` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.auth.delete_base_user`<a id="nocodbauthdelete_base_user"></a>

Delete a given user in a given base. Exclusive for Super Admin. Access with API Tokens will be blocked.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_base_user_response = nocodb.auth.delete_base_user(
    base_id="string",
    user_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### user_id: [`Id`](./noco_db_python_sdk/type/.py)<a id="user_id-idnoco_db_python_sdktypepy"></a>

Unique User ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`AuthDeleteBaseUserResponse`](./noco_db_python_sdk/pydantic/auth_delete_base_user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/users/{userId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.auth.list_base_users`<a id="nocodbauthlist_base_users"></a>

List all users in the given base.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_base_users_response = nocodb.auth.list_base_users(
    base_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`AuthListBaseUsersResponse`](./noco_db_python_sdk/pydantic/auth_list_base_users_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.auth.resend_invite_user`<a id="nocodbauthresend_invite_user"></a>

Resend Invitation to a specific user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
resend_invite_user_response = nocodb.auth.resend_invite_user(
    base_id="string",
    user_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### user_id: [`Id`](./noco_db_python_sdk/type/.py)<a id="user_id-idnoco_db_python_sdktypepy"></a>

Unique User ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`AuthResendInviteUserResponse`](./noco_db_python_sdk/pydantic/auth_resend_invite_user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/users/{userId}/resend-invite` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.auth.update_base_user`<a id="nocodbauthupdate_base_user"></a>

Update a given user in a given base. Exclusive for Super Admin. Access with API Tokens will be blocked.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_base_user_response = nocodb.auth.update_base_user(
    email="user@example.com",
    roles="owner",
    base_id="string",
    user_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

Base User Email

##### roles: `str`<a id="roles-str"></a>

Base User Role

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### user_id: [`Id`](./noco_db_python_sdk/type/.py)<a id="user_id-idnoco_db_python_sdktypepy"></a>

Unique User ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectUserReq`](./noco_db_python_sdk/type/project_user_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AuthUpdateBaseUserResponse`](./noco_db_python_sdk/pydantic/auth_update_base_user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/users/{userId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.base.calculate_cost`<a id="nocodbbasecalculate_cost"></a>

Calculate the Base Cost

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
calculate_cost_response = nocodb.base.calculate_cost(
    base_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/cost` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.base.check_empty_filters`<a id="nocodbbasecheck_empty_filters"></a>

Check if a base contains empty and null filters. Used in `Show NULL and EMPTY in Filter` in Base Setting.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_empty_filters_response = nocodb.base.check_empty_filters(
    base_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/has-empty-or-null-filters` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.base.create_new_base`<a id="nocodbbasecreate_new_base"></a>

Create a new base

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_base_response = nocodb.base.create_new_base(
    body=None,
    title="My Base",
    description="This is my base description",
    sources=[
        {
            "alias": "My Source",
            "inflection_column": "camelize",
            "inflection_table": "camelize",
            "is_meta": True,
            "type": "mysql",
        }
    ],
    color="#24716E",
    status=None,
    type="database",
    linked_db_project_ids=[
        "string_example"
    ],
    meta=None,
    external=False,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

Base Title

##### description: `str`<a id="description-str"></a>

Base Description

##### sources: List[`BaseReq`]<a id="sources-listbasereq"></a>

Array of Bases

##### color: `str`<a id="color-str"></a>

Primary Theme Color

##### status: `StringOrNull`<a id="status-stringornull"></a>

##### type: `str`<a id="type-str"></a>

##### linked_db_project_ids: [`ProjectReqLinkedDbProjectIds`](./noco_db_python_sdk/type/project_req_linked_db_project_ids.py)<a id="linked_db_project_ids-projectreqlinkeddbprojectidsnoco_db_python_sdktypeproject_req_linked_db_project_idspy"></a>

##### meta: `Meta`<a id="meta-meta"></a>

##### external: `bool`<a id="external-bool"></a>

If true, the base will us an external database else it will use the root database

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BaseCreateNewBaseRequest`](./noco_db_python_sdk/type/base_create_new_base_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Base`](./noco_db_python_sdk/pydantic/base.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.base.create_shared_base`<a id="nocodbbasecreate_shared_base"></a>

Create Base Shared Base

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_shared_base_response = nocodb.base.create_shared_base(
    base_id="string",
    password="password123",
    roles="editor",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### password: `str`<a id="password-str"></a>

Password to protect the base

##### roles: `str`<a id="roles-str"></a>

The role given the target user

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SharedBaseReq`](./noco_db_python_sdk/type/shared_base_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BaseCreateSharedBaseResponse`](./noco_db_python_sdk/pydantic/base_create_shared_base_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/shared` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.base.create_ui_acl`<a id="nocodbbasecreate_ui_acl"></a>

Hide / show views based on user role

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_ui_acl_response = nocodb.base.create_ui_acl(
    body=[{
}],
    base_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

##### requestBody: [`VisibilityRuleReq`](./noco_db_python_sdk/type/visibility_rule_req.py)<a id="requestbody-visibilityrulereqnoco_db_python_sdktypevisibility_rule_reqpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`BaseCreateUiAclResponse`](./noco_db_python_sdk/pydantic/base_create_ui_acl_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/visibility-rules` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.base.delete_shared_base`<a id="nocodbbasedelete_shared_base"></a>

Delete Base Shared Base

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_shared_base_response = nocodb.base.delete_shared_base(
    base_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/shared` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.base.duplicate_base_post`<a id="nocodbbaseduplicate_base_post"></a>

Duplicate a base

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
duplicate_base_post_response = nocodb.base.duplicate_base_post(
    base_id="string",
    options={
    },
    base={},
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### options: [`BaseDuplicateBasePostRequestOptions`](./noco_db_python_sdk/type/base_duplicate_base_post_request_options.py)<a id="options-baseduplicatebasepostrequestoptionsnoco_db_python_sdktypebase_duplicate_base_post_request_optionspy"></a>


##### base: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="base-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BaseDuplicateBasePostRequest`](./noco_db_python_sdk/type/base_duplicate_base_post_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BaseDuplicateBasePostResponse`](./noco_db_python_sdk/pydantic/base_duplicate_base_post_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/duplicate/{baseId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.base.duplicate_post`<a id="nocodbbaseduplicate_post"></a>

Duplicate a base

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
duplicate_post_response = nocodb.base.duplicate_post(
    base_id="string",
    options={
    },
    base={},
    xc_auth="string_example",
    source_id="string",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### options: [`BaseDuplicatePostRequestOptions`](./noco_db_python_sdk/type/base_duplicate_post_request_options.py)<a id="options-baseduplicatepostrequestoptionsnoco_db_python_sdktypebase_duplicate_post_request_optionspy"></a>


##### base: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="base-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

##### source_id: `Id`<a id="source_id-id"></a>

Unique Source ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BaseDuplicatePostRequest`](./noco_db_python_sdk/type/base_duplicate_post_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BaseDuplicatePostResponse`](./noco_db_python_sdk/pydantic/base_duplicate_post_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/duplicate/{baseId}/{sourceId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.base.get_info`<a id="nocodbbaseget_info"></a>

Get the info of a given base

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_info_response = nocodb.base.get_info(
    base_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`Base`](./noco_db_python_sdk/pydantic/base.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.base.get_info_by_id`<a id="nocodbbaseget_info_by_id"></a>

Get info such as node version, arch, platform, is docker, rootdb and package version of a given base

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_info_by_id_response = nocodb.base.get_info_by_id(
    base_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`BaseGetInfoByIdResponse`](./noco_db_python_sdk/pydantic/base_get_info_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/info` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.base.get_shared_base`<a id="nocodbbaseget_shared_base"></a>

Get Base Shared Base

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_shared_base_response = nocodb.base.get_shared_base(
    base_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`BaseGetSharedBaseResponse`](./noco_db_python_sdk/pydantic/base_get_shared_base_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/shared` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.base.get_ui_acl`<a id="nocodbbaseget_ui_acl"></a>

Hide / show views based on user role

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_ui_acl_response = nocodb.base.get_ui_acl(
    base_id="string",
    include_m2_m=True,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### include_m2_m: `bool`<a id="include_m2_m-bool"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`BaseGetUiAclResponse`](./noco_db_python_sdk/pydantic/base_get_ui_acl_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/visibility-rules` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.base.list_audits_in_base`<a id="nocodbbaselist_audits_in_base"></a>

List all audit data in the given base

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_audits_in_base_response = nocodb.base.list_audits_in_base(
    base_id="string",
    offset=0,
    limit=1,
    source_id="string_example",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### offset: `int`<a id="offset-int"></a>

##### limit: `int`<a id="limit-int"></a>

##### source_id: `str`<a id="source_id-str"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`BaseListAuditsInBaseResponse`](./noco_db_python_sdk/pydantic/base_list_audits_in_base_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/audits` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.base.list_bases`<a id="nocodbbaselist_bases"></a>

List all base meta data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_bases_response = nocodb.base.list_bases(
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectList`](./noco_db_python_sdk/pydantic/project_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.base.meta_diff_get`<a id="nocodbbasemeta_diff_get"></a>

Get the meta data difference between NC_DB and external data sources 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
meta_diff_get_response = nocodb.base.meta_diff_get(
    base_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`BaseMetaDiffGetResponse`](./noco_db_python_sdk/pydantic/base_meta_diff_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/meta-diff` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.base.remove_base`<a id="nocodbbaseremove_base"></a>

Delete the given base

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_base_response = nocodb.base.remove_base(
    base_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.base.sync_meta_diff`<a id="nocodbbasesync_meta_diff"></a>

Synchronise the meta data difference between NC_DB and external data sources 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sync_meta_diff_response = nocodb.base.sync_meta_diff(
    base_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`BaseSyncMetaDiffResponse`](./noco_db_python_sdk/pydantic/base_sync_meta_diff_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/meta-diff` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.base.update_base_meta`<a id="nocodbbaseupdate_base_meta"></a>

Update the given base

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_base_meta_response = nocodb.base.update_base_meta(
    base_id="string",
    title="My Base",
    color="#24716E",
    meta=None,
    status=None,
    linked_db_project_ids=[
        "string_example"
    ],
    order=1,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### title: `str`<a id="title-str"></a>

Base Title

##### color: `str`<a id="color-str"></a>

Primary Theme Color

##### meta: `Meta`<a id="meta-meta"></a>

##### status: `StringOrNull`<a id="status-stringornull"></a>

##### linked_db_project_ids: [`ProjectUpdateReqLinkedDbProjectIds`](./noco_db_python_sdk/type/project_update_req_linked_db_project_ids.py)<a id="linked_db_project_ids-projectupdatereqlinkeddbprojectidsnoco_db_python_sdktypeproject_update_req_linked_db_project_idspy"></a>

##### order: `Union[int, float]`<a id="order-unionint-float"></a>

The order of the list of projects.

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectUpdateReq`](./noco_db_python_sdk/type/project_update_req.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.base.update_meta_user`<a id="nocodbbaseupdate_meta_user"></a>

Base user meta update

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
nocodb.base.update_meta_user(
    base_id="baseId_example",
    starred=None,
    order=1,
    hidden=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `str`<a id="base_id-str"></a>

##### starred: `ModelBool`<a id="starred-modelbool"></a>

##### order: `Union[int, float]`<a id="order-unionint-float"></a>

The order among the bases

##### hidden: `ModelBool`<a id="hidden-modelbool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectUserMetaReq`](./noco_db_python_sdk/type/project_user_meta_req.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/user` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.base.update_shared_base`<a id="nocodbbaseupdate_shared_base"></a>

Update Base Shared Base

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_shared_base_response = nocodb.base.update_shared_base(
    base_id="string",
    password="password123",
    roles="editor",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### password: `str`<a id="password-str"></a>

Password to protect the base

##### roles: `str`<a id="roles-str"></a>

The role given the target user

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SharedBaseReq`](./noco_db_python_sdk/type/shared_base_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BaseUpdateSharedBaseResponse`](./noco_db_python_sdk/pydantic/base_update_shared_base_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/shared` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table.create_new_table`<a id="nocodbdb_tablecreate_new_table"></a>

Create a new table in a given base

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_table_response = nocodb.db_table.create_new_table(
    columns=[
        {
            "title": "string",
            "column_name": "string",
            "dt": "string",
            "uidt": "ID",
        }
    ],
    table_name="my_table",
    base_id="string",
    title="My Table",
    meta=None,
    order=1,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### columns: List[`NormalColumnRequest`]<a id="columns-listnormalcolumnrequest"></a>

The column models in this table

##### table_name: `str`<a id="table_name-str"></a>

Table name

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### title: `str`<a id="title-str"></a>

Table title

##### meta: `Meta`<a id="meta-meta"></a>

##### order: `Union[int, float]`<a id="order-unionint-float"></a>

The order of table list

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TableReq`](./noco_db_python_sdk/type/table_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Table`](./noco_db_python_sdk/pydantic/table.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/tables` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table.delete_by_table_id`<a id="nocodbdb_tabledelete_by_table_id"></a>

Delete the table meta data by the given table ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_by_table_id_response = nocodb.db_table.delete_by_table_id(
    table_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### table_id: `Id`<a id="table_id-id"></a>

Unique Table ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/tables/{tableId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table.duplicate_table_post`<a id="nocodbdb_tableduplicate_table_post"></a>

Duplicate a table

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
duplicate_table_post_response = nocodb.db_table.duplicate_table_post(
    base_id="string",
    table_id="string",
    options={
    },
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### table_id: `Id`<a id="table_id-id"></a>

Unique Table ID

##### options: [`DbTableDuplicateTablePostRequestOptions`](./noco_db_python_sdk/type/db_table_duplicate_table_post_request_options.py)<a id="options-dbtableduplicatetablepostrequestoptionsnoco_db_python_sdktypedb_table_duplicate_table_post_request_optionspy"></a>


##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DbTableDuplicateTablePostRequest`](./noco_db_python_sdk/type/db_table_duplicate_table_post_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DbTableDuplicateTablePostResponse`](./noco_db_python_sdk/pydantic/db_table_duplicate_table_post_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/duplicate/{baseId}/table/{tableId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table.list_tables`<a id="nocodbdb_tablelist_tables"></a>

List all tables in a given base

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_tables_response = nocodb.db_table.list_tables(
    base_id="string",
    xc_auth="string_example",
    page=3.14,
    page_size=3.14,
    sort="string_example",
    include_m2_m=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

##### page_size: `Union[int, float]`<a id="page_size-unionint-float"></a>

##### sort: `str`<a id="sort-str"></a>

##### include_m2_m: `bool`<a id="include_m2_m-bool"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TableList`](./noco_db_python_sdk/pydantic/table_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/tables` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table.read_by_table_id`<a id="nocodbdb_tableread_by_table_id"></a>

Read the table meta data by the given table ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
read_by_table_id_response = nocodb.db_table.read_by_table_id(
    table_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### table_id: `Id`<a id="table_id-id"></a>

Unique Table ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`Table`](./noco_db_python_sdk/pydantic/table.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/tables/{tableId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table.update_meta`<a id="nocodbdb_tableupdate_meta"></a>

Update the table meta data by the given table ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_meta_response = nocodb.db_table.update_meta(
    table_id="string",
    title="Users",
    table_name="users",
    base_id="p_124hhlkbeasewh",
    meta=None,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### table_id: `Id`<a id="table_id-id"></a>

Unique Table ID

##### title: `str`<a id="title-str"></a>

Table title

##### table_name: `str`<a id="table_name-str"></a>

Table name

##### base_id: `str`<a id="base_id-str"></a>

Base ID

##### meta: `Meta`<a id="meta-meta"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DbTableUpdateMetaRequest`](./noco_db_python_sdk/type/db_table_update_meta_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DbTableUpdateMetaResponse`](./noco_db_python_sdk/pydantic/db_table_update_meta_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/tables/{tableId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table.update_table_order`<a id="nocodbdb_tableupdate_table_order"></a>

Update the order of the given Table

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_table_order_response = nocodb.db_table.update_table_order(
    table_id="string",
    order=3.14,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### table_id: `Id`<a id="table_id-id"></a>

Unique Table ID

##### order: `Union[int, float]`<a id="order-unionint-float"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DbTableUpdateTableOrderRequest`](./noco_db_python_sdk/type/db_table_update_table_order_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/tables/{tableId}/reorder` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_column.bulk_create_update`<a id="nocodbdb_table_columnbulk_create_update"></a>

Bulk create-update-delete columns

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bulk_create_update_response = nocodb.db_table_column.bulk_create_update(
    table_id="string",
    hash="string_example",
    ops=[
        None
    ],
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### table_id: `Id`<a id="table_id-id"></a>

Unique Table ID

##### hash: `str`<a id="hash-str"></a>

Columns hash

##### ops: [`DbTableColumnBulkCreateUpdateRequestOps`](./noco_db_python_sdk/type/db_table_column_bulk_create_update_request_ops.py)<a id="ops-dbtablecolumnbulkcreateupdaterequestopsnoco_db_python_sdktypedb_table_column_bulk_create_update_request_opspy"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DbTableColumnBulkCreateUpdateRequest`](./noco_db_python_sdk/type/db_table_column_bulk_create_update_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DbTableColumnBulkCreateUpdateResponse`](./noco_db_python_sdk/pydantic/db_table_column_bulk_create_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/tables/{tableId}/columns/bulk` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_column.create_new_column`<a id="nocodbdb_table_columncreate_new_column"></a>

Create a new column in a given Table

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
nocodb.db_table_column.create_new_column(
    table_id="string",
    title="a",
    formula="CONCAT(\"FOO\", {{cl_c5knoi4xs4sfpt}})",
    formula_raw="CONCAT(\"FOO\", {Title})",
    uidt="Rollup",
    child_id="string",
    parent_id="string",
    type="hm",
    virtual=None,
    fk_lookup_column_id="string",
    fk_relation_column_id="string",
    ai=None,
    au=None,
    cc=None,
    cdf=None,
    column_name="string_example",
    csn=None,
    dt="string",
    dtx=None,
    dtxp=None,
    dtxs=None,
    np=None,
    ns=None,
    pk=None,
    pv=None,
    rqd=None,
    un=None,
    unique=None,
    fk_rollup_column_id="string",
    rollup_function="avg",
    column_order={
    },
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### table_id: `Id`<a id="table_id-id"></a>

Unique Table ID

##### title: `str`<a id="title-str"></a>

##### formula: `str`<a id="formula-str"></a>

Formula with column ID replaced

##### formula_raw: `str`<a id="formula_raw-str"></a>

Original Formula inputted in UI

##### uidt: `str`<a id="uidt-str"></a>

UI DataType

##### child_id: [`Id`](./noco_db_python_sdk/type/id.py)<a id="child_id-idnoco_db_python_sdktypeidpy"></a>

##### parent_id: [`Id`](./noco_db_python_sdk/type/id.py)<a id="parent_id-idnoco_db_python_sdktypeidpy"></a>

##### type: `str`<a id="type-str"></a>

The type of the relationship

##### virtual: `ModelBool`<a id="virtual-modelbool"></a>

##### fk_lookup_column_id: [`Id`](./noco_db_python_sdk/type/id.py)<a id="fk_lookup_column_id-idnoco_db_python_sdktypeidpy"></a>

##### fk_relation_column_id: [`Id`](./noco_db_python_sdk/type/id.py)<a id="fk_relation_column_id-idnoco_db_python_sdktypeidpy"></a>

##### ai: `ModelBool`<a id="ai-modelbool"></a>

##### au: `ModelBool`<a id="au-modelbool"></a>

##### cc: `StringOrNull`<a id="cc-stringornull"></a>

##### cdf: `StringOrNullOrBooleanOrNumber`<a id="cdf-stringornullorbooleanornumber"></a>

##### column_name: `str`<a id="column_name-str"></a>

##### csn: `StringOrNull`<a id="csn-stringornull"></a>

##### dt: `str`<a id="dt-str"></a>

Data Type

##### dtx: `StringOrNull`<a id="dtx-stringornull"></a>

##### dtxp: Union[`str`, `Union[int, float]`, `none_type`]<a id="dtxp-unionstr-unionint-float-none_type"></a>


Data Type Extra Precision

##### dtxs: Union[`StringOrNull`, `Union[int, float]`]<a id="dtxs-unionstringornull-unionint-float"></a>


Data Type Extra Scale

##### np: Union[`StringOrNull`, `int`]<a id="np-unionstringornull-int"></a>


Numeric Precision

##### ns: Union[`StringOrNull`, `int`]<a id="ns-unionstringornull-int"></a>


Numeric Scale

##### pk: `ModelBool`<a id="pk-modelbool"></a>

##### pv: `ModelBool`<a id="pv-modelbool"></a>

##### rqd: `ModelBool`<a id="rqd-modelbool"></a>

##### un: `ModelBool`<a id="un-modelbool"></a>

##### unique: `ModelBool`<a id="unique-modelbool"></a>

##### fk_rollup_column_id: [`Id`](./noco_db_python_sdk/type/id.py)<a id="fk_rollup_column_id-idnoco_db_python_sdktypeidpy"></a>

##### rollup_function: `str`<a id="rollup_function-str"></a>

Rollup Function

##### column_order: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./noco_db_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="column_order-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


Column order in a specific view

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ColumnReq`](./noco_db_python_sdk/type/column_req.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/tables/{tableId}/columns` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_column.delete_by_column_id`<a id="nocodbdb_table_columndelete_by_column_id"></a>

Delete the existing column by the given column ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
nocodb.db_table_column.delete_by_column_id(
    column_id="columnId_example",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### column_id: `str`<a id="column_id-str"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/columns/{columnId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_column.get_column_by_id`<a id="nocodbdb_table_columnget_column_by_id"></a>

Get the existing column by the given column ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
nocodb.db_table_column.get_column_by_id(
    column_id="columnId_example",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### column_id: `str`<a id="column_id-str"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/columns/{columnId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_column.get_table_columns_hash`<a id="nocodbdb_table_columnget_table_columns_hash"></a>

Get columns hash for table

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_table_columns_hash_response = nocodb.db_table_column.get_table_columns_hash(
    table_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### table_id: `Id`<a id="table_id-id"></a>

Unique Table ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`DbTableColumnGetTableColumnsHashResponse`](./noco_db_python_sdk/pydantic/db_table_column_get_table_columns_hash_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/tables/{tableId}/columns/hash` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_column.set_primary_value`<a id="nocodbdb_table_columnset_primary_value"></a>

Set a primary value on a given column

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
set_primary_value_response = nocodb.db_table_column.set_primary_value(
    column_id="columnId_example",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### column_id: `str`<a id="column_id-str"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/columns/{columnId}/primary` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_column.update_by_column_id`<a id="nocodbdb_table_columnupdate_by_column_id"></a>

Update the existing column by the given column ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_column_id_response = nocodb.db_table_column.update_by_column_id(
    column_id="columnId_example",
    title="a",
    formula="CONCAT(\"FOO\", {{cl_c5knoi4xs4sfpt}})",
    formula_raw="CONCAT(\"FOO\", {Title})",
    uidt="Rollup",
    child_id="string",
    parent_id="string",
    type="hm",
    virtual=None,
    fk_lookup_column_id="string",
    fk_relation_column_id="string",
    ai=None,
    au=None,
    cc=None,
    cdf=None,
    column_name="string_example",
    csn=None,
    dt="string",
    dtx=None,
    dtxp=None,
    dtxs=None,
    np=None,
    ns=None,
    pk=None,
    pv=None,
    rqd=None,
    un=None,
    unique=None,
    fk_rollup_column_id="string",
    rollup_function="avg",
    column_order={
    },
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### column_id: `str`<a id="column_id-str"></a>

##### title: `str`<a id="title-str"></a>

##### formula: `str`<a id="formula-str"></a>

Formula with column ID replaced

##### formula_raw: `str`<a id="formula_raw-str"></a>

Original Formula inputted in UI

##### uidt: `str`<a id="uidt-str"></a>

UI DataType

##### child_id: [`Id`](./noco_db_python_sdk/type/id.py)<a id="child_id-idnoco_db_python_sdktypeidpy"></a>

##### parent_id: [`Id`](./noco_db_python_sdk/type/id.py)<a id="parent_id-idnoco_db_python_sdktypeidpy"></a>

##### type: `str`<a id="type-str"></a>

The type of the relationship

##### virtual: `ModelBool`<a id="virtual-modelbool"></a>

##### fk_lookup_column_id: [`Id`](./noco_db_python_sdk/type/id.py)<a id="fk_lookup_column_id-idnoco_db_python_sdktypeidpy"></a>

##### fk_relation_column_id: [`Id`](./noco_db_python_sdk/type/id.py)<a id="fk_relation_column_id-idnoco_db_python_sdktypeidpy"></a>

##### ai: `ModelBool`<a id="ai-modelbool"></a>

##### au: `ModelBool`<a id="au-modelbool"></a>

##### cc: `StringOrNull`<a id="cc-stringornull"></a>

##### cdf: `StringOrNullOrBooleanOrNumber`<a id="cdf-stringornullorbooleanornumber"></a>

##### column_name: `str`<a id="column_name-str"></a>

##### csn: `StringOrNull`<a id="csn-stringornull"></a>

##### dt: `str`<a id="dt-str"></a>

Data Type

##### dtx: `StringOrNull`<a id="dtx-stringornull"></a>

##### dtxp: Union[`str`, `Union[int, float]`, `none_type`]<a id="dtxp-unionstr-unionint-float-none_type"></a>


Data Type Extra Precision

##### dtxs: Union[`StringOrNull`, `Union[int, float]`]<a id="dtxs-unionstringornull-unionint-float"></a>


Data Type Extra Scale

##### np: Union[`StringOrNull`, `int`]<a id="np-unionstringornull-int"></a>


Numeric Precision

##### ns: Union[`StringOrNull`, `int`]<a id="ns-unionstringornull-int"></a>


Numeric Scale

##### pk: `ModelBool`<a id="pk-modelbool"></a>

##### pv: `ModelBool`<a id="pv-modelbool"></a>

##### rqd: `ModelBool`<a id="rqd-modelbool"></a>

##### un: `ModelBool`<a id="un-modelbool"></a>

##### unique: `ModelBool`<a id="unique-modelbool"></a>

##### fk_rollup_column_id: [`Id`](./noco_db_python_sdk/type/id.py)<a id="fk_rollup_column_id-idnoco_db_python_sdktypeidpy"></a>

##### rollup_function: `str`<a id="rollup_function-str"></a>

Rollup Function

##### column_order: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./noco_db_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="column_order-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


Column order in a specific view

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ColumnReq`](./noco_db_python_sdk/type/column_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Column`](./noco_db_python_sdk/pydantic/column.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/columns/{columnId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_filter.create_view_filter`<a id="nocodbdb_table_filtercreate_view_filter"></a>

Update the filter data in a given View

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_view_filter_response = nocodb.db_table_filter.create_view_filter(
    view_id="vw_wtdg2meyig5l4q",
    comparison_op="eq",
    comparison_sub_op="daysAgo",
    fk_column_id=None,
    fk_parent_id=None,
    is_group=None,
    logical_op="and",
    value=None,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### view_id: `str`<a id="view_id-str"></a>

Unique View ID

##### comparison_op: `Optional[str]`<a id="comparison_op-optionalstr"></a>

Comparison Operator

##### comparison_sub_op: `Optional[str]`<a id="comparison_sub_op-optionalstr"></a>

Comparison Sub-Operator

##### fk_column_id: `StringOrNull`<a id="fk_column_id-stringornull"></a>

##### fk_parent_id: `StringOrNull`<a id="fk_parent_id-stringornull"></a>

##### is_group: `ModelBool`<a id="is_group-modelbool"></a>

##### logical_op: `str`<a id="logical_op-str"></a>

Logical Operator

##### value: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./noco_db_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="value-unionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

The filter value. Can be NULL for some operators.

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FilterReq`](./noco_db_python_sdk/type/filter_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Filter`](./noco_db_python_sdk/pydantic/filter.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/views/{viewId}/filters` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_filter.delete_by_id`<a id="nocodbdb_table_filterdelete_by_id"></a>

Delete the filter data with a given Filter ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_by_id_response = nocodb.db_table_filter.delete_by_id(
    filter_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filter_id: [`Id`](./noco_db_python_sdk/type/.py)<a id="filter_id-idnoco_db_python_sdktypepy"></a>

Unique Filter ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/filters/{filterId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_filter.get_by_id`<a id="nocodbdb_table_filterget_by_id"></a>

Get the filter data with a given Filter ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = nocodb.db_table_filter.get_by_id(
    filter_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filter_id: [`Id`](./noco_db_python_sdk/type/.py)<a id="filter_id-idnoco_db_python_sdktypepy"></a>

Unique Filter ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`Filter`](./noco_db_python_sdk/pydantic/filter.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/filters/{filterId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_filter.get_children`<a id="nocodbdb_table_filterget_children"></a>

Get Filter Group Children of a given group ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_children_response = nocodb.db_table_filter.get_children(
    filter_group_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filter_group_id: [`Id`](./noco_db_python_sdk/type/.py)<a id="filter_group_id-idnoco_db_python_sdktypepy"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`FilterList`](./noco_db_python_sdk/pydantic/filter_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/filters/{filterGroupId}/children` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_filter.get_view_data`<a id="nocodbdb_table_filterget_view_data"></a>

Get the filter data in a given View

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_view_data_response = nocodb.db_table_filter.get_view_data(
    view_id="vw_wtdg2meyig5l4q",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### view_id: `str`<a id="view_id-str"></a>

Unique View ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`FilterList`](./noco_db_python_sdk/pydantic/filter_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/views/{viewId}/filters` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_filter.update_by_id`<a id="nocodbdb_table_filterupdate_by_id"></a>

Update the filter data with a given Filter ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = nocodb.db_table_filter.update_by_id(
    filter_id="string",
    comparison_op="eq",
    comparison_sub_op="daysAgo",
    fk_column_id=None,
    fk_parent_id=None,
    is_group=None,
    logical_op="and",
    value=None,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filter_id: [`Id`](./noco_db_python_sdk/type/.py)<a id="filter_id-idnoco_db_python_sdktypepy"></a>

Unique Filter ID

##### comparison_op: `Optional[str]`<a id="comparison_op-optionalstr"></a>

Comparison Operator

##### comparison_sub_op: `Optional[str]`<a id="comparison_sub_op-optionalstr"></a>

Comparison Sub-Operator

##### fk_column_id: `StringOrNull`<a id="fk_column_id-stringornull"></a>

##### fk_parent_id: `StringOrNull`<a id="fk_parent_id-stringornull"></a>

##### is_group: `ModelBool`<a id="is_group-modelbool"></a>

##### logical_op: `str`<a id="logical_op-str"></a>

Logical Operator

##### value: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./noco_db_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="value-unionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

The filter value. Can be NULL for some operators.

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FilterReq`](./noco_db_python_sdk/type/filter_req.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/filters/{filterId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_sort.delete_by_id`<a id="nocodbdb_table_sortdelete_by_id"></a>

Delete the sort data by Sort ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_by_id_response = nocodb.db_table_sort.delete_by_id(
    sort_id="so_xd4t51uv60ghzl",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sort_id: `str`<a id="sort_id-str"></a>

Unique Sort ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/sorts/{sortId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_sort.get_all_sorts`<a id="nocodbdb_table_sortget_all_sorts"></a>

List all the sort data in a given View

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_sorts_response = nocodb.db_table_sort.get_all_sorts(
    view_id="vw_wtdg2meyig5l4q",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### view_id: `str`<a id="view_id-str"></a>

Unique View ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`SortList`](./noco_db_python_sdk/pydantic/sort_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/views/{viewId}/sorts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_sort.get_sort_by_id`<a id="nocodbdb_table_sortget_sort_by_id"></a>

Get the sort data by Sort ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_sort_by_id_response = nocodb.db_table_sort.get_sort_by_id(
    sort_id="so_xd4t51uv60ghzl",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sort_id: `str`<a id="sort_id-str"></a>

Unique Sort ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`Sort`](./noco_db_python_sdk/pydantic/sort.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/sorts/{sortId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_sort.update_sort_by_id`<a id="nocodbdb_table_sortupdate_sort_by_id"></a>

Update the sort data by Sort ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_sort_by_id_response = nocodb.db_table_sort.update_sort_by_id(
    sort_id="so_xd4t51uv60ghzl",
    fk_column_id="string",
    direction="asc",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sort_id: `str`<a id="sort_id-str"></a>

Unique Sort ID

##### fk_column_id: [`Id`](./noco_db_python_sdk/type/id.py)<a id="fk_column_id-idnoco_db_python_sdktypeidpy"></a>

##### direction: `str`<a id="direction-str"></a>

Sort direction

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SortReq`](./noco_db_python_sdk/type/sort_req.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/sorts/{sortId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_sort.update_view_sort`<a id="nocodbdb_table_sortupdate_view_sort"></a>

Update the sort data in a given View

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_view_sort_response = nocodb.db_table_sort.update_view_sort(
    body=None,
    view_id="vw_wtdg2meyig5l4q",
    fk_column_id="string",
    direction="asc",
    push_to_top=True,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### view_id: `str`<a id="view_id-str"></a>

Unique View ID

##### fk_column_id: [`Id`](./noco_db_python_sdk/type/id.py)<a id="fk_column_id-idnoco_db_python_sdktypeidpy"></a>

##### direction: `str`<a id="direction-str"></a>

Sort direction

##### push_to_top: `bool`<a id="push_to_top-bool"></a>

Push the sort to the top of the list

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DbTableSortUpdateViewSortRequest`](./noco_db_python_sdk/type/db_table_sort_update_view_sort_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/views/{viewId}/sorts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_webhook.create_hook`<a id="nocodbdb_table_webhookcreate_hook"></a>

Create a hook in the given table

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_hook_response = nocodb.db_table_webhook.create_hook(
    title="My Webhook",
    event="after",
    notification=None,
    operation="insert",
    table_id="string",
    description=None,
    active=None,
    _async=None,
    env="all",
    fk_model_id="md_rsu68aqjsbyqtl",
    id="string",
    retries=10,
    retry_interval=60000,
    timeout=60000,
    type=None,
    condition=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

Hook Title

##### event: `str`<a id="event-str"></a>

Event Type for the operation

##### notification: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./noco_db_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="notification-unionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Hook Notification including info such as type, payload, method, body, and etc

##### operation: `str`<a id="operation-str"></a>

Hook Operation

##### table_id: `Id`<a id="table_id-id"></a>

Unique Table ID

##### description: `StringOrNull`<a id="description-stringornull"></a>

##### active: `ModelBool`<a id="active-modelbool"></a>

##### _async: `ModelBool`<a id="_async-modelbool"></a>

##### env: `str`<a id="env-str"></a>

Environment for the hook

##### fk_model_id: `str`<a id="fk_model_id-str"></a>

Foreign Key to Model

##### id: [`Id`](./noco_db_python_sdk/type/id.py)<a id="id-idnoco_db_python_sdktypeidpy"></a>

##### retries: `Union[int, float]`<a id="retries-unionint-float"></a>

Retry Count

##### retry_interval: `Union[int, float]`<a id="retry_interval-unionint-float"></a>

Retry Interval

##### timeout: `Union[int, float]`<a id="timeout-unionint-float"></a>

Timeout

##### type: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./noco_db_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="type-unionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Hook Type

##### condition: `ModelBool`<a id="condition-modelbool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`HookReq`](./noco_db_python_sdk/type/hook_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Hook`](./noco_db_python_sdk/pydantic/hook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/tables/{tableId}/hooks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_webhook.delete_by_id`<a id="nocodbdb_table_webhookdelete_by_id"></a>

Delete the exsiting hook by its ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_by_id_response = nocodb.db_table_webhook.delete_by_id(
    hook_id="hk_0063k4o1frnxbr",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### hook_id: `str`<a id="hook_id-str"></a>

Unique Hook ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/hooks/{hookId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_webhook.get_sample_payload`<a id="nocodbdb_table_webhookget_sample_payload"></a>

Get the sample hook payload

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_sample_payload_response = nocodb.db_table_webhook.get_sample_payload(
    table_id="string",
    operation="insert",
    version="v1",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### table_id: `Id`<a id="table_id-id"></a>

Unique Table ID

##### operation: `str`<a id="operation-str"></a>

Hook Operation

##### version: `str`<a id="version-str"></a>

Hook Version

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`DbTableWebhookGetSamplePayloadResponse`](./noco_db_python_sdk/pydantic/db_table_webhook_get_sample_payload_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/tables/{tableId}/hooks/samplePayload/{operation}/{version}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_webhook.list_table_hooks`<a id="nocodbdb_table_webhooklist_table_hooks"></a>

List all hook records in the given Table

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_table_hooks_response = nocodb.db_table_webhook.list_table_hooks(
    table_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### table_id: `Id`<a id="table_id-id"></a>

Unique Table ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`HookList`](./noco_db_python_sdk/pydantic/hook_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/tables/{tableId}/hooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_webhook.test_hook_create`<a id="nocodbdb_table_webhooktest_hook_create"></a>

Test the hook in the given Table

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
test_hook_create_response = nocodb.db_table_webhook.test_hook_create(
    hook={
        "title": "My Webhook",
        "env": "all",
        "event": "after",
        "fk_model_id": "md_rsu68aqjsbyqtl",
        "id": "string",
        "notification": None,
        "operation": "insert",
        "retries": 10,
        "retry_interval": 60000,
        "timeout": 60000,
    },
    payload=None,
    table_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### hook: [`HookReq`](./noco_db_python_sdk/type/hook_req.py)<a id="hook-hookreqnoco_db_python_sdktypehook_reqpy"></a>


##### payload: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./noco_db_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="payload-unionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Payload to be sent

##### table_id: `Id`<a id="table_id-id"></a>

Unique Table ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`HookTestReq`](./noco_db_python_sdk/type/hook_test_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DbTableWebhookTestHookCreateResponse`](./noco_db_python_sdk/pydantic/db_table_webhook_test_hook_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/tables/{tableId}/hooks/test` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_webhook.update_by_id`<a id="nocodbdb_table_webhookupdate_by_id"></a>

Update the exsiting hook by its ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = nocodb.db_table_webhook.update_by_id(
    hook_id="hk_0063k4o1frnxbr",
    title="My Webhook",
    description="This is my hook description",
    version="v2",
    active=None,
    _async=None,
    env="all",
    event="after",
    fk_model_id="md_rsu68aqjsbyqtl",
    id="string",
    notification=None,
    operation="insert",
    retries=10,
    retry_interval=60000,
    timeout=60000,
    type="string_example",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### hook_id: `str`<a id="hook_id-str"></a>

Unique Hook ID

##### title: `str`<a id="title-str"></a>

Hook Title

##### description: `str`<a id="description-str"></a>

Hook Description

##### version: `str`<a id="version-str"></a>

Hook Version

##### active: `ModelBool`<a id="active-modelbool"></a>

##### _async: `ModelBool`<a id="_async-modelbool"></a>

##### env: `str`<a id="env-str"></a>

Environment for the hook

##### event: `str`<a id="event-str"></a>

Event Type for the operation

##### fk_model_id: `str`<a id="fk_model_id-str"></a>

Foreign Key to Model

##### id: [`Id`](./noco_db_python_sdk/type/id.py)<a id="id-idnoco_db_python_sdktypeidpy"></a>

##### notification: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./noco_db_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="notification-unionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Hook Notification including info such as type, payload, method, body, and etc

##### operation: `str`<a id="operation-str"></a>

Hook Operation

##### retries: `Union[int, float]`<a id="retries-unionint-float"></a>

Retry Count

##### retry_interval: `Union[int, float]`<a id="retry_interval-unionint-float"></a>

Retry Interval

##### timeout: `Union[int, float]`<a id="timeout-unionint-float"></a>

Timeout

##### type: `str`<a id="type-str"></a>

Hook Type

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Hook`](./noco_db_python_sdk/type/hook.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Hook`](./noco_db_python_sdk/pydantic/hook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/hooks/{hookId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_webhook_filter.create_new_filter`<a id="nocodbdb_table_webhook_filtercreate_new_filter"></a>

Create filter(s) in a given Hook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_filter_response = nocodb.db_table_webhook_filter.create_new_filter(
    hook_id="string",
    comparison_op="eq",
    comparison_sub_op="daysAgo",
    fk_column_id=None,
    fk_parent_id=None,
    is_group=None,
    logical_op="and",
    value=None,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### hook_id: [`Id`](./noco_db_python_sdk/type/.py)<a id="hook_id-idnoco_db_python_sdktypepy"></a>

Unique Hook ID

##### comparison_op: `Optional[str]`<a id="comparison_op-optionalstr"></a>

Comparison Operator

##### comparison_sub_op: `Optional[str]`<a id="comparison_sub_op-optionalstr"></a>

Comparison Sub-Operator

##### fk_column_id: `StringOrNull`<a id="fk_column_id-stringornull"></a>

##### fk_parent_id: `StringOrNull`<a id="fk_parent_id-stringornull"></a>

##### is_group: `ModelBool`<a id="is_group-modelbool"></a>

##### logical_op: `str`<a id="logical_op-str"></a>

Logical Operator

##### value: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./noco_db_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="value-unionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

The filter value. Can be NULL for some operators.

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FilterReq`](./noco_db_python_sdk/type/filter_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Filter`](./noco_db_python_sdk/pydantic/filter.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/hooks/{hookId}/filters` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_webhook_filter.get_hook_filter`<a id="nocodbdb_table_webhook_filterget_hook_filter"></a>

Get the filter data in a given Hook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_hook_filter_response = nocodb.db_table_webhook_filter.get_hook_filter(
    hook_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### hook_id: [`Id`](./noco_db_python_sdk/type/.py)<a id="hook_id-idnoco_db_python_sdktypepy"></a>

Unique Hook ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`FilterList`](./noco_db_python_sdk/pydantic/filter_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/hooks/{hookId}/filters` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_table_webhook_logs.list`<a id="nocodbdb_table_webhook_logslist"></a>

List the log data in a given Hook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = nocodb.db_table_webhook_logs.list(
    hook_id="string",
    limit=1,
    offset=0,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### hook_id: [`Id`](./noco_db_python_sdk/type/.py)<a id="hook_id-idnoco_db_python_sdktypepy"></a>

Unique Hook ID

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`HookLogList`](./noco_db_python_sdk/pydantic/hook_log_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/hooks/{hookId}/logs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view.create_form_view`<a id="nocodbdb_viewcreate_form_view"></a>

Create a new form view in a given Table

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_form_view_response = nocodb.db_view.create_form_view(
    title="My View",
    table_id="string",
    type=3,
    copy_from_id=None,
    fk_grp_col_id=None,
    fk_geo_data_col_id=None,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

View Title

##### table_id: `Id`<a id="table_id-id"></a>

Unique Table ID

##### type: `Union[int, float]`<a id="type-unionint-float"></a>

View Type

##### copy_from_id: `StringOrNull`<a id="copy_from_id-stringornull"></a>

##### fk_grp_col_id: `StringOrNull`<a id="fk_grp_col_id-stringornull"></a>

##### fk_geo_data_col_id: `StringOrNull`<a id="fk_geo_data_col_id-stringornull"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ViewCreateReq`](./noco_db_python_sdk/type/view_create_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`View`](./noco_db_python_sdk/pydantic/view.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/tables/{tableId}/forms` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view.create_gallery_view`<a id="nocodbdb_viewcreate_gallery_view"></a>

Create Gallery View

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_gallery_view_response = nocodb.db_view.create_gallery_view(
    title="My View",
    table_id="string",
    type=3,
    copy_from_id=None,
    fk_grp_col_id=None,
    fk_geo_data_col_id=None,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

View Title

##### table_id: [`Id`](./noco_db_python_sdk/type/.py)<a id="table_id-idnoco_db_python_sdktypepy"></a>

Unique Table ID

##### type: `Union[int, float]`<a id="type-unionint-float"></a>

View Type

##### copy_from_id: `StringOrNull`<a id="copy_from_id-stringornull"></a>

##### fk_grp_col_id: `StringOrNull`<a id="fk_grp_col_id-stringornull"></a>

##### fk_geo_data_col_id: `StringOrNull`<a id="fk_geo_data_col_id-stringornull"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ViewCreateReq`](./noco_db_python_sdk/type/view_create_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`View`](./noco_db_python_sdk/pydantic/view.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/tables/{tableId}/galleries` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view.create_grid_view`<a id="nocodbdb_viewcreate_grid_view"></a>

Create a new grid view in a given Table

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_grid_view_response = nocodb.db_view.create_grid_view(
    title="My View",
    table_id="string",
    type=3,
    copy_from_id=None,
    fk_grp_col_id=None,
    fk_geo_data_col_id=None,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

View Title

##### table_id: `Id`<a id="table_id-id"></a>

Unique Table ID

##### type: `Union[int, float]`<a id="type-unionint-float"></a>

View Type

##### copy_from_id: `StringOrNull`<a id="copy_from_id-stringornull"></a>

##### fk_grp_col_id: `StringOrNull`<a id="fk_grp_col_id-stringornull"></a>

##### fk_geo_data_col_id: `StringOrNull`<a id="fk_geo_data_col_id-stringornull"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ViewCreateReq`](./noco_db_python_sdk/type/view_create_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`View`](./noco_db_python_sdk/pydantic/view.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/tables/{tableId}/grids` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view.create_kanban_view`<a id="nocodbdb_viewcreate_kanban_view"></a>

Create a new Kanban View

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_kanban_view_response = nocodb.db_view.create_kanban_view(
    title="My View",
    table_id="string",
    type=3,
    copy_from_id=None,
    fk_grp_col_id=None,
    fk_geo_data_col_id=None,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

View Title

##### table_id: `Id`<a id="table_id-id"></a>

Unique Table ID

##### type: `Union[int, float]`<a id="type-unionint-float"></a>

View Type

##### copy_from_id: `StringOrNull`<a id="copy_from_id-stringornull"></a>

##### fk_grp_col_id: `StringOrNull`<a id="fk_grp_col_id-stringornull"></a>

##### fk_geo_data_col_id: `StringOrNull`<a id="fk_geo_data_col_id-stringornull"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ViewCreateReq`](./noco_db_python_sdk/type/view_create_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`View`](./noco_db_python_sdk/pydantic/view.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/tables/{tableId}/kanbans` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view.create_map_view`<a id="nocodbdb_viewcreate_map_view"></a>

Create a new Map View

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_map_view_response = nocodb.db_view.create_map_view(
    title="My View",
    table_id="string",
    type=3,
    copy_from_id=None,
    fk_grp_col_id=None,
    fk_geo_data_col_id=None,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

View Title

##### table_id: `Id`<a id="table_id-id"></a>

Unique Table ID

##### type: `Union[int, float]`<a id="type-unionint-float"></a>

View Type

##### copy_from_id: `StringOrNull`<a id="copy_from_id-stringornull"></a>

##### fk_grp_col_id: `StringOrNull`<a id="fk_grp_col_id-stringornull"></a>

##### fk_geo_data_col_id: `StringOrNull`<a id="fk_geo_data_col_id-stringornull"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ViewCreateReq`](./noco_db_python_sdk/type/view_create_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`View`](./noco_db_python_sdk/pydantic/view.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/tables/{tableId}/maps` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view.delete_view_by_id`<a id="nocodbdb_viewdelete_view_by_id"></a>

Delete the view with the given view Id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_view_by_id_response = nocodb.db_view.delete_view_by_id(
    view_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### view_id: [`Id`](./noco_db_python_sdk/type/.py)<a id="view_id-idnoco_db_python_sdktypepy"></a>

Unique View ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/views/{viewId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view.get_form_by_id`<a id="nocodbdb_viewget_form_by_id"></a>

Get the form data by Form ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_form_by_id_response = nocodb.db_view.get_form_by_id(
    form_view_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### form_view_id: [`Id`](./noco_db_python_sdk/type/.py)<a id="form_view_id-idnoco_db_python_sdktypepy"></a>

Unique Form View ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`Form`](./noco_db_python_sdk/pydantic/form.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/forms/{formViewId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view.get_gallery_view`<a id="nocodbdb_viewget_gallery_view"></a>

Get the Gallery View data with Gallery ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_gallery_view_response = nocodb.db_view.get_gallery_view(
    gallery_view_id="vw_1eq2wk2xe3a9j5",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### gallery_view_id: `str`<a id="gallery_view_id-str"></a>

Unique Gallery View ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`Gallery`](./noco_db_python_sdk/pydantic/gallery.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/galleries/{galleryViewId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view.get_map_view_by_id`<a id="nocodbdb_viewget_map_view_by_id"></a>

Get the Map View data by Map ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_map_view_by_id_response = nocodb.db_view.get_map_view_by_id(
    map_view_id="vw_1eq2wk2xe3a9j5",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### map_view_id: `str`<a id="map_view_id-str"></a>

Unique Map View ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`Map`](./noco_db_python_sdk/pydantic/map.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/maps/{mapViewId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view.hide_all_columns`<a id="nocodbdb_viewhide_all_columns"></a>

Hide All Columns in a given View

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hide_all_columns_response = nocodb.db_view.hide_all_columns(
    view_id="string",
    ignore_ids=[
        None
    ],
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### view_id: [`Id`](./noco_db_python_sdk/type/.py)<a id="view_id-idnoco_db_python_sdktypepy"></a>

Unique View ID

##### ignore_ids: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./noco_db_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="ignore_ids-listunionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/views/{viewId}/hide-all` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view.kanban_view_get`<a id="nocodbdb_viewkanban_view_get"></a>

Get the Kanban View data by Kanban ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
kanban_view_get_response = nocodb.db_view.kanban_view_get(
    kanban_view_id="vw_1eq2wk2xe3a9j5",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### kanban_view_id: `str`<a id="kanban_view_id-str"></a>

Unique Kanban View ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`Kanban`](./noco_db_python_sdk/pydantic/kanban.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/kanbans/{kanbanViewId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view.list_grid_columns`<a id="nocodbdb_viewlist_grid_columns"></a>

List all columns in the given Grid

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_grid_columns_response = nocodb.db_view.list_grid_columns(
    grid_id="vw_q6k13mmygdi3yz",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### grid_id: `str`<a id="grid_id-str"></a>

Grid View ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`DbViewListGridColumnsResponse`](./noco_db_python_sdk/pydantic/db_view_list_grid_columns_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/grids/{gridId}/grid-columns` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view.list_table_views`<a id="nocodbdb_viewlist_table_views"></a>

List all views in a given Table.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_table_views_response = nocodb.db_view.list_table_views(
    table_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### table_id: `Id`<a id="table_id-id"></a>

Unique Table ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`ViewList`](./noco_db_python_sdk/pydantic/view_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/tables/{tableId}/views` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view.show_all_columns`<a id="nocodbdb_viewshow_all_columns"></a>

Show All Columns in a given View

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
show_all_columns_response = nocodb.db_view.show_all_columns(
    view_id="string",
    ignore_ids=[
        None
    ],
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### view_id: [`Id`](./noco_db_python_sdk/type/.py)<a id="view_id-idnoco_db_python_sdktypepy"></a>

Unique View ID

##### ignore_ids: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./noco_db_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="ignore_ids-listunionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/views/{viewId}/show-all` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view.update_by_id`<a id="nocodbdb_viewupdate_by_id"></a>

Update the view with the given view Id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = nocodb.db_view.update_by_id(
    view_id="string",
    title="Grid View 1",
    uuid="e2457bbf-e29c-4fec-866e-fe3b01dba57f",
    password="password123",
    lock_type="collaborative",
    meta=None,
    order=1,
    show_system_fields=None,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### view_id: [`Id`](./noco_db_python_sdk/type/.py)<a id="view_id-idnoco_db_python_sdktypepy"></a>

Unique View ID

##### title: `str`<a id="title-str"></a>

View Title

##### uuid: `str`<a id="uuid-str"></a>

View UUID. Used in Shared View.

##### password: `str`<a id="password-str"></a>

View Password. Used in Shared View.

##### lock_type: `str`<a id="lock_type-str"></a>

Lock type of View.

##### meta: `Meta`<a id="meta-meta"></a>

##### order: `Union[int, float]`<a id="order-unionint-float"></a>

The order of the list of views.

##### show_system_fields: `ModelBool`<a id="show_system_fields-modelbool"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ViewUpdateReq`](./noco_db_python_sdk/type/view_update_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`View`](./noco_db_python_sdk/pydantic/view.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/views/{viewId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view.update_form_column`<a id="nocodbdb_viewupdate_form_column"></a>

Update the form column(s) by Form View Column ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_form_column_response = nocodb.db_view.update_form_column(
    form_view_column_id="string",
    description=None,
    help=None,
    label=None,
    meta=None,
    order=1,
    required=None,
    show=None,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### form_view_column_id: `Id`<a id="form_view_column_id-id"></a>

Unique Form View Column ID

##### description: `TextOrNull`<a id="description-textornull"></a>

##### help: `TextOrNull`<a id="help-textornull"></a>

##### label: `TextOrNull`<a id="label-textornull"></a>

##### meta: `Meta`<a id="meta-meta"></a>

##### order: `Union[int, float]`<a id="order-unionint-float"></a>

The order among all the columns in the form

##### required: `ModelBool`<a id="required-modelbool"></a>

##### show: `ModelBool`<a id="show-modelbool"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FormColumnReq`](./noco_db_python_sdk/type/form_column_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FormColumnReq`](./noco_db_python_sdk/pydantic/form_column_req.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/form-columns/{formViewColumnId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view.update_form_view`<a id="nocodbdb_viewupdate_form_view"></a>

Update the form data by Form ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_form_view_response = nocodb.db_view.update_form_view(
    form_view_id="string",
    banner_image_url=None,
    email=None,
    heading="My Form",
    logo_url=None,
    meta=None,
    redirect_after_secs=None,
    redirect_url=None,
    show_blank_form=None,
    subheading=None,
    submit_another_form=None,
    success_msg=None,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### form_view_id: [`Id`](./noco_db_python_sdk/type/.py)<a id="form_view_id-idnoco_db_python_sdktypepy"></a>

Unique Form View ID

##### banner_image_url: Union[`AttachmentReq`, `none_type`]<a id="banner_image_url-unionattachmentreq-none_type"></a>


Banner Image URL

##### email: `StringOrNull`<a id="email-stringornull"></a>

##### heading: `str`<a id="heading-str"></a>

The heading of the form

##### logo_url: Union[`AttachmentReq`, `none_type`]<a id="logo_url-unionattachmentreq-none_type"></a>


Logo URL.

##### meta: `Meta`<a id="meta-meta"></a>

##### redirect_after_secs: `StringOrNull`<a id="redirect_after_secs-stringornull"></a>

##### redirect_url: `TextOrNull`<a id="redirect_url-textornull"></a>

##### show_blank_form: `ModelBool`<a id="show_blank_form-modelbool"></a>

##### subheading: `TextOrNull`<a id="subheading-textornull"></a>

##### submit_another_form: `ModelBool`<a id="submit_another_form-modelbool"></a>

##### success_msg: `TextOrNull`<a id="success_msg-textornull"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FormUpdateReq`](./noco_db_python_sdk/type/form_update_req.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/forms/{formViewId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view.update_gallery_view_data`<a id="nocodbdb_viewupdate_gallery_view_data"></a>

Update the Gallery View data with Gallery ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_gallery_view_data_response = nocodb.db_view.update_gallery_view_data(
    gallery_view_id="vw_1eq2wk2xe3a9j5",
    fk_cover_image_col_id=None,
    meta=None,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### gallery_view_id: `str`<a id="gallery_view_id-str"></a>

Unique Gallery View ID

##### fk_cover_image_col_id: `StringOrNull`<a id="fk_cover_image_col_id-stringornull"></a>

##### meta: `Meta`<a id="meta-meta"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GalleryUpdateReq`](./noco_db_python_sdk/type/gallery_update_req.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/galleries/{galleryViewId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view.update_grid_column_patch`<a id="nocodbdb_viewupdate_grid_column_patch"></a>

Update grid column(s) in the given Grid

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_grid_column_patch_response = nocodb.db_view.update_grid_column_patch(
    column_id="string",
    fk_column_id="string",
    help="string_example",
    label="My Column",
    width="200px",
    group_by=None,
    group_by_order=1,
    group_by_sort=None,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### column_id: `Id`<a id="column_id-id"></a>

Unique Column ID

##### fk_column_id: [`Id`](./noco_db_python_sdk/type/id.py)<a id="fk_column_id-idnoco_db_python_sdktypeidpy"></a>

##### help: `str`<a id="help-str"></a>

##### label: `str`<a id="label-str"></a>

The label of the column

##### width: `str`<a id="width-str"></a>

The width of the column

##### group_by: `ModelBool`<a id="group_by-modelbool"></a>

##### group_by_order: `Union[int, float]`<a id="group_by_order-unionint-float"></a>

Group By Order

##### group_by_sort: `StringOrNull`<a id="group_by_sort-stringornull"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GridColumnReq`](./noco_db_python_sdk/type/grid_column_req.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/grid-columns/{columnId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view.update_grid_view`<a id="nocodbdb_viewupdate_grid_view"></a>

Update Grid View

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_grid_view_response = nocodb.db_view.update_grid_view(
    view_id="vw_wtdg2meyig5l4q",
    row_height=1,
    meta=None,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### view_id: `str`<a id="view_id-str"></a>

Unique View ID

##### row_height: `Union[int, float]`<a id="row_height-unionint-float"></a>

Row Height

##### meta: `Meta`<a id="meta-meta"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GridUpdateReq`](./noco_db_python_sdk/type/grid_update_req.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/grids/{viewId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view.update_kanban_view`<a id="nocodbdb_viewupdate_kanban_view"></a>

Update the Kanban View data with Kanban ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_kanban_view_response = nocodb.db_view.update_kanban_view(
    kanban_view_id="vw_1eq2wk2xe3a9j5",
    fk_grp_col_id=None,
    fk_cover_image_col_id=None,
    meta=None,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### kanban_view_id: `str`<a id="kanban_view_id-str"></a>

Unique Kanban View ID

##### fk_grp_col_id: `StringOrNull`<a id="fk_grp_col_id-stringornull"></a>

##### fk_cover_image_col_id: `StringOrNull`<a id="fk_cover_image_col_id-stringornull"></a>

##### meta: `Meta`<a id="meta-meta"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`KanbanUpdateReq`](./noco_db_python_sdk/type/kanban_update_req.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/kanbans/{kanbanViewId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view.update_map_view_data`<a id="nocodbdb_viewupdate_map_view_data"></a>

Update the Map View data by Map ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_map_view_data_response = nocodb.db_view.update_map_view_data(
    map_view_id="vw_1eq2wk2xe3a9j5",
    fk_geo_data_col_id="cl_8iw2o4ejzvdyna",
    meta=None,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### map_view_id: `str`<a id="map_view_id-str"></a>

Unique Map View ID

##### fk_geo_data_col_id: `str`<a id="fk_geo_data_col_id-str"></a>

Foreign Key to GeoData Column

##### meta: `Meta`<a id="meta-meta"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MapUpdateReq`](./noco_db_python_sdk/type/map_update_req.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/maps/{mapViewId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view_column.create_new_column`<a id="nocodbdb_view_columncreate_new_column"></a>

Create a new column in a given View

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_column_response = nocodb.db_view_column.create_new_column(
    view_id="vw_wtdg2meyig5l4q",
    fk_column_id="string",
    show=None,
    order=1,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### view_id: `str`<a id="view_id-str"></a>

Unique View ID

##### fk_column_id: [`Id`](./noco_db_python_sdk/type/id.py)<a id="fk_column_id-idnoco_db_python_sdktypeidpy"></a>

##### show: `ModelBool`<a id="show-modelbool"></a>

##### order: `Union[int, float]`<a id="order-unionint-float"></a>

The order of the list of views.

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ViewColumnReq`](./noco_db_python_sdk/type/view_column_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Column`](./noco_db_python_sdk/pydantic/column.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/views/{viewId}/columns` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view_column.list_by_view`<a id="nocodbdb_view_columnlist_by_view"></a>

List all columns by ViewID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_view_response = nocodb.db_view_column.list_by_view(
    view_id="vw_wtdg2meyig5l4q",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### view_id: `str`<a id="view_id-str"></a>

Unique View ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`ColumnList`](./noco_db_python_sdk/pydantic/column_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/views/{viewId}/columns` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view_column.update_column`<a id="nocodbdb_view_columnupdate_column"></a>

Update a column in a View

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_column_response = nocodb.db_view_column.update_column(
    view_id="string",
    column_id="string",
    show=None,
    order=1,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### view_id: [`Id`](./noco_db_python_sdk/type/.py)<a id="view_id-idnoco_db_python_sdktypepy"></a>

##### column_id: `Id`<a id="column_id-id"></a>

Unique Column ID

##### show: `ModelBool`<a id="show-modelbool"></a>

##### order: `Union[int, float]`<a id="order-unionint-float"></a>

The order of the list of views.

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ViewColumnUpdateReq`](./noco_db_python_sdk/type/view_column_update_req.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/views/{viewId}/columns/{columnId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view_share.create_shared_view`<a id="nocodbdb_view_sharecreate_shared_view"></a>

Create a shared view in a given View..

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_shared_view_response = nocodb.db_view_share.create_shared_view(
    view_id="vw_wtdg2meyig5l4q",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### view_id: `str`<a id="view_id-str"></a>

Unique View ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`SharedViewReq`](./noco_db_python_sdk/pydantic/shared_view_req.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/views/{viewId}/share` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view_share.delete_shared_view`<a id="nocodbdb_view_sharedelete_shared_view"></a>

Delete a shared view in a given View.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_shared_view_response = nocodb.db_view_share.delete_shared_view(
    view_id="vw_wtdg2meyig5l4q",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### view_id: `str`<a id="view_id-str"></a>

Unique View ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/views/{viewId}/share` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view_share.list_shared_views`<a id="nocodbdb_view_sharelist_shared_views"></a>

List all shared views in a given Table

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_shared_views_response = nocodb.db_view_share.list_shared_views(
    table_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### table_id: `Id`<a id="table_id-id"></a>

Unique Table ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`SharedViewList`](./noco_db_python_sdk/pydantic/shared_view_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/tables/{tableId}/share` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.db_view_share.update_shared_view`<a id="nocodbdb_view_shareupdate_shared_view"></a>

Update a shared view in a given View..

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_shared_view_response = nocodb.db_view_share.update_shared_view(
    view_id="vw_wtdg2meyig5l4q",
    meta=None,
    password=None,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### view_id: `str`<a id="view_id-str"></a>

Unique View ID

##### meta: `Meta`<a id="meta-meta"></a>

##### password: `StringOrNull`<a id="password-stringornull"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SharedViewReq`](./noco_db_python_sdk/type/shared_view_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`View`](./noco_db_python_sdk/pydantic/view.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/views/{viewId}/share` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.plugin.get_data_by_id`<a id="nocodbpluginget_data_by_id"></a>

Get the plugin data by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_data_by_id_response = nocodb.plugin.get_data_by_id(
    plugin_id="pluginId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### plugin_id: `str`<a id="plugin_id-str"></a>

Plugin ID

#### 🔄 Return<a id="🔄-return"></a>

[`Plugin`](./noco_db_python_sdk/pydantic/plugin.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/plugins/{pluginId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.plugin.get_status`<a id="nocodbpluginget_status"></a>

Check plugin is active or not

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_status_response = nocodb.plugin.get_status(
    plugin_title="pluginTitle_example",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### plugin_title: `str`<a id="plugin_title-str"></a>

Plugin Title

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/plugins/{pluginTitle}/status` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.plugin.list_all_plugins`<a id="nocodbpluginlist_all_plugins"></a>

List all plugins

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_plugins_response = nocodb.plugin.list_all_plugins(
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`PluginListAllPluginsResponse`](./noco_db_python_sdk/pydantic/plugin_list_all_plugins_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/plugins` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.plugin.test_configuration_post`<a id="nocodbplugintest_configuration_post"></a>

Test if the plugin is working with the given configurations

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
test_configuration_post_response = nocodb.plugin.test_configuration_post(
    title="Plugin Foo",
    input=None,
    category="Email",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

Plugin Title

##### input: Union[`str`, `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="input-unionstr-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>


##### category: `str`<a id="category-str"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PluginTestReq`](./noco_db_python_sdk/type/plugin_test_req.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/plugins/test` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.plugin.update_by_id`<a id="nocodbpluginupdate_by_id"></a>

Update the plugin data by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = nocodb.plugin.update_by_id(
    plugin_id="pluginId_example",
    active=None,
    input=None,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### plugin_id: `str`<a id="plugin_id-str"></a>

Plugin ID

##### active: `ModelBool`<a id="active-modelbool"></a>

##### input: Union[`str`, `none_type`]<a id="input-unionstr-none_type"></a>


Plugin Input

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PluginReq`](./noco_db_python_sdk/type/plugin_req.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/plugins/{pluginId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.plugin.webhook_list_plugins`<a id="nocodbpluginwebhook_list_plugins"></a>

List all webhook plugins

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
webhook_list_plugins_response = nocodb.plugin.webhook_list_plugins(
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`PluginWebhookListPluginsResponse`](./noco_db_python_sdk/pydantic/plugin_webhook_list_plugins_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/plugins/webhook` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.public.calendar_view_count_by_date`<a id="nocodbpubliccalendar_view_count_by_date"></a>

Count of Records in Dates in Calendar View

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
calendar_view_count_by_date_response = nocodb.public.calendar_view_count_by_date(
    shared_view_uuid="24a6d0bb-e45d-4b1a-bfef-f492d870de9f",
    xc_password="string_example",
    sort=[
        None
    ],
    where="string_example",
    limit=1,
    offset=0,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shared_view_uuid: `str`<a id="shared_view_uuid-str"></a>

Shared View UUID

##### xc_password: `str`<a id="xc_password-str"></a>

Shared view password

##### sort: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./noco_db_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="sort-listunionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

##### where: `str`<a id="where-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### offset: `int`<a id="offset-int"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/public/calendar-view/{sharedViewUuid}/countByDate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.public.calendar_view_list_shared_rows`<a id="nocodbpubliccalendar_view_list_shared_rows"></a>

List all shared view rows

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
calendar_view_list_shared_rows_response = nocodb.public.calendar_view_list_shared_rows(
    shared_view_uuid="24a6d0bb-e45d-4b1a-bfef-f492d870de9f",
    xc_password="string_example",
    fields=[
        None
    ],
    sort=None,
    from_date="string_example",
    to_date="string_example",
    where="string_example",
    offset=0,
    limit=1,
    sort_arr_json="string_example",
    filter_arr_json="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shared_view_uuid: `str`<a id="shared_view_uuid-str"></a>

Shared View UUID

##### xc_password: `str`<a id="xc_password-str"></a>

Shared view password

##### fields: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./noco_db_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="fields-listunionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Which fields to be shown

##### sort: Union[`List[str]`, `str`]<a id="sort-unionliststr-str"></a>


The result will be sorted based on `sort` query

##### from_date: `str`<a id="from_date-str"></a>

From Date

##### to_date: `str`<a id="to_date-str"></a>

To Date

##### where: `str`<a id="where-str"></a>

Extra filtering

##### offset: `int`<a id="offset-int"></a>

Offset in rows

##### limit: `int`<a id="limit-int"></a>

Limit in rows

##### sort_arr_json: `str`<a id="sort_arr_json-str"></a>

Used for multiple sort queries

##### filter_arr_json: `str`<a id="filter_arr_json-str"></a>

Used for multiple filter queries

#### 🔄 Return<a id="🔄-return"></a>

[`SharedViewList`](./noco_db_python_sdk/pydantic/shared_view_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/public/calendar-view/{sharedViewUuid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.public.create_shared_view_row`<a id="nocodbpubliccreate_shared_view_row"></a>

Create a new row for the target shared view

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_shared_view_row_response = nocodb.public.create_shared_view_row(
    body=None,
    shared_view_uuid="24a6d0bb-e45d-4b1a-bfef-f492d870de9f",
    xc_password="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shared_view_uuid: `str`<a id="shared_view_uuid-str"></a>

Shared View UUID

##### xc_password: `str`<a id="xc_password-str"></a>

Shared view password

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Union[bool, date, datetime, dict, float, int, list, str, None]`
#### 🔄 Return<a id="🔄-return"></a>

[`PublicCreateSharedViewRowResponse`](./noco_db_python_sdk/pydantic/public_create_shared_view_row_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/public/shared-view/{sharedViewUuid}/rows` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.public.list_nested_data`<a id="nocodbpubliclist_nested_data"></a>

List all nested list data in a given shared view

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_nested_data_response = nocodb.public.list_nested_data(
    shared_view_uuid="24a6d0bb-e45d-4b1a-bfef-f492d870de9f",
    row_id=None,
    relation_type="mm",
    column_name="columnName_example",
    fields=[
        None
    ],
    sort=None,
    where="string_example",
    offset=0,
    limit=1,
    sort_arr_json="string_example",
    filter_arr_json="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shared_view_uuid: `str`<a id="shared_view_uuid-str"></a>

Shared View UUID

##### row_id: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./noco_db_python_sdk/type/.py)<a id="row_id-unionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypepy"></a>

Unique Row ID

##### relation_type: `str`<a id="relation_type-str"></a>

Relation Type

##### column_name: `str`<a id="column_name-str"></a>

Column Name

##### fields: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./noco_db_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="fields-listunionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Which fields to be shown

##### sort: Union[`List[str]`, `str`]<a id="sort-unionliststr-str"></a>


The result will be sorted based on `sort` query

##### where: `str`<a id="where-str"></a>

Extra filtering

##### offset: `int`<a id="offset-int"></a>

Offset in rows

##### limit: `int`<a id="limit-int"></a>

Limit in rows

##### sort_arr_json: `str`<a id="sort_arr_json-str"></a>

Used for multiple sort queries

##### filter_arr_json: `str`<a id="filter_arr_json-str"></a>

Used for multiple filter queries

#### 🔄 Return<a id="🔄-return"></a>

[`PublicListNestedDataResponse`](./noco_db_python_sdk/pydantic/public_list_nested_data_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/public/shared-view/{sharedViewUuid}/rows/{rowId}/{relationType}/{columnName}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.public.list_shared_rows`<a id="nocodbpubliclist_shared_rows"></a>

List all shared view rows

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_shared_rows_response = nocodb.public.list_shared_rows(
    shared_view_uuid="24a6d0bb-e45d-4b1a-bfef-f492d870de9f",
    xc_password="string_example",
    fields=[
        None
    ],
    sort=None,
    where="string_example",
    offset=0,
    limit=1,
    sort_arr_json="string_example",
    filter_arr_json="string_example",
    pks="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shared_view_uuid: `str`<a id="shared_view_uuid-str"></a>

Shared View UUID

##### xc_password: `str`<a id="xc_password-str"></a>

Shared view password

##### fields: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./noco_db_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="fields-listunionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Which fields to be shown

##### sort: Union[`List[str]`, `str`]<a id="sort-unionliststr-str"></a>


The result will be sorted based on `sort` query

##### where: `str`<a id="where-str"></a>

Extra filtering

##### offset: `int`<a id="offset-int"></a>

Offset in rows

##### limit: `int`<a id="limit-int"></a>

Limit in rows

##### sort_arr_json: `str`<a id="sort_arr_json-str"></a>

Used for multiple sort queries

##### filter_arr_json: `str`<a id="filter_arr_json-str"></a>

Used for multiple filter queries

##### pks: `str`<a id="pks-str"></a>

Comma separated list of pks

#### 🔄 Return<a id="🔄-return"></a>

[`SharedViewList`](./noco_db_python_sdk/pydantic/shared_view_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/public/shared-view/{sharedViewUuid}/rows` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.public.list_shared_view_rows_group_by`<a id="nocodbpubliclist_shared_view_rows_group_by"></a>

List all shared view rows grouped by a column

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_shared_view_rows_group_by_response = nocodb.public.list_shared_view_rows_group_by(
    shared_view_uuid="24a6d0bb-e45d-4b1a-bfef-f492d870de9f",
    xc_password="string_example",
    fields=[
        None
    ],
    sort=None,
    where="string_example",
    offset=0,
    limit=1,
    sort_arr_json="string_example",
    filter_arr_json="string_example",
    column_name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shared_view_uuid: `str`<a id="shared_view_uuid-str"></a>

Shared View UUID

##### xc_password: `str`<a id="xc_password-str"></a>

Shared view password

##### fields: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./noco_db_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="fields-listunionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Which fields to be shown

##### sort: Union[`List[str]`, `str`]<a id="sort-unionliststr-str"></a>


The result will be sorted based on `sort` query

##### where: `str`<a id="where-str"></a>

Extra filtering

##### offset: `int`<a id="offset-int"></a>

Offset in rows

##### limit: `int`<a id="limit-int"></a>

Limit in rows

##### sort_arr_json: `str`<a id="sort_arr_json-str"></a>

Used for multiple sort queries

##### filter_arr_json: `str`<a id="filter_arr_json-str"></a>

Used for multiple filter queries

##### column_name: `str`<a id="column_name-str"></a>

Columns to group by

#### 🔄 Return<a id="🔄-return"></a>

[`SharedViewList`](./noco_db_python_sdk/pydantic/shared_view_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/public/shared-view/{sharedViewUuid}/groupby` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.public.nested_data_relation_list`<a id="nocodbpublicnested_data_relation_list"></a>

List Nested Data Relation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
nested_data_relation_list_response = nocodb.public.nested_data_relation_list(
    shared_view_uuid="24a6d0bb-e45d-4b1a-bfef-f492d870de9f",
    column_name="columnName_example",
    xc_password="string_example",
    fields=[
        None
    ],
    sort=None,
    where="string_example",
    offset=0,
    limit=1,
    sort_arr_json="string_example",
    filter_arr_json="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shared_view_uuid: `str`<a id="shared_view_uuid-str"></a>

Shared View UUID

##### column_name: `str`<a id="column_name-str"></a>

Column Name

##### xc_password: `str`<a id="xc_password-str"></a>

Shared view password

##### fields: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./noco_db_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="fields-listunionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Which fields to be shown

##### sort: Union[`List[str]`, `str`]<a id="sort-unionliststr-str"></a>


The result will be sorted based on `sort` query

##### where: `str`<a id="where-str"></a>

Extra filtering

##### offset: `int`<a id="offset-int"></a>

Offset in rows

##### limit: `int`<a id="limit-int"></a>

Limit in rows

##### sort_arr_json: `str`<a id="sort_arr_json-str"></a>

Used for multiple sort queries

##### filter_arr_json: `str`<a id="filter_arr_json-str"></a>

Used for multiple filter queries

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/public/shared-view/{sharedViewUuid}/nested/{columnName}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.public.rows_export_type`<a id="nocodbpublicrows_export_type"></a>

Export all rows in Share View in a CSV / Excel Format

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rows_export_type_response = nocodb.public.rows_export_type(
    shared_view_uuid="76d44b86-bc65-4500-8956-ab512c80ab25",
    type="csv",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shared_view_uuid: `str`<a id="shared_view_uuid-str"></a>

Shared View UUID

##### type: `str`<a id="type-str"></a>

Export Type

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/public/shared-view/{sharedViewUuid}/rows/export/{type}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.public.shared_base_meta_get`<a id="nocodbpublicshared_base_meta_get"></a>

Get Share Source Meta

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shared_base_meta_get_response = nocodb.public.shared_base_meta_get(
    shared_base_uuid="24a6d0bb-e45d-4b1a-bfef-f492d870de9f",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shared_base_uuid: `str`<a id="shared_base_uuid-str"></a>

Shared Base UUID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`PublicSharedBaseMetaGetResponse`](./noco_db_python_sdk/pydantic/public_shared_base_meta_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/public/shared-base/{sharedBaseUuid}/meta` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.public.shared_erd_meta_get`<a id="nocodbpublicshared_erd_meta_get"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
nocodb.public.shared_erd_meta_get(
    shared_erd_uuid="sharedErdUuid_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shared_erd_uuid: `str`<a id="shared_erd_uuid-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/public/shared-erd/{sharedErdUuid}/meta` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.public.shared_view_group_data_list`<a id="nocodbpublicshared_view_group_data_list"></a>

List Shared View Grouped Data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
shared_view_group_data_list_response = nocodb.public.shared_view_group_data_list(
    shared_view_uuid="24a6d0bb-e45d-4b1a-bfef-f492d870de9f",
    column_id="string",
    xc_password="string_example",
    fields=[
        None
    ],
    sort=None,
    where="string_example",
    offset=0,
    limit=1,
    sort_arr_json="string_example",
    filter_arr_json="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shared_view_uuid: `str`<a id="shared_view_uuid-str"></a>

Shared View UUID

##### column_id: `Id`<a id="column_id-id"></a>

Unique Column ID

##### xc_password: `str`<a id="xc_password-str"></a>

Shared view password

##### fields: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./noco_db_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="fields-listunionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Which fields to be shown

##### sort: Union[`List[str]`, `str`]<a id="sort-unionliststr-str"></a>


The result will be sorted based on `sort` query

##### where: `str`<a id="where-str"></a>

Extra filtering

##### offset: `int`<a id="offset-int"></a>

Offset in rows

##### limit: `int`<a id="limit-int"></a>

Limit in rows

##### sort_arr_json: `str`<a id="sort_arr_json-str"></a>

Used for multiple sort queries

##### filter_arr_json: `str`<a id="filter_arr_json-str"></a>

Used for multiple filter queries

#### 🔄 Return<a id="🔄-return"></a>

[`PublicSharedViewGroupDataListResponse`](./noco_db_python_sdk/pydantic/public_shared_view_group_data_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/public/shared-view/{sharedViewUuid}/group/{columnId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.public.view_meta_get`<a id="nocodbpublicview_meta_get"></a>

Get Share View Meta

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
view_meta_get_response = nocodb.public.view_meta_get(
    shared_view_uuid="24a6d0bb-e45d-4b1a-bfef-f492d870de9f",
    xc_password="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shared_view_uuid: `str`<a id="shared_view_uuid-str"></a>

Shared View UUID

##### xc_password: `str`<a id="xc_password-str"></a>

Shared view password

#### 🔄 Return<a id="🔄-return"></a>

[`PublicViewMetaGetResponse`](./noco_db_python_sdk/pydantic/public_view_meta_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/public/shared-view/{sharedViewUuid}/meta` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.source.base_id_sources_list`<a id="nocodbsourcebase_id_sources_list"></a>

Get base source list

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
base_id_sources_list_response = nocodb.source.base_id_sources_list(
    base_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/sources` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.source.create_erd_share`<a id="nocodbsourcecreate_erd_share"></a>

share ERD view

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_erd_share_response = nocodb.source.create_erd_share(
    base_id="baseId_example",
    source_id="sourceId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `str`<a id="base_id-str"></a>

##### source_id: `str`<a id="source_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Source`](./noco_db_python_sdk/pydantic/source.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/sources/{sourceId}/share/erd` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.source.create_new_source`<a id="nocodbsourcecreate_new_source"></a>

Create a new source on a given base

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_source_response = nocodb.source.create_new_source(
    body=None,
    base_id="string",
    alias=None,
    config=None,
    enabled=None,
    id="ds_krsappzu9f8vmoX",
    inflection_column="camelize",
    inflection_table="camelize",
    is_meta=None,
    is_local=None,
    order=1,
    base_id="p_01clqvzik3izk6",
    type="mysql2",
    external=False,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### alias: `StringOrNull`<a id="alias-stringornull"></a>

##### config: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./noco_db_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="config-unionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Source Configuration

##### enabled: `ModelBool`<a id="enabled-modelbool"></a>

##### id: `str`<a id="id-str"></a>

Unique Source ID

##### inflection_column: `str`<a id="inflection_column-str"></a>

Inflection for columns

##### inflection_table: `str`<a id="inflection_table-str"></a>

Inflection for tables

##### is_meta: `ModelBool`<a id="is_meta-modelbool"></a>

##### is_local: `ModelBool`<a id="is_local-modelbool"></a>

##### order: `Union[int, float]`<a id="order-unionint-float"></a>

The order of the list of sources

##### base_id: `str`<a id="base_id-str"></a>

The base ID that this source belongs to

##### type: `str`<a id="type-str"></a>

DB Type

##### external: `bool`<a id="external-bool"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SourceCreateNewSourceRequest`](./noco_db_python_sdk/type/source_create_new_source_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Source`](./noco_db_python_sdk/pydantic/source.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/sources` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.source.create_sql_view`<a id="nocodbsourcecreate_sql_view"></a>

Create sql view

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_sql_view_response = nocodb.source.create_sql_view(
    base_id="baseId_example",
    source_id="sourceId_example",
    view_name="string_example",
    view_definition="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `str`<a id="base_id-str"></a>

##### source_id: `str`<a id="source_id-str"></a>

##### view_name: `str`<a id="view_name-str"></a>

##### view_definition: `str`<a id="view_definition-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SourceCreateSqlViewRequest`](./noco_db_python_sdk/type/source_create_sql_view_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/:baseId/sources/:sourceId/sqlView` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.source.create_table`<a id="nocodbsourcecreate_table"></a>

Create a new table in a given Base and Source

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_table_response = nocodb.source.create_table(
    columns=[
        {
            "title": "string",
            "column_name": "string",
            "dt": "string",
            "uidt": "ID",
        }
    ],
    table_name="my_table",
    base_id="string",
    source_id="ds_j04jmxh5xg10l",
    title="My Table",
    meta=None,
    order=1,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### columns: List[`NormalColumnRequest`]<a id="columns-listnormalcolumnrequest"></a>

The column models in this table

##### table_name: `str`<a id="table_name-str"></a>

Table name

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### source_id: `str`<a id="source_id-str"></a>

Unique Source ID

##### title: `str`<a id="title-str"></a>

Table title

##### meta: `Meta`<a id="meta-meta"></a>

##### order: `Union[int, float]`<a id="order-unionint-float"></a>

The order of table list

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TableReq`](./noco_db_python_sdk/type/table_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Table`](./noco_db_python_sdk/pydantic/table.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/{sourceId}/tables` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.source.delete_details`<a id="nocodbsourcedelete_details"></a>

Delete the source details of a given base

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_details_response = nocodb.source.delete_details(
    base_id="string",
    source_id="ds_j04jmxh5xg10l",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### source_id: `str`<a id="source_id-str"></a>

Unique Source ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/sources/{sourceId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.source.delete_erd_share`<a id="nocodbsourcedelete_erd_share"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
nocodb.source.delete_erd_share(
    base_id="baseId_example",
    source_id="sourceId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `str`<a id="base_id-str"></a>

##### source_id: `str`<a id="source_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/sources/{sourceId}/share/erd` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.source.get_details`<a id="nocodbsourceget_details"></a>

Get the source details of a given base

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = nocodb.source.get_details(
    base_id="string",
    source_id="ds_j04jmxh5xg10l",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### source_id: `str`<a id="source_id-str"></a>

Unique Source ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`Source`](./noco_db_python_sdk/pydantic/source.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/sources/{sourceId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.source.get_meta_diff`<a id="nocodbsourceget_meta_diff"></a>

Get the meta data difference between NC_DB and external data sources in a given Source

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_meta_diff_response = nocodb.source.get_meta_diff(
    base_id="string",
    source_id="ds_j04jmxh5xg10l",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### source_id: `str`<a id="source_id-str"></a>

Unique Source ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`SourceGetMetaDiffResponse`](./noco_db_python_sdk/pydantic/source_get_meta_diff_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/meta-diff/{sourceId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.source.get_tables`<a id="nocodbsourceget_tables"></a>

List all tables in a given Base and Source

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tables_response = nocodb.source.get_tables(
    base_id="string",
    source_id="ds_j04jmxh5xg10l",
    xc_auth="string_example",
    page=3.14,
    page_size=3.14,
    sort="string_example",
    include_m2_m=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### source_id: `str`<a id="source_id-str"></a>

Unique Source ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

##### page_size: `Union[int, float]`<a id="page_size-unionint-float"></a>

##### sort: `str`<a id="sort-str"></a>

##### include_m2_m: `bool`<a id="include_m2_m-bool"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TableList`](./noco_db_python_sdk/pydantic/table_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/{sourceId}/tables` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.source.sync_meta_diff`<a id="nocodbsourcesync_meta_diff"></a>

Synchronise the meta data difference between NC_DB and external data sources in a given Source

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sync_meta_diff_response = nocodb.source.sync_meta_diff(
    base_id="string",
    source_id="ds_j04jmxh5xg10l",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### source_id: `str`<a id="source_id-str"></a>

Unique Source ID

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`SourceSyncMetaDiffResponse`](./noco_db_python_sdk/pydantic/source_sync_meta_diff_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/meta-diff/{sourceId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.source.update_details`<a id="nocodbsourceupdate_details"></a>

Update the source details of a given base

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_details_response = nocodb.source.update_details(
    base_id="string",
    source_id="ds_j04jmxh5xg10l",
    alias="sakila",
    type="mysql2",
    config={
        "client": "mysql2",
    },
    inflection_column="camelize",
    inflection_table="camelize",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### base_id: `Id`<a id="base_id-id"></a>

Unique Base ID

##### source_id: `str`<a id="source_id-str"></a>

Unique Source ID

##### alias: `str`<a id="alias-str"></a>

##### type: `str`<a id="type-str"></a>

##### config: [`SourceUpdateDetailsRequestConfig`](./noco_db_python_sdk/type/source_update_details_request_config.py)<a id="config-sourceupdatedetailsrequestconfignoco_db_python_sdktypesource_update_details_request_configpy"></a>


##### inflection_column: `str`<a id="inflection_column-str"></a>

##### inflection_table: `str`<a id="inflection_table-str"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SourceUpdateDetailsRequest`](./noco_db_python_sdk/type/source_update_details_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/bases/{baseId}/sources/{sourceId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.storage.upload_attachment`<a id="nocodbstorageupload_attachment"></a>

Upload attachment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
nocodb.storage.upload_attachment(
    path="download/noco/jango_fett/Table1/attachment/uVbjPVQxC_SSfs8Ctx.jpg",
    xc_auth="string_example",
    title="22bc-kavypmq4869759 (1).jpg",
    mimetype="image/jpeg",
    path2="download/noco/jango_fett/Table1/attachment/uVbjPVQxC_SSfs8Ctx.jpg",
    size=13052,
    url="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### path: `str`<a id="path-str"></a>

Target File Path

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

##### title: `str`<a id="title-str"></a>

The title of the attachment used in UI

##### mimetype: `str`<a id="mimetype-str"></a>

The mimetype of the attachment

##### path2: `str`<a id="path2-str"></a>

The file path of the attachment

##### size: `Union[int, float]`<a id="size-unionint-float"></a>

The size of the attachment

##### url: `str`<a id="url-str"></a>

Attachment URL to be uploaded via upload-by-url

##### requestBody: [`AttachmentReq`](./noco_db_python_sdk/type/attachment_req.py)<a id="requestbody-attachmentreqnoco_db_python_sdktypeattachment_reqpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/storage/upload` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.storage.upload_by_url`<a id="nocodbstorageupload_by_url"></a>

Upload attachment by URL. Used in Airtable Migration.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
nocodb.storage.upload_by_url(
    body=[
        {
            "title": "22bc-kavypmq4869759 (1).jpg",
            "mimetype": "image/jpeg",
            "path": "download/noco/jango_fett/Table1/attachment/uVbjPVQxC_SSfs8Ctx.jpg",
            "size": 13052,
        }
    ],
    path="download/noco/jango_fett/Table1/attachment/c7z_UF8sZBgJUxMjpN.jpg",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### path: `str`<a id="path-str"></a>

Target File Path

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

##### requestBody: [`StorageUploadByUrlRequest`](./noco_db_python_sdk/type/storage_upload_by_url_request.py)<a id="requestbody-storageuploadbyurlrequestnoco_db_python_sdktypestorage_upload_by_url_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/storage/upload-by-url` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.table_records.create_new_record`<a id="nocodbtable_recordscreate_new_record"></a>

This API endpoint allows the creation of new records within a specified table. Records to be inserted are input as an array of key-value pair objects, where each key corresponds to a field name. Ensure that all the required fields are included in the payload, with exceptions for fields designated as auto-increment or those having default values. 

When dealing with 'Links' or 'Link To Another Record' field types, you should utilize the 'Create Link' API to insert relevant data. 

Certain read-only field types will be disregarded if included in the request. These field types include 'Look Up,' 'Roll Up,' 'Formula,' 'Auto Number,' 'Created By,' 'Updated By,' 'Created At,' 'Updated At,' 'Barcode,' and 'QR Code.'

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_record_response = nocodb.table_records.create_new_record(
    body=None,
    table_id="tableId_example",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### table_id: `str`<a id="table_id-str"></a>

**Table Identifier**.

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

##### requestBody: [`TableRecordsCreateNewRecordRequest`](./noco_db_python_sdk/type/table_records_create_new_record_request.py)<a id="requestbody-tablerecordscreatenewrecordrequestnoco_db_python_sdktypetable_records_create_new_record_requestpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TableRecordsCreateNewRecordResponse`](./noco_db_python_sdk/pydantic/table_records_create_new_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/tables/{tableId}/records` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.table_records.delete_by_array`<a id="nocodbtable_recordsdelete_by_array"></a>

This API endpoint allows deleting existing records within a specified table identified by an array of Record-IDs, serving as unique identifier for the record. Records to be deleted are input as an array of record-identifiers.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_by_array_response = nocodb.table_records.delete_by_array(
    body=None,
    table_id="tableId_example",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### table_id: `str`<a id="table_id-str"></a>

**Table Identifier**.

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

##### requestBody: [`TableRecordsDeleteByArrayRequest`](./noco_db_python_sdk/type/table_records_delete_by_array_request.py)<a id="requestbody-tablerecordsdeletebyarrayrequestnoco_db_python_sdktypetable_records_delete_by_array_requestpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TableRecordsDeleteByArrayResponse`](./noco_db_python_sdk/pydantic/table_records_delete_by_array_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/tables/{tableId}/records` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.table_records.get_count`<a id="nocodbtable_recordsget_count"></a>

This API endpoint allows you to retrieve the total number of records from a specified table or a view. You can narrow down search results by applying `where` query parameter

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_count_response = nocodb.table_records.get_count(
    table_id="tableId_example",
    view_id="string_example",
    where="string_example",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### table_id: `str`<a id="table_id-str"></a>

**Table Identifier**

##### view_id: `str`<a id="view_id-str"></a>

**View Identifier**. Allows you to fetch record count that are currently visible within a specific view.

##### where: `str`<a id="where-str"></a>

Enables you to define specific conditions for filtering record count in your API response. Multiple conditions can be combined using logical operators such as 'and' and 'or'. Each condition consists of three parts: a field name, a comparison operator, and a value.  Example: `where=(field1,eq,value1)~and(field2,eq,value2)` will filter records where 'field1' is equal to 'value1' AND 'field2' is equal to 'value2'.   You can also use other comparison operators like 'ne' (not equal), 'gt' (greater than), 'lt' (less than), and more, to create complex filtering rules.  If `viewId` query parameter is also included, then the filters included here will be applied over the filtering configuration defined in the view.   Please remember to maintain the specified format, and do not include spaces between the different condition components

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`TableRecordsGetCountResponse`](./noco_db_python_sdk/pydantic/table_records_get_count_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/tables/{tableId}/records/count` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.table_records.link_records_post`<a id="nocodbtable_recordslink_records_post"></a>

This API endpoint allows you to link records to a specific `Link field` and `Record ID`. The request payload is an array of record-ids from the adjacent table for linking purposes. Note that any existing links, if present, will be unaffected during this operation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
link_records_post_response = nocodb.table_records.link_records_post(
    body=None,
    table_id="tableId_example",
    link_field_id="linkFieldId_example",
    record_id="recordId_example",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### table_id: `str`<a id="table_id-str"></a>

**Table Identifier**

##### link_field_id: `str`<a id="link_field_id-str"></a>

**Links Field Identifier** corresponding to the relation field `Links` established between tables.

##### record_id: `str`<a id="record_id-str"></a>

**Record Identifier** corresponding to the record in this table for which links are being created.

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

##### requestBody: [`TableRecordsLinkRecordsPostRequest`](./noco_db_python_sdk/type/table_records_link_records_post_request.py)<a id="requestbody-tablerecordslinkrecordspostrequestnoco_db_python_sdktypetable_records_link_records_post_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/tables/{tableId}/links/{linkFieldId}/records/{recordId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.table_records.list`<a id="nocodbtable_recordslist"></a>

This API endpoint allows you to retrieve records from a specified table. You can customize the response by applying various query parameters for filtering, sorting, and formatting.

**Pagination**: The response is paginated by default, with the first page being returned initially. The response includes the following additional information in the `pageInfo` JSON block:

- `totalRows`: Indicates the total number of rows available for the specified conditions (if any).
- `page`: Specifies the current page number.
- `pageSize`: Defaults to 25 and defines the number of records on each page.
- `isFirstPage`: A boolean value that indicates whether the current page is the first page of records in the dataset.
- `isLastPage`: A boolean value that indicates whether the current page is the last page of records in the dataset.

The `pageInfo` attributes are particularly valuable when dealing with large datasets that are divided into multiple pages. They enable you to determine whether additional pages of records are available for retrieval or if you've reached the end of the dataset.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = nocodb.table_records.list(
    table_id="tableId_example",
    fields="string_example",
    sort="string_example",
    where="string_example",
    offset=0,
    limit=1,
    view_id="string_example",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### table_id: `str`<a id="table_id-str"></a>

**Table Identifier**.

##### fields: `str`<a id="fields-str"></a>

Allows you to specify the fields that you wish to include in your API response. By default, all the fields are included in the response.  Example: `fields=field1,field2` will include only 'field1' and 'field2' in the API response.   Please note that it's essential not to include spaces between field names in the comma-separated list.

##### sort: `str`<a id="sort-str"></a>

Allows you to specify the fields by which you want to sort the records in your API response. By default, sorting is done in ascending order for the designated fields. To sort in descending order, add a '-' symbol before the field name.  Example: `sort=field1,-field2` will sort the records first by 'field1' in ascending order and then by 'field2' in descending order.  If `viewId` query parameter is also included, the sort included here will take precedence over any sorting configuration defined in the view.  Please note that it's essential not to include spaces between field names in the comma-separated list.

##### where: `str`<a id="where-str"></a>

Enables you to define specific conditions for filtering records in your API response. Multiple conditions can be combined using logical operators such as 'and' and 'or'. Each condition consists of three parts: a field name, a comparison operator, and a value.  Example: `where=(field1,eq,value1)~and(field2,eq,value2)` will filter records where 'field1' is equal to 'value1' AND 'field2' is equal to 'value2'.   You can also use other comparison operators like 'ne' (not equal), 'gt' (greater than), 'lt' (less than), and more, to create complex filtering rules.  If `viewId` query parameter is also included, then the filters included here will be applied over the filtering configuration defined in the view.   Please remember to maintain the specified format, and do not include spaces between the different condition components

##### offset: `int`<a id="offset-int"></a>

Enables you to control the pagination of your API response by specifying the number of records you want to skip from the beginning of the result set. The default value for this parameter is set to 0, meaning no records are skipped by default.  Example: `offset=25` will skip the first 25 records in your API response, allowing you to access records starting from the 26th position.  Please note that the 'offset' value represents the number of records to exclude, not an index value, so an offset of 25 will skip the first 25 records.

##### limit: `int`<a id="limit-int"></a>

Enables you to set a limit on the number of records you want to retrieve in your API response. By default, your response includes all the available records, but by using this parameter, you can control the quantity you receive.  Example: `limit=100` will constrain your response to the first 100 records in the dataset.

##### view_id: `str`<a id="view_id-str"></a>

***View Identifier***. Allows you to fetch records that are currently visible within a specific view. API retrieves records in the order they are displayed if the SORT option is enabled within that view.  Additionally, if you specify a `sort` query parameter, it will take precedence over any sorting configuration defined in the view. If you specify a `where` query parameter, it will be applied over the filtering configuration defined in the view.   By default, all fields, including those that are disabled within the view, are included in the response. To explicitly specify which fields to include or exclude, you can use the `fields` query parameter to customize the output according to your requirements.

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`TableRecordsListResponse`](./noco_db_python_sdk/pydantic/table_records_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/tables/{tableId}/records` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.table_records.list_linked_records`<a id="nocodbtable_recordslist_linked_records"></a>

This API endpoint allows you to retrieve list of linked records for a specific `Link field` and `Record ID`. The response is an array of objects containing Primary Key and its corresponding display value.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_linked_records_response = nocodb.table_records.list_linked_records(
    table_id="tableId_example",
    link_field_id="linkFieldId_example",
    record_id="recordId_example",
    fields="string_example",
    sort="string_example",
    where="string_example",
    offset=0,
    limit=1,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### table_id: `str`<a id="table_id-str"></a>

**Table Identifier**

##### link_field_id: `str`<a id="link_field_id-str"></a>

**Links Field Identifier** corresponding to the relation field `Links` established between tables.

##### record_id: `str`<a id="record_id-str"></a>

**Record Identifier** corresponding to the record in this table for which linked records are being fetched.

##### fields: `str`<a id="fields-str"></a>

Allows you to specify the fields that you wish to include from the linked records in your API response. By default, only Primary Key and associated display value field is included.  Example: `fields=field1,field2` will include only 'field1' and 'field2' in the API response.   Please note that it's essential not to include spaces between field names in the comma-separated list.

##### sort: `str`<a id="sort-str"></a>

Allows you to specify the fields by which you want to sort linked records in your API response. By default, sorting is done in ascending order for the designated fields. To sort in descending order, add a '-' symbol before the field name.  Example: `sort=field1,-field2` will sort the records first by 'field1' in ascending order and then by 'field2' in descending order.  Please note that it's essential not to include spaces between field names in the comma-separated list.

##### where: `str`<a id="where-str"></a>

Enables you to define specific conditions for filtering linked records in your API response. Multiple conditions can be combined using logical operators such as 'and' and 'or'. Each condition consists of three parts: a field name, a comparison operator, and a value.  Example: `where=(field1,eq,value1)~and(field2,eq,value2)` will filter linked records where 'field1' is equal to 'value1' AND 'field2' is equal to 'value2'.   You can also use other comparison operators like 'ne' (not equal), 'gt' (greater than), 'lt' (less than), and more, to create complex filtering rules.  Please remember to maintain the specified format, and do not include spaces between the different condition components

##### offset: `int`<a id="offset-int"></a>

Enables you to control the pagination of your API response by specifying the number of linked records you want to skip from the beginning of the result set. The default value for this parameter is set to 0, meaning no linked records are skipped by default.  Example: `offset=25` will skip the first 25 linked records in your API response, allowing you to access linked records starting from the 26th position.  Please note that the 'offset' value represents the number of linked records to exclude, not an index value, so an offset of 25 will skip the first 25 linked records.

##### limit: `int`<a id="limit-int"></a>

Enables you to set a limit on the number of linked records you want to retrieve in your API response. By default, your response includes all the available linked records, but by using this parameter, you can control the quantity you receive.  Example: `limit=100` will constrain your response to the first 100 linked records in the dataset.

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`TableRecordsListLinkedRecordsResponse`](./noco_db_python_sdk/pydantic/table_records_list_linked_records_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/tables/{tableId}/links/{linkFieldId}/records/{recordId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.table_records.read_by_id`<a id="nocodbtable_recordsread_by_id"></a>

This API endpoint allows you to retrieve a single record identified by Record-ID, serving as unique identifier for the record from a specified table.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
read_by_id_response = nocodb.table_records.read_by_id(
    table_id="tableId_example",
    record_id="recordId_example",
    fields="string_example",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### table_id: `str`<a id="table_id-str"></a>

**Table Identifier**

##### record_id: `str`<a id="record_id-str"></a>

Record ID

##### fields: `str`<a id="fields-str"></a>

Allows you to specify the fields that you wish to include in your API response. By default, all the fields are included in the response.  Example: `fields=field1,field2` will include only 'field1' and 'field2' in the API response.   Please note that it's essential not to include spaces between field names in the comma-separated list.

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`TableRecordsReadByIdResponse`](./noco_db_python_sdk/pydantic/table_records_read_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/tables/{tableId}/records/{recordId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.table_records.unlink_records`<a id="nocodbtable_recordsunlink_records"></a>

This API endpoint allows you to unlink records from a specific `Link field` and `Record ID`. The request payload is an array of record-ids from the adjacent table for unlinking purposes. Note that, 
- duplicated record-ids will be ignored.
- non-existent record-ids will be ignored.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
unlink_records_response = nocodb.table_records.unlink_records(
    body=None,
    table_id="tableId_example",
    link_field_id="linkFieldId_example",
    record_id="recordId_example",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### table_id: `str`<a id="table_id-str"></a>

**Table Identifier**

##### link_field_id: `str`<a id="link_field_id-str"></a>

**Links Field Identifier** corresponding to the relation field `Links` established between tables.

##### record_id: `str`<a id="record_id-str"></a>

**Record Identifier** corresponding to the record in this table for which links are being removed.

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

##### requestBody: [`TableRecordsUnlinkRecordsRequest`](./noco_db_python_sdk/type/table_records_unlink_records_request.py)<a id="requestbody-tablerecordsunlinkrecordsrequestnoco_db_python_sdktypetable_records_unlink_records_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/tables/{tableId}/links/{linkFieldId}/records/{recordId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.table_records.update_patch_table_records`<a id="nocodbtable_recordsupdate_patch_table_records"></a>

This API endpoint allows updating existing records within a specified table identified by an array of Record-IDs, serving as unique identifier for the record. Records to be updated are input as an array of key-value pair objects, where each key corresponds to a field name. Ensure that all the required fields are included in the payload, with exceptions for fields designated as auto-increment or those having default values. 

When dealing with 'Links' or 'Link To Another Record' field types, you should utilize the 'Create Link' API to insert relevant data. 

Certain read-only field types will be disregarded if included in the request. These field types include 'Look Up,' 'Roll Up,' 'Formula,' 'Auto Number,' 'Created By,' 'Updated By,' 'Created At,' 'Updated At,' 'Barcode,' and 'QR Code.'

Note that a PATCH request only updates the specified fields while leaving other fields unaffected. Currently, PUT requests are not supported by this endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_patch_table_records_response = nocodb.table_records.update_patch_table_records(
    body=None,
    table_id="tableId_example",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### table_id: `str`<a id="table_id-str"></a>

**Table Identifier**.

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

##### requestBody: [`TableRecordsUpdatePatchTableRecordsRequest`](./noco_db_python_sdk/type/table_records_update_patch_table_records_request.py)<a id="requestbody-tablerecordsupdatepatchtablerecordsrequestnoco_db_python_sdktypetable_records_update_patch_table_records_requestpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TableRecordsUpdatePatchTableRecordsResponse`](./noco_db_python_sdk/pydantic/table_records_update_patch_table_records_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/tables/{tableId}/records` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.utils.clear_noco_cache`<a id="nocodbutilsclear_noco_cache"></a>

Delete All K/V pairs in NocoCache

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
clear_noco_cache_response = nocodb.utils.clear_noco_cache(
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/cache` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.utils.count_comments`<a id="nocodbutilscount_comments"></a>

Return the number of comments in the given query.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
count_comments_response = nocodb.utils.count_comments(
    UNKNOWN_PARAMETER_NAME=,
    fk_model_id="string",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### UNKNOWN_PARAMETER_NAME: [``](./noco_db_python_sdk/type/.py)<a id="unknown_parameter_name-noco_db_python_sdktypepy"></a>

Comment IDs

##### fk_model_id: [`Id`](./noco_db_python_sdk/type/.py)<a id="fk_model_id-idnoco_db_python_sdktypepy"></a>

Foreign Key to Model

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`UtilsCountCommentsResponse`](./noco_db_python_sdk/pydantic/utils_count_comments_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/audits/comments/count` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.utils.create_new_comment_row`<a id="nocodbutilscreate_new_comment_row"></a>

Create a new comment in a row. Logged in Audit.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_comment_row_response = nocodb.utils.create_new_comment_row(
    fk_model_id="md_ehn5izr99m7d45",
    row_id="3",
    description="This is the comment for the row",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### fk_model_id: `str`<a id="fk_model_id-str"></a>

Foreign Key to Model

##### row_id: `str`<a id="row_id-str"></a>

Row ID

##### description: `str`<a id="description-str"></a>

Description for the target row

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CommentReq`](./noco_db_python_sdk/type/comment_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Audit`](./noco_db_python_sdk/pydantic/audit.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/audits/comments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.utils.get_all_noco_cache`<a id="nocodbutilsget_all_noco_cache"></a>

Get All K/V pairs in NocoCache

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
nocodb.utils.get_all_noco_cache(
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/cache` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.utils.get_app_info`<a id="nocodbutilsget_app_info"></a>

Get the application info such as authType, defaultLimit, version and etc.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_app_info_response = nocodb.utils.get_app_info(
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### 🔄 Return<a id="🔄-return"></a>

[`UtilsGetAppInfoResponse`](./noco_db_python_sdk/pydantic/utils_get_app_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/nocodb/info` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.utils.list_comments`<a id="nocodbutilslist_comments"></a>

List all comments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_comments_response = nocodb.utils.list_comments(
    row_id="10",
    fk_model_id="string",
    xc_auth="string_example",
    comments_only=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### row_id: `str`<a id="row_id-str"></a>

Row ID

##### fk_model_id: [`Id`](./noco_db_python_sdk/type/.py)<a id="fk_model_id-idnoco_db_python_sdktypepy"></a>

Foreign Key to Model

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

##### comments_only: `bool`<a id="comments_only-bool"></a>

Is showing comments only?

#### 🔄 Return<a id="🔄-return"></a>

[`UtilsListCommentsResponse`](./noco_db_python_sdk/pydantic/utils_list_comments_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/audits/comments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.utils.make_axios_request`<a id="nocodbutilsmake_axios_request"></a>

Generic Axios Call

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
make_axios_request_response = nocodb.utils.make_axios_request(
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/axiosRequestMake` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.utils.select_connection_post`<a id="nocodbutilsselect_connection_post"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
select_connection_post_response = nocodb.utils.select_connection_post(
    body=None,
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Union[bool, date, datetime, dict, float, int, list, str, None]`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/connection/select` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.utils.test_db_connection`<a id="nocodbutilstest_db_connection"></a>

Test the DB Connection

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
test_db_connection_response = nocodb.utils.test_db_connection(
    client="mysql2",
    connection={
        "host": "localhost",
        "port": "3306",
        "user": "root",
        "password": "password",
    },
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### client: `str`<a id="client-str"></a>

DB Type

##### connection: [`UtilsTestDbConnectionRequestConnection`](./noco_db_python_sdk/type/utils_test_db_connection_request_connection.py)<a id="connection-utilstestdbconnectionrequestconnectionnoco_db_python_sdktypeutils_test_db_connection_request_connectionpy"></a>


##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UtilsTestDbConnectionRequest`](./noco_db_python_sdk/type/utils_test_db_connection_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UtilsTestDbConnectionResponse`](./noco_db_python_sdk/pydantic/utils_test_db_connection_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/connection/test` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.utils.update_audit_comment`<a id="nocodbutilsupdate_audit_comment"></a>

Update comment in Audit

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_audit_comment_response = nocodb.utils.update_audit_comment(
    audit_id="adt_zlskd6rlf3liay",
    description="This is the comment for the row",
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### audit_id: `str`<a id="audit_id-str"></a>

Audit ID

##### description: `str`<a id="description-str"></a>

Description for the target row

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CommentUpdateReq`](./noco_db_python_sdk/type/comment_update_req.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/audits/{auditId}/comment` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nocodb.utils.update_audit_row`<a id="nocodbutilsupdate_audit_row"></a>

Update Audit Row

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_audit_row_response = nocodb.utils.update_audit_row(
    row_id=None,
    column_name="baz",
    fk_model_id="md_ehn5izr99m7d45",
    row_id="rec0Adp9PMG9o7uJy",
    prev_value=None,
    value=None,
    xc_auth="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### row_id: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./noco_db_python_sdk/type/.py)<a id="row_id-unionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypepy"></a>

Unique Row ID

##### column_name: `str`<a id="column_name-str"></a>

Column Name

##### fk_model_id: `str`<a id="fk_model_id-str"></a>

Foreign Key to Model

##### row_id: `str`<a id="row_id-str"></a>

Row ID

##### prev_value: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./noco_db_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="prev_value-unionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

The previous value before the action

##### value: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./noco_db_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="value-unionbool-date-datetime-dict-float-int-list-str-nonenoco_db_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

The current value after the action

##### xc_auth: `str`<a id="xc_auth-str"></a>

Auth Token is a JWT Token generated based on the logged-in user. By default, the token is only valid for 10 hours. However, you can change the value by defining it using environment variable NC_JWT_EXPIRES_IN.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuditRowUpdateReq`](./noco_db_python_sdk/type/audit_row_update_req.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Audit`](./noco_db_python_sdk/pydantic/audit.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/meta/audits/rows/{rowId}/update` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
