# coding: utf-8

"""
    NocoDB v2

    NocoDB API Documentation

    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from noco_db_python_sdk import schemas  # noqa: F401


class TableRecordsListLinkedRecordsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "pageInfo",
            "list",
        }
        
        class properties:
        
            @staticmethod
            def _list() -> typing.Type['TableRecordsListLinkedRecordsResponseList']:
                return TableRecordsListLinkedRecordsResponseList
        
            @staticmethod
            def pageInfo() -> typing.Type['Paginated']:
                return Paginated
            __annotations__ = {
                "list": _list,
                "pageInfo": pageInfo,
            }
    
    pageInfo: 'Paginated'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["list"]) -> 'TableRecordsListLinkedRecordsResponseList': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageInfo"]) -> 'Paginated': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["list", "pageInfo", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["list"]) -> 'TableRecordsListLinkedRecordsResponseList': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageInfo"]) -> 'Paginated': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["list", "pageInfo", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        pageInfo: 'Paginated',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TableRecordsListLinkedRecordsResponse':
        return super().__new__(
            cls,
            *args,
            pageInfo=pageInfo,
            _configuration=_configuration,
            **kwargs,
        )

from noco_db_python_sdk.model.paginated import Paginated
from noco_db_python_sdk.model.table_records_list_linked_records_response_list import TableRecordsListLinkedRecordsResponseList
