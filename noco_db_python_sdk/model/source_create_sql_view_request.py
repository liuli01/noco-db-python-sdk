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


class SourceCreateSqlViewRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            view_name = schemas.StrSchema
            view_definition = schemas.StrSchema
            __annotations__ = {
                "view_name": view_name,
                "view_definition": view_definition,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["view_name"]) -> MetaOapg.properties.view_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["view_definition"]) -> MetaOapg.properties.view_definition: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["view_name", "view_definition", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["view_name"]) -> typing.Union[MetaOapg.properties.view_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["view_definition"]) -> typing.Union[MetaOapg.properties.view_definition, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["view_name", "view_definition", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        view_name: typing.Union[MetaOapg.properties.view_name, str, schemas.Unset] = schemas.unset,
        view_definition: typing.Union[MetaOapg.properties.view_definition, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SourceCreateSqlViewRequest':
        return super().__new__(
            cls,
            *args,
            view_name=view_name,
            view_definition=view_definition,
            _configuration=_configuration,
            **kwargs,
        )
