# kinde-sdk
Provides endpoints to manage your Kinde Businesses

The `kinde_sdk` package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://kinde.com/docs/](https://kinde.com/docs/)

## Requirements.

Python &gt;&#x3D;3.7

## Installation & Usage

This python library package is generated without supporting files like setup.py or requirements files

To be able to use it, you will need these dependencies in your own package that uses this library:

* urllib3 >= 1.15
* certifi
* python-dateutil

## Documentation for API Endpoints

All URIs are relative to *https://app.kinde.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BusinessApi* | [**get_business**](kinde_sdk/docs/apis/tags/BusinessApi.md#get_business) | **get** /api/v1/business | List business details
*BusinessApi* | [**update_business**](kinde_sdk/docs/apis/tags/BusinessApi.md#update_business) | **patch** /api/v1/business | Update business details
*CallbacksApi* | [**add_redirect_callback_urls**](kinde_sdk/docs/apis/tags/CallbacksApi.md#add_redirect_callback_urls) | **post** /api/v1/applications/{app_id}/auth_redirect_urls | Add Redirect Callback URLs
*CallbacksApi* | [**delete_callback_urls**](kinde_sdk/docs/apis/tags/CallbacksApi.md#delete_callback_urls) | **delete** /api/v1/applications/{app_id}/auth_redirect_urls | Delete Callback URLs
*CallbacksApi* | [**get_callback_urls**](kinde_sdk/docs/apis/tags/CallbacksApi.md#get_callback_urls) | **get** /api/v1/applications/{app_id}/auth_redirect_urls | List Callback URLs
*CallbacksApi* | [**replace_redirect_callback_urls**](kinde_sdk/docs/apis/tags/CallbacksApi.md#replace_redirect_callback_urls) | **put** /api/v1/applications/{app_id}/auth_redirect_urls | Replace Redirect Callback URLs
*ConnectedAppsApi* | [**get_connected_app_auth_url**](kinde_sdk/docs/apis/tags/ConnectedAppsApi.md#get_connected_app_auth_url) | **get** /api/v1/connected_apps/auth_url | Get Connected App URL
*ConnectedAppsApi* | [**get_connected_app_token**](kinde_sdk/docs/apis/tags/ConnectedAppsApi.md#get_connected_app_token) | **get** /api/v1/connected_apps/token | Get Connected App Token
*ConnectedAppsApi* | [**revoke_connected_app_token**](kinde_sdk/docs/apis/tags/ConnectedAppsApi.md#revoke_connected_app_token) | **post** /api/v1/connected_apps/revoke | Revoke Connected App Token
*EnvironmentsApi* | [**delete_environement_feature_flag_override**](kinde_sdk/docs/apis/tags/EnvironmentsApi.md#delete_environement_feature_flag_override) | **delete** /api/v1/environment/feature_flags/{feature_flag_key} | Delete Environment Feature Flag Override
*EnvironmentsApi* | [**delete_environement_feature_flag_overrides**](kinde_sdk/docs/apis/tags/EnvironmentsApi.md#delete_environement_feature_flag_overrides) | **delete** /api/v1/environment/feature_flags | Delete Environment Feature Flag Overrides
*EnvironmentsApi* | [**get_environement_feature_flags**](kinde_sdk/docs/apis/tags/EnvironmentsApi.md#get_environement_feature_flags) | **get** /api/v1/environment/feature_flags | List Environment Feature Flags
*EnvironmentsApi* | [**update_environement_feature_flag_override**](kinde_sdk/docs/apis/tags/EnvironmentsApi.md#update_environement_feature_flag_override) | **patch** /api/v1/environment/feature_flags/{feature_flag_key} | Update Environment Feature Flag Override
*FeatureFlagsApi* | [**create_feature_flag**](kinde_sdk/docs/apis/tags/FeatureFlagsApi.md#create_feature_flag) | **post** /api/v1/feature_flags | Create Feature Flag
*FeatureFlagsApi* | [**delete_feature_flag**](kinde_sdk/docs/apis/tags/FeatureFlagsApi.md#delete_feature_flag) | **delete** /api/v1/feature_flags/{feature_flag_key} | Delete Feature Flag
*FeatureFlagsApi* | [**update_feature_flag**](kinde_sdk/docs/apis/tags/FeatureFlagsApi.md#update_feature_flag) | **put** /api/v1/feature_flags/{feature_flag_key} | Replace Feature Flag
*IndustriesApi* | [**get_industries**](kinde_sdk/docs/apis/tags/IndustriesApi.md#get_industries) | **get** /api/v1/industries | List industries and industry keys.
*OAuthApi* | [**get_user**](kinde_sdk/docs/apis/tags/OAuthApi.md#get_user) | **get** /oauth2/user_profile | Get User Profile
*OAuthApi* | [**get_user_profile_v2**](kinde_sdk/docs/apis/tags/OAuthApi.md#get_user_profile_v2) | **get** /oauth2/v2/user_profile | Returns the details of the currently logged in user
*OrganizationsApi* | [**add_organization_users**](kinde_sdk/docs/apis/tags/OrganizationsApi.md#add_organization_users) | **post** /api/v1/organizations/{org_code}/users | Add Organization Users
*OrganizationsApi* | [**create_organization**](kinde_sdk/docs/apis/tags/OrganizationsApi.md#create_organization) | **post** /api/v1/organization | Create Organization
*OrganizationsApi* | [**create_organization_user_role**](kinde_sdk/docs/apis/tags/OrganizationsApi.md#create_organization_user_role) | **post** /api/v1/organizations/{org_code}/users/{user_id}/roles | Add Organization User Role
*OrganizationsApi* | [**delete_organization_feature_flag_override**](kinde_sdk/docs/apis/tags/OrganizationsApi.md#delete_organization_feature_flag_override) | **delete** /api/v1/organizations/{org_code}/feature_flags/{feature_flag_key} | Delete Organization Feature Flag Override
*OrganizationsApi* | [**delete_organization_feature_flag_overrides**](kinde_sdk/docs/apis/tags/OrganizationsApi.md#delete_organization_feature_flag_overrides) | **delete** /api/v1/organizations/{org_code}/feature_flags | Delete Organization Feature Flag Overrides
*OrganizationsApi* | [**delete_organization_user_role**](kinde_sdk/docs/apis/tags/OrganizationsApi.md#delete_organization_user_role) | **delete** /api/v1/organizations/{org_code}/users/{user_id}/roles/{role_id} | Delete Organization User Role
*OrganizationsApi* | [**get_organization**](kinde_sdk/docs/apis/tags/OrganizationsApi.md#get_organization) | **get** /api/v1/organization | Get Organization
*OrganizationsApi* | [**get_organization_feature_flags**](kinde_sdk/docs/apis/tags/OrganizationsApi.md#get_organization_feature_flags) | **get** /api/v1/organizations/{org_code}/feature_flags | List Organization Feature Flags
*OrganizationsApi* | [**get_organization_user_roles**](kinde_sdk/docs/apis/tags/OrganizationsApi.md#get_organization_user_roles) | **get** /api/v1/organizations/{org_code}/users/{user_id}/roles | List Organization User Roles
*OrganizationsApi* | [**get_organization_users**](kinde_sdk/docs/apis/tags/OrganizationsApi.md#get_organization_users) | **get** /api/v1/organizations/{org_code}/users | List Organization Users
*OrganizationsApi* | [**get_organizations**](kinde_sdk/docs/apis/tags/OrganizationsApi.md#get_organizations) | **get** /api/v1/organizations | List Organizations
*OrganizationsApi* | [**remove_organization_user**](kinde_sdk/docs/apis/tags/OrganizationsApi.md#remove_organization_user) | **delete** /api/v1/organizations/{org_code}/users/{user_id} | Remove Organization User
*OrganizationsApi* | [**update_organization**](kinde_sdk/docs/apis/tags/OrganizationsApi.md#update_organization) | **patch** /api/v1/organization/{org_code} | Update Organization
*OrganizationsApi* | [**update_organization_feature_flag_override**](kinde_sdk/docs/apis/tags/OrganizationsApi.md#update_organization_feature_flag_override) | **patch** /api/v1/organizations/{org_code}/feature_flags/{feature_flag_key} | Update Organization Feature Flag Override
*OrganizationsApi* | [**update_organization_users**](kinde_sdk/docs/apis/tags/OrganizationsApi.md#update_organization_users) | **patch** /api/v1/organizations/{org_code}/users | Update Organization Users
*PermissionsApi* | [**create_permission**](kinde_sdk/docs/apis/tags/PermissionsApi.md#create_permission) | **post** /api/v1/permissions | Create Permission
*PermissionsApi* | [**get_permissions**](kinde_sdk/docs/apis/tags/PermissionsApi.md#get_permissions) | **get** /api/v1/permissions | List Permissions
*PermissionsApi* | [**update_permissions**](kinde_sdk/docs/apis/tags/PermissionsApi.md#update_permissions) | **patch** /api/v1/permissions/{permission_id} | Update Permission
*RolesApi* | [**create_role**](kinde_sdk/docs/apis/tags/RolesApi.md#create_role) | **post** /api/v1/role | Create Role
*RolesApi* | [**get_roles**](kinde_sdk/docs/apis/tags/RolesApi.md#get_roles) | **get** /api/v1/roles | List Roles
*RolesApi* | [**update_roles**](kinde_sdk/docs/apis/tags/RolesApi.md#update_roles) | **patch** /api/v1/roles/{role_id} | Update Role
*SubscribersApi* | [**create_subscriber**](kinde_sdk/docs/apis/tags/SubscribersApi.md#create_subscriber) | **post** /api/v1/subscribers | Create Subscriber
*SubscribersApi* | [**get_subscriber**](kinde_sdk/docs/apis/tags/SubscribersApi.md#get_subscriber) | **get** /api/v1/subscribers/{subscriber_id} | Get Subscriber
*SubscribersApi* | [**get_subscribers**](kinde_sdk/docs/apis/tags/SubscribersApi.md#get_subscribers) | **get** /api/v1/subscribers | List Subscribers
*TimezonesApi* | [**get_timezones**](kinde_sdk/docs/apis/tags/TimezonesApi.md#get_timezones) | **get** /api/v1/timezones | List timezones and timezone IDs.
*UsersApi* | [**create_user**](kinde_sdk/docs/apis/tags/UsersApi.md#create_user) | **post** /api/v1/user | Create User
*UsersApi* | [**delete_user**](kinde_sdk/docs/apis/tags/UsersApi.md#delete_user) | **delete** /api/v1/user | Delete User
*UsersApi* | [**get_user_data**](kinde_sdk/docs/apis/tags/UsersApi.md#get_user_data) | **get** /api/v1/user | Get User
*UsersApi* | [**get_users**](kinde_sdk/docs/apis/tags/UsersApi.md#get_users) | **get** /api/v1/users | List Users
*UsersApi* | [**update_user**](kinde_sdk/docs/apis/tags/UsersApi.md#update_user) | **patch** /api/v1/user | Update User

## Documentation For Models

 - [AddOrganizationUsersResponse](kinde_sdk/docs/models/AddOrganizationUsersResponse.md)
 - [ApiResult](kinde_sdk/docs/models/ApiResult.md)
 - [Application](kinde_sdk/docs/models/Application.md)
 - [ConnectedAppsAccessToken](kinde_sdk/docs/models/ConnectedAppsAccessToken.md)
 - [ConnectedAppsAuthUrl](kinde_sdk/docs/models/ConnectedAppsAuthUrl.md)
 - [CreateOrganizationResponse](kinde_sdk/docs/models/CreateOrganizationResponse.md)
 - [CreateSubscriberSuccessResponse](kinde_sdk/docs/models/CreateSubscriberSuccessResponse.md)
 - [CreateUserResponse](kinde_sdk/docs/models/CreateUserResponse.md)
 - [Error](kinde_sdk/docs/models/Error.md)
 - [ErrorResponse](kinde_sdk/docs/models/ErrorResponse.md)
 - [GetApplicationsResponse](kinde_sdk/docs/models/GetApplicationsResponse.md)
 - [GetEnvironmentFeatureFlagsResponse](kinde_sdk/docs/models/GetEnvironmentFeatureFlagsResponse.md)
 - [GetOrganizationFeatureFlagsResponse](kinde_sdk/docs/models/GetOrganizationFeatureFlagsResponse.md)
 - [GetOrganizationUsersResponse](kinde_sdk/docs/models/GetOrganizationUsersResponse.md)
 - [GetOrganizationsResponse](kinde_sdk/docs/models/GetOrganizationsResponse.md)
 - [GetOrganizationsUserRolesResponse](kinde_sdk/docs/models/GetOrganizationsUserRolesResponse.md)
 - [GetRedirectCallbackUrlsResponse](kinde_sdk/docs/models/GetRedirectCallbackUrlsResponse.md)
 - [GetRolesResponse](kinde_sdk/docs/models/GetRolesResponse.md)
 - [GetSubscriberResponse](kinde_sdk/docs/models/GetSubscriberResponse.md)
 - [GetSubscribersResponse](kinde_sdk/docs/models/GetSubscribersResponse.md)
 - [Organization](kinde_sdk/docs/models/Organization.md)
 - [OrganizationUser](kinde_sdk/docs/models/OrganizationUser.md)
 - [OrganizationUserRole](kinde_sdk/docs/models/OrganizationUserRole.md)
 - [OrganizationUsers](kinde_sdk/docs/models/OrganizationUsers.md)
 - [Organizations](kinde_sdk/docs/models/Organizations.md)
 - [Permissions](kinde_sdk/docs/models/Permissions.md)
 - [RedirectCallbackUrls](kinde_sdk/docs/models/RedirectCallbackUrls.md)
 - [Role](kinde_sdk/docs/models/Role.md)
 - [Roles](kinde_sdk/docs/models/Roles.md)
 - [Subscriber](kinde_sdk/docs/models/Subscriber.md)
 - [SubscribersSubscriber](kinde_sdk/docs/models/SubscribersSubscriber.md)
 - [SuccessResponse](kinde_sdk/docs/models/SuccessResponse.md)
 - [UpdateOrganizationUsersResponse](kinde_sdk/docs/models/UpdateOrganizationUsersResponse.md)
 - [User](kinde_sdk/docs/models/User.md)
 - [UserIdentity](kinde_sdk/docs/models/UserIdentity.md)
 - [UserProfile](kinde_sdk/docs/models/UserProfile.md)
 - [UserProfileV2](kinde_sdk/docs/models/UserProfileV2.md)
 - [Users](kinde_sdk/docs/models/Users.md)
 - [UsersResponse](kinde_sdk/docs/models/UsersResponse.md)

## Documentation For Authorization

 Authentication schemes defined for the API:
## kindeBearerAuth

- **Type**: Bearer authentication (JWT)


## Author

support@kinde.com
support@kinde.com
support@kinde.com
support@kinde.com
support@kinde.com
support@kinde.com
support@kinde.com
support@kinde.com
support@kinde.com
support@kinde.com
support@kinde.com
support@kinde.com
support@kinde.com

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in kinde_sdk.apis and kinde_sdk.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from kinde_sdk.apis.default_api import DefaultApi`
- `from kinde_sdk.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import kinde_sdk
from kinde_sdk.apis import *
from kinde_sdk.models import *
```
