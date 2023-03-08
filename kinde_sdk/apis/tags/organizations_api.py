# coding: utf-8

"""
    Kinde Management API

    Provides endpoints to manage your Kinde Businesses  # noqa: E501

    The version of the OpenAPI document: 1
    Contact: support@kinde.com
    Generated by: https://openapi-generator.tech
"""

from kinde_sdk.paths.api_v1_organization_users.post import AddOrganizationUsers
from kinde_sdk.paths.api_v1_organization.post import CreateOrganization
from kinde_sdk.paths.api_v1_organizations_org_code_feature_flags_feature_flag_key.delete import (
    DeleteOrganizationFeatureFlagOverride,
)
from kinde_sdk.paths.api_v1_organizations_org_code_feature_flags.delete import (
    DeleteOrganizationFeatureFlagOverrides,
)
from kinde_sdk.paths.api_v1_organizations.get import GetOrgainzations
from kinde_sdk.paths.api_v1_organization.get import GetOrganization
from kinde_sdk.paths.api_v1_organization_users.get import GetOrganizationUsers
from kinde_sdk.paths.api_v1_organization_users.patch import RemoveOrganizationUsers
from kinde_sdk.paths.api_v1_organizations_org_code_feature_flags_feature_flag_key.patch import (
    UpdateOrganizationFeatureFlagOverride,
)


class OrganizationsApi(
    AddOrganizationUsers,
    CreateOrganization,
    DeleteOrganizationFeatureFlagOverride,
    DeleteOrganizationFeatureFlagOverrides,
    GetOrgainzations,
    GetOrganization,
    GetOrganizationUsers,
    RemoveOrganizationUsers,
    UpdateOrganizationFeatureFlagOverride,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    pass
