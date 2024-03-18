# coding: utf-8

"""
    Upstox Developer API

    Build your App on the Upstox platform  ![Banner](https://api-v2.upstox.com/api-docs/images/banner.jpg \"banner\")  # Introduction  Upstox API is a set of rest APIs that provide data required to build a complete investment and trading platform. Execute orders in real time, manage user portfolio, stream live market data (using Websocket), and more, with the easy to understand API collection.  All requests are over HTTPS and the requests are sent with the content-type ‘application/json’. Developers have the option of choosing the response type as JSON or CSV for a few API calls.  To be able to use these APIs you need to create an App in the Developer Console and generate your **apiKey** and **apiSecret**. You can use a redirect URL which will be called after the login flow.  If you are a **trader**, you can directly create apps from Upstox mobile app or the desktop platform itself from **Apps** sections inside the **Account** Tab. Head over to <a href=\"http://account.upstox.com/developer/apps\" target=\"_blank\">account.upstox.com/developer/apps</a>.</br> If you are a **business** looking to integrate Upstox APIs, reach out to us and we will get a custom app created for you in no time.  It is highly recommended that you do not embed the **apiSecret** in your frontend app. Create a remote backend which does the handshake on behalf of the frontend app. Marking the apiSecret in the frontend app will make your app vulnerable to threats and potential issues.   # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from upstox_client.api_client import ApiClient


class LoginApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def authorize(self, client_id, redirect_uri, api_version, **kwargs):  # noqa: E501
        """Authorize API  # noqa: E501

        This provides details on the login endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authorize(client_id, redirect_uri, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: (required)
        :param str redirect_uri: (required)
        :param str api_version: API Version Header (required)
        :param str state:
        :param str scope:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.authorize_with_http_info(client_id, redirect_uri, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.authorize_with_http_info(client_id, redirect_uri, api_version, **kwargs)  # noqa: E501
            return data

    def authorize_with_http_info(self, client_id, redirect_uri, api_version, **kwargs):  # noqa: E501
        """Authorize API  # noqa: E501

        This provides details on the login endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authorize_with_http_info(client_id, redirect_uri, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: (required)
        :param str redirect_uri: (required)
        :param str api_version: API Version Header (required)
        :param str state:
        :param str scope:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_id', 'redirect_uri', 'api_version', 'state', 'scope']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authorize" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `authorize`")  # noqa: E501
        # verify the required parameter 'redirect_uri' is set
        if ('redirect_uri' not in params or
                params['redirect_uri'] is None):
            raise ValueError("Missing the required parameter `redirect_uri` when calling `authorize`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `authorize`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'client_id' in params:
            query_params.append(('client_id', params['client_id']))  # noqa: E501
        if 'redirect_uri' in params:
            query_params.append(('redirect_uri', params['redirect_uri']))  # noqa: E501
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501
        if 'scope' in params:
            query_params.append(('scope', params['scope']))  # noqa: E501

        header_params = {}
        if 'api_version' in params:
            header_params['Api-Version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2/login/authorization/dialog', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def logout(self, api_version, **kwargs):  # noqa: E501
        """Logout  # noqa: E501

        Logout  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logout(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: API Version Header (required)
        :return: LogoutResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.logout_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.logout_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def logout_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """Logout  # noqa: E501

        Logout  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logout_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: API Version Header (required)
        :return: LogoutResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method logout" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `logout`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['Api-Version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAUTH2']  # noqa: E501

        return self.api_client.call_api(
            '/v2/logout', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LogoutResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def token(self, api_version, **kwargs):  # noqa: E501
        """Get token API  # noqa: E501

        This API provides the functionality to obtain opaque token from authorization_code exchange and also provides the user’s profile in the same response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.token(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: API Version Header (required)
        :param str code:
        :param str client_id:
        :param str client_secret:
        :param str redirect_uri:
        :param str grant_type:
        :return: TokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.token_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.token_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def token_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """Get token API  # noqa: E501

        This API provides the functionality to obtain opaque token from authorization_code exchange and also provides the user’s profile in the same response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.token_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: API Version Header (required)
        :param str code:
        :param str client_id:
        :param str client_secret:
        :param str redirect_uri:
        :param str grant_type:
        :return: TokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version', 'code', 'client_id', 'client_secret', 'redirect_uri', 'grant_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `token`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['Api-Version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'code' in params:
            form_params.append(('code', params['code']))  # noqa: E501
        if 'client_id' in params:
            form_params.append(('client_id', params['client_id']))  # noqa: E501
        if 'client_secret' in params:
            form_params.append(('client_secret', params['client_secret']))  # noqa: E501
        if 'redirect_uri' in params:
            form_params.append(('redirect_uri', params['redirect_uri']))  # noqa: E501
        if 'grant_type' in params:
            form_params.append(('grant_type', params['grant_type']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2/login/authorization/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
