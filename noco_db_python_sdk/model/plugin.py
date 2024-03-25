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


class Plugin(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Model for Plugin
    """


    class MetaOapg:
        
        class properties:
            tags = schemas.StrSchema
            title = schemas.StrSchema
            description = schemas.StrSchema
            version = schemas.StrSchema
        
            @staticmethod
            def active() -> typing.Type['ModelBool']:
                return ModelBool
            category = schemas.StrSchema
            creator = schemas.StrSchema
            creator_website = schemas.StrSchema
            docs = schemas.StrSchema
            icon = schemas.StrSchema
        
            @staticmethod
            def id() -> typing.Type['Id']:
                return Id
            
            
            class input(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_1 = schemas.IntSchema
                    
                    @classmethod
                    @functools.lru_cache()
                    def one_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            StringOrNull,
                            cls.one_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'input':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            input_schema = schemas.StrSchema
            logo = schemas.StrSchema
            price = schemas.StrSchema
            rating = schemas.NumberSchema
            status = schemas.StrSchema
            status_details = schemas.StrSchema
            __annotations__ = {
                "tags": tags,
                "title": title,
                "description": description,
                "version": version,
                "active": active,
                "category": category,
                "creator": creator,
                "creator_website": creator_website,
                "docs": docs,
                "icon": icon,
                "id": id,
                "input": input,
                "input_schema": input_schema,
                "logo": logo,
                "price": price,
                "rating": rating,
                "status": status,
                "status_details": status_details,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creator"]) -> MetaOapg.properties.creator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creator_website"]) -> MetaOapg.properties.creator_website: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["docs"]) -> MetaOapg.properties.docs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["icon"]) -> MetaOapg.properties.icon: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'Id': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["input"]) -> MetaOapg.properties.input: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["input_schema"]) -> MetaOapg.properties.input_schema: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logo"]) -> MetaOapg.properties.logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rating"]) -> MetaOapg.properties.rating: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status_details"]) -> MetaOapg.properties.status_details: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tags", "title", "description", "version", "active", "category", "creator", "creator_website", "docs", "icon", "id", "input", "input_schema", "logo", "price", "rating", "status", "status_details", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union[MetaOapg.properties.tags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> typing.Union[MetaOapg.properties.version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> typing.Union[MetaOapg.properties.category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creator"]) -> typing.Union[MetaOapg.properties.creator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creator_website"]) -> typing.Union[MetaOapg.properties.creator_website, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["docs"]) -> typing.Union[MetaOapg.properties.docs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["icon"]) -> typing.Union[MetaOapg.properties.icon, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union['Id', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["input"]) -> typing.Union[MetaOapg.properties.input, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["input_schema"]) -> typing.Union[MetaOapg.properties.input_schema, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logo"]) -> typing.Union[MetaOapg.properties.logo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> typing.Union[MetaOapg.properties.price, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rating"]) -> typing.Union[MetaOapg.properties.rating, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status_details"]) -> typing.Union[MetaOapg.properties.status_details, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tags", "title", "description", "version", "active", "category", "creator", "creator_website", "docs", "icon", "id", "input", "input_schema", "logo", "price", "rating", "status", "status_details", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        tags: typing.Union[MetaOapg.properties.tags, str, schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        version: typing.Union[MetaOapg.properties.version, str, schemas.Unset] = schemas.unset,
        active: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        category: typing.Union[MetaOapg.properties.category, str, schemas.Unset] = schemas.unset,
        creator: typing.Union[MetaOapg.properties.creator, str, schemas.Unset] = schemas.unset,
        creator_website: typing.Union[MetaOapg.properties.creator_website, str, schemas.Unset] = schemas.unset,
        docs: typing.Union[MetaOapg.properties.docs, str, schemas.Unset] = schemas.unset,
        icon: typing.Union[MetaOapg.properties.icon, str, schemas.Unset] = schemas.unset,
        id: typing.Union['Id', schemas.Unset] = schemas.unset,
        input: typing.Union[MetaOapg.properties.input, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        input_schema: typing.Union[MetaOapg.properties.input_schema, str, schemas.Unset] = schemas.unset,
        logo: typing.Union[MetaOapg.properties.logo, str, schemas.Unset] = schemas.unset,
        price: typing.Union[MetaOapg.properties.price, str, schemas.Unset] = schemas.unset,
        rating: typing.Union[MetaOapg.properties.rating, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        status_details: typing.Union[MetaOapg.properties.status_details, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Plugin':
        return super().__new__(
            cls,
            *args,
            tags=tags,
            title=title,
            description=description,
            version=version,
            active=active,
            category=category,
            creator=creator,
            creator_website=creator_website,
            docs=docs,
            icon=icon,
            id=id,
            input=input,
            input_schema=input_schema,
            logo=logo,
            price=price,
            rating=rating,
            status=status,
            status_details=status_details,
            _configuration=_configuration,
            **kwargs,
        )

from noco_db_python_sdk.model.id import Id
from noco_db_python_sdk.model.model_bool import ModelBool
from noco_db_python_sdk.model.string_or_null import StringOrNull