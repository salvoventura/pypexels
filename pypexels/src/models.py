###############################################################################
#    Copyright (c) 2017 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: models.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 27 Sep 2017
#   Purpose: Data models for parsing data
#
#  Revision: 1
#   Comment: What's new in revision 1
#            Parse Photo
#
###############################################################################


from builtins import object
class Photo(object):

    @classmethod
    def parse(cls, data):
        """
        Converts JSON structure into Photo object where
        each JSON key,value has become a Photo property

        :param data: json body of a single photo entry
        :return: Photo object
        """
        data = data or {}
        photo = cls() if data else None
        for key, value in list(data.items()):
            setattr(photo, key, value)
        return photo
