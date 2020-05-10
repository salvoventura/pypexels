###############################################################################
#    Copyright (c) 2020 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: video_search.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 05 May 2020
#   Purpose: Handle Search photo pages
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################
# from .liblogging import logger
from .errors import PexelsError
from .models import Video
from .pexelspage import PexelsPage
from .settings import API_VERSION   # /videos/ API URL does not contain the API VERSION


class VideosSearch(PexelsPage):

    def __init__(self, api_key, url='/videos/search', api_version=API_VERSION, **kwargs):

        if url.find('/videos/search') == -1:
            raise PexelsError('Invalid _url for class VideosSearch(): %s' % url)

        if 'query' not in kwargs and 'query' not in url:
            raise PexelsError('Parameter "query" is mandatory for class VideosSearch()')

        valid_options = ['page', 'per_page', 'query', 'min_width', 'max_width', 'min_duration', 'max_duration']
        super(VideosSearch, self).__init__(url=url, api_key=api_key, api_version=api_version,
                                           valid_options=valid_options,
                                           **kwargs)

    @property
    def entries(self):
        for entry in self.body.get('videos', []):
            yield Video.parse(entry)
