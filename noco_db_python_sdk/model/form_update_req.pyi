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


class FormUpdateReq(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Model for Form Update Request
    """


    class MetaOapg:
        
        class properties:
            
            
            class banner_image_url(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_1 = schemas.NoneSchema
                    
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
                            AttachmentReq,
                            cls.one_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'banner_image_url':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
        
            @staticmethod
            def email() -> typing.Type['StringOrNull']:
                return StringOrNull
            
            
            class heading(
                schemas.StrSchema
            ):
                pass
            
            
            class logo_url(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_1 = schemas.NoneSchema
                    
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
                            AttachmentReq,
                            cls.one_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'logo_url':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
        
            @staticmethod
            def meta() -> typing.Type['Meta']:
                return Meta
        
            @staticmethod
            def redirect_after_secs() -> typing.Type['StringOrNull']:
                return StringOrNull
        
            @staticmethod
            def redirect_url() -> typing.Type['TextOrNull']:
                return TextOrNull
        
            @staticmethod
            def show_blank_form() -> typing.Type['ModelBool']:
                return ModelBool
        
            @staticmethod
            def subheading() -> typing.Type['TextOrNull']:
                return TextOrNull
        
            @staticmethod
            def submit_another_form() -> typing.Type['ModelBool']:
                return ModelBool
        
            @staticmethod
            def success_msg() -> typing.Type['TextOrNull']:
                return TextOrNull
            __annotations__ = {
                "banner_image_url": banner_image_url,
                "email": email,
                "heading": heading,
                "logo_url": logo_url,
                "meta": meta,
                "redirect_after_secs": redirect_after_secs,
                "redirect_url": redirect_url,
                "show_blank_form": show_blank_form,
                "subheading": subheading,
                "submit_another_form": submit_another_form,
                "success_msg": success_msg,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["banner_image_url"]) -> MetaOapg.properties.banner_image_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> 'StringOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["heading"]) -> MetaOapg.properties.heading: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logo_url"]) -> MetaOapg.properties.logo_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'Meta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirect_after_secs"]) -> 'StringOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirect_url"]) -> 'TextOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["show_blank_form"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subheading"]) -> 'TextOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["submit_another_form"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["success_msg"]) -> 'TextOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["banner_image_url", "email", "heading", "logo_url", "meta", "redirect_after_secs", "redirect_url", "show_blank_form", "subheading", "submit_another_form", "success_msg", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["banner_image_url"]) -> typing.Union[MetaOapg.properties.banner_image_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union['StringOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["heading"]) -> typing.Union[MetaOapg.properties.heading, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logo_url"]) -> typing.Union[MetaOapg.properties.logo_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['Meta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirect_after_secs"]) -> typing.Union['StringOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirect_url"]) -> typing.Union['TextOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["show_blank_form"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subheading"]) -> typing.Union['TextOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["submit_another_form"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["success_msg"]) -> typing.Union['TextOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["banner_image_url", "email", "heading", "logo_url", "meta", "redirect_after_secs", "redirect_url", "show_blank_form", "subheading", "submit_another_form", "success_msg", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        banner_image_url: typing.Union[MetaOapg.properties.banner_image_url, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        email: typing.Union['StringOrNull', schemas.Unset] = schemas.unset,
        heading: typing.Union[MetaOapg.properties.heading, str, schemas.Unset] = schemas.unset,
        logo_url: typing.Union[MetaOapg.properties.logo_url, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        meta: typing.Union['Meta', schemas.Unset] = schemas.unset,
        redirect_after_secs: typing.Union['StringOrNull', schemas.Unset] = schemas.unset,
        redirect_url: typing.Union['TextOrNull', schemas.Unset] = schemas.unset,
        show_blank_form: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        subheading: typing.Union['TextOrNull', schemas.Unset] = schemas.unset,
        submit_another_form: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        success_msg: typing.Union['TextOrNull', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FormUpdateReq':
        return super().__new__(
            cls,
            *args,
            banner_image_url=banner_image_url,
            email=email,
            heading=heading,
            logo_url=logo_url,
            meta=meta,
            redirect_after_secs=redirect_after_secs,
            redirect_url=redirect_url,
            show_blank_form=show_blank_form,
            subheading=subheading,
            submit_another_form=submit_another_form,
            success_msg=success_msg,
            _configuration=_configuration,
            **kwargs,
        )

from noco_db_python_sdk.model.attachment_req import AttachmentReq
from noco_db_python_sdk.model.meta import Meta
from noco_db_python_sdk.model.model_bool import ModelBool
from noco_db_python_sdk.model.string_or_null import StringOrNull
from noco_db_python_sdk.model.text_or_null import TextOrNull
