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


class DbViewListGridColumnsResponse(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['GridColumn']:
            return GridColumn

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['GridColumn'], typing.List['GridColumn']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DbViewListGridColumnsResponse':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'GridColumn':
        return super().__getitem__(i)

from noco_db_python_sdk.model.grid_column import GridColumn
