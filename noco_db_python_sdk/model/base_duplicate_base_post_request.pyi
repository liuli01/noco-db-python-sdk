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


class BaseDuplicateBasePostRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def options() -> typing.Type['BaseDuplicateBasePostRequestOptions']:
                return BaseDuplicateBasePostRequestOptions
            base = schemas.DictSchema
            __annotations__ = {
                "options": options,
                "base": base,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> 'BaseDuplicateBasePostRequestOptions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["base"]) -> MetaOapg.properties.base: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["options", "base", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> typing.Union['BaseDuplicateBasePostRequestOptions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["base"]) -> typing.Union[MetaOapg.properties.base, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["options", "base", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        options: typing.Union['BaseDuplicateBasePostRequestOptions', schemas.Unset] = schemas.unset,
        base: typing.Union[MetaOapg.properties.base, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BaseDuplicateBasePostRequest':
        return super().__new__(
            cls,
            *args,
            options=options,
            base=base,
            _configuration=_configuration,
            **kwargs,
        )

from noco_db_python_sdk.model.base_duplicate_base_post_request_options import BaseDuplicateBasePostRequestOptions
