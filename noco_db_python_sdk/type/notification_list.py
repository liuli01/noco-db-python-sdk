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

from noco_db_python_sdk.type.notification import Notification
from noco_db_python_sdk.type.paginated import Paginated

RequiredNotificationList = TypedDict("RequiredNotificationList", {
    # List of notification objects
    "list": typing.List[Notification],

    "pageInfo": Paginated,
    })

OptionalNotificationList = TypedDict("OptionalNotificationList", {
    }, total=False)

class NotificationList(RequiredNotificationList, OptionalNotificationList):
    pass
