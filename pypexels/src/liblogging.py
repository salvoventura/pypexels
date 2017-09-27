###############################################################################
#    Copyright (c) 2017 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: liblogging.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 27 Sep 2017
#   Purpose: Library logging facility
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################
import logging

from .settings import LIB_NAME, LOG_LEVEL

logger = logging.getLogger(LIB_NAME)
logger.addHandler(logging.NullHandler())
logger.setLevel(LOG_LEVEL)
