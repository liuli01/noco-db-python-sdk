# coding: utf-8

"""
    NocoDB v2

    NocoDB API Documentation

    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from noco_db_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from noco_db_python_sdk.api_response import AsyncGeneratorResponse
from noco_db_python_sdk import api_client, exceptions
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

from noco_db_python_sdk.model.filter_list import FilterList as FilterListSchema
from noco_db_python_sdk.model.auth_list_base_users400_response import AuthListBaseUsers400Response as AuthListBaseUsers400ResponseSchema
from noco_db_python_sdk.model.id import Id as IdSchema

from noco_db_python_sdk.type.id import Id
from noco_db_python_sdk.type.filter_list import FilterList
from noco_db_python_sdk.type.auth_list_base_users400_response import AuthListBaseUsers400Response

from ...api_client import Dictionary
from noco_db_python_sdk.pydantic.filter_list import FilterList as FilterListPydantic
from noco_db_python_sdk.pydantic.id import Id as IdPydantic
from noco_db_python_sdk.pydantic.auth_list_base_users400_response import AuthListBaseUsers400Response as AuthListBaseUsers400ResponsePydantic

from . import path

# Header params
XcAuthSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'xc-auth': typing.Union[XcAuthSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_xc_auth = api_client.HeaderParameter(
    name="xc-auth",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XcAuthSchema,
)
# Path params
FilterGroupIdSchema = schemas.Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'filterGroupId': typing.Union[IdSchema, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_filter_group_id = api_client.PathParameter(
    name="filterGroupId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = FilterListSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: FilterList


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: FilterList


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = AuthListBaseUsers400ResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: AuthListBaseUsers400Response


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: AuthListBaseUsers400Response


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_children_mapped_args(
        self,
        filter_group_id: Id,
        xc_auth: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        if xc_auth is not None:
            _header_params["xc-auth"] = xc_auth
        if filter_group_id is not None:
            _path_params["filterGroupId"] = filter_group_id
        args.header = _header_params
        args.path = _path_params
        return args

    async def _aget_children_oapg(
        self,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get Filter Group Children
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_filter_group_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_xc_auth,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v2/meta/filters/{filterGroupId}/children',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_children_oapg(
        self,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get Filter Group Children
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_filter_group_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_xc_auth,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v2/meta/filters/{filterGroupId}/children',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetChildrenRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_children(
        self,
        filter_group_id: Id,
        xc_auth: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_children_mapped_args(
            filter_group_id=filter_group_id,
            xc_auth=xc_auth,
        )
        return await self._aget_children_oapg(
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def get_children(
        self,
        filter_group_id: Id,
        xc_auth: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_children_mapped_args(
            filter_group_id=filter_group_id,
            xc_auth=xc_auth,
        )
        return self._get_children_oapg(
            header_params=args.header,
            path_params=args.path,
        )

class GetChildren(BaseApi):

    async def aget_children(
        self,
        filter_group_id: Id,
        xc_auth: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> FilterListPydantic:
        raw_response = await self.raw.aget_children(
            filter_group_id=filter_group_id,
            xc_auth=xc_auth,
            **kwargs,
        )
        if validate:
            return FilterListPydantic(**raw_response.body)
        return api_client.construct_model_instance(FilterListPydantic, raw_response.body)
    
    
    def get_children(
        self,
        filter_group_id: Id,
        xc_auth: typing.Optional[str] = None,
        validate: bool = False,
    ) -> FilterListPydantic:
        raw_response = self.raw.get_children(
            filter_group_id=filter_group_id,
            xc_auth=xc_auth,
        )
        if validate:
            return FilterListPydantic(**raw_response.body)
        return api_client.construct_model_instance(FilterListPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        filter_group_id: Id,
        xc_auth: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_children_mapped_args(
            filter_group_id=filter_group_id,
            xc_auth=xc_auth,
        )
        return await self._aget_children_oapg(
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        filter_group_id: Id,
        xc_auth: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_children_mapped_args(
            filter_group_id=filter_group_id,
            xc_auth=xc_auth,
        )
        return self._get_children_oapg(
            header_params=args.header,
            path_params=args.path,
        )

