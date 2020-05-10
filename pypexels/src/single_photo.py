###############################################################################
#    Copyright (c) 2020 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: single_photo.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 5/8/2020
#   Purpose: Handle Photo Page (direct photo access)
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


class SinglePhoto(PexelsPage):

    def __init__(self, api_key, photo_id, api_version=API_VERSION):
        url = '/photos/{}'.format(photo_id)
        super(SinglePhoto, self).__init__(url=url, api_key=api_key, api_version=api_version)

    @property
    def entries(self):  # this is abstract so needs to be implemented unless we refactor
        return Photo.parse(self.body)
