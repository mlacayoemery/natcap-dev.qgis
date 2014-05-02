# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RouteDEM
                                 A QGIS plugin
  d-infinity flow direction algorithm
                             -------------------
        begin                : 2014-04-08
        copyright            : (C) 2014 by Natural Capital Project
        email                : richsharp@stanford.edu
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load RouteDEM class from file RouteDEM
    from routedem import RouteDEM
    return RouteDEM(iface)
