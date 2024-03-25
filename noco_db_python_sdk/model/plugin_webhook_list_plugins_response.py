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


class PluginWebhookListPluginsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class _list(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    unique_items = True
                    min_items = 1
                    
                    @staticmethod
                    def items() -> typing.Type['Plugin']:
                        return Plugin
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Plugin'], typing.List['Plugin']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> '_list':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Plugin':
                    return super().__getitem__(i)
        
            @staticmethod
            def pageInfo() -> typing.Type['Paginated']:
                return Paginated
            __annotations__ = {
                "list": _list,
                "pageInfo": pageInfo,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["list"]) -> MetaOapg.properties._list: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageInfo"]) -> 'Paginated': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["list", "pageInfo", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["list"]) -> typing.Union[MetaOapg.properties._list, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageInfo"]) -> typing.Union['Paginated', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["list", "pageInfo", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        pageInfo: typing.Union['Paginated', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PluginWebhookListPluginsResponse':
        return super().__new__(
            cls,
            *args,
            pageInfo=pageInfo,
            _configuration=_configuration,
            **kwargs,
        )

from noco_db_python_sdk.model.paginated import Paginated
from noco_db_python_sdk.model.plugin import Plugin
