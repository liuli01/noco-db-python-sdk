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

from noco_db_python_sdk.model.model_bool import ModelBool as ModelBoolSchema
from noco_db_python_sdk.model.string_or_null import StringOrNull as StringOrNullSchema
from noco_db_python_sdk.model.hook import Hook as HookSchema
from noco_db_python_sdk.model.hook_req import HookReq as HookReqSchema
from noco_db_python_sdk.model.auth_list_base_users400_response import AuthListBaseUsers400Response as AuthListBaseUsers400ResponseSchema
from noco_db_python_sdk.model.id import Id as IdSchema

from noco_db_python_sdk.type.id import Id
from noco_db_python_sdk.type.string_or_null import StringOrNull
from noco_db_python_sdk.type.hook import Hook
from noco_db_python_sdk.type.hook_req import HookReq
from noco_db_python_sdk.type.model_bool import ModelBool
from noco_db_python_sdk.type.auth_list_base_users400_response import AuthListBaseUsers400Response

from ...api_client import Dictionary
from noco_db_python_sdk.pydantic.hook import Hook as HookPydantic
from noco_db_python_sdk.pydantic.id import Id as IdPydantic
from noco_db_python_sdk.pydantic.hook_req import HookReq as HookReqPydantic
from noco_db_python_sdk.pydantic.auth_list_base_users400_response import AuthListBaseUsers400Response as AuthListBaseUsers400ResponsePydantic
from noco_db_python_sdk.pydantic.model_bool import ModelBool as ModelBoolPydantic
from noco_db_python_sdk.pydantic.string_or_null import StringOrNull as StringOrNullPydantic

# Path params
TableIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'tableId': typing.Union[IdSchema, str, ],
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


request_path_table_id = api_client.PathParameter(
    name="tableId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = HookReqSchema


request_body_hook_req = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = HookSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Hook


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Hook


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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_hook_mapped_args(
        self,
        title: str,
        event: str,
        notification: typing.Union[bool, date, datetime, dict, float, int, list, str, None],
        operation: str,
        table_id: Id,
        description: typing.Optional[StringOrNull] = None,
        active: typing.Optional[ModelBool] = None,
        _async: typing.Optional[ModelBool] = None,
        env: typing.Optional[str] = None,
        fk_model_id: typing.Optional[str] = None,
        id: typing.Optional[Id] = None,
        retries: typing.Optional[typing.Union[int, float]] = None,
        retry_interval: typing.Optional[typing.Union[int, float]] = None,
        timeout: typing.Optional[typing.Union[int, float]] = None,
        type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        condition: typing.Optional[ModelBool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if title is not None:
            _body["title"] = title
        if description is not None:
            _body["description"] = description
        if active is not None:
            _body["active"] = active
        if _async is not None:
            _body["async"] = _async
        if env is not None:
            _body["env"] = env
        if event is not None:
            _body["event"] = event
        if fk_model_id is not None:
            _body["fk_model_id"] = fk_model_id
        if id is not None:
            _body["id"] = id
        if notification is not None:
            _body["notification"] = notification
        if operation is not None:
            _body["operation"] = operation
        if retries is not None:
            _body["retries"] = retries
        if retry_interval is not None:
            _body["retry_interval"] = retry_interval
        if timeout is not None:
            _body["timeout"] = timeout
        if type is not None:
            _body["type"] = type
        if condition is not None:
            _body["condition"] = condition
        args.body = _body
        if table_id is not None:
            _path_params["tableId"] = table_id
        args.path = _path_params
        return args

    async def _acreate_hook_oapg(
        self,
        body: typing.Any = None,
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
        Create Table Hook
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_table_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
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
            path_template='/api/v2/meta/tables/{tableId}/hooks',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_hook_req.serialize(body, content_type)
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


    def _create_hook_oapg(
        self,
        body: typing.Any = None,
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
        Create Table Hook
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_table_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
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
            path_template='/api/v2/meta/tables/{tableId}/hooks',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_hook_req.serialize(body, content_type)
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


class CreateHookRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_hook(
        self,
        title: str,
        event: str,
        notification: typing.Union[bool, date, datetime, dict, float, int, list, str, None],
        operation: str,
        table_id: Id,
        description: typing.Optional[StringOrNull] = None,
        active: typing.Optional[ModelBool] = None,
        _async: typing.Optional[ModelBool] = None,
        env: typing.Optional[str] = None,
        fk_model_id: typing.Optional[str] = None,
        id: typing.Optional[Id] = None,
        retries: typing.Optional[typing.Union[int, float]] = None,
        retry_interval: typing.Optional[typing.Union[int, float]] = None,
        timeout: typing.Optional[typing.Union[int, float]] = None,
        type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        condition: typing.Optional[ModelBool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_hook_mapped_args(
            title=title,
            event=event,
            notification=notification,
            operation=operation,
            table_id=table_id,
            description=description,
            active=active,
            _async=_async,
            env=env,
            fk_model_id=fk_model_id,
            id=id,
            retries=retries,
            retry_interval=retry_interval,
            timeout=timeout,
            type=type,
            condition=condition,
        )
        return await self._acreate_hook_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def create_hook(
        self,
        title: str,
        event: str,
        notification: typing.Union[bool, date, datetime, dict, float, int, list, str, None],
        operation: str,
        table_id: Id,
        description: typing.Optional[StringOrNull] = None,
        active: typing.Optional[ModelBool] = None,
        _async: typing.Optional[ModelBool] = None,
        env: typing.Optional[str] = None,
        fk_model_id: typing.Optional[str] = None,
        id: typing.Optional[Id] = None,
        retries: typing.Optional[typing.Union[int, float]] = None,
        retry_interval: typing.Optional[typing.Union[int, float]] = None,
        timeout: typing.Optional[typing.Union[int, float]] = None,
        type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        condition: typing.Optional[ModelBool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_hook_mapped_args(
            title=title,
            event=event,
            notification=notification,
            operation=operation,
            table_id=table_id,
            description=description,
            active=active,
            _async=_async,
            env=env,
            fk_model_id=fk_model_id,
            id=id,
            retries=retries,
            retry_interval=retry_interval,
            timeout=timeout,
            type=type,
            condition=condition,
        )
        return self._create_hook_oapg(
            body=args.body,
            path_params=args.path,
        )

class CreateHook(BaseApi):

    async def acreate_hook(
        self,
        title: str,
        event: str,
        notification: typing.Union[bool, date, datetime, dict, float, int, list, str, None],
        operation: str,
        table_id: Id,
        description: typing.Optional[StringOrNull] = None,
        active: typing.Optional[ModelBool] = None,
        _async: typing.Optional[ModelBool] = None,
        env: typing.Optional[str] = None,
        fk_model_id: typing.Optional[str] = None,
        id: typing.Optional[Id] = None,
        retries: typing.Optional[typing.Union[int, float]] = None,
        retry_interval: typing.Optional[typing.Union[int, float]] = None,
        timeout: typing.Optional[typing.Union[int, float]] = None,
        type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        condition: typing.Optional[ModelBool] = None,
        validate: bool = False,
        **kwargs,
    ) -> HookPydantic:
        raw_response = await self.raw.acreate_hook(
            title=title,
            event=event,
            notification=notification,
            operation=operation,
            table_id=table_id,
            description=description,
            active=active,
            _async=_async,
            env=env,
            fk_model_id=fk_model_id,
            id=id,
            retries=retries,
            retry_interval=retry_interval,
            timeout=timeout,
            type=type,
            condition=condition,
            **kwargs,
        )
        if validate:
            return HookPydantic(**raw_response.body)
        return api_client.construct_model_instance(HookPydantic, raw_response.body)
    
    
    def create_hook(
        self,
        title: str,
        event: str,
        notification: typing.Union[bool, date, datetime, dict, float, int, list, str, None],
        operation: str,
        table_id: Id,
        description: typing.Optional[StringOrNull] = None,
        active: typing.Optional[ModelBool] = None,
        _async: typing.Optional[ModelBool] = None,
        env: typing.Optional[str] = None,
        fk_model_id: typing.Optional[str] = None,
        id: typing.Optional[Id] = None,
        retries: typing.Optional[typing.Union[int, float]] = None,
        retry_interval: typing.Optional[typing.Union[int, float]] = None,
        timeout: typing.Optional[typing.Union[int, float]] = None,
        type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        condition: typing.Optional[ModelBool] = None,
        validate: bool = False,
    ) -> HookPydantic:
        raw_response = self.raw.create_hook(
            title=title,
            event=event,
            notification=notification,
            operation=operation,
            table_id=table_id,
            description=description,
            active=active,
            _async=_async,
            env=env,
            fk_model_id=fk_model_id,
            id=id,
            retries=retries,
            retry_interval=retry_interval,
            timeout=timeout,
            type=type,
            condition=condition,
        )
        if validate:
            return HookPydantic(**raw_response.body)
        return api_client.construct_model_instance(HookPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        title: str,
        event: str,
        notification: typing.Union[bool, date, datetime, dict, float, int, list, str, None],
        operation: str,
        table_id: Id,
        description: typing.Optional[StringOrNull] = None,
        active: typing.Optional[ModelBool] = None,
        _async: typing.Optional[ModelBool] = None,
        env: typing.Optional[str] = None,
        fk_model_id: typing.Optional[str] = None,
        id: typing.Optional[Id] = None,
        retries: typing.Optional[typing.Union[int, float]] = None,
        retry_interval: typing.Optional[typing.Union[int, float]] = None,
        timeout: typing.Optional[typing.Union[int, float]] = None,
        type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        condition: typing.Optional[ModelBool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_hook_mapped_args(
            title=title,
            event=event,
            notification=notification,
            operation=operation,
            table_id=table_id,
            description=description,
            active=active,
            _async=_async,
            env=env,
            fk_model_id=fk_model_id,
            id=id,
            retries=retries,
            retry_interval=retry_interval,
            timeout=timeout,
            type=type,
            condition=condition,
        )
        return await self._acreate_hook_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        title: str,
        event: str,
        notification: typing.Union[bool, date, datetime, dict, float, int, list, str, None],
        operation: str,
        table_id: Id,
        description: typing.Optional[StringOrNull] = None,
        active: typing.Optional[ModelBool] = None,
        _async: typing.Optional[ModelBool] = None,
        env: typing.Optional[str] = None,
        fk_model_id: typing.Optional[str] = None,
        id: typing.Optional[Id] = None,
        retries: typing.Optional[typing.Union[int, float]] = None,
        retry_interval: typing.Optional[typing.Union[int, float]] = None,
        timeout: typing.Optional[typing.Union[int, float]] = None,
        type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        condition: typing.Optional[ModelBool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_hook_mapped_args(
            title=title,
            event=event,
            notification=notification,
            operation=operation,
            table_id=table_id,
            description=description,
            active=active,
            _async=_async,
            env=env,
            fk_model_id=fk_model_id,
            id=id,
            retries=retries,
            retry_interval=retry_interval,
            timeout=timeout,
            type=type,
            condition=condition,
        )
        return self._create_hook_oapg(
            body=args.body,
            path_params=args.path,
        )

