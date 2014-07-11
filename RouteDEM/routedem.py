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
"""
import sys
import os

import webbrowser

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "site-packages"))
sys.argv = {}

from invest_natcap.routing import routedem
from invest_natcap.iui import modelui
from invest_natcap.iui import base_widgets

# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from routedemdialog import RouteDEMDialog
import os.path


class RouteDEM:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'routedem_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = base_widgets.MainWindow(modelui.ModelUI,
                                   "/home/mlacayo/workspace/invest3/invest_natcap/iui/routedem.json")

    def initGui(self):
        # Add toolbar 
        self.toolBar = self.iface.addToolBar("RouteDEM")
        self.toolBar.setObjectName("RouteDEM")
        
        self.menu = QMenu()
        self.menu.setTitle( QCoreApplication.translate( "RouteDEM","&RouteDEM" ) )
        self.routedem_help = QAction( QCoreApplication.translate("RouteDEM", "Help" ), self.iface.mainWindow() )
        self.routedem_routedem  = QAction( QCoreApplication.translate("RouteDEM", "RouteDEM" ), self.iface.mainWindow() )
        self.routedem_about = QAction( QCoreApplication.translate("RouteDEM", "About" ), self.iface.mainWindow() )

        self.new_menu = QMenu()
        self.new_menu.setTitle( QCoreApplication.translate( "RouteDEM_group","&Group" ) )
        self.new_menu.addActions([self.routedem_routedem])
        self.menu.addMenu(self.new_menu)

        self.menu.addActions( [self.routedem_help, self.routedem_routedem, self.routedem_about] )

        menu_bar = self.iface.mainWindow().menuBar()
        actions = menu_bar.actions()
        lastAction = actions[ len( actions ) - 1 ]
        menu_bar.insertMenu( lastAction, self.menu )

        self.routedem_about.triggered.connect(self.doAbout)
        self.routedem_help.triggered.connect(self.doHelp)
        self.routedem_routedem.triggered.connect(self.run)
       
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/routedem/icon.png"),
            u"RouteDEM", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
##        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&RouteDEM", self.action)

        self.toolBar.addAction(self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&RouteDEM", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            pass

    def doAbout(self):
        webbrowser.open("about:blank")
        
    def doHelp(self):
        webbrowser.open("about:blank")        
