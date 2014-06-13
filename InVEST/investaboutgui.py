# -*- coding: latin1 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from ui_investabout import Ui_InVEST_About
import webbrowser, os

currentPath = os.path.dirname(__file__)

class InVESTAboutGui(QDialog, QObject, Ui_InVEST_About):
    def __init__(self, iface):
        QDialog.__init__(self, iface)
        self.iface = iface
        self.setupUi(self)
        self.btnWeb.clicked.connect(self.openWeb)
        self.btnHelp.clicked.connect(self.openHelp)
        self.lblVersion.setText("InVEST 3.0.2")
        self.txtAbout.setText(self.getText())    
    
    def openWeb(self):
        webbrowser.open("http://naturalcapitalproject.org/")

    def openHelp(self):
        webbrowser.open("http://ncp-dev.stanford.edu/~dataportal/nightly-build/release_tip/release_tip/documentation/")    
        
    def getText(self):
        return self.tr(""" 
InVEST is family of models to explore ecosystem service benefits and tradeoffs between spatial planning scenarios at a regional scale.

Ported to QGIS 2.0 API version by Martin Lacayo (mlacayo@stanford.edu)

LICENSING INFORMATION:

This tool has an open license. All people are invited to use the tool
under the following conditions and terms:

Copyright (c) 2013, The Natural Capital Project

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

 * Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.

 * Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the
   distribution.

 * Neither the name of the Natural Capital Project nor the names of
   its contributors may be used to endorse or promote products derived
   from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
""")

