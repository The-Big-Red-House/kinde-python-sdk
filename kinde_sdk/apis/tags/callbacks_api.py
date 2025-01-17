# coding: utf-8

"""
    Kinde Management API

    Provides endpoints to manage your Kinde Businesses  # noqa: E501

    The version of the OpenAPI document: 1
    Contact: support@kinde.com
    Generated by: https://openapi-generator.tech
"""

from kinde_sdk.paths.api_v1_applications_app_id_auth_redirect_urls.post import AddRedirectCallbackUrls
from kinde_sdk.paths.api_v1_applications_app_id_auth_redirect_urls.delete import DeleteCallbackUrls
from kinde_sdk.paths.api_v1_applications_app_id_auth_redirect_urls.get import GetCallbackUrls
from kinde_sdk.paths.api_v1_applications_app_id_auth_redirect_urls.put import ReplaceRedirectCallbackUrls


class CallbacksApi(
    AddRedirectCallbackUrls,
    DeleteCallbackUrls,
    GetCallbackUrls,
    ReplaceRedirectCallbackUrls,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
