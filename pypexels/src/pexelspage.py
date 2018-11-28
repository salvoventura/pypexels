###############################################################################
#    Copyright (c) 2017 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: pexelspage.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 27 Sep 2017
#   Purpose: Base class for Pexels API pages
#
#  Revision: 1
#   Comment: What's new in revision 1
#            Any object exposes GET
#               _url is optional; if none provided, the current _url is used.
#               next, previous, last, first *might* be available and usable.
#               Object itself has no memory.
#               GET, next, previous, last, first return a new object
#
###############################################################################
from .errors import PexelsError
from .liblogging import logger
from .rest import Rest
from .settings import API_VERSION


class PexelsPage(Rest):

    def __init__(self, url, api_key, api_version=API_VERSION, valid_options=None, **kwargs):
        if url is None:
            raise PexelsError('PexelsPage: _url cannot be None')

        super(PexelsPage, self).__init__(api_key=api_key, api_version=api_version)
        self._valid_options = valid_options

        self._url = self._sanitized_url(url)
        self._query_parameters = self._sanitized_query_parameters(kwargs)
        self._navigation = None

        # Load the page at the given URL, and if status OK, parse it too
        self._response = self.get(self._url, self._query_parameters)
        if self._status_code == 200:
            self._parse_navigation()

    @property
    def body(self):
        if self._response and self._status_code == 200:
            return self._body

    @property
    def entries(self):
        # must override in child class
        raise NotImplementedError

    @property
    def headers(self):
        if self._response:
            return self._headers

    @property
    def link_self(self):
        return self._ret_link('self')

    @property
    def link_next(self):
        return self._ret_link('next')

    @property
    def link_previous(self):
        return self._ret_link('prev')

    @property
    def link_first(self):
        return self._ret_link('first')

    @property
    def link_last(self):
        return self._ret_link('last')

    @property
    def has_next(self):
        return self.link_next is not None

    @property
    def has_previous(self):
        return self.link_previous is not None

    def get_page(self, page):
        url = '%s&per_page=%s&page=%s' % (self.nopaging_url, self.per_page, page)
        return self.__class__(url=url, api_key=self.api_key, api_version=self.api_version)

    def get_next_page(self):
        if self.link_next:
            return self.__class__(url=self.link_next, api_key=self.api_key, api_version=self.api_version)

    def get_previous_page(self):
        if self.link_previous:
            return self.__class__(url=self.link_previous, api_key=self.api_key, api_version=self.api_version)

    def get_first_page(self):
        if self.link_first:
            return self.__class__(url=self.link_first, api_key=self.api_key, api_version=self.api_version)

    def get_last_page(self):
        if self.link_last:
            return self.__class__(url=self.link_last, api_key=self.api_key, api_version=self.api_version)

    def _sanitized_query_parameters(self, kwargs):
        logger.debug('Call _sanitized_query_parameters(%s)', kwargs)
        query_params = {}
        for key in kwargs:
            if self._valid_options and key not in self._valid_options:
                logger.debug('Invalid parameter %s, safely ignoring it', key)
                continue
            query_params[key] = kwargs[key]
        # add defaults for page and per_page
        if 'page' not in query_params:
            query_params['page'] = 1
        if 'per_page' not in query_params:
            query_params['per_page'] = 15
        logger.debug('     returning %s', query_params)
        return query_params

    def _parse_navigation(self):
        nopaging_query_parameters = ['{}={}'.format(k, v) for k, v in self._query_parameters.items() if
                                     k not in ['page', 'per_page']]
        self.nopaging_url = '?'.join([self._url, '&'.join(nopaging_query_parameters)])
        self.page = int(self.body.get('page', 1))
        self.per_page = int(self.body.get('per_page', 15))
        self.total_results = int(self.body.get('total_results', 0))

        self._navigation = {
            'self': self._url,
            'first': '%s&per_page=%s&page=%s' % (self.nopaging_url, self.per_page, 1),
            'prev': self.body.get('prev_page', None),
            'next': self.body.get('next_page', None),
            'last': '%s&per_page=%s&page=%s' % (
            self.nopaging_url, self.per_page, self.total_results / self.per_page + 1),
        }

    def _ret_link(self, which):
        if self._navigation:
            return self._navigation.get(which, None)
