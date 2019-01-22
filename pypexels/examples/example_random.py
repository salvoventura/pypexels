###############################################################################
#    Copyright (c) 2019 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: example_random.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 20 Jan 2019
#   Purpose: Exemplify usage of Random
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
logging.basicConfig(filename='app_random.log', level=logging.DEBUG)

# pypexels logger defaults to level logging.ERROR
# If you need to change that, use getLogger/setLevel
# on the module logger, like this:
logging.getLogger(PyPexels.logger_name).setLevel(logging.DEBUG)

# add a headers to the log
logger.debug(80*'=')
logging.debug('Testing PyPexels.random()')
logger.debug(80*'=')

# instantiate PyPexels object
py_pexel = PyPexels(api_key=api_key)


random_photos_page = py_pexel.random(per_page=7)
for photo in random_photos_page.entries:
    print(photo.id, photo.photographer, photo.url)

