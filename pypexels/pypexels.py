###############################################################################
#    Copyright (c) 2017 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: pypexels.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 27 Sep 2017
#   Purpose: Main PyPexels class
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################
# from .src.liblogging import logger
from random import randint
from .src import API_VERSION, LIB_NAME
from .src import Popular
from .src import Curated
from .src import Search
from .src import Random
from .src import SinglePhoto
from .src import SingleVideo
from .src import VideosSearch
from .src import VideosPopular


class PyPexels(object):
    logger_name = LIB_NAME

    def __init__(self, api_key, api_version=API_VERSION):
        self.api_key = api_key
        self.api_version = api_version

    # Photos
    def popular(self, **kwargs):
        return Popular(api_key=self.api_key, api_version=self.api_version, **kwargs)

    def curated(self, **kwargs):
        return Curated(api_key=self.api_key, api_version=self.api_version, **kwargs)

    def search(self, **kwargs):
        return Search(api_key=self.api_key, api_version=self.api_version, **kwargs)

    def random(self, **kwargs):
        return Random(api_key=self.api_key, api_version=self.api_version, **kwargs)

    def single_photo(self, photo_id):
        sp = SinglePhoto(api_key=self.api_key, photo_id=photo_id, api_version=self.api_version)
        return sp.entries

    # Videos
    def videos_popular(self, **kwargs):
        return VideosPopular(api_key=self.api_key, api_version=self.api_version, **kwargs)

    def videos_search(self, **kwargs):
        return VideosSearch(api_key=self.api_key, api_version=self.api_version, **kwargs)

    def single_video(self, video_id):
        sv = SingleVideo(api_key=self.api_key, video_id=video_id, api_version=self.api_version)
        return sv.entries
