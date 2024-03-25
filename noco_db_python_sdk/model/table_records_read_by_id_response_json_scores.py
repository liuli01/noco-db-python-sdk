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


class TableRecordsReadByIdResponseJsonScores(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            math = schemas.NumberSchema
            science = schemas.NumberSchema
            history = schemas.NumberSchema
            __annotations__ = {
                "math": math,
                "science": science,
                "history": history,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["math"]) -> MetaOapg.properties.math: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["science"]) -> MetaOapg.properties.science: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["history"]) -> MetaOapg.properties.history: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["math", "science", "history", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["math"]) -> typing.Union[MetaOapg.properties.math, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["science"]) -> typing.Union[MetaOapg.properties.science, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["history"]) -> typing.Union[MetaOapg.properties.history, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["math", "science", "history", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        math: typing.Union[MetaOapg.properties.math, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        science: typing.Union[MetaOapg.properties.science, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        history: typing.Union[MetaOapg.properties.history, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TableRecordsReadByIdResponseJsonScores':
        return super().__new__(
            cls,
            *args,
            math=math,
            science=science,
            history=history,
            _configuration=_configuration,
            **kwargs,
        )
