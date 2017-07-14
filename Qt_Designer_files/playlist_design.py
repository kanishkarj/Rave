# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playlist.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_playlist(object):
    def setupUi(self, playlist):
        playlist.setObjectName(_fromUtf8("playlist"))
        playlist.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(playlist)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mediaList = QtGui.QListWidget(playlist)
        self.mediaList.setObjectName(_fromUtf8("mediaList"))
        self.gridLayout.addWidget(self.mediaList, 1, 0, 1, 4)
        self.listAdd = QtGui.QPushButton(playlist)
        self.listAdd.setMinimumSize(QtCore.QSize(50, 50))
        self.listAdd.setMaximumSize(QtCore.QSize(50, 50))
        self.listAdd.setText(_fromUtf8(""))
        self.listAdd.setObjectName(_fromUtf8("listAdd"))
        self.gridLayout.addWidget(self.listAdd, 0, 0, 1, 1)
        self.listRemove = QtGui.QPushButton(playlist)
        self.listRemove.setMinimumSize(QtCore.QSize(50, 50))
        self.listRemove.setMaximumSize(QtCore.QSize(50, 50))
        self.listRemove.setText(_fromUtf8(""))
        self.listRemove.setObjectName(_fromUtf8("listRemove"))
        self.gridLayout.addWidget(self.listRemove, 0, 1, 1, 1)
        self.listRearrange = QtGui.QPushButton(playlist)
        self.listRearrange.setMinimumSize(QtCore.QSize(50, 50))
        self.listRearrange.setMaximumSize(QtCore.QSize(50, 50))
        self.listRearrange.setText(_fromUtf8(""))
        self.listRearrange.setObjectName(_fromUtf8("listRearrange"))
        self.gridLayout.addWidget(self.listRearrange, 0, 2, 1, 1)

        self.retranslateUi(playlist)
        QtCore.QMetaObject.connectSlotsByName(playlist)

    def retranslateUi(self, playlist):
        playlist.setWindowTitle(_translate("playlist", "Playlist", None))

