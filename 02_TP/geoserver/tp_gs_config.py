# -*- coding: UTF-8 -*-
#!/usr/bin/env python
from __future__ import (absolute_import, print_function, unicode_literals)

# ----------------------------------------------------------------------------
# Name:         Published layers from GeoServer
# Purpose:      List published layers on a GeoServer
#
# Author:       Julien Moura (https://github.com/Guts/)
#
# Python:       2.7.x
# Created:      04/04/2016
# Updated:      2016
# Licence:      GPL 3
# ----------------------------------------------------------------------------

# ############################################################################
# ########## Libraries #############
# ##################################
# Standard library
import logging
from logging.handlers import RotatingFileHandler
from os import path

# Python 3 backported
from collections import OrderedDict

# 3rd party libraries
from geoserver.catalog import Catalog
from geoserver.resource import Coverage, FeatureType
from geoserver.util import shapefile_and_friends

# ############################################################################
# ########## MAIN #############
# ##################################

# connection
cat = Catalog("http://localhost:8080/geoserver/rest", "admin", "geoserver")

# READ
all_layers = cat.get_layers()

print(len(all_layers))

# WRITE
wks_esipe = cat.get_workspace("ESIPE_IG3")
shapefile_plus_sidecars = shapefile_and_friends(r"data_samples\idf_RGP_emploi_exh")
feat = cat.create_featurestore("test_gsoncif_write", workspace=wks_esipe, data=shapefile_plus_sidecars)
