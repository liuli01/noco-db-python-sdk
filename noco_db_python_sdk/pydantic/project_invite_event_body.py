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


class ProjectInviteEventBody(BaseModel):
    # The title of the base being invited to
    title: str = Field(alias='title')

    # The ID of the base being invited to
    id: str = Field(alias='id')

    # The type of the base being invited to
    type: str = Field(alias='type')

    # The email address of the user who invited the recipient
    invited_by: str = Field(alias='invited_by')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )