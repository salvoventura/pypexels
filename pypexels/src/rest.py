###############################################################################
#    Copyright (c) 2017 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: rest.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 27 Sep 2017
#   Purpose: Base REST API client class
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################
import requests

from .errors import PexelsError
from .liblogging import logger
from .settings import API_ROOT, API_VERSION


class Rest(object):
    api_root = API_ROOT

    def __init__(self, api_key, api_version=API_VERSION):
        self.api_version = api_version
        self.api_key = api_key
        self.req_headers = {
            'Authorization': '%s' % api_key,
        }
        self._status_code = None
        self._body = None
        self._headers = None

    @staticmethod
    def _query_parameters(query_parameters):
        """
        Prepare the query parameter string to be appended to the _url

        :param query_parameters: dictionary of query parameters and their values
        :return:
        """
        logger.debug('Calling _query_parameters(%s)', query_parameters)
        if query_parameters is None:
            return ''

        tmp = []
        for k, v in query_parameters.items():
            if v is None:
                continue
            tmp.append('{}={}'.format(k, v))
        return '&'.join(tmp)

    def _sanitized_url(self, url):
        logger.debug('Call _sanitized_url(%s)', url)
        if url.startswith(self.api_root):
            good_url = url
        elif url.startswith('/'):
            good_url = '{}/{}{}'.format(self.api_root, self.api_version, url)
        else:
            good_url = '{}/{}/{}'.format(self.api_root, self.api_version, url)
        logger.debug('     returning %s', good_url)
        return good_url

    def _request(self, url, method, query_params=None, data=None, **kwargs):
        logger.debug('Calling REST %s %s %s %s', method, url, query_params, data)
        req_url = self._sanitized_url(url)
        logger.debug('Wiring REST %s %s %s %s', method, req_url, query_params, data)

        try:
            response = requests.request(method, req_url, params=query_params, data=data, headers=self.req_headers,
                                        **kwargs)
        except Exception as e:
            raise PexelsError("Connection error: %s" % e)

        try:
            self._status_code = response.status_code
            self._headers = response.headers
            self._body = response.json()
            if self._status_code != requests.codes.ok:
                logger.error(
                    'HTTP status %s: %s', self._status_code, self._body.get('errors', ['No error message'])
                )

        except ValueError as e:
            logger.error('EXCEPTION: %s', e)
            if self._status_code != requests.codes.ok:
                logger.error('HTTP EXC status %s: %s', self._status_code, response.text)
            raise PexelsError("Exception: %s" % e)

        logger.debug('REST rsp status %s body %s headers %s', self._status_code, self._body, self._headers)
        return response

    def get(self, url, query_params=None):
        return self._request(url, 'GET', query_params)
