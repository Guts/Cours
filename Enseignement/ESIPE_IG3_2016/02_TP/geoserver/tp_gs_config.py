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
# from collections import OrderedDict

# 3rd party libraries
from geoserver.catalog import Catalog
from geoserver.resource import Coverage, FeatureType
from geoserver.util import shapefile_and_friends

# ############################################################################
# ########## GLOBALS ###############
# ##################################
# LOG FILE ##
logger = logging.getLogger()
logging.captureWarnings(True)
logger.setLevel(logging.INFO)  # all errors will be get
log_form = logging.Formatter("%(asctime)s || %(levelname)s "
                             "|| %(module)s || %(message)s")
logfile = RotatingFileHandler("LOG_infos_geoserver.log", "a", 10000000, 2)
logfile.setLevel(logging.INFO)
logfile.setFormatter(log_form)
logger.addHandler(logfile)
logger.info('=================================================')

# ############################################################################
# ########## MAIN ##################
# ##################################

# connection
cat = Catalog("http://localhost:8080/geoserver/rest", "admin", "geoserver")

# READ --------------------------------------------------------------------
all_layers = cat.get_layers()

print("Total layers count: " + len(all_layers))

# WRITE -------------------------------------------------------------------
# publish a shapefiles
wks_esipe = cat.get_workspace("ESIPE_IG3")
input_shapefiles = shapefile_and_friends(path.realpath(r"data_samples\idf_RGP_emploi_exh"))
feat = cat.create_featurestore("test_gsoncif_write", workspace=wks_esipe, data=input_shapefiles)
