import sys
import os.path
from packages.libvlc import vlc
from PyQt4 import QtCore, QtGui
from math import floor
from playlist_design import Ui_playlist

playlistDialog = 1
playlistDialog = QtGui.QDialog()
playlistDialog.window = Ui_playlist()
playlistDialog.window.setupUi(playlistDialog)
