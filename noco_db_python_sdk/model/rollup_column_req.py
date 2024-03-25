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


class RollupColumnReq(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Model for Rollup Column Request
    """


    class MetaOapg:
        
        class properties:
            
            
            class title(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
        
            @staticmethod
            def fk_relation_column_id() -> typing.Type['Id']:
                return Id
        
            @staticmethod
            def fk_rollup_column_id() -> typing.Type['Id']:
                return Id
            
            
            class rollup_function(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "avg": "AVG",
                        "avgDistinct": "AVG_DISTINCT",
                        "count": "COUNT",
                        "countDistinct": "COUNT_DISTINCT",
                        "max": "MAX",
                        "min": "MIN",
                        "sum": "SUM",
                        "sumDistinct": "SUM_DISTINCT",
                    }
                
                @schemas.classproperty
                def AVG(cls):
                    return cls("avg")
                
                @schemas.classproperty
                def AVG_DISTINCT(cls):
                    return cls("avgDistinct")
                
                @schemas.classproperty
                def COUNT(cls):
                    return cls("count")
                
                @schemas.classproperty
                def COUNT_DISTINCT(cls):
                    return cls("countDistinct")
                
                @schemas.classproperty
                def MAX(cls):
                    return cls("max")
                
                @schemas.classproperty
                def MIN(cls):
                    return cls("min")
                
                @schemas.classproperty
                def SUM(cls):
                    return cls("sum")
                
                @schemas.classproperty
                def SUM_DISTINCT(cls):
                    return cls("sumDistinct")
            
            
            class uidt(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Rollup": "ROLLUP",
                    }
                
                @schemas.classproperty
                def ROLLUP(cls):
                    return cls("Rollup")
            __annotations__ = {
                "title": title,
                "fk_relation_column_id": fk_relation_column_id,
                "fk_rollup_column_id": fk_rollup_column_id,
                "rollup_function": rollup_function,
                "uidt": uidt,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fk_relation_column_id"]) -> 'Id': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fk_rollup_column_id"]) -> 'Id': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rollup_function"]) -> MetaOapg.properties.rollup_function: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uidt"]) -> MetaOapg.properties.uidt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "fk_relation_column_id", "fk_rollup_column_id", "rollup_function", "uidt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fk_relation_column_id"]) -> typing.Union['Id', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fk_rollup_column_id"]) -> typing.Union['Id', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rollup_function"]) -> typing.Union[MetaOapg.properties.rollup_function, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uidt"]) -> typing.Union[MetaOapg.properties.uidt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "fk_relation_column_id", "fk_rollup_column_id", "rollup_function", "uidt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        fk_relation_column_id: typing.Union['Id', schemas.Unset] = schemas.unset,
        fk_rollup_column_id: typing.Union['Id', schemas.Unset] = schemas.unset,
        rollup_function: typing.Union[MetaOapg.properties.rollup_function, str, schemas.Unset] = schemas.unset,
        uidt: typing.Union[MetaOapg.properties.uidt, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RollupColumnReq':
        return super().__new__(
            cls,
            *args,
            title=title,
            fk_relation_column_id=fk_relation_column_id,
            fk_rollup_column_id=fk_rollup_column_id,
            rollup_function=rollup_function,
            uidt=uidt,
            _configuration=_configuration,
            **kwargs,
        )

from noco_db_python_sdk.model.id import Id