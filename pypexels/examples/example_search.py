from __future__ import print_function
###############################################################################
#    Copyright (c) 2017 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: example_search.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 27 Sep 2017
#   Purpose: Exemplify usage of Search
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################
import logging
import os
from pypexels import PyPexels
api_key = os.environ.get('API_KEY', None) or 'DUMMY_API_KEY'


# Initialize app logging
logger = logging.getLogger()
logging.basicConfig(filename='app_search.log', level=logging.DEBUG)

# pypexels logger defaults to level logging.ERROR
# If you need to change that, use getLogger/setLevel
# on the module logger, like this:
logging.getLogger(PyPexels.logger_name).setLevel(logging.DEBUG)

# add a headers to the log
logger.debug(80*'=')
logging.debug('Testing PyPexels.search()')
logger.debug(80*'=')

# instantiate PyPexels object
py_pexel = PyPexels(api_key=api_key)

# Start with a search query, maximize number of items per page
# Note: this will run until all results pages have been visited,
#       unless a connection error occurs.
#       Typically the API hourly limit gets hit during this
#
search_results_page = py_pexel.search(query='red flowers', per_page=40)
while True:
    for photo in search_results_page.entries:
        print((photo.id, photo.photographer, photo.url))
    if not search_results_page.has_next:
        break
    search_results_page = search_results_page.get_next_page()
