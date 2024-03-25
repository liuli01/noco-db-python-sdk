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

from noco_db_python_sdk.type.id import Id
from noco_db_python_sdk.type.model_bool import ModelBool
from noco_db_python_sdk.type.string_or_null import StringOrNull

RequiredHookReq = TypedDict("RequiredHookReq", {
    # Hook Title
    "title": str,

    # Event Type for the operation
    "event": str,

    # Hook Notification including info such as type, payload, method, body, and etc
    "notification": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    # Hook Operation
    "operation": str,
    })

OptionalHookReq = TypedDict("OptionalHookReq", {
    "description": StringOrNull,

    "active": ModelBool,

    "async": ModelBool,

    # Environment for the hook
    "env": str,

    # Foreign Key to Model
    "fk_model_id": str,

    "id": Id,

    # Retry Count
    "retries": typing.Union[int, float],

    # Retry Interval
    "retry_interval": typing.Union[int, float],

    # Timeout
    "timeout": typing.Union[int, float],

    # Hook Type
    "type": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "condition": ModelBool,
    }, total=False)

class HookReq(RequiredHookReq, OptionalHookReq):
    pass