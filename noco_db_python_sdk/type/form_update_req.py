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

from noco_db_python_sdk.type.attachment_req import AttachmentReq
from noco_db_python_sdk.type.meta import Meta
from noco_db_python_sdk.type.model_bool import ModelBool
from noco_db_python_sdk.type.string_or_null import StringOrNull
from noco_db_python_sdk.type.text_or_null import TextOrNull

class RequiredFormUpdateReq(TypedDict):
    pass

class OptionalFormUpdateReq(TypedDict, total=False):
    # Banner Image URL
    banner_image_url: typing.Union[AttachmentReq, none_type]

    email: StringOrNull

    # The heading of the form
    heading: str

    # Logo URL.
    logo_url: typing.Union[AttachmentReq, none_type]

    meta: Meta

    redirect_after_secs: StringOrNull

    redirect_url: TextOrNull

    show_blank_form: ModelBool

    subheading: TextOrNull

    submit_another_form: ModelBool

    success_msg: TextOrNull

class FormUpdateReq(RequiredFormUpdateReq, OptionalFormUpdateReq):
    pass