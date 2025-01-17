# Kinde Python SDK

The Kinde Python SDK allows developers to quickly and securely integrate a new or an existing Python application to the Kinde platform.

## Register for Kinde

If you haven’t already got a Kinde account, [register for free here](http://app.kinde.com/register) (no credit card
required).

You need a Kinde domain to get started, e.g. `yourapp.kinde.com`.

## Set callback URLs

1. In Kinde, go to **Settings** > **App keys**.
2. Add your callback URLs in the relevant fields. For example:

    - Allowed callback URLs - for example, `https://localhost:8000/callback`
    - Allowed logout redirect URLs - for example, `https://localhost:8000`

3. Select **Save**.

## Add environments

Kinde comes with a production environment, but you can set up other environments if you want to. Note that each
environment needs to be set up independently, so you need to use the Environment subdomain in the code block above for
those new environments.

## Installing Kinde Python SDK and Supported Versions

Clone this repository and install dependencies by running:

```console
$ pip install -r requirements.txt
```

Kinde Python SDK officially supports Python 3.7+.

## Configure your app

**Environment variables**

The following variables need to be replaced in the code snippets below.

- `SITE_HOST` - e.g. `"localhost"`
- `SITE_PORT` - e.g. `"8000"`
- `SITE_URL` - e.g. `f"http://{SITE_HOST}:{SITE_PORT}"`
- `KINDE_ISSUER_URL` - your Kinde domain - e.g. `"https://your_kinde_domain.kinde.com"`
- `KINDE_CALLBACK_URL` - your callback url, make sure this URL is under your allowed callback redirect URLs. -
  e.g. http://localhost:8000/callback
- `LOGOUT_REDIRECT_URL` - where you want users to be redirected to after logging out, make sure this URL is under your
  allowed logout redirect URLs. - e.g. `"/callback"`
- `CLIENT_ID` - you can find this on the **App keys** page - e.g. `"your_kinde_client_id"`
- `CLIENT_SECRET` - you can find this on the **App keys** page - e.g. `"your_kinde_client_secret"`
- `GRANT_TYPE` - one
  of `GrantType: GrantType.CLIENT_CREDENTIALS`, `GrantType.AUTHORIZATION_CODE`, `GrantType.AUTHORIZATION_CODE_WITH_PKCE`
- `CODE_VERIFIER` - required only if `GRANT_TYPE == GrantType.AUTHORIZATION_CODE_WITH_PKCE`;
  this code can be generated by e.g:

```python
from authlib.common.security import generate_token

CODE_VERIFIER = generate_token(48)
```

## Getting token

**Client Credentials flow**

```python
from kinde_sdk import Configuration
from kinde_sdk.kinde_api_client import GrantType, KindeApiClient

CLIENT_ID = "YOUR_KINDE_CLIENT_ID"
CLIENT_SECRET = "YOUR_KINDE_CLIENT_SECRET"
KINDE_ISSUER_URL = "https://[your_subdomain].kinde.com"
KINDE_CALLBACK_URL = "KINDE_CALLBACK_URL"
GRANT_TYPE = GrantType.CLIENT_CREDENTIALS

configuration = Configuration(host=KINDE_ISSUER_URL)
kinde_client = KindeApiClient(
    configuration=configuration,
    domain=KINDE_ISSUER_URL,
    callback_url=KINDE_CALLBACK_URL,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    grant_type=GRANT_TYPE,
)

kinde_client.fetch_token()
```

**Authorisation Code flow**

```python
from kinde_sdk import Configuration
from kinde_sdk.kinde_api_client import GrantType, KindeApiClient

CLIENT_ID = "YOUR_KINDE_CLIENT_ID"
CLIENT_SECRET = "YOUR_KINDE_CLIENT_SECRET"
KINDE_ISSUER_URL = "https://[your_subdomain].kinde.com"
KINDE_CALLBACK_URL = "KINDE_CALLBACK_URL"
GRANT_TYPE = GrantType.AUTHORIZATION_CODE

configuration = Configuration(host=KINDE_ISSUER_URL)
kinde_client = KindeApiClient(
    configuration=configuration,
    domain=KINDE_ISSUER_URL,
    callback_url=KINDE_CALLBACK_URL,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    grant_type=GRANT_TYPE,
)
```

*Login or register*<br />
The Kinde client provides methods for an easy to implement login/register flow.
These methods return the authorization URL to the authorization server.
You need to redirect the user to this URL to initiate the OAuth2 login/register flow.

```python
kinde_client.get_login_url()
kinde_client.get_register_url()
```

*Handle redirect and fetch token*<br />
The authorization server will redirect you back to your site (`authorization_response`). Use it as parameter to fetch
token.

```python
kinde_client.fetch_token(authorization_response=authorization_response)
```

*Logout*<br />
This is implemented in much the same way as logging in or registering.<br />
The below method removes the token from the client and returns URL to the authorization server to log out.<br />
Parameter "redirect_to" - URL to your site where redirect from the authorization server after logging out.

```python
kinde_client.logout(redirect_to=redirect_to)
```

**Authorisation Code with PKCE flow**

This flow is similar to Authorisation Code, but you need CODE_VERIFIER. This code can be generated by e.g:

```python
from authlib.common.security import generate_token

CODE_VERIFIER = generate_token(48)
```

```python
from kinde_sdk import Configuration
from kinde_sdk.kinde_api_client import GrantType, KindeApiClient

CLIENT_ID = "YOUR_KINDE_CLIENT_ID"
CLIENT_SECRET = "YOUR_KINDE_CLIENT_SECRET"
KINDE_ISSUER_URL = "https://[your_subdomain].kinde.com"
KINDE_CALLBACK_URL = "KINDE_CALLBACK_URL"
GRANT_TYPE = GrantType.AUTHORIZATION_CODE_WITH_PKCE
CODE_VERIFIER = "CODE_VERIFIER"

configuration = Configuration(host=KINDE_ISSUER_URL)
kinde_client = KindeApiClient(
    configuration=configuration,
    domain=KINDE_ISSUER_URL,
    callback_url=KINDE_CALLBACK_URL,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    grant_type=GRANT_TYPE,
    code_verifier=CODE_VERIFIER,
)
```

*Login or register*<br />
The Kinde client provides methods for an easy to implement login/register flow.
These methods return the authorization URL to the authorization server.
You need to redirect the user to this URL to initiate the OAuth2 login/register flow.

```python
kinde_client.get_login_url()
kinde_client.get_register_url()
```

*Handle redirect and fetch token*<br />
The authorization server will redirect you back to your site (`authorization_response`). Use it as parameter to fetch
token.

```python
kinde_client.fetch_token(authorization_response=authorization_response)
```

*Logout*<br />
This is implemented in much the same way as logging in or registering.<br />
The below method removes the token from the client and returns URL to the authorization server to log out.<br />
Parameter "redirect_to" - URL to your site where redirect from the authorization server after logging out.

```python
kinde_client.logout(redirect_to=redirect_to)
```

## Scope

By default the Kinde Python SDK requests the following scopes:

- profile
- email
- offline
- openid

You can override this by passing scope into the KindeApiClient e.g.

```python
KindeApiClient(..., scope="profile email")
```

## Audience

An `audience` is the intended recipient of an access token - for example the API for your application. The audience
argument can be passed to the Kinde client to request an audience be added to the provided token.

The audience of a token is the intended recipient of the token.

```python
KindeApiClient(..., audience="api.example.com/v1")
```

For details on how to connect, see [Register an API](https://kinde.com/docs/developer-tools/register-an-api/)

## Getting user details

```python
kinde_client.get_user_details()
```

Result:

```python
{
    id: id_token.sub,
    given_name: id_token.given_name,
    family_name: id_token.family_name,
    email: id_token.email,
    picture: id_token.picture
}
```

## Getting claims

We have provided a helper to grab any claim from your id or access tokens. The helper defaults to access tokens.

```python
kinde_client.get_claim("aud")
# {
#   "name": "aud",
#   "value": ["api.stakesocial.com/v1"]
# }

kinde_client.get_claim("given_name", "id_token")
# {
#   "name": "given_name",
#   "value": "David"
# }
```

## Feature Flags

Get feature_flags claim of the access token.

Sample data

```python
feature_flags: {
  theme: {
    t: "s",
    v: "pink"
  },
  is_dark_mode: {
    t: "b",
    v: true
  },
  competitions_limit: {
    t: "i",
    v: 5
  }
}
```
In order to minimize the payload in the token we have used single letter keys / values where possible. The single letters represent the following:

t = type

v = value

s = string

b = boolean

i = integer

We provide helper functions to more easily access feature flags:

```python

# Get a flag from the feature_flags claim of the access_token.
#   @param {string} code - The name of the flag.
#   @param {obj} [defaultValue] - A fallback value if the flag isn't found.
#   @param {'s'|'b'|'i'|undefined} [flagType] - The data type of the flag
#   (integer / boolean / string).
#   @return {object} Flag details.

kinde_client.get_flag(code, defaultValue, flagType)

# Example usage:

kinde_client.get_flag("theme")
# {
#   "code": "theme",
#   "type": "string",
#   "value": "pink",
#   "is_default": false // whether the fallback value had to be used
# }

# If flag does not exist, default value provided
kinde_client.get_flag("create_competition", default_value=False)
# {
#   "code": "create_competition",
#   "value": false,
#   "is_default": true
# }

kinde_client.get_flag("competitions_limit", default_value=3, flat_type='i')
# {
#   "code": "competitions_limit",
#   "type": "integer",
#   "value": 5,
#   "is_default": false
# }
```

If flag_type is provided and not the same as the flag value, an error will be raise.

#### Get boolean flag

Get a boolean flag from the feature_flags claim of the access_token.

```python

# Get a boolean flag from the feature_flags claim of the access_token.
#   @param {string} code - The name of the flag.
#   @param {bool} [defaultValue] - A fallback value if the flag isn't found.
#   @return {bool}

kinde_client.get_boolean_flag(code, defaultValue)

# Example usage:

kinde_client.get_boolean_flag("is_dark_mode")
# True

kinde_client.get_boolean_flag("is_dark_mode", False)
# False

kinde_client.get_boolean_flag("new_feature", False)
# False (flag does not exist so falls back to default)

kinde_client.get_boolean_flag("new_feature")
# Error - flag does not exist and no default provided

kinde_client.get_boolean_flag("theme", False)
# Error - Flag "theme" is of type string not boolean
```

#### Get string flag

Get a string flag from the feature_flags claim of the access_token.

```python
# Get a string flag from the feature_flags claim of the access_token.
#   @param {string} code - The name of the flag.
#   @param {string} [defaultValue] - A fallback value if the flag isn't found.
#   @return {string}

kinde_client.get_string_flag(code, defaultValue)

# Example usage:

kinde_client.get_string_flag("theme")
# "pink"

kinde_client.get_string_flag("theme", "orange")
# "pink"

kinde_client.get_string_flag("cta_color", "blue")
# "blue" (flag does not exist so falls back to default)

kinde_client.get_string_flag("cta_color")
# Error - flag does not exist and no default provided

kinde_client.get_string_flag("is_dark_mode", False)
# Error - Flag "is_dark_mode" is of type boolean not string
```

#### Get integer flag

Get a integer flag from the feature_flags claim of the access_token.

```python
# Get an integer flag from the feature_flags claim of the access_token.
#   @param {string} code - The name of the flag.
#   @param {int} [defaultValue] - A fallback value if the flag isn't found.
#   @return {int}

kinde_client.get_tnteger_flag(code, defaultValue)

# Example usage:

kinde_client.get_integer_flag("competitions_limit")
# 5

kinde_client.get_integer_flag("competitions_limit", 3)
# 5

kinde_client.get_integer_flag("team_count", 2)
# 2 (flag does not exist so falls back to default)

kinde_client.get_integer_flag("team_count")
# Error - flag does not exist and no default provided

kinde_client.get_integer_flag("is_dark_mode", False)
# Error - Flag "is_dark_mode" is of type boolean not integer
```

## Get user information from API

```python
from kinde_sdk import ApiException
from kinde_sdk.api import o_auth_api

api_instance = o_auth_api.OAuthApi(kinde_client)
try:
    # Returns the details of the currently logged in user
    api_response = api_instance.get_user()
    print(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->get_user: %s\n" % e)
```

## SDK API Reference

| Property      | Type                                      | Is required                                         | Default                      | Description                                                                                                 |
|---------------|-------------------------------------------|-----------------------------------------------------|------------------------------|-------------------------------------------------------------------------------------------------------------|
| domain        | string                                    | Yes                                                 |                              | Either your Kinde instance url or your custom domain. e.g: https://yourapp.kinde.com                        |
| callback_url  | string                                    | Yes                                                 |                              | The url that the user will be returned to after authentication                                              |
| client_id     | string                                    | Yes                                                 |                              | The id of your application - get this from the Kinde admin area                                             |
| client_secret | string                                    | Yes                                                 |                              | The id secret of your application - get this from the Kinde admin area                                      |
| grant_type    | enum kinde_sdk.kinde_api_client.GrantType | Yes                                                 |                              | One of GrantType.CLIENT_CREDENTIALS, GrantType.AUTHORIZATION_CODE or GrantType.AUTHORIZATION_CODE_WITH_PKCE |
| scope         | string                                    | No                                                  | openid profile email offline | The scopes to be requested from Kinde                                                                       |
| code_verifier | string                                    | Yes when grant_type is AUTHORIZATION_CODE_WITH_PKCE |                              | code_verifier for code_challenge when AUTHORIZATION_CODE_WITH_PKCE grant_type is used                       |
| audience      | string                                    | No                                                  |                              | An unique identifier for this API                                                                           |
| org_code      | string                                    | No                                                  |                              | A specific org is to be signed up into or registered into                                                   |

## KindeSDK methods

| Property               | Description                                                                            | Arguments                       | Usage                                              | Sample output                                                                                 |
|------------------------|----------------------------------------------------------------------------------------|---------------------------------|----------------------------------------------------|-----------------------------------------------------------------------------------------------|
| get_login_url          | Returns redirect url for log in                                                        |                                 | kinde_client.get_login_url()                       | 'https://your_kinde_domain.kinde.com/login'                                                   |
| get_register_url       | Returns redirect url for registration                                                  |                                 | kinde_client.get_register_url()                    | 'https://your_kinde_domain.kinde.com/login&start_page=registration'                           |
| logout                 | Logs the user out of Kinde                                                             |                                 | kinde_client.logout()                              | 'https://your_kinde_domain.kinde.com/logout'                                                  |
| is_authenticated       | Check if user is authenticated                                                         |                                 | kinde_client.is_authenticated()                    | True                                                                                          |
| create_org             | Constructs redirect url for creating an organization                                   |                                 | kinde_client.create_org()                          | 'https://your_kinde_domain.kinde.com/login&start_page=registration&is_create_org=true'        |
| get_claim              | Gets a claim from an access or id token                                                | key: string, token_name: string | kinde_client.get_claim('given\_name', 'id\_token') | {'name': 'given\_name', 'value': 'David'}                                                                                       |
| get_permission         | Returns the state of a given permission                                                | permission: string              | kinde_client.get_permission('read:todos')          | \{'org_code': 'org\_1234', 'is_granted': True\}                                               |
| get_permissions        | Returns all permissions for the current user for the organization they are logged into |                                 | kinde_client.get_permissions()                     | \{'org_code':'org\_1234', 'permissions': \['create:todos', 'update:todos', 'read:todos'\]\}   |
| get_organization       | Get details for the organization your user is logged into                              |                                 | kinde_client.get_organization()                    | \{'org_code': 'org\_1234'\}                                                                   |
| get_user_details       | Returns the profile for the current user                                               |                                 | kinde_client.get_user_details()                    | \{'given\_name': 'Dave', 'id': 'abcdef', 'family\_name': 'Smith', 'email': 'dave@smith.com', 'picture': '<https://google-avatar.com/12455>'\} |
| get_user_organizations | Gets an array of all organizations the user has access to                              |                                 | kinde_client.get_user_organizations()              | \{'org_codes': ['org\_1234', 'org\_2345']\}                                                   |
| get_flag          | Returns feature_flags claim of the access_token                                                        | code: string, default_value: any (optional), flag_type: str (optional)                               | kinde_client.get_flag("theme")                       | {"code": "theme","type": "string","value": "pink","is_default": False}                                               |
| get_boolean_flag          | Returns a boolean flag from the feature_flags claim of the access_token                                                        | code: string, default_value: any (optional)                               | kinde_client.get_boolean_flag("is_dark_mode")                       | True
| get_string_flag          | Returns a string flag from the feature_flags claim of the access_token                                                        | code: string, default_value: any (optional)                               | kinde_client.get_string_flag("theme")                       | "pink"
| get_integer_flag          | Returns an integer flag from the feature_flags claim of the access_token                                                        | code: string, default_value: any (optional)                               | kinde_client.get_integer_flag("competitions_limit")                       | 5
| call_api                 | Returns deserialized data | resource_path: string, method: string, headers: optional, body: optional, fields: optional, auth_settings: optional, async_req: optional, stream: optional, timeout: optional, host: optional | kinde_client.call_api("/api/v1/user", "GET") | <urllib3.response.HTTPResponse> object
If you need help connecting to Kinde, please contact us at [support@kinde.com](mailto:support@kinde.com).

## Autogenerated API reference
See autogenerated API reference in [kinde_sdk_README.md](kinde_sdk_README.md).
