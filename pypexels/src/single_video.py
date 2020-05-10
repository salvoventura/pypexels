###############################################################################
#    Copyright (c) 2020 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: single_video.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 5/8/2020
#   Purpose: Handle Video Page (direct video access)
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################
# from .liblogging import logger
from .errors import PexelsError
from .models import Video
from .pexelspage import PexelsPage
from .settings import API_VERSION


class SingleVideo(PexelsPage):

    def __init__(self, api_key, video_id, api_version=API_VERSION):
        url = '/videos/videos/{}'.format(video_id)
        super(SingleVideo, self).__init__(url=url, api_key=api_key, api_version=api_version)

    @property
    def entries(self):  # this is abstract so needs to be implemented unless we refactor
        return Video.parse(self.body)
