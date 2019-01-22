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


class PyPexels(object):
    logger_name = LIB_NAME

    def __init__(self, api_key, api_version=API_VERSION):
        self.api_key = api_key
        self.api_version = api_version

    def popular(self, **kwargs):
        return Popular(api_key=self.api_key, api_version=self.api_version, **kwargs)

    def curated(self, **kwargs):
        return Curated(api_key=self.api_key, api_version=self.api_version, **kwargs)

    def search(self, **kwargs):
        return Search(api_key=self.api_key, api_version=self.api_version, **kwargs)

    def random(self, **kwargs):
        return Random(api_key=self.api_key, api_version=self.api_version, **kwargs)
