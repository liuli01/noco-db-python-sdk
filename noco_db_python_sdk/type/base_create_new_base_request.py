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

from noco_db_python_sdk.type.project_req import ProjectReq

BaseCreateNewBaseRequest = typing.Union[ProjectReq,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
