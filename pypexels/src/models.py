###############################################################################
#    Copyright (c) 2017 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: models.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 27 Sep 2017
#   Purpose: Data models for parsing data
#
#      Date: 08 May 2020
#  Revision: 2
#   Comment: What's new in revision 2
#            BaseModel parser class
#            Video and Photo, inherit from BaseModel
#
#  Revision: 1
#   Comment: What's new in revision 1
#            Parse Photo
#
###############################################################################


class BaseModel(object):

    @classmethod
    def parse(cls, data):
        """
        Converts JSON structure into BaseModel object where
        each JSON key,value has become a BaseModel property
        This is up to the first level.

        :param data: json body of a single entry
        :return: BaseModel object
        """
        data = data or {}
        base_object = cls() if data else None
        for key, value in data.items():
            setattr(base_object, key, value)
        return base_object


class Photo(BaseModel):
    def get_attribution(self, _format='txt'):
        if _format == 'txt':
            return 'Photo by {} from Pexels'.format(self.photographer)

        if _format == 'html':
            return '<div>' \
                   'Photo by ' \
                   '<strong>' \
                   '<a href="{}>{}</a>' \
                   '</strong> from <strong>' \
                   '<a href="{}">Pexels</a></strong>' \
                   '</div>'.format(self.photographer_url, self.photographer, self.url)


class Video(BaseModel):
    def get_attribution(self, _format='str'):
        if _format == 'str':
            return 'Video by {} from Pexels'.format(self.user.get('name', ''))

        if _format == 'html':
            user_name = self.user.get('name', '')
            user_url = self.user.get('url', '')

            return '<div>' \
                   'Video by ' \
                   '<strong>' \
                   '<a href="{}>{}</a>' \
                   '</strong> from <strong>' \
                   '<a href="{}">Pexels</a></strong>' \
                   '</div>'.format(user_url, user_name, self.url)
