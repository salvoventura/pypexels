###############################################################################
#    Copyright (c) 2017 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: errors.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 27 Sep 2017
#   Purpose: Exceptions and Errors
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################


from builtins import str
class PexelsError(Exception):

    def __init__(self, message):
        self.message = str(message) if message else "Unknown error"
        super(PexelsError, self).__init__(message)

    def __str__(self):
        return self.message
