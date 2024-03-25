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


class Column(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Model for Column
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
        
            @staticmethod
            def ai() -> typing.Type['ModelBool']:
                return ModelBool
        
            @staticmethod
            def au() -> typing.Type['ModelBool']:
                return ModelBool
            source_id = schemas.StrSchema
            cc = schemas.StrSchema
        
            @staticmethod
            def cdf() -> typing.Type['StringOrNullOrBooleanOrNumber']:
                return StringOrNullOrBooleanOrNumber
            
            
            class clen(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.IntSchema
                    one_of_1 = schemas.NoneSchema
                    one_of_2 = schemas.StrSchema
                    
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
                            cls.one_of_0,
                            cls.one_of_1,
                            cls.one_of_2,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'clen':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class colOptions(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    any_of_5 = schemas.DictSchema
                    
                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            Formula,
                            LinkToAnotherRecord,
                            Lookup,
                            Rollup,
                            SelectOptions,
                            cls.any_of_5,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'colOptions':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            column_name = schemas.StrSchema
            cop = schemas.StrSchema
        
            @staticmethod
            def csn() -> typing.Type['StringOrNull']:
                return StringOrNull
            ct = schemas.StrSchema
        
            @staticmethod
            def deleted() -> typing.Type['ModelBool']:
                return ModelBool
            dt = schemas.StrSchema
            dtx = schemas.StrSchema
            
            
            class dtxp(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.NoneSchema
                    one_of_1 = schemas.NumberSchema
                    one_of_2 = schemas.StrSchema
                    
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
                            cls.one_of_0,
                            cls.one_of_1,
                            cls.one_of_2,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'dtxp':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class dtxs(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.NoneSchema
                    one_of_1 = schemas.NumberSchema
                    one_of_2 = schemas.StrSchema
                    
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
                            cls.one_of_0,
                            cls.one_of_1,
                            cls.one_of_2,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'dtxs':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            fk_model_id = schemas.StrSchema
        
            @staticmethod
            def id() -> typing.Type['Id']:
                return Id
        
            @staticmethod
            def meta() -> typing.Type['Meta']:
                return Meta
            
            
            class np(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.IntSchema
                    one_of_1 = schemas.NoneSchema
                    one_of_2 = schemas.StrSchema
                    
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
                            cls.one_of_0,
                            cls.one_of_1,
                            cls.one_of_2,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'np':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class ns(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.IntSchema
                    one_of_1 = schemas.NoneSchema
                    one_of_2 = schemas.StrSchema
                    
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
                            cls.one_of_0,
                            cls.one_of_1,
                            cls.one_of_2,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'ns':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            order = schemas.NumberSchema
        
            @staticmethod
            def pk() -> typing.Type['ModelBool']:
                return ModelBool
        
            @staticmethod
            def pv() -> typing.Type['ModelBool']:
                return ModelBool
        
            @staticmethod
            def rqd() -> typing.Type['ModelBool']:
                return ModelBool
        
            @staticmethod
            def system() -> typing.Type['ModelBool']:
                return ModelBool
            
            
            class uidt(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Attachment": "ATTACHMENT",
                        "AutoNumber": "AUTO_NUMBER",
                        "Barcode": "BARCODE",
                        "Button": "BUTTON",
                        "Checkbox": "CHECKBOX",
                        "Collaborator": "COLLABORATOR",
                        "Count": "COUNT",
                        "CreatedTime": "CREATED_TIME",
                        "Currency": "CURRENCY",
                        "Date": "DATE",
                        "DateTime": "DATE_TIME",
                        "Decimal": "DECIMAL",
                        "Duration": "DURATION",
                        "Email": "EMAIL",
                        "Formula": "FORMULA",
                        "ForeignKey": "FOREIGN_KEY",
                        "GeoData": "GEO_DATA",
                        "Geometry": "GEOMETRY",
                        "ID": "ID",
                        "JSON": "JSON",
                        "LastModifiedTime": "LAST_MODIFIED_TIME",
                        "LongText": "LONG_TEXT",
                        "LinkToAnotherRecord": "LINK_TO_ANOTHER_RECORD",
                        "Lookup": "LOOKUP",
                        "MultiSelect": "MULTI_SELECT",
                        "Number": "NUMBER",
                        "Percent": "PERCENT",
                        "PhoneNumber": "PHONE_NUMBER",
                        "Rating": "RATING",
                        "Rollup": "ROLLUP",
                        "SingleLineText": "SINGLE_LINE_TEXT",
                        "SingleSelect": "SINGLE_SELECT",
                        "SpecificDBType": "SPECIFIC_DBTYPE",
                        "Time": "TIME",
                        "URL": "URL",
                        "Year": "YEAR",
                        "QrCode": "QR_CODE",
                        "Links": "LINKS",
                        "User": "USER",
                        "CreatedBy": "CREATED_BY",
                        "LastModifiedBy": "LAST_MODIFIED_BY",
                    }
                
                @schemas.classproperty
                def ATTACHMENT(cls):
                    return cls("Attachment")
                
                @schemas.classproperty
                def AUTO_NUMBER(cls):
                    return cls("AutoNumber")
                
                @schemas.classproperty
                def BARCODE(cls):
                    return cls("Barcode")
                
                @schemas.classproperty
                def BUTTON(cls):
                    return cls("Button")
                
                @schemas.classproperty
                def CHECKBOX(cls):
                    return cls("Checkbox")
                
                @schemas.classproperty
                def COLLABORATOR(cls):
                    return cls("Collaborator")
                
                @schemas.classproperty
                def COUNT(cls):
                    return cls("Count")
                
                @schemas.classproperty
                def CREATED_TIME(cls):
                    return cls("CreatedTime")
                
                @schemas.classproperty
                def CURRENCY(cls):
                    return cls("Currency")
                
                @schemas.classproperty
                def DATE(cls):
                    return cls("Date")
                
                @schemas.classproperty
                def DATE_TIME(cls):
                    return cls("DateTime")
                
                @schemas.classproperty
                def DECIMAL(cls):
                    return cls("Decimal")
                
                @schemas.classproperty
                def DURATION(cls):
                    return cls("Duration")
                
                @schemas.classproperty
                def EMAIL(cls):
                    return cls("Email")
                
                @schemas.classproperty
                def FORMULA(cls):
                    return cls("Formula")
                
                @schemas.classproperty
                def FOREIGN_KEY(cls):
                    return cls("ForeignKey")
                
                @schemas.classproperty
                def GEO_DATA(cls):
                    return cls("GeoData")
                
                @schemas.classproperty
                def GEOMETRY(cls):
                    return cls("Geometry")
                
                @schemas.classproperty
                def ID(cls):
                    return cls("ID")
                
                @schemas.classproperty
                def JSON(cls):
                    return cls("JSON")
                
                @schemas.classproperty
                def LAST_MODIFIED_TIME(cls):
                    return cls("LastModifiedTime")
                
                @schemas.classproperty
                def LONG_TEXT(cls):
                    return cls("LongText")
                
                @schemas.classproperty
                def LINK_TO_ANOTHER_RECORD(cls):
                    return cls("LinkToAnotherRecord")
                
                @schemas.classproperty
                def LOOKUP(cls):
                    return cls("Lookup")
                
                @schemas.classproperty
                def MULTI_SELECT(cls):
                    return cls("MultiSelect")
                
                @schemas.classproperty
                def NUMBER(cls):
                    return cls("Number")
                
                @schemas.classproperty
                def PERCENT(cls):
                    return cls("Percent")
                
                @schemas.classproperty
                def PHONE_NUMBER(cls):
                    return cls("PhoneNumber")
                
                @schemas.classproperty
                def RATING(cls):
                    return cls("Rating")
                
                @schemas.classproperty
                def ROLLUP(cls):
                    return cls("Rollup")
                
                @schemas.classproperty
                def SINGLE_LINE_TEXT(cls):
                    return cls("SingleLineText")
                
                @schemas.classproperty
                def SINGLE_SELECT(cls):
                    return cls("SingleSelect")
                
                @schemas.classproperty
                def SPECIFIC_DBTYPE(cls):
                    return cls("SpecificDBType")
                
                @schemas.classproperty
                def TIME(cls):
                    return cls("Time")
                
                @schemas.classproperty
                def URL(cls):
                    return cls("URL")
                
                @schemas.classproperty
                def YEAR(cls):
                    return cls("Year")
                
                @schemas.classproperty
                def QR_CODE(cls):
                    return cls("QrCode")
                
                @schemas.classproperty
                def LINKS(cls):
                    return cls("Links")
                
                @schemas.classproperty
                def USER(cls):
                    return cls("User")
                
                @schemas.classproperty
                def CREATED_BY(cls):
                    return cls("CreatedBy")
                
                @schemas.classproperty
                def LAST_MODIFIED_BY(cls):
                    return cls("LastModifiedBy")
        
            @staticmethod
            def un() -> typing.Type['ModelBool']:
                return ModelBool
        
            @staticmethod
            def unique() -> typing.Type['ModelBool']:
                return ModelBool
        
            @staticmethod
            def visible() -> typing.Type['ModelBool']:
                return ModelBool
            __annotations__ = {
                "title": title,
                "ai": ai,
                "au": au,
                "source_id": source_id,
                "cc": cc,
                "cdf": cdf,
                "clen": clen,
                "colOptions": colOptions,
                "column_name": column_name,
                "cop": cop,
                "csn": csn,
                "ct": ct,
                "deleted": deleted,
                "dt": dt,
                "dtx": dtx,
                "dtxp": dtxp,
                "dtxs": dtxs,
                "fk_model_id": fk_model_id,
                "id": id,
                "meta": meta,
                "np": np,
                "ns": ns,
                "order": order,
                "pk": pk,
                "pv": pv,
                "rqd": rqd,
                "system": system,
                "uidt": uidt,
                "un": un,
                "unique": unique,
                "visible": visible,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ai"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["au"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source_id"]) -> MetaOapg.properties.source_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cc"]) -> MetaOapg.properties.cc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cdf"]) -> 'StringOrNullOrBooleanOrNumber': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clen"]) -> MetaOapg.properties.clen: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["colOptions"]) -> MetaOapg.properties.colOptions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["column_name"]) -> MetaOapg.properties.column_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cop"]) -> MetaOapg.properties.cop: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["csn"]) -> 'StringOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ct"]) -> MetaOapg.properties.ct: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleted"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dt"]) -> MetaOapg.properties.dt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dtx"]) -> MetaOapg.properties.dtx: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dtxp"]) -> MetaOapg.properties.dtxp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dtxs"]) -> MetaOapg.properties.dtxs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fk_model_id"]) -> MetaOapg.properties.fk_model_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'Id': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'Meta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["np"]) -> MetaOapg.properties.np: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ns"]) -> MetaOapg.properties.ns: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pk"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pv"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rqd"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["system"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uidt"]) -> MetaOapg.properties.uidt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["un"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unique"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visible"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "ai", "au", "source_id", "cc", "cdf", "clen", "colOptions", "column_name", "cop", "csn", "ct", "deleted", "dt", "dtx", "dtxp", "dtxs", "fk_model_id", "id", "meta", "np", "ns", "order", "pk", "pv", "rqd", "system", "uidt", "un", "unique", "visible", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ai"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["au"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source_id"]) -> typing.Union[MetaOapg.properties.source_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cc"]) -> typing.Union[MetaOapg.properties.cc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cdf"]) -> typing.Union['StringOrNullOrBooleanOrNumber', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clen"]) -> typing.Union[MetaOapg.properties.clen, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["colOptions"]) -> typing.Union[MetaOapg.properties.colOptions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["column_name"]) -> typing.Union[MetaOapg.properties.column_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cop"]) -> typing.Union[MetaOapg.properties.cop, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["csn"]) -> typing.Union['StringOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ct"]) -> typing.Union[MetaOapg.properties.ct, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleted"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dt"]) -> typing.Union[MetaOapg.properties.dt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dtx"]) -> typing.Union[MetaOapg.properties.dtx, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dtxp"]) -> typing.Union[MetaOapg.properties.dtxp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dtxs"]) -> typing.Union[MetaOapg.properties.dtxs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fk_model_id"]) -> typing.Union[MetaOapg.properties.fk_model_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union['Id', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['Meta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["np"]) -> typing.Union[MetaOapg.properties.np, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ns"]) -> typing.Union[MetaOapg.properties.ns, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> typing.Union[MetaOapg.properties.order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pk"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pv"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rqd"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["system"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uidt"]) -> typing.Union[MetaOapg.properties.uidt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["un"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unique"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visible"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "ai", "au", "source_id", "cc", "cdf", "clen", "colOptions", "column_name", "cop", "csn", "ct", "deleted", "dt", "dtx", "dtxp", "dtxs", "fk_model_id", "id", "meta", "np", "ns", "order", "pk", "pv", "rqd", "system", "uidt", "un", "unique", "visible", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        ai: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        au: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        source_id: typing.Union[MetaOapg.properties.source_id, str, schemas.Unset] = schemas.unset,
        cc: typing.Union[MetaOapg.properties.cc, str, schemas.Unset] = schemas.unset,
        cdf: typing.Union['StringOrNullOrBooleanOrNumber', schemas.Unset] = schemas.unset,
        clen: typing.Union[MetaOapg.properties.clen, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        colOptions: typing.Union[MetaOapg.properties.colOptions, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        column_name: typing.Union[MetaOapg.properties.column_name, str, schemas.Unset] = schemas.unset,
        cop: typing.Union[MetaOapg.properties.cop, str, schemas.Unset] = schemas.unset,
        csn: typing.Union['StringOrNull', schemas.Unset] = schemas.unset,
        ct: typing.Union[MetaOapg.properties.ct, str, schemas.Unset] = schemas.unset,
        deleted: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        dt: typing.Union[MetaOapg.properties.dt, str, schemas.Unset] = schemas.unset,
        dtx: typing.Union[MetaOapg.properties.dtx, str, schemas.Unset] = schemas.unset,
        dtxp: typing.Union[MetaOapg.properties.dtxp, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        dtxs: typing.Union[MetaOapg.properties.dtxs, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        fk_model_id: typing.Union[MetaOapg.properties.fk_model_id, str, schemas.Unset] = schemas.unset,
        id: typing.Union['Id', schemas.Unset] = schemas.unset,
        meta: typing.Union['Meta', schemas.Unset] = schemas.unset,
        np: typing.Union[MetaOapg.properties.np, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        ns: typing.Union[MetaOapg.properties.ns, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        order: typing.Union[MetaOapg.properties.order, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        pk: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        pv: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        rqd: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        system: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        uidt: typing.Union[MetaOapg.properties.uidt, str, schemas.Unset] = schemas.unset,
        un: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        unique: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        visible: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Column':
        return super().__new__(
            cls,
            *args,
            title=title,
            ai=ai,
            au=au,
            source_id=source_id,
            cc=cc,
            cdf=cdf,
            clen=clen,
            colOptions=colOptions,
            column_name=column_name,
            cop=cop,
            csn=csn,
            ct=ct,
            deleted=deleted,
            dt=dt,
            dtx=dtx,
            dtxp=dtxp,
            dtxs=dtxs,
            fk_model_id=fk_model_id,
            id=id,
            meta=meta,
            np=np,
            ns=ns,
            order=order,
            pk=pk,
            pv=pv,
            rqd=rqd,
            system=system,
            uidt=uidt,
            un=un,
            unique=unique,
            visible=visible,
            _configuration=_configuration,
            **kwargs,
        )

from noco_db_python_sdk.model.formula import Formula
from noco_db_python_sdk.model.id import Id
from noco_db_python_sdk.model.link_to_another_record import LinkToAnotherRecord
from noco_db_python_sdk.model.lookup import Lookup
from noco_db_python_sdk.model.meta import Meta
from noco_db_python_sdk.model.model_bool import ModelBool
from noco_db_python_sdk.model.rollup import Rollup
from noco_db_python_sdk.model.select_options import SelectOptions
from noco_db_python_sdk.model.string_or_null import StringOrNull
from noco_db_python_sdk.model.string_or_null_or_boolean_or_number import StringOrNullOrBooleanOrNumber
