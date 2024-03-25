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


class ProjectEvent(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "body",
            "type",
            "fk_user_id",
        }
        
        class properties:
            fk_user_id = schemas.StrSchema
            type = schemas.StrSchema
        
            @staticmethod
            def body() -> typing.Type['ProjectEventBody']:
                return ProjectEventBody
            __annotations__ = {
                "fk_user_id": fk_user_id,
                "type": type,
                "body": body,
            }
    
    body: 'ProjectEventBody'
    type: MetaOapg.properties.type
    fk_user_id: MetaOapg.properties.fk_user_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fk_user_id"]) -> MetaOapg.properties.fk_user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> 'ProjectEventBody': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["fk_user_id", "type", "body", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fk_user_id"]) -> MetaOapg.properties.fk_user_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> 'ProjectEventBody': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["fk_user_id", "type", "body", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        body: 'ProjectEventBody',
        type: typing.Union[MetaOapg.properties.type, str, ],
        fk_user_id: typing.Union[MetaOapg.properties.fk_user_id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectEvent':
        return super().__new__(
            cls,
            *args,
            body=body,
            type=type,
            fk_user_id=fk_user_id,
            _configuration=_configuration,
            **kwargs,
        )

from noco_db_python_sdk.model.project_event_body import ProjectEventBody
