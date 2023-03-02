#
# This file is part of goes2image utility.
# Copyright (C) 2023 INPE.
#
# goes2image is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

__author__ = 'Douglas Uba'
__email__  = 'douglas.uba@inpe.br'

from osgeo import osr

# Define KM_PER_DEGREE
KM_PER_DEGREE = 40075.16/360.0

# Define Lat/Lon WSG84 Spatial Reference System (EPSG:4326)
LAT_LON_WGS84 = osr.SpatialReference()
LAT_LON_WGS84.ImportFromProj4('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
