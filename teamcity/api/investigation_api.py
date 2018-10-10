# coding: utf-8

"""
    TeamCity REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from teamcity.models.investigation import Investigation  # noqa: F401,E501
from teamcity.models.investigations import Investigations  # noqa: F401,E501


class InvestigationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """
    base_name = 'Investigation'

    def __init__(self, api_client=None):
        self.api_client = api_client

    def get_investigations(self, **kwargs):  # noqa: E501
        """get_investigations  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_investigations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str locator:
        :param str fields:
        :return: Investigations
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_investigations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.__get_investigations_with_http_info(**kwargs)  # noqa: E501
            return data

    def __get_investigations_with_http_info(self, **kwargs):  # noqa: E501
        """get_investigations  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.__get_investigations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str locator:
        :param str fields:
        :return: Investigations
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['locator', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_investigations" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'locator' in params:
            query_params.append(('locator', params['locator']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/app/rest/investigations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Investigations',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def serve_instance(self, investigation_locator, **kwargs):  # noqa: E501
        """serve_instance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.serve_instance(investigation_locator, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str investigation_locator: (required)
        :param str fields:
        :return: Investigation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__serve_instance_with_http_info(investigation_locator, **kwargs)  # noqa: E501
        else:
            (data) = self.__serve_instance_with_http_info(investigation_locator, **kwargs)  # noqa: E501
            return data

    def __serve_instance_with_http_info(self, investigation_locator, **kwargs):  # noqa: E501
        """serve_instance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.__serve_instance_with_http_info(investigation_locator, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str investigation_locator: (required)
        :param str fields:
        :return: Investigation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['investigation_locator', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method serve_instance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'investigation_locator' is set
        if ('investigation_locator' not in params or
                params['investigation_locator'] is None):
            raise ValueError("Missing the required parameter `investigation_locator` when calling `serve_instance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'investigation_locator' in params:
            path_params['investigationLocator'] = params['investigation_locator']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/app/rest/investigations/{investigationLocator}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Investigation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
