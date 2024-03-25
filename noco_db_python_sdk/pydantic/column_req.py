# coding: utf-8

"""
    NocoDB v2

    NocoDB API Documentation

    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from noco_db_python_sdk.pydantic.formula_column_req import FormulaColumnReq
from noco_db_python_sdk.pydantic.link_to_another_column_req import LinkToAnotherColumnReq
from noco_db_python_sdk.pydantic.lookup_column_req import LookupColumnReq
from noco_db_python_sdk.pydantic.normal_column_request import NormalColumnRequest
from noco_db_python_sdk.pydantic.rollup_column_req import RollupColumnReq

class ColumnReq(BaseModel):
    title: typing.Optional[str] = Field(None, alias='title')

    ai: typing.Optional[typing.Union[int, float]] = Field(None, alias='ai')

    au: typing.Optional[typing.Union[int, float]] = Field(None, alias='au')

    source_id: typing.Optional[str] = Field(None, alias='source_id')

    cc: typing.Optional[str] = Field(None, alias='cc')

    cdf: typing.Optional[typing.Optional[str]] = Field(None, alias='cdf')

    clen: typing.Optional[str] = Field(None, alias='clen')

    column_name: typing.Optional[str] = Field(None, alias='column_name')

    cop: typing.Optional[str] = Field(None, alias='cop')

    created_at: typing.Optional[str] = Field(None, alias='created_at')

    csn: typing.Optional[str] = Field(None, alias='csn')

    ct: typing.Optional[str] = Field(None, alias='ct')

    deleted: typing.Optional[typing.Optional[str]] = Field(None, alias='deleted')

    dt: typing.Optional[str] = Field(None, alias='dt')

    dtx: typing.Optional[str] = Field(None, alias='dtx')

    dtxp: typing.Optional[str] = Field(None, alias='dtxp')

    dtxs: typing.Optional[typing.Optional[str]] = Field(None, alias='dtxs')

    fk_model_id: typing.Optional[str] = Field(None, alias='fk_model_id')

    id: typing.Optional[str] = Field(None, alias='id')

    meta: typing.Optional[typing.Optional[str]] = Field(None, alias='meta')

    np: typing.Optional[typing.Optional[str]] = Field(None, alias='np')

    ns: typing.Optional[typing.Optional[str]] = Field(None, alias='ns')

    order: typing.Optional[typing.Union[int, float]] = Field(None, alias='order')

    pk: typing.Optional[typing.Union[int, float]] = Field(None, alias='pk')

    base_id: typing.Optional[str] = Field(None, alias='base_id')

    pv: typing.Optional[typing.Union[int, float]] = Field(None, alias='pv')

    rqd: typing.Optional[typing.Union[int, float]] = Field(None, alias='rqd')

    system: typing.Optional[typing.Union[int, float]] = Field(None, alias='system')

    uidt: typing.Optional[str] = Field(None, alias='uidt')

    un: typing.Optional[typing.Union[int, float]] = Field(None, alias='un')

    unique: typing.Optional[typing.Union[int, float]] = Field(None, alias='unique')

    updated_at: typing.Optional[str] = Field(None, alias='updated_at')

    validate: typing.Optional[typing.Optional[str]] = Field(None, alias='validate')

    virtual: typing.Optional[typing.Optional[str]] = Field(None, alias='virtual')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
ColumnReq = typing.Union[typing.Union[FormulaColumnReq, LinkToAnotherColumnReq, LookupColumnReq, NormalColumnRequest, RollupColumnReq],typing.Union[bool, date, datetime, dict, float, int, list, str, None]]