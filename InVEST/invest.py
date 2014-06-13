# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

import webbrowser, os
import os.path, sys

# Set up current path.
currentPath = os.path.dirname( __file__ )

#Import own tools
from site-packages.invest_natcap.routing import RouteDEM

from investaboutgui import InVESTAboutGui

class InVEST:

    def __init__(self, iface):
    # Save reference to the QGIS interface
        self.iface = iface
        self.canvas = self.iface.mapCanvas()

        # Initialise the translation environment.
        userPluginPath = QFileInfo(QgsApplication.qgisUserDbFilePath()).path()+"/python/plugins/InVEST"  
        systemPluginPath = QgsApplication.prefixPath()+"/share/qgis/python/plugins/InVEST"
        locale = QSettings().value("locale/userLocale")
        myLocale = locale[0:2]       
            
        if QFileInfo(userPluginPath).exists():
          pluginPath = userPluginPath+"/i18n/invest_"+myLocale+".qm"
        elif QFileInfo(systemPluginPath).exists():
          pluginPath = systemPluginPath+"/i18n/invest_"+myLocale+".qm"

        self.localePath = pluginPath
        if QFileInfo(self.localePath).exists():
          self.translator = QTranslator()
          self.translator.load(self.localePath)
          
          if qVersion() > '4.3.3':        
            QCoreApplication.installTranslator(self.translator)

    def initGui(self):
        # Add toolbar 
        self.toolBar = self.iface.addToolBar("InVEST")
        self.toolBar.setObjectName("InVEST")
        
        self.menu = QMenu()
        self.menu.setTitle( QCoreApplication.translate( "InVEST","&InVEST" ) )
        self.invest_help = QAction( QCoreApplication.translate("InVEST", "Help" ), self.iface.mainWindow() )
        self.invest_about = QAction( QCoreApplication.translate("InVEST", "About" ), self.iface.mainWindow() )
        self.invest_settings = QAction( QCoreApplication.translate("InVEST", "Settings" ), self.iface.mainWindow() )
        
        # this is just a test.....
##        self.cadtools_dock = QAction( QCoreApplication.translate("CadTools","dock test"), self.iface.mainWindow() )
##        self.menu.addActions( [self.cadtools_help, self.cadtools_about, self.cadtools_dock] )
  
        self.menu.addActions( [self.invest_help, self.invest_about,  self.invest_settings] )

        menu_bar = self.iface.mainWindow().menuBar()
        actions = menu_bar.actions()
        lastAction = actions[ len( actions ) - 1 ]
        menu_bar.insertMenu( lastAction, self.menu )

        self.invest_about.triggered.connect(self.doAbout)
        self.invest_help.triggered.connect(self.doHelp)
        self.invest_settings.triggered.connect(self.doSettings)

        # this is just a test......... 
##        self.cadtools_dock.triggered.connect(self.doTheDock)
        
        # Get the tools
        self.routedem = RouteDEM(self.iface) #,  self.toolBar)

        #self.orthogonaldigitizer = OrthogonalDigitizerTool(self.iface,  self.toolBar, self.menu)
        
        
##    def doTheDock(self):
##        self.dockWidget=CadConsole(self)
##        self.dockWidget.initGui()
##        self.iface.addDockWidget(Qt.BottomDockWidgetArea, self.dockWidget)
        
        
    def doAbout(self):
        d = InVESTAboutGui(self.iface.mainWindow())
        d.show()

    def doHelp(self):
        webbrowser.open("http://ncp-dev.stanford.edu/~dataportal/nightly-build/release_tip/release_tip/documentation/")
        
    def doSettings(self):
        settings = InVESTSettingsGui(self.iface.mainWindow())
        settings.show()

    def unload(self):
        # remove toolbar and menubar
        del self.toolBar
        del self.menu
        
        
