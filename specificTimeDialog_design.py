# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'specificTimeDialog.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(360, 100)
        Dialog.setMinimumSize(QtCore.QSize(360, 100))
        Dialog.setMaximumSize(QtCore.QSize(360, 100))
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 42))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(90, 40))
        self.label.setMaximumSize(QtCore.QSize(90, 40))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.hours = QtGui.QSpinBox(self.horizontalLayoutWidget)
        self.hours.setMinimumSize(QtCore.QSize(45, 30))
        self.hours.setMaximumSize(QtCore.QSize(45, 30))
        self.hours.setMaximum(24)
        self.hours.setProperty("value", 0)
        self.hours.setObjectName(_fromUtf8("hours"))
        self.horizontalLayout.addWidget(self.hours)
        self.label_1 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.horizontalLayout.addWidget(self.label_1)
        self.minutes = QtGui.QSpinBox(self.horizontalLayoutWidget)
        self.minutes.setMinimumSize(QtCore.QSize(45, 30))
        self.minutes.setMaximumSize(QtCore.QSize(45, 30))
        self.minutes.setMaximum(59)
        self.minutes.setObjectName(_fromUtf8("minutes"))
        self.horizontalLayout.addWidget(self.minutes)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.seconds = QtGui.QSpinBox(self.horizontalLayoutWidget)
        self.seconds.setMinimumSize(QtCore.QSize(45, 30))
        self.seconds.setMaximumSize(QtCore.QSize(45, 30))
        self.seconds.setMaximum(59)
        self.seconds.setObjectName(_fromUtf8("seconds"))
        self.horizontalLayout.addWidget(self.seconds)
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.reset = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.reset.setMinimumSize(QtCore.QSize(30, 30))
        self.reset.setMaximumSize(QtCore.QSize(30, 30))
        self.reset.setText(_fromUtf8(""))
        self.reset.setObjectName(_fromUtf8("reset"))
        self.horizontalLayout.addWidget(self.reset)
        self.goButton = QtGui.QPushButton(Dialog)
        self.goButton.setGeometry(QtCore.QRect(250, 60, 99, 30))
        self.goButton.setObjectName(_fromUtf8("goButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Go To Time", None))
        self.label.setText(_translate("Dialog", "Go To Time: ", None))
        self.label_1.setText(_translate("Dialog", "H", None))
        self.label_2.setText(_translate("Dialog", "m", None))
        self.label_3.setText(_translate("Dialog", "s", None))
        self.goButton.setText(_translate("Dialog", "Go", None))

