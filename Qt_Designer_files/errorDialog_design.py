# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'errorDialog.ui'
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

class Ui_errorDialog(object):
    def setupUi(self, errorDialog):
        errorDialog.setObjectName(_fromUtf8("errorDialog"))
        errorDialog.resize(450, 150)
        errorDialog.setMinimumSize(QtCore.QSize(450, 150))
        errorDialog.setMaximumSize(QtCore.QSize(450, 150))
        errorDialog.setWindowTitle(_fromUtf8(""))
        self.verticalLayout = QtGui.QVBoxLayout(errorDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.errorMessage = QtGui.QLabel(errorDialog)
        self.errorMessage.setMinimumSize(QtCore.QSize(432, 90))
        self.errorMessage.setMaximumSize(QtCore.QSize(432, 90))
        self.errorMessage.setText(_fromUtf8(""))
        self.errorMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.errorMessage.setWordWrap(True)
        self.errorMessage.setObjectName(_fromUtf8("errorMessage"))
        self.verticalLayout.addWidget(self.errorMessage)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(180, -1, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.button1 = QtGui.QPushButton(errorDialog)
        self.button1.setMinimumSize(QtCore.QSize(120, 35))
        self.button1.setMaximumSize(QtCore.QSize(120, 35))
        self.button1.setText(_fromUtf8(""))
        self.button1.setObjectName(_fromUtf8("button1"))
        self.horizontalLayout.addWidget(self.button1)
        self.button2 = QtGui.QPushButton(errorDialog)
        self.button2.setMinimumSize(QtCore.QSize(120, 35))
        self.button2.setMaximumSize(QtCore.QSize(120, 35))
        self.button2.setToolTip(_fromUtf8(""))
        self.button2.setWhatsThis(_fromUtf8(""))
        self.button2.setText(_fromUtf8(""))
        self.button2.setObjectName(_fromUtf8("button2"))
        self.horizontalLayout.addWidget(self.button2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(errorDialog)
        QtCore.QMetaObject.connectSlotsByName(errorDialog)

    def retranslateUi(self, errorDialog):
        pass

