import sys
import os.path
from packages.libvlc import vlc
from PyQt4 import QtCore, QtGui
from playlist_design import Ui_playlist

class Playlist(QtGui.QDialog):
    def __init__(self):
        super(Playlist,self).__init__()
        self.window=Ui_playlist()
        self.window.setupUi(self)
        self.mediaList=vlc.Instance().media_list_new()

    def setSingleFile(self,filename):
        self.mediaList.add_media(filename)

        self.window.mediaList.clear()
        
        for media in self.mediaList:
           self.window.mediaList.addItem(media.get_meta(0))

        return self.mediaList[len(self.mediaList)-1]

    def setMultipleFiles(self,filenames):
        for file in filenames:
            self.mediaList.add_media(file)

        self.window.mediaList.clear()
        
        for media in self.mediaList:
           self.window.mediaList.addItem(media.get_meta(0))

        return self.mediaList[len(self.mediaList)-len(filenames)]

