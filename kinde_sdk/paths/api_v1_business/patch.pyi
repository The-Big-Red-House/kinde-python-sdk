# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from kinde_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from kinde_sdk import schemas  # noqa: F401

from kinde_sdk.model.success_response import SuccessResponse
from kinde_sdk.model.error_response import ErrorResponse

# Query params
BusinessNameSchema = schemas.StrSchema
PrimaryEmailSchema = schemas.StrSchema


class PrimaryPhoneSchema(
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    def __new__(
        cls,
        *_args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PrimaryPhoneSchema':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
        )
IndustryKeySchema = schemas.StrSchema
TimezoneIdSchema = schemas.StrSchema


class PrivacyUrlSchema(
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    def __new__(
        cls,
        *_args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PrivacyUrlSchema':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
        )


class TermsUrlSchema(
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    def __new__(
        cls,
        *_args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TermsUrlSchema':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
        )


class IsShowKindeBrandingSchema(
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    def __new__(
        cls,
        *_args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IsShowKindeBrandingSchema':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
        )


class IsClickWrapSchema(
    schemas.BoolBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneBoolMixin
):


    def __new__(
        cls,
        *_args: typing.Union[None, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IsClickWrapSchema':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
        )


class PartnerCodeSchema(
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    def __new__(
        cls,
        *_args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PartnerCodeSchema':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
        )
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'business_name': typing.Union[BusinessNameSchema, str, ],
        'primary_email': typing.Union[PrimaryEmailSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'primary_phone': typing.Union[PrimaryPhoneSchema, None, str, ],
        'industry_key': typing.Union[IndustryKeySchema, str, ],
        'timezone_id': typing.Union[TimezoneIdSchema, str, ],
        'privacy_url': typing.Union[PrivacyUrlSchema, None, str, ],
        'terms_url': typing.Union[TermsUrlSchema, None, str, ],
        'is_show_kinde_branding': typing.Union[IsShowKindeBrandingSchema, None, str, ],
        'is_click_wrap': typing.Union[IsClickWrapSchema, None, bool, ],
        'partner_code': typing.Union[PartnerCodeSchema, None, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_business_name = api_client.QueryParameter(
    name="business_name",
    style=api_client.ParameterStyle.FORM,
    schema=BusinessNameSchema,
    required=True,
    explode=True,
)
request_query_primary_email = api_client.QueryParameter(
    name="primary_email",
    style=api_client.ParameterStyle.FORM,
    schema=PrimaryEmailSchema,
    required=True,
    explode=True,
)
request_query_primary_phone = api_client.QueryParameter(
    name="primary_phone",
    style=api_client.ParameterStyle.FORM,
    schema=PrimaryPhoneSchema,
    explode=True,
)
request_query_industry_key = api_client.QueryParameter(
    name="industry_key",
    style=api_client.ParameterStyle.FORM,
    schema=IndustryKeySchema,
    explode=True,
)
request_query_timezone_id = api_client.QueryParameter(
    name="timezone_id",
    style=api_client.ParameterStyle.FORM,
    schema=TimezoneIdSchema,
    explode=True,
)
request_query_privacy_url = api_client.QueryParameter(
    name="privacy_url",
    style=api_client.ParameterStyle.FORM,
    schema=PrivacyUrlSchema,
    explode=True,
)
request_query_terms_url = api_client.QueryParameter(
    name="terms_url",
    style=api_client.ParameterStyle.FORM,
    schema=TermsUrlSchema,
    explode=True,
)
request_query_is_show_kinde_branding = api_client.QueryParameter(
    name="is_show_kinde_branding",
    style=api_client.ParameterStyle.FORM,
    schema=IsShowKindeBrandingSchema,
    explode=True,
)
request_query_is_click_wrap = api_client.QueryParameter(
    name="is_click_wrap",
    style=api_client.ParameterStyle.FORM,
    schema=IsClickWrapSchema,
    explode=True,
)
request_query_partner_code = api_client.QueryParameter(
    name="partner_code",
    style=api_client.ParameterStyle.FORM,
    schema=PartnerCodeSchema,
    explode=True,
)
SchemaFor201ResponseBodyApplicationJsonCharsetutf8 = SuccessResponse


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor201ResponseBodyApplicationJsonCharsetutf8,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    content={
        'application/json; charset=utf-8': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJsonCharsetutf8),
    },
)
SchemaFor400ResponseBodyApplicationJsonCharsetutf8 = ErrorResponse


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor400ResponseBodyApplicationJsonCharsetutf8,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    content={
        'application/json; charset=utf-8': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJsonCharsetutf8),
    },
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
)
_all_accept_content_types = (
    'application/json; charset=utf-8',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _update_business_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor201,
    ]: ...

    @typing.overload
    def _update_business_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _update_business_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _update_business_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Update business details
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_business_name,
            request_query_primary_email,
            request_query_primary_phone,
            request_query_industry_key,
            request_query_timezone_id,
            request_query_privacy_url,
            request_query_terms_url,
            request_query_is_show_kinde_branding,
            request_query_is_click_wrap,
            request_query_partner_code,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='patch'.upper(),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class UpdateBusiness(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def update_business(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor201,
    ]: ...

    @typing.overload
    def update_business(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def update_business(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def update_business(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._update_business_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def patch(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor201,
    ]: ...

    @typing.overload
    def patch(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def patch(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def patch(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._update_business_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


