# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# -----------------------------------------------------------------------------
# Name:         UData Python Client
# Purpose:      Abstraction class to manipulate data.gouv.fr API
#
# Author:       Julien Moura (@geojulien)
#
# Python:       3.6+
# -----------------------------------------------------------------------------

# #############################################################################
# ########## Libraries #############
# ##################################

# Standard library
import logging
from os import environ
from sys import platform as opersys, exit

# 3rd party library
import requests

# ##############################################################################
# ############ Globals ############
# #################################

# LOG
logger = logging.getLogger("uDataPyClient")

# #############################################################################
# ########## Classes ###############
# ##################################


class UiWindowTitleSetter(object):
    """Use DataGouvFR REST API.

    Full doc at (French): https://www.data.gouv.fr/fr/apidoc/
    """

    def __init__(self, window, new_title="ABCDEFGHIJK"):
        """TO DOC"""
        window.setWindowTitle(new_title)

# ##############################################################################
# ##### Stand alone program ########
# ##################################
if __name__ == '__main__':
    """ standalone execution """
