###############################################################################
#    Copyright (c) 2017 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: test_popular.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 27 Sep 2017
#   Purpose: Unit Test for Popular()
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


class TestPopular:
    # TODO: avoid code duplication
    # Need to workout how to combine responses.activate so as to avoid
    # code duplication, as the testcases are pretty much the same for all

    # TOXINIDIR comes from tox.ini
    root_path = os.environ.get('TRAVIS_BUILD_DIR', None) or os.environ.get('TOXINIDIR', None)

    store_mapping = {
        'popular': os.sep.join(
            [root_path, 'pypexels', 'tests', 'resources', 'resource__popular_per_page_5_page_2.json']),
    }

    @responses.activate
    def test_popular(self):
        index = 'popular'
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
        popular_results_page = py_pexels.popular(page=2, per_page=5)

        # Page properties
        print(popular_results_page.page)
        print(popular_results_page.per_page)
        print(popular_results_page.has_next)
        print(popular_results_page.has_previous)
        print(popular_results_page.link_self)
        print(popular_results_page.link_first)
        print(popular_results_page.link_last)
        print(popular_results_page.link_next)
        print(popular_results_page.link_previous)

        # Entries
        for photo in popular_results_page.entries:
            print(photo.id, photo.photographer, photo.width, photo.height, photo.url)
            print(photo.src)
