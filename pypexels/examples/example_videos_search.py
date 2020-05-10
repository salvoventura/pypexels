###############################################################################
#    Copyright (c) 2020 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: example_video_search.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 08 May 2020
#   Purpose: Exemplify usage of Video Search
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
logging.basicConfig(filename='app_video_search.log', level=logging.DEBUG)

# pypexels logger defaults to level logging.ERROR
# If you need to change that, use getLogger/setLevel
# on the module logger, like this:
logging.getLogger(PyPexels.logger_name).setLevel(logging.DEBUG)

# add a headers to the log
logger.debug(80*'=')
logging.debug('Testing PyPexels.videos_search()')
logger.debug(80*'=')

# instantiate PyPexels object
py_pexel = PyPexels(api_key=api_key)

# Start with the generic collection, maximize number of items per page
# Note: this will run until all popular photos have been visited,
#       unless a connection error occurs.
#       Typically the API hourly limit gets hit during this
#
#  Note2: the video API is not currently (May 2020) producing next_page/prev_page links
#         so this example will not be able to keep walking forward
#
search_videos_page = py_pexel.videos_search(query="red+flower", per_page=40)
while True:
    for video in search_videos_page.entries:
        print(video.id, video.user.get('name'), video.url)
    if not search_videos_page.has_next:
        break
    search_videos_page = search_videos_page.get_next_page()
