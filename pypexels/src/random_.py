###############################################################################
#    Copyright (c) 2019 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: random_.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 20 Jan 2019
#   Purpose: Emulate random photo pages, using the Curated Photos endpoint and
#            setting per_page=1, page=random(1,1000), and making it an iterator
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################
from .liblogging import logger
from random import randint
from .errors import PexelsError
from .models import Photo
from .pexelspage import PexelsPage
from .settings import API_VERSION


class Random(PexelsPage):

    def __init__(self, api_key, url='/curated', api_version=API_VERSION, **kwargs):
        valid_options = ['page', 'per_page']
        self.entries_count = kwargs.get('per_page', 0)
        kwargs['per_page'] = 1
        kwargs['page'] = 1
        super(Random, self).__init__(url=url, api_key=api_key, api_version=api_version, valid_options=valid_options, **kwargs)

    @property
    def entries(self):
        for _ in range(self.entries_count):
            random_page = randint(1, 1000)
            random_collection = self.get_page(random_page)
            for entry in random_collection.body.get('photos', []):
                yield Photo.parse(entry)

    @property
    def has_next(self):
        # You can continue to get pages of random photos forever
        return True

    @property
    def has_previous(self):
        # You can't go back in time: no history is kept (for now)
        return False
