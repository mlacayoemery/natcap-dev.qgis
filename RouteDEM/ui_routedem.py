# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_routedem.ui'
#
# Created: Fri May  2 10:13:06 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_RouteDEM(object):
    def setupUi(self, RouteDEM):
        RouteDEM.setObjectName(_fromUtf8("RouteDEM"))
        RouteDEM.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(RouteDEM)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(RouteDEM)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), RouteDEM.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), RouteDEM.reject)
        QtCore.QMetaObject.connectSlotsByName(RouteDEM)

    def retranslateUi(self, RouteDEM):
        RouteDEM.setWindowTitle(QtGui.QApplication.translate("RouteDEM", "RouteDEM", None, QtGui.QApplication.UnicodeUTF8))

