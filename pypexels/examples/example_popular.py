###############################################################################
#    Copyright (c) 2017 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: example_popular.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 27 Sep 2017
#   Purpose: Exemplify usage of Popular
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
logging.basicConfig(filename='app_popular.log', level=logging.DEBUG)

# pypexels logger defaults to level logging.ERROR
# If you need to change that, use getLogger/setLevel
# on the module logger, like this:
logging.getLogger(PyPexels.logger_name).setLevel(logging.DEBUG)

# add a headers to the log
logger.debug(80*'=')
logging.debug('Testing PyPexels.popular()')
logger.debug(80*'=')

# instantiate PyPexels object
py_pexel = PyPexels(api_key=api_key)

# Start with the generic collection, maximize number of items per page
# Note: this will run until all popular photos have been visited,
#       unless a connection error occurs.
#       Typically the API hourly limit gets hit during this
#
popular_photos_page = py_pexel.popular(per_page=40)
while True:
    for photo in popular_photos_page.entries:
        print(photo.id, photo.photographer, photo.url)
    if not popular_photos_page.has_next:
        break
    popular_photos_page = popular_photos_page.get_next_page()
