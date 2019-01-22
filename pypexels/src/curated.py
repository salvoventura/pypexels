###############################################################################
#    Copyright (c) 2019 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: curated.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 20 Jan 2019
#   Purpose: Handle Curated photo pages
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################
# from .liblogging import logger
from .errors import PexelsError
from .models import Photo
from .pexelspage import PexelsPage
from .settings import API_VERSION


class Curated(PexelsPage):

    def __init__(self, api_key, url='/curated', api_version=API_VERSION, **kwargs):

        if url.find('/curated') == -1:
            raise PexelsError('Invalid _url for class Curated(): %s' % url)

        valid_options = ['page', 'per_page']
        super(Curated, self).__init__(url=url, api_key=api_key, api_version=api_version, valid_options=valid_options,
                                      **kwargs)

    @property
    def entries(self):
        for entry in self.body.get('photos', []):
            yield Photo.parse(entry)
