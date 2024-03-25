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

from noco_db_python_sdk.model.audit import Audit as AuditSchema
from noco_db_python_sdk.model.audit_row_update_req import AuditRowUpdateReq as AuditRowUpdateReqSchema
from noco_db_python_sdk.model.auth_list_base_users400_response import AuthListBaseUsers400Response as AuthListBaseUsers400ResponseSchema

from noco_db_python_sdk.type.audit_row_update_req import AuditRowUpdateReq
from noco_db_python_sdk.type.audit import Audit
from noco_db_python_sdk.type.auth_list_base_users400_response import AuthListBaseUsers400Response

from ...api_client import Dictionary
from noco_db_python_sdk.pydantic.audit_row_update_req import AuditRowUpdateReq as AuditRowUpdateReqPydantic
from noco_db_python_sdk.pydantic.auth_list_base_users400_response import AuthListBaseUsers400Response as AuthListBaseUsers400ResponsePydantic
from noco_db_python_sdk.pydantic.audit import Audit as AuditPydantic

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
RowIdSchema = schemas.AnyTypeSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'rowId': typing.Union[RowIdSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
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


request_path_row_id = api_client.PathParameter(
    name="rowId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=RowIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = AuditRowUpdateReqSchema


request_body_audit_row_update_req = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = AuditSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Audit


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Audit


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

    def _update_audit_row_mapped_args(
        self,
        row_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None],
        column_name: typing.Optional[str] = None,
        fk_model_id: typing.Optional[str] = None,
        row_id: typing.Optional[str] = None,
        prev_value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        xc_auth: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        _body = {}
        if column_name is not None:
            _body["column_name"] = column_name
        if fk_model_id is not None:
            _body["fk_model_id"] = fk_model_id
        if row_id is not None:
            _body["row_id"] = row_id
        if prev_value is not None:
            _body["prev_value"] = prev_value
        if value is not None:
            _body["value"] = value
        args.body = _body
        if xc_auth is not None:
            _header_params["xc-auth"] = xc_auth
        if row_id is not None:
            _path_params["rowId"] = row_id
        args.header = _header_params
        args.path = _path_params
        return args

    async def _aupdate_audit_row_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update Audit Row
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_row_id,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v2/meta/audits/rows/{rowId}/update',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_audit_row_update_req.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


    def _update_audit_row_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update Audit Row
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_row_id,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v2/meta/audits/rows/{rowId}/update',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_audit_row_update_req.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


class UpdateAuditRowRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_audit_row(
        self,
        row_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None],
        column_name: typing.Optional[str] = None,
        fk_model_id: typing.Optional[str] = None,
        row_id: typing.Optional[str] = None,
        prev_value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        xc_auth: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_audit_row_mapped_args(
            row_id=row_id,
            column_name=column_name,
            fk_model_id=fk_model_id,
            row_id=row_id,
            prev_value=prev_value,
            value=value,
            xc_auth=xc_auth,
        )
        return await self._aupdate_audit_row_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def update_audit_row(
        self,
        row_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None],
        column_name: typing.Optional[str] = None,
        fk_model_id: typing.Optional[str] = None,
        row_id: typing.Optional[str] = None,
        prev_value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        xc_auth: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_audit_row_mapped_args(
            row_id=row_id,
            column_name=column_name,
            fk_model_id=fk_model_id,
            row_id=row_id,
            prev_value=prev_value,
            value=value,
            xc_auth=xc_auth,
        )
        return self._update_audit_row_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

class UpdateAuditRow(BaseApi):

    async def aupdate_audit_row(
        self,
        row_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None],
        column_name: typing.Optional[str] = None,
        fk_model_id: typing.Optional[str] = None,
        row_id: typing.Optional[str] = None,
        prev_value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        xc_auth: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> AuditPydantic:
        raw_response = await self.raw.aupdate_audit_row(
            row_id=row_id,
            column_name=column_name,
            fk_model_id=fk_model_id,
            row_id=row_id,
            prev_value=prev_value,
            value=value,
            xc_auth=xc_auth,
            **kwargs,
        )
        if validate:
            return AuditPydantic(**raw_response.body)
        return api_client.construct_model_instance(AuditPydantic, raw_response.body)
    
    
    def update_audit_row(
        self,
        row_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None],
        column_name: typing.Optional[str] = None,
        fk_model_id: typing.Optional[str] = None,
        row_id: typing.Optional[str] = None,
        prev_value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        xc_auth: typing.Optional[str] = None,
        validate: bool = False,
    ) -> AuditPydantic:
        raw_response = self.raw.update_audit_row(
            row_id=row_id,
            column_name=column_name,
            fk_model_id=fk_model_id,
            row_id=row_id,
            prev_value=prev_value,
            value=value,
            xc_auth=xc_auth,
        )
        if validate:
            return AuditPydantic(**raw_response.body)
        return api_client.construct_model_instance(AuditPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        row_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None],
        column_name: typing.Optional[str] = None,
        fk_model_id: typing.Optional[str] = None,
        row_id: typing.Optional[str] = None,
        prev_value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        xc_auth: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_audit_row_mapped_args(
            row_id=row_id,
            column_name=column_name,
            fk_model_id=fk_model_id,
            row_id=row_id,
            prev_value=prev_value,
            value=value,
            xc_auth=xc_auth,
        )
        return await self._aupdate_audit_row_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        row_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None],
        column_name: typing.Optional[str] = None,
        fk_model_id: typing.Optional[str] = None,
        row_id: typing.Optional[str] = None,
        prev_value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        xc_auth: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_audit_row_mapped_args(
            row_id=row_id,
            column_name=column_name,
            fk_model_id=fk_model_id,
            row_id=row_id,
            prev_value=prev_value,
            value=value,
            xc_auth=xc_auth,
        )
        return self._update_audit_row_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

