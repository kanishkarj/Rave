import sys
import os.path
from packages.libvlc import vlc
from PyQt4 import QtCore, QtGui
from Qt_Designer_files.playlist_design import Ui_playlist

class Playlist(QtGui.QDialog):
    def __init__(self):
        super(Playlist,self).__init__()
        self.window=Ui_playlist()
        self.window.setupUi(self)
        self.mediaList=vlc.Instance().media_list_new()

        self.window.listAdd.setIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__),'icons/svg/IconSet2/addMedia.svg')))
        self.window.listAdd.setIconSize(QtCore.QSize(40,40))
        self.window.listAdd.setStyleSheet ('background-color:transparent; border-radius:5em;')

        self.window.listRemove.setIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__),'icons/svg/IconSet2/removeMedia.svg')))
        self.window.listRemove.setIconSize(QtCore.QSize(30,30))
        self.window.listRemove.setStyleSheet ('background-color:transparent; border-radius:5em;')

        self.window.listRearrange.setIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__),'icons/svg/IconSet2/rearrange.svg')))
        self.window.listRearrange.setIconSize(QtCore.QSize(30,30))
        self.window.listRearrange.setStyleSheet ('background-color:transparent; border-radius:5em;')
        
        self.window.mediaList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.connect(self.window.listRearrange,QtCore.SIGNAL("clicked()"),self.rearrangePlaylist)
        
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
        for media in self.mediaList:
            if media.get_meta(0)==item.text():
                return media
    
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
                self.window.mediaList.item(i).setIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__),'icons/svg/IconSet2/nowPlaying.svg')))
            else:
                self.window.mediaList.item(i).setIcon(QtGui.QIcon(''))
    
    def rearrangePlaylist(self):
        if self.window.mediaList.dragDropMode()!= QtGui.QAbstractItemView.InternalMove:
            self.window.mediaList.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
            self.window.listRearrange.setIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__),'icons/svg/IconSet2/done.svg')))
            self.window.listRearrange.setIconSize(QtCore.QSize(30,30))
            self.window.listRearrange.setStyleSheet ('background-color:transparent;')
        else:
            self.window.mediaList.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
            self.window.listRearrange.setIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__),'icons/svg/IconSet2/rearrange.svg')))
            self.window.listRearrange.setIconSize(QtCore.QSize(30,30))
            self.window.listRearrange.setStyleSheet ('background-color:transparent;')
            mList=vlc.Instance().media_list_new()
            for i in range(self.window.mediaList.count()):
                mList.add_media(self.itemToMedia(self.window.mediaList.item(i)))
            self.mediaList=mList