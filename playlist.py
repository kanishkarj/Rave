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
        self.window.mediaList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
            
    def setSingleFile(self,filename):
        self.mediaList.add_media(filename)
        self.updatePlaylistUi()
        return self.mediaList[len(self.mediaList)-1]

    def setMultipleFiles(self,filenames):
        for file in filenames:
            self.mediaList.add_media(file)
        self.updatePlaylistUi()
        return self.mediaList[len(self.mediaList)-len(filenames)]

    def itemToMedia(self,item):
        i=self.window.mediaList.row(item)
        return self.mediaList[i]
    
    def mediaToItem(self,media):
        i=self.mediaList.index_of_item(media)
        return self.window.mediaList.item(i)

    def updatePlaylistUi(self):
        self.window.mediaList.clear()
        for media in self.mediaList:
           self.window.mediaList.addItem(media.get_meta(0))
        
    def setNowPlaying(self,media):
        item=self.mediaToItem(media)
        for i in range(self.window.mediaList.count()):
            if item==self.window.mediaList.item(i):
                self.window.mediaList.item(i).setIcon(QtGui.QIcon('icons/svg/IconSet2/nowPlaying.svg'))
            else:
                self.window.mediaList.item(i).setIcon(QtGui.QIcon(''))
        