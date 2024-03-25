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


class HookLog(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Model for Hook Log
    """


    class MetaOapg:
        
        class properties:
            source_id = schemas.StrSchema
            conditions = schemas.StrSchema
        
            @staticmethod
            def error() -> typing.Type['StringOrNull']:
                return StringOrNull
        
            @staticmethod
            def error_code() -> typing.Type['StringOrNull']:
                return StringOrNull
        
            @staticmethod
            def error_message() -> typing.Type['StringOrNull']:
                return StringOrNull
            
            
            class event(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def AFTER(cls):
                    return cls("after")
                
                @schemas.classproperty
                def BEFORE(cls):
                    return cls("before")
            execution_time = schemas.StrSchema
        
            @staticmethod
            def fk_hook_id() -> typing.Type['StringOrNull']:
                return StringOrNull
        
            @staticmethod
            def id() -> typing.Type['StringOrNull']:
                return StringOrNull
            notifications = schemas.StrSchema
            
            
            class operation(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INSERT(cls):
                    return cls("insert")
                
                @schemas.classproperty
                def UPDATE(cls):
                    return cls("update")
                
                @schemas.classproperty
                def DELETE(cls):
                    return cls("delete")
                
                @schemas.classproperty
                def BULK_INSERT(cls):
                    return cls("bulkInsert")
                
                @schemas.classproperty
                def BULK_UPDATE(cls):
                    return cls("bulkUpdate")
                
                @schemas.classproperty
                def BULK_DELETE(cls):
                    return cls("bulkDelete")
            payload = schemas.StrSchema
            base_id = schemas.StrSchema
        
            @staticmethod
            def response() -> typing.Type['StringOrNull']:
                return StringOrNull
        
            @staticmethod
            def test_call() -> typing.Type['ModelBool']:
                return ModelBool
        
            @staticmethod
            def triggered_by() -> typing.Type['StringOrNull']:
                return StringOrNull
            type = schemas.StrSchema
            __annotations__ = {
                "source_id": source_id,
                "conditions": conditions,
                "error": error,
                "error_code": error_code,
                "error_message": error_message,
                "event": event,
                "execution_time": execution_time,
                "fk_hook_id": fk_hook_id,
                "id": id,
                "notifications": notifications,
                "operation": operation,
                "payload": payload,
                "base_id": base_id,
                "response": response,
                "test_call": test_call,
                "triggered_by": triggered_by,
                "type": type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source_id"]) -> MetaOapg.properties.source_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditions"]) -> MetaOapg.properties.conditions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> 'StringOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error_code"]) -> 'StringOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error_message"]) -> 'StringOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event"]) -> MetaOapg.properties.event: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["execution_time"]) -> MetaOapg.properties.execution_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fk_hook_id"]) -> 'StringOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'StringOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notifications"]) -> MetaOapg.properties.notifications: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operation"]) -> MetaOapg.properties.operation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payload"]) -> MetaOapg.properties.payload: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["base_id"]) -> MetaOapg.properties.base_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["response"]) -> 'StringOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["test_call"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["triggered_by"]) -> 'StringOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["source_id", "conditions", "error", "error_code", "error_message", "event", "execution_time", "fk_hook_id", "id", "notifications", "operation", "payload", "base_id", "response", "test_call", "triggered_by", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source_id"]) -> typing.Union[MetaOapg.properties.source_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditions"]) -> typing.Union[MetaOapg.properties.conditions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union['StringOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error_code"]) -> typing.Union['StringOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error_message"]) -> typing.Union['StringOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event"]) -> typing.Union[MetaOapg.properties.event, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["execution_time"]) -> typing.Union[MetaOapg.properties.execution_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fk_hook_id"]) -> typing.Union['StringOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union['StringOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notifications"]) -> typing.Union[MetaOapg.properties.notifications, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operation"]) -> typing.Union[MetaOapg.properties.operation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payload"]) -> typing.Union[MetaOapg.properties.payload, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["base_id"]) -> typing.Union[MetaOapg.properties.base_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["response"]) -> typing.Union['StringOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["test_call"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["triggered_by"]) -> typing.Union['StringOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["source_id", "conditions", "error", "error_code", "error_message", "event", "execution_time", "fk_hook_id", "id", "notifications", "operation", "payload", "base_id", "response", "test_call", "triggered_by", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        source_id: typing.Union[MetaOapg.properties.source_id, str, schemas.Unset] = schemas.unset,
        conditions: typing.Union[MetaOapg.properties.conditions, str, schemas.Unset] = schemas.unset,
        error: typing.Union['StringOrNull', schemas.Unset] = schemas.unset,
        error_code: typing.Union['StringOrNull', schemas.Unset] = schemas.unset,
        error_message: typing.Union['StringOrNull', schemas.Unset] = schemas.unset,
        event: typing.Union[MetaOapg.properties.event, str, schemas.Unset] = schemas.unset,
        execution_time: typing.Union[MetaOapg.properties.execution_time, str, schemas.Unset] = schemas.unset,
        fk_hook_id: typing.Union['StringOrNull', schemas.Unset] = schemas.unset,
        id: typing.Union['StringOrNull', schemas.Unset] = schemas.unset,
        notifications: typing.Union[MetaOapg.properties.notifications, str, schemas.Unset] = schemas.unset,
        operation: typing.Union[MetaOapg.properties.operation, str, schemas.Unset] = schemas.unset,
        payload: typing.Union[MetaOapg.properties.payload, str, schemas.Unset] = schemas.unset,
        base_id: typing.Union[MetaOapg.properties.base_id, str, schemas.Unset] = schemas.unset,
        response: typing.Union['StringOrNull', schemas.Unset] = schemas.unset,
        test_call: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        triggered_by: typing.Union['StringOrNull', schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'HookLog':
        return super().__new__(
            cls,
            *args,
            source_id=source_id,
            conditions=conditions,
            error=error,
            error_code=error_code,
            error_message=error_message,
            event=event,
            execution_time=execution_time,
            fk_hook_id=fk_hook_id,
            id=id,
            notifications=notifications,
            operation=operation,
            payload=payload,
            base_id=base_id,
            response=response,
            test_call=test_call,
            triggered_by=triggered_by,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from noco_db_python_sdk.model.model_bool import ModelBool
from noco_db_python_sdk.model.string_or_null import StringOrNull
