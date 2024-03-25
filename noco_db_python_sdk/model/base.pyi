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


class Base(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Model for Base
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
            description = schemas.StrSchema
            
            
            class sources(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Source']:
                        return Source
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Source'], typing.List['Source']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sources':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Source':
                    return super().__getitem__(i)
            color = schemas.StrSchema
        
            @staticmethod
            def deleted() -> typing.Type['ModelBool']:
                return ModelBool
            id = schemas.StrSchema
        
            @staticmethod
            def is_meta() -> typing.Type['ModelBool']:
                return ModelBool
        
            @staticmethod
            def meta() -> typing.Type['Meta']:
                return Meta
            order = schemas.NumberSchema
            prefix = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DATABASE(cls):
                    return cls("database")
                
                @schemas.classproperty
                def DOCUMENTATION(cls):
                    return cls("documentation")
                
                @schemas.classproperty
                def DASHBOARD(cls):
                    return cls("dashboard")
            
            
            class linked_db_projects(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Base']:
                        return Base
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Base'], typing.List['Base']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'linked_db_projects':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Base':
                    return super().__getitem__(i)
            status = schemas.StrSchema
            __annotations__ = {
                "title": title,
                "description": description,
                "sources": sources,
                "color": color,
                "deleted": deleted,
                "id": id,
                "is_meta": is_meta,
                "meta": meta,
                "order": order,
                "prefix": prefix,
                "type": type,
                "linked_db_projects": linked_db_projects,
                "status": status,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sources"]) -> MetaOapg.properties.sources: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleted"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_meta"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'Meta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prefix"]) -> MetaOapg.properties.prefix: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["linked_db_projects"]) -> MetaOapg.properties.linked_db_projects: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "description", "sources", "color", "deleted", "id", "is_meta", "meta", "order", "prefix", "type", "linked_db_projects", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sources"]) -> typing.Union[MetaOapg.properties.sources, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> typing.Union[MetaOapg.properties.color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleted"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_meta"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['Meta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> typing.Union[MetaOapg.properties.order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prefix"]) -> typing.Union[MetaOapg.properties.prefix, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["linked_db_projects"]) -> typing.Union[MetaOapg.properties.linked_db_projects, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "description", "sources", "color", "deleted", "id", "is_meta", "meta", "order", "prefix", "type", "linked_db_projects", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        sources: typing.Union[MetaOapg.properties.sources, list, tuple, schemas.Unset] = schemas.unset,
        color: typing.Union[MetaOapg.properties.color, str, schemas.Unset] = schemas.unset,
        deleted: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        is_meta: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        meta: typing.Union['Meta', schemas.Unset] = schemas.unset,
        order: typing.Union[MetaOapg.properties.order, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        prefix: typing.Union[MetaOapg.properties.prefix, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        linked_db_projects: typing.Union[MetaOapg.properties.linked_db_projects, list, tuple, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Base':
        return super().__new__(
            cls,
            *args,
            title=title,
            description=description,
            sources=sources,
            color=color,
            deleted=deleted,
            id=id,
            is_meta=is_meta,
            meta=meta,
            order=order,
            prefix=prefix,
            type=type,
            linked_db_projects=linked_db_projects,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from noco_db_python_sdk.model.meta import Meta
from noco_db_python_sdk.model.model_bool import ModelBool
from noco_db_python_sdk.model.source import Source
