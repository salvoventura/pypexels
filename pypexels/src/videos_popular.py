###############################################################################
#    Copyright (c) 2020 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: video_popular.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 05 May 2020
#   Purpose: Handle Popular photo pages
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################
# from .liblogging import logger
from .errors import PexelsError
from .models import Video
from .pexelspage import PexelsPage
from .settings import API_VERSION  # /videos/ API URL does not contain the API VERSION


class VideosPopular(PexelsPage):

    def __init__(self, api_key, url='/videos/popular', api_version="", **kwargs):

        if url.find('/videos/popular') == -1:
            raise PexelsError('Invalid _url for class VideosPopular(): %s' % url)

        valid_options = ['page', 'per_page', 'query', 'min_width', 'max_width', 'min_duration', 'max_duration']
        super(VideosPopular, self).__init__(url=url, api_key=api_key, api_version=api_version,
                                            valid_options=valid_options,
                                            **kwargs)

    @property
    def entries(self):
        for entry in self.body.get('videos', []):
            yield Video.parse(entry)
