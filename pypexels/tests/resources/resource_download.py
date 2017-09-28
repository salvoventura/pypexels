###############################################################################
#    Copyright (c) 2017 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: resource_download.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 27 Sep 2017
#   Purpose: Download and save resources for unit testing
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################
from pypexels.src.settings import API_ROOT, API_VERSION
import requests
import os
import json
import time

api_key = os.environ.get('API_KEY', None) or 'DUMMY_API_KEY'

req_headers = {
    'Authorization': '%s' % api_key,
}


def _save_content(sub_url):
    url = '{}/{}{}'.format(API_ROOT, API_VERSION, sub_url)
    r = requests.get(url=url, headers=req_headers)

    d_headers = dict(r.headers)
    del d_headers["Content-Encoding"]   # if anything compressed, this will break responses: remove
    del d_headers["Set-Cookie"]         # cookies will expire, breaking responses: remove

    out = {
        '_url': sub_url,
        'body': r.json(),
        'headers': d_headers,
        'status_code': r.status_code,
        'last_update': time.ctime()
    }

    # save to file
    filename = sub_url.replace('/', '_').replace('?', '_').replace('=', '_').replace('&', '_').replace('+', '_')
    print(os.getcwd())
    filepath = os.sep.join(['.', 'pypexels', 'tests', 'resources', 'resource_{}.json'.format(filename)])
    with open(filepath, 'w') as f:
        f.write(json.dumps(out))


def get_resources_popular():
    for sub_url in ['/popular?per_page=5&page=2']:
        _save_content(sub_url)


def get_resources_search():
    for sub_url in ['/search?per_page=5&page=2&query=red+flower']:
        _save_content(sub_url)


def main():
    get_resources_popular()
    get_resources_search()


if __name__ == '__main__':
    main()
