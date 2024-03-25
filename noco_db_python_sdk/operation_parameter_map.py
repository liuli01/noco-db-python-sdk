operation_parameter_map = {
    '/api/v2/meta/bases/{baseId}/api-tokens-POST': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/api-tokens/{token}-DELETE': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'token'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/api-tokens-GET': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/users-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'roles'
            },
            {
                'name': 'baseId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/users/{userId}-DELETE': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/users-GET': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/users/{userId}/resend-invite-POST': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/users/{userId}-PATCH': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'roles'
            },
            {
                'name': 'baseId'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/cost-GET': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/has-empty-or-null-filters-GET': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'description'
            },
            {
                'name': 'sources'
            },
            {
                'name': 'color'
            },
            {
                'name': 'status'
            },
            {
                'name': 'type'
            },
            {
                'name': 'linked_db_project_ids'
            },
            {
                'name': 'meta'
            },
            {
                'name': 'external'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/shared-POST': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'password'
            },
            {
                'name': 'roles'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/visibility-rules-POST': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/shared-DELETE': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/duplicate/{baseId}-POST': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'options'
            },
            {
                'name': 'base'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/duplicate/{baseId}/{sourceId}-POST': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'options'
            },
            {
                'name': 'base'
            },
            {
                'name': 'xc-auth'
            },
            {
                'name': 'sourceId'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}-GET': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/info-GET': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/shared-GET': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/visibility-rules-GET': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'includeM2M'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/audits-GET': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'sourceId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases-GET': {
        'parameters': [
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/meta-diff-GET': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}-DELETE': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/meta-diff-POST': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}-PATCH': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'title'
            },
            {
                'name': 'color'
            },
            {
                'name': 'meta'
            },
            {
                'name': 'status'
            },
            {
                'name': 'linked_db_project_ids'
            },
            {
                'name': 'order'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/user-PATCH': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'starred'
            },
            {
                'name': 'order'
            },
            {
                'name': 'hidden'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/shared-PATCH': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'password'
            },
            {
                'name': 'roles'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/tables-POST': {
        'parameters': [
            {
                'name': 'columns'
            },
            {
                'name': 'table_name'
            },
            {
                'name': 'baseId'
            },
            {
                'name': 'title'
            },
            {
                'name': 'meta'
            },
            {
                'name': 'order'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/tables/{tableId}-DELETE': {
        'parameters': [
            {
                'name': 'tableId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/duplicate/{baseId}/table/{tableId}-POST': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'tableId'
            },
            {
                'name': 'options'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/tables-GET': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'xc-auth'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'includeM2M'
            },
        ]
    },
    '/api/v2/meta/tables/{tableId}-GET': {
        'parameters': [
            {
                'name': 'tableId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/tables/{tableId}-PATCH': {
        'parameters': [
            {
                'name': 'tableId'
            },
            {
                'name': 'title'
            },
            {
                'name': 'table_name'
            },
            {
                'name': 'base_id'
            },
            {
                'name': 'meta'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/tables/{tableId}/reorder-POST': {
        'parameters': [
            {
                'name': 'tableId'
            },
            {
                'name': 'order'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/tables/{tableId}/columns/bulk-POST': {
        'parameters': [
            {
                'name': 'tableId'
            },
            {
                'name': 'hash'
            },
            {
                'name': 'ops'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/tables/{tableId}/columns-POST': {
        'parameters': [
            {
                'name': 'tableId'
            },
            {
                'name': 'title'
            },
            {
                'name': 'formula'
            },
            {
                'name': 'formula_raw'
            },
            {
                'name': 'uidt'
            },
            {
                'name': 'childId'
            },
            {
                'name': 'parentId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'virtual'
            },
            {
                'name': 'fk_lookup_column_id'
            },
            {
                'name': 'fk_relation_column_id'
            },
            {
                'name': 'ai'
            },
            {
                'name': 'au'
            },
            {
                'name': 'cc'
            },
            {
                'name': 'cdf'
            },
            {
                'name': 'column_name'
            },
            {
                'name': 'csn'
            },
            {
                'name': 'dt'
            },
            {
                'name': 'dtx'
            },
            {
                'name': 'dtxp'
            },
            {
                'name': 'dtxs'
            },
            {
                'name': 'np'
            },
            {
                'name': 'ns'
            },
            {
                'name': 'pk'
            },
            {
                'name': 'pv'
            },
            {
                'name': 'rqd'
            },
            {
                'name': 'un'
            },
            {
                'name': 'unique'
            },
            {
                'name': 'fk_rollup_column_id'
            },
            {
                'name': 'rollup_function'
            },
            {
                'name': 'column_order'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/columns/{columnId}-DELETE': {
        'parameters': [
            {
                'name': 'columnId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/columns/{columnId}-GET': {
        'parameters': [
            {
                'name': 'columnId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/tables/{tableId}/columns/hash-GET': {
        'parameters': [
            {
                'name': 'tableId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/columns/{columnId}/primary-POST': {
        'parameters': [
            {
                'name': 'columnId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/columns/{columnId}-PATCH': {
        'parameters': [
            {
                'name': 'columnId'
            },
            {
                'name': 'title'
            },
            {
                'name': 'formula'
            },
            {
                'name': 'formula_raw'
            },
            {
                'name': 'uidt'
            },
            {
                'name': 'childId'
            },
            {
                'name': 'parentId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'virtual'
            },
            {
                'name': 'fk_lookup_column_id'
            },
            {
                'name': 'fk_relation_column_id'
            },
            {
                'name': 'ai'
            },
            {
                'name': 'au'
            },
            {
                'name': 'cc'
            },
            {
                'name': 'cdf'
            },
            {
                'name': 'column_name'
            },
            {
                'name': 'csn'
            },
            {
                'name': 'dt'
            },
            {
                'name': 'dtx'
            },
            {
                'name': 'dtxp'
            },
            {
                'name': 'dtxs'
            },
            {
                'name': 'np'
            },
            {
                'name': 'ns'
            },
            {
                'name': 'pk'
            },
            {
                'name': 'pv'
            },
            {
                'name': 'rqd'
            },
            {
                'name': 'un'
            },
            {
                'name': 'unique'
            },
            {
                'name': 'fk_rollup_column_id'
            },
            {
                'name': 'rollup_function'
            },
            {
                'name': 'column_order'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/views/{viewId}/filters-POST': {
        'parameters': [
            {
                'name': 'viewId'
            },
            {
                'name': 'comparison_op'
            },
            {
                'name': 'comparison_sub_op'
            },
            {
                'name': 'fk_column_id'
            },
            {
                'name': 'fk_parent_id'
            },
            {
                'name': 'is_group'
            },
            {
                'name': 'logical_op'
            },
            {
                'name': 'value'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/filters/{filterId}-DELETE': {
        'parameters': [
            {
                'name': 'filterId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/filters/{filterId}-GET': {
        'parameters': [
            {
                'name': 'filterId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/filters/{filterGroupId}/children-GET': {
        'parameters': [
            {
                'name': 'filterGroupId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/views/{viewId}/filters-GET': {
        'parameters': [
            {
                'name': 'viewId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/filters/{filterId}-PATCH': {
        'parameters': [
            {
                'name': 'filterId'
            },
            {
                'name': 'comparison_op'
            },
            {
                'name': 'comparison_sub_op'
            },
            {
                'name': 'fk_column_id'
            },
            {
                'name': 'fk_parent_id'
            },
            {
                'name': 'is_group'
            },
            {
                'name': 'logical_op'
            },
            {
                'name': 'value'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/sorts/{sortId}-DELETE': {
        'parameters': [
            {
                'name': 'sortId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/views/{viewId}/sorts-GET': {
        'parameters': [
            {
                'name': 'viewId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/sorts/{sortId}-GET': {
        'parameters': [
            {
                'name': 'sortId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/sorts/{sortId}-PATCH': {
        'parameters': [
            {
                'name': 'sortId'
            },
            {
                'name': 'fk_column_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/views/{viewId}/sorts-POST': {
        'parameters': [
            {
                'name': 'viewId'
            },
            {
                'name': 'fk_column_id'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'push_to_top'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/tables/{tableId}/hooks-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'event'
            },
            {
                'name': 'notification'
            },
            {
                'name': 'operation'
            },
            {
                'name': 'tableId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'active'
            },
            {
                'name': 'async'
            },
            {
                'name': 'env'
            },
            {
                'name': 'fk_model_id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'retries'
            },
            {
                'name': 'retry_interval'
            },
            {
                'name': 'timeout'
            },
            {
                'name': 'type'
            },
            {
                'name': 'condition'
            },
        ]
    },
    '/api/v2/meta/hooks/{hookId}-DELETE': {
        'parameters': [
            {
                'name': 'hookId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/tables/{tableId}/hooks/samplePayload/{operation}/{version}-GET': {
        'parameters': [
            {
                'name': 'tableId'
            },
            {
                'name': 'operation'
            },
            {
                'name': 'version'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/tables/{tableId}/hooks-GET': {
        'parameters': [
            {
                'name': 'tableId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/tables/{tableId}/hooks/test-POST': {
        'parameters': [
            {
                'name': 'hook'
            },
            {
                'name': 'payload'
            },
            {
                'name': 'tableId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/hooks/{hookId}-PATCH': {
        'parameters': [
            {
                'name': 'hookId'
            },
            {
                'name': 'title'
            },
            {
                'name': 'description'
            },
            {
                'name': 'version'
            },
            {
                'name': 'active'
            },
            {
                'name': 'async'
            },
            {
                'name': 'env'
            },
            {
                'name': 'event'
            },
            {
                'name': 'fk_model_id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'notification'
            },
            {
                'name': 'operation'
            },
            {
                'name': 'retries'
            },
            {
                'name': 'retry_interval'
            },
            {
                'name': 'timeout'
            },
            {
                'name': 'type'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/hooks/{hookId}/filters-POST': {
        'parameters': [
            {
                'name': 'hookId'
            },
            {
                'name': 'comparison_op'
            },
            {
                'name': 'comparison_sub_op'
            },
            {
                'name': 'fk_column_id'
            },
            {
                'name': 'fk_parent_id'
            },
            {
                'name': 'is_group'
            },
            {
                'name': 'logical_op'
            },
            {
                'name': 'value'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/hooks/{hookId}/filters-GET': {
        'parameters': [
            {
                'name': 'hookId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/hooks/{hookId}/logs-GET': {
        'parameters': [
            {
                'name': 'hookId'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/tables/{tableId}/forms-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'tableId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'copy_from_id'
            },
            {
                'name': 'fk_grp_col_id'
            },
            {
                'name': 'fk_geo_data_col_id'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/tables/{tableId}/galleries-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'tableId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'copy_from_id'
            },
            {
                'name': 'fk_grp_col_id'
            },
            {
                'name': 'fk_geo_data_col_id'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/tables/{tableId}/grids-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'tableId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'copy_from_id'
            },
            {
                'name': 'fk_grp_col_id'
            },
            {
                'name': 'fk_geo_data_col_id'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/tables/{tableId}/kanbans-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'tableId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'copy_from_id'
            },
            {
                'name': 'fk_grp_col_id'
            },
            {
                'name': 'fk_geo_data_col_id'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/tables/{tableId}/maps-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'tableId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'copy_from_id'
            },
            {
                'name': 'fk_grp_col_id'
            },
            {
                'name': 'fk_geo_data_col_id'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/views/{viewId}-DELETE': {
        'parameters': [
            {
                'name': 'viewId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/forms/{formViewId}-GET': {
        'parameters': [
            {
                'name': 'formViewId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/galleries/{galleryViewId}-GET': {
        'parameters': [
            {
                'name': 'galleryViewId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/maps/{mapViewId}-GET': {
        'parameters': [
            {
                'name': 'mapViewId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/views/{viewId}/hide-all-POST': {
        'parameters': [
            {
                'name': 'viewId'
            },
            {
                'name': 'ignoreIds'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/kanbans/{kanbanViewId}-GET': {
        'parameters': [
            {
                'name': 'kanbanViewId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/grids/{gridId}/grid-columns-GET': {
        'parameters': [
            {
                'name': 'gridId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/tables/{tableId}/views-GET': {
        'parameters': [
            {
                'name': 'tableId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/views/{viewId}/show-all-POST': {
        'parameters': [
            {
                'name': 'viewId'
            },
            {
                'name': 'ignoreIds'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/views/{viewId}-PATCH': {
        'parameters': [
            {
                'name': 'viewId'
            },
            {
                'name': 'title'
            },
            {
                'name': 'uuid'
            },
            {
                'name': 'password'
            },
            {
                'name': 'lock_type'
            },
            {
                'name': 'meta'
            },
            {
                'name': 'order'
            },
            {
                'name': 'show_system_fields'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/form-columns/{formViewColumnId}-PATCH': {
        'parameters': [
            {
                'name': 'formViewColumnId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'help'
            },
            {
                'name': 'label'
            },
            {
                'name': 'meta'
            },
            {
                'name': 'order'
            },
            {
                'name': 'required'
            },
            {
                'name': 'show'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/forms/{formViewId}-PATCH': {
        'parameters': [
            {
                'name': 'formViewId'
            },
            {
                'name': 'banner_image_url'
            },
            {
                'name': 'email'
            },
            {
                'name': 'heading'
            },
            {
                'name': 'logo_url'
            },
            {
                'name': 'meta'
            },
            {
                'name': 'redirect_after_secs'
            },
            {
                'name': 'redirect_url'
            },
            {
                'name': 'show_blank_form'
            },
            {
                'name': 'subheading'
            },
            {
                'name': 'submit_another_form'
            },
            {
                'name': 'success_msg'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/galleries/{galleryViewId}-PATCH': {
        'parameters': [
            {
                'name': 'galleryViewId'
            },
            {
                'name': 'fk_cover_image_col_id'
            },
            {
                'name': 'meta'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/grid-columns/{columnId}-PATCH': {
        'parameters': [
            {
                'name': 'columnId'
            },
            {
                'name': 'fk_column_id'
            },
            {
                'name': 'help'
            },
            {
                'name': 'label'
            },
            {
                'name': 'width'
            },
            {
                'name': 'group_by'
            },
            {
                'name': 'group_by_order'
            },
            {
                'name': 'group_by_sort'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/grids/{viewId}-PATCH': {
        'parameters': [
            {
                'name': 'viewId'
            },
            {
                'name': 'row_height'
            },
            {
                'name': 'meta'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/kanbans/{kanbanViewId}-PATCH': {
        'parameters': [
            {
                'name': 'kanbanViewId'
            },
            {
                'name': 'fk_grp_col_id'
            },
            {
                'name': 'fk_cover_image_col_id'
            },
            {
                'name': 'meta'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/maps/{mapViewId}-PATCH': {
        'parameters': [
            {
                'name': 'mapViewId'
            },
            {
                'name': 'fk_geo_data_col_id'
            },
            {
                'name': 'meta'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/views/{viewId}/columns-POST': {
        'parameters': [
            {
                'name': 'viewId'
            },
            {
                'name': 'fk_column_id'
            },
            {
                'name': 'show'
            },
            {
                'name': 'order'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/views/{viewId}/columns-GET': {
        'parameters': [
            {
                'name': 'viewId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/views/{viewId}/columns/{columnId}-PATCH': {
        'parameters': [
            {
                'name': 'viewId'
            },
            {
                'name': 'columnId'
            },
            {
                'name': 'show'
            },
            {
                'name': 'order'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/views/{viewId}/share-POST': {
        'parameters': [
            {
                'name': 'viewId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/views/{viewId}/share-DELETE': {
        'parameters': [
            {
                'name': 'viewId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/tables/{tableId}/share-GET': {
        'parameters': [
            {
                'name': 'tableId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/views/{viewId}/share-PATCH': {
        'parameters': [
            {
                'name': 'viewId'
            },
            {
                'name': 'meta'
            },
            {
                'name': 'password'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/plugins/{pluginId}-GET': {
        'parameters': [
            {
                'name': 'pluginId'
            },
        ]
    },
    '/api/v2/meta/plugins/{pluginTitle}/status-GET': {
        'parameters': [
            {
                'name': 'pluginTitle'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/plugins-GET': {
        'parameters': [
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/plugins/test-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'input'
            },
            {
                'name': 'category'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/plugins/{pluginId}-PATCH': {
        'parameters': [
            {
                'name': 'pluginId'
            },
            {
                'name': 'active'
            },
            {
                'name': 'input'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/plugins/webhook-GET': {
        'parameters': [
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/public/calendar-view/{sharedViewUuid}/countByDate-GET': {
        'parameters': [
            {
                'name': 'sharedViewUuid'
            },
            {
                'name': 'xc-password'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'where'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/public/calendar-view/{sharedViewUuid}-GET': {
        'parameters': [
            {
                'name': 'sharedViewUuid'
            },
            {
                'name': 'xc-password'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'from_date'
            },
            {
                'name': 'to_date'
            },
            {
                'name': 'where'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'sortArrJson'
            },
            {
                'name': 'filterArrJson'
            },
        ]
    },
    '/api/v2/public/shared-view/{sharedViewUuid}/rows-POST': {
        'parameters': [
            {
                'name': 'sharedViewUuid'
            },
            {
                'name': 'xc-password'
            },
        ]
    },
    '/api/v2/public/shared-view/{sharedViewUuid}/rows/{rowId}/{relationType}/{columnName}-GET': {
        'parameters': [
            {
                'name': 'sharedViewUuid'
            },
            {
                'name': 'rowId'
            },
            {
                'name': 'relationType'
            },
            {
                'name': 'columnName'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'where'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'sortArrJson'
            },
            {
                'name': 'filterArrJson'
            },
        ]
    },
    '/api/v2/public/shared-view/{sharedViewUuid}/rows-GET': {
        'parameters': [
            {
                'name': 'sharedViewUuid'
            },
            {
                'name': 'xc-password'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'where'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'sortArrJson'
            },
            {
                'name': 'filterArrJson'
            },
            {
                'name': 'pks'
            },
        ]
    },
    '/api/v2/public/shared-view/{sharedViewUuid}/groupby-GET': {
        'parameters': [
            {
                'name': 'sharedViewUuid'
            },
            {
                'name': 'xc-password'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'where'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'sortArrJson'
            },
            {
                'name': 'filterArrJson'
            },
            {
                'name': 'column_name'
            },
        ]
    },
    '/api/v2/public/shared-view/{sharedViewUuid}/nested/{columnName}-GET': {
        'parameters': [
            {
                'name': 'sharedViewUuid'
            },
            {
                'name': 'columnName'
            },
            {
                'name': 'xc-password'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'where'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'sortArrJson'
            },
            {
                'name': 'filterArrJson'
            },
        ]
    },
    '/api/v2/public/shared-view/{sharedViewUuid}/rows/export/{type}-GET': {
        'parameters': [
            {
                'name': 'sharedViewUuid'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v2/public/shared-base/{sharedBaseUuid}/meta-GET': {
        'parameters': [
            {
                'name': 'sharedBaseUuid'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/public/shared-erd/{sharedErdUuid}/meta-GET': {
        'parameters': [
            {
                'name': 'sharedErdUuid'
            },
        ]
    },
    '/api/v2/public/shared-view/{sharedViewUuid}/group/{columnId}-GET': {
        'parameters': [
            {
                'name': 'sharedViewUuid'
            },
            {
                'name': 'columnId'
            },
            {
                'name': 'xc-password'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'where'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'sortArrJson'
            },
            {
                'name': 'filterArrJson'
            },
        ]
    },
    '/api/v2/public/shared-view/{sharedViewUuid}/meta-GET': {
        'parameters': [
            {
                'name': 'sharedViewUuid'
            },
            {
                'name': 'xc-password'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/sources-GET': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/sources/{sourceId}/share/erd-POST': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'sourceId'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/sources-POST': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'alias'
            },
            {
                'name': 'config'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'id'
            },
            {
                'name': 'inflection_column'
            },
            {
                'name': 'inflection_table'
            },
            {
                'name': 'is_meta'
            },
            {
                'name': 'is_local'
            },
            {
                'name': 'order'
            },
            {
                'name': 'base_id'
            },
            {
                'name': 'type'
            },
            {
                'name': 'external'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/:baseId/sources/:sourceId/sqlView-POST': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'sourceId'
            },
            {
                'name': 'view_name'
            },
            {
                'name': 'view_definition'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/{sourceId}/tables-POST': {
        'parameters': [
            {
                'name': 'columns'
            },
            {
                'name': 'table_name'
            },
            {
                'name': 'baseId'
            },
            {
                'name': 'sourceId'
            },
            {
                'name': 'title'
            },
            {
                'name': 'meta'
            },
            {
                'name': 'order'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/sources/{sourceId}-DELETE': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'sourceId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/sources/{sourceId}/share/erd-DELETE': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'sourceId'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/sources/{sourceId}-GET': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'sourceId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/meta-diff/{sourceId}-GET': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'sourceId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/{sourceId}/tables-GET': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'sourceId'
            },
            {
                'name': 'xc-auth'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'includeM2M'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/meta-diff/{sourceId}-POST': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'sourceId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/bases/{baseId}/sources/{sourceId}-PATCH': {
        'parameters': [
            {
                'name': 'baseId'
            },
            {
                'name': 'sourceId'
            },
            {
                'name': 'alias'
            },
            {
                'name': 'type'
            },
            {
                'name': 'config'
            },
            {
                'name': 'inflection_column'
            },
            {
                'name': 'inflection_table'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/storage/upload-POST': {
        'parameters': [
            {
                'name': 'path'
            },
            {
                'name': 'xc-auth'
            },
            {
                'name': 'title'
            },
            {
                'name': 'mimetype'
            },
            {
                'name': 'path'
            },
            {
                'name': 'size'
            },
            {
                'name': 'url'
            },
        ]
    },
    '/api/v2/storage/upload-by-url-POST': {
        'parameters': [
            {
                'name': 'path'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/tables/{tableId}/records-POST': {
        'parameters': [
            {
                'name': 'tableId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/tables/{tableId}/records-DELETE': {
        'parameters': [
            {
                'name': 'tableId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/tables/{tableId}/records/count-GET': {
        'parameters': [
            {
                'name': 'tableId'
            },
            {
                'name': 'viewId'
            },
            {
                'name': 'where'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/tables/{tableId}/links/{linkFieldId}/records/{recordId}-POST': {
        'parameters': [
            {
                'name': 'tableId'
            },
            {
                'name': 'linkFieldId'
            },
            {
                'name': 'recordId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/tables/{tableId}/records-GET': {
        'parameters': [
            {
                'name': 'tableId'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'where'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'viewId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/tables/{tableId}/links/{linkFieldId}/records/{recordId}-GET': {
        'parameters': [
            {
                'name': 'tableId'
            },
            {
                'name': 'linkFieldId'
            },
            {
                'name': 'recordId'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'where'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/tables/{tableId}/records/{recordId}-GET': {
        'parameters': [
            {
                'name': 'tableId'
            },
            {
                'name': 'recordId'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/tables/{tableId}/links/{linkFieldId}/records/{recordId}-DELETE': {
        'parameters': [
            {
                'name': 'tableId'
            },
            {
                'name': 'linkFieldId'
            },
            {
                'name': 'recordId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/tables/{tableId}/records-PATCH': {
        'parameters': [
            {
                'name': 'tableId'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/cache-DELETE': {
        'parameters': [
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/audits/comments/count-GET': {
        'parameters': [
            {
                'name': 'ids'
            },
            {
                'name': 'fk_model_id'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/audits/comments-POST': {
        'parameters': [
            {
                'name': 'fk_model_id'
            },
            {
                'name': 'row_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/cache-GET': {
        'parameters': [
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/nocodb/info-GET': {
        'parameters': [
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/audits/comments-GET': {
        'parameters': [
            {
                'name': 'row_id'
            },
            {
                'name': 'fk_model_id'
            },
            {
                'name': 'xc-auth'
            },
            {
                'name': 'comments_only'
            },
        ]
    },
    '/api/v2/meta/axiosRequestMake-POST': {
        'parameters': [
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/connection/select-POST': {
        'parameters': [
        ]
    },
    '/api/v2/meta/connection/test-POST': {
        'parameters': [
            {
                'name': 'client'
            },
            {
                'name': 'connection'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/audits/{auditId}/comment-PATCH': {
        'parameters': [
            {
                'name': 'auditId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
    '/api/v2/meta/audits/rows/{rowId}/update-POST': {
        'parameters': [
            {
                'name': 'rowId'
            },
            {
                'name': 'column_name'
            },
            {
                'name': 'fk_model_id'
            },
            {
                'name': 'row_id'
            },
            {
                'name': 'prev_value'
            },
            {
                'name': 'value'
            },
            {
                'name': 'xc-auth'
            },
        ]
    },
};