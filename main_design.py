# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.12
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(751, 484)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 340, 721, 98))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.controllerView = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.controllerView.setMargin(0)
        self.controllerView.setObjectName(_fromUtf8("controllerView"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.timeDone = QtGui.QLabel(self.verticalLayoutWidget)
        self.timeDone.setObjectName(_fromUtf8("timeDone"))
        self.horizontalLayout_2.addWidget(self.timeDone)
        self.seekBar = QtGui.QSlider(self.verticalLayoutWidget)
        self.seekBar.setOrientation(QtCore.Qt.Horizontal)
        self.seekBar.setObjectName(_fromUtf8("seekBar"))
        self.horizontalLayout_2.addWidget(self.seekBar)
        self.timeLeft = QtGui.QLabel(self.verticalLayoutWidget)
        self.timeLeft.setObjectName(_fromUtf8("timeLeft"))
        self.horizontalLayout_2.addWidget(self.timeLeft)
        self.controllerView.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.previous = QtGui.QPushButton(self.verticalLayoutWidget)
        self.previous.setObjectName(_fromUtf8("previous"))
        self.horizontalLayout.addWidget(self.previous)
        self.playState = QtGui.QPushButton(self.verticalLayoutWidget)
        self.playState.setObjectName(_fromUtf8("playState"))
        self.horizontalLayout.addWidget(self.playState)
        self.next = QtGui.QPushButton(self.verticalLayoutWidget)
        self.next.setObjectName(_fromUtf8("next"))
        self.horizontalLayout.addWidget(self.next)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.volumeBar = QtGui.QSlider(self.verticalLayoutWidget)
        self.volumeBar.setEnabled(True)
        self.volumeBar.setMaximumSize(QtCore.QSize(100, 16777215))
        self.volumeBar.setOrientation(QtCore.Qt.Horizontal)
        self.volumeBar.setObjectName(_fromUtf8("volumeBar"))
        self.horizontalLayout.addWidget(self.volumeBar)
        self.controllerView.addLayout(self.horizontalLayout)
        self.mediaView = QtGui.QFrame(self.centralwidget)
        self.mediaView.setGeometry(QtCore.QRect(9, 9, 731, 321))
        self.mediaView.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mediaView.setFrameShadow(QtGui.QFrame.Raised)
        self.mediaView.setObjectName(_fromUtf8("mediaView"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_File = QtGui.QAction(MainWindow)
        self.actionOpen_File.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionOpen_File.setObjectName(_fromUtf8("actionOpen_File"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.timeDone.setText(_translate("MainWindow", "TextLabel", None))
        self.timeLeft.setText(_translate("MainWindow", "TextLabel", None))
        self.previous.setText(_translate("MainWindow", "PushButton", None))
        self.playState.setText(_translate("MainWindow", "PushButton", None))
        self.next.setText(_translate("MainWindow", "PushButton", None))
        self.menuFile.setTitle(_translate("MainWindow", "&Media", None))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File", None))
        self.actionOpen_File.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

