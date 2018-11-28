###############################################################################
#    Copyright (c) 2017 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: test_search.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 27 Sep 2017
#   Purpose: Unit Test for Search()
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################
from __future__ import print_function
import responses
import json
import os
from pypexels import PyPexels
from pypexels.src.settings import API_ROOT, API_VERSION

api_key = os.environ.get('API_KEY', None) or 'API_KEY'


class TestSearch:
    # TODO: avoid code duplication
    # Need to workout how to combine responses.activate so as to avoid
    # code duplication, as the testcases are pretty much the same for all

    # TOXINIDIR comes from tox.ini
    root_path = os.environ.get('TRAVIS_BUILD_DIR', None) or os.environ.get('TOXINIDIR', None)

    store_mapping = {
        'redflower': os.sep.join(
            [root_path, 'pypexels', 'tests', 'resources', 'resource__search_per_page_5_page_2_query_red_flower.json']),
    }

    @responses.activate
    def test_search(self):
        index = 'redflower'
        resource_filepath = self.store_mapping[index]
        stored_response = json.loads(open(resource_filepath).read())

        responses.add(
            responses.GET,
            '{}/{}{}'.format(API_ROOT, API_VERSION, stored_response.get('_url')),
            # _url contains only the short path like /popular?page=2&per_page=5
            json=stored_response.get('body'),
            status=stored_response.get('status_code'),
            content_type='application/json',
            adding_headers=stored_response.get('headers'),
            match_querystring=True,
        )
        py_pexels = PyPexels(api_key=api_key)
        search_results_page = py_pexels.search(query='red flower', page=2, per_page=5)

        # Page properties
        print(search_results_page.page)
        print(search_results_page.per_page)
        print(search_results_page.has_next)
        print(search_results_page.has_previous)
        print(search_results_page.link_self)
        print(search_results_page.link_first)
        print(search_results_page.link_last)
        print(search_results_page.link_next)
        print(search_results_page.link_previous)

        # Entries
        for photo in search_results_page.entries:
            print(photo.id, photo.photographer, photo.width, photo.height, photo.url)
            print(photo.src)
