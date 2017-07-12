import sys
import os.path
from packages.libvlc import vlc
from PyQt4 import QtCore, QtGui
from math import floor
from main_design import Ui_MainWindow
from specificTimeDialog_design import Ui_Dialog
from playlist import Playlist

class VlcPlayer(QtGui.QMainWindow):
    resized = QtCore.pyqtSignal()

    def  __init__(self,param_app, parent=None):
        super(VlcPlayer, self).__init__(parent=parent)
        self.window = Ui_MainWindow()
        self.window.setupUi(self)

        self.resized.connect(self.windowResized)
         # creating a basic vlc instance
        self.vlcInstance = vlc.Instance()
        # creating an empty vlc media player
        self.mediaPlayer = self.vlcInstance.media_player_new()
        self.mediaListPlayer = self.vlcInstance.media_list_player_new()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(200)
        self.isPaused = False
        self.isFullscreen = False
        self.connectControllers()
        self.setUI()

        self.playlist = Playlist()

        self.dialog=QtGui.QDialog()
        self.dialog.window=Ui_Dialog()
        self.dialog.window.setupUi(self.dialog)
        self.dialog.window.reset.setIcon(QtGui.QIcon('icons/svg/IconSet2/refresh.svg'))
        self.dialog.window.reset.setIconSize(QtCore.QSize(30,30))
        self.dialog.window.reset.setStyleSheet ('background-color:transparent;')

        self.app = param_app
        self.window.centralwidget.setMouseTracking(True)
        self.window.volumeBar.setValue(50)
        self.setVolume(50)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(VlcPlayer, self).resizeEvent(event)

    def windowResized(self):
        if self.isFullScreen() == False:
            cvHeight = 130
            mvMinHeight = 200
            self.window.mediaView.setGeometry(QtCore.QRect(0, 0, self.width(), self.height()-25-cvHeight))
            self.window.controlView.setGeometry(QtCore.QRect(0,self.window.mediaView.height(), self.width(), cvHeight))
        
    def connectControllers(self):
        self.connect(self.window.actionOpen_File, QtCore.SIGNAL("triggered()"), self.OpenFile)
        self.connect(self.window.actionOpen_Multiple_Files, QtCore.SIGNAL("triggered()"), self.OpenMultipleFiles)
        self.connect(self.window.actionExit, QtCore.SIGNAL("triggered()"), sys.exit)
        self.connect(self.timer, QtCore.SIGNAL("timeout()"),self.updateUI)
        self.connect(self.window.seekBar,QtCore.SIGNAL("sliderMoved(int)"),self.setSeekPosition)
        self.connect(self.window.playState, QtCore.SIGNAL("clicked()"),self.setPlayPause)
        self.connect(self.window.next, QtCore.SIGNAL("clicked()"),self.setNext)
        self.connect(self.window.previous, QtCore.SIGNAL("clicked()"),self.setPrevious)
        self.connect(self.window.fullscreenButton, QtCore.SIGNAL("clicked()"),self.toggleFullscreen)
        self.connect(self.window.volumeBar,QtCore.SIGNAL("valueChanged(int)"),self.setVolume)
        self.connect(self.window.playlistButton,QtCore.SIGNAL("clicked()"),self.showPlaylist)
        self.connect(self.window.stopButton,QtCore.SIGNAL("clicked()"),self.stopPlayer)
        self.connect(self.window.muteButton,QtCore.SIGNAL("clicked()"),self.toggleMute)
        self.connect(self.window.actionX0_5,QtCore.SIGNAL("triggered()"),lambda rate=0.5: self.mediaPlayer.set_rate(rate))
        self.connect(self.window.actionX_1,QtCore.SIGNAL("triggered()"),lambda rate=1: self.mediaPlayer.set_rate(rate))
        self.connect(self.window.actionX_2,QtCore.SIGNAL("triggered()"),lambda rate=2: self.mediaPlayer.set_rate(rate))
        self.connect(self.window.actionX_4,QtCore.SIGNAL("triggered()"),lambda rate=4: self.mediaPlayer.set_rate(rate))
        self.connect(self.window.actionX_8,QtCore.SIGNAL("triggered()"),lambda rate=8: self.mediaPlayer.set_rate(rate))
        self.connect(self.window.actionJump_Forward,QtCore.SIGNAL("triggered()"),self.jumpForward)
        self.connect(self.window.actionJump_Backward,QtCore.SIGNAL("triggered()"),self.jumpBackward)
        self.connect(self.window.actionMute,QtCore.SIGNAL("triggered()"),self.toggleMute)
        self.connect(self.window.actionFullscreen,QtCore.SIGNAL("triggered()"),self.toggleFullscreen)
        self.connect(self.window.actionPlay,QtCore.SIGNAL("triggered()"),self.setPlayPause)
        self.connect(self.window.actionStop,QtCore.SIGNAL("triggered()"),self.stopPlayer)
        self.connect(self.window.actionPrevious,QtCore.SIGNAL("triggered()"),self.setPrevious)
        self.connect(self.window.actionNext,QtCore.SIGNAL("triggered()"),self.setNext)  
        self.connect(self.window.actionJump_to_specific_time,QtCore.SIGNAL("triggered()"),self.jumpToSpecificTime)                     
        QtGui.QShortcut("Ctrl+T", self, self.jumpToSpecificTime)


    def keyPressEvent(self,event):
        if self.isFullScreen() and event.key()==QtCore.Qt.Key_Escape:
            self.showMaximized()
            self.window.menubar.show()
            self.window.centralwidget.setStyleSheet("")
            self.window.controlView.show()
        if event.key()==QtCore.Qt.Key_F:
            self.toggleFullscreen()
        if event.key()==QtCore.Qt.Key_M:
            self.toggleMute()
        if event.key()==QtCore.Qt.Key_Space:
            self.setPlayPause()

    def mouseDoubleClickEvent(self,event):
        if self.isFullScreen()==False:
            self.showFullScreen()
            self.window.controlView.hide()
            self.window.menubar.hide()
            scr_res = self.app.desktop().screenGeometry();
            self.window.mediaView.setGeometry(QtCore.QRect(0, 0, scr_res.width(), scr_res.height()))
            
        else:            
            self.showMaximized()
            self.window.controlView.show()
            self.window.menubar.show()
    
    

    def setNext(self) :
        pos=self.playlist.mediaList.index_of_item(self.mediaPlayer.get_media())
        if pos!= self.playlist.mediaList.count()-1:
            self.media=self.playlist.mediaList.item_at_index(pos+1)
        else:
            self.media=self.playlist.mediaList.item_at_index(pos)
        self.mediaPlayer.set_media(self.media)
        self.media.parse()
        self.setWindowTitle(self.media.get_meta(0))
        self.setPlayPause()
    
    def setPrevious(self) :
        pos=self.playlist.mediaList.index_of_item(self.mediaPlayer.get_media())
        if pos!= 0:
            self.media=self.playlist.mediaList.item_at_index(pos-1)
        else:
            self.media=self.playlist.mediaList.item_at_index(pos)
        self.mediaPlayer.set_media(self.media)
        self.media.parse()
        self.setWindowTitle(self.media.get_meta(0))
        self.setPlayPause()

    def toggleFullscreen(self):
        if self.isFullScreen()==False:
            self.showFullScreen()
            self.window.controlView.hide()
            self.window.menubar.hide()
            scr_res = self.app.desktop().screenGeometry();
            self.window.mediaView.setGeometry(QtCore.QRect(0, 0, scr_res.width(), scr_res.height()))
            
        else:
            self.showMaximized()
            self.window.controlView.show()
            self.window.menubar.show()
    

    def setUI(self):
        
        self.window.mediaView.setStyleSheet('background-color:black;border-radius:1px;')
        
        self.window.playState.setIcon(QtGui.QIcon('icons/svg/IconSet2/play.svg'))
        self.window.playState.setIconSize(QtCore.QSize(50,50))
        self.window.playState.setStyleSheet ('background-color:transparent;')
        
        self.window.previous.setIcon(QtGui.QIcon('icons/svg/IconSet2/previous.svg'))
        self.window.previous.setIconSize(QtCore.QSize(40,40))
        self.window.previous.setStyleSheet ('background-color:transparent;')

        self.window.next.setIcon(QtGui.QIcon('icons/svg/IconSet2/next.svg'))
        self.window.next.setIconSize(QtCore.QSize(40,40))
        self.window.next.setStyleSheet ('background-color:transparent;')

        self.window.fullscreenButton.setIcon(QtGui.QIcon('icons/svg/IconSet2/fullscreen.svg'))
        self.window.fullscreenButton.setIconSize(QtCore.QSize(20,20))
        self.window.fullscreenButton.setStyleSheet ('background-color:transparent;')

        self.window.playlistButton.setIcon(QtGui.QIcon('icons/svg/IconSet2/playlist.svg'))
        self.window.playlistButton.setIconSize(QtCore.QSize(30,30))
        self.window.playlistButton.setStyleSheet ('background-color:transparent;')

        self.window.stopButton.setIcon(QtGui.QIcon('icons/svg/IconSet2/stop.svg'))
        self.window.stopButton.setIconSize(QtCore.QSize(30,30))
        self.window.stopButton.setStyleSheet ('background-color:transparent;')

        self.window.seekBar.setMaximum(1000)
        self.window.volumeBar.setMaximum(100)
        self.window.volumeBar.setValue(self.mediaPlayer.audio_get_volume())
        if sys.platform.startswith('linux'): # for Linux using the X Server
            self.mediaPlayer.set_xwindow(self.window.mediaView.winId())
        elif sys.platform == "win32": # for Windows
            self.mediaPlayer.set_hwnd(self.window.mediaView.winId())
        elif sys.platform == "darwin": # for MacOS
            self.mediaPlayer.set_nsobject(self.window.mediaView.winId())
            
    def setSeekPosition(self, position):
        self.mediaPlayer.set_position(position / 1000.0)

    def setPlayPause(self):
        if self.mediaPlayer.is_playing():
            self.mediaPlayer.pause()
            self.window.playState.setIcon(QtGui.QIcon('icons/svg/IconSet2/play.svg'))
            self.isPaused = True
        else:
            if self.mediaPlayer.play() == -1 :
                self.OpenFile()
                return
            self.mediaPlayer.play()
            self.window.playState.setIcon(QtGui.QIcon('icons/svg/IconSet2/pause.svg'))
            self.timer.start()
            self.isPaused = False

    def setVolume(self, volume):
        # here the factor is multiplied with 2, hence the volume is out of 200%
        self.mediaPlayer.audio_set_volume(volume*2)
        if volume==0:
            self.window.muteButton.setIcon(QtGui.QIcon('icons/svg/IconSet2/volume-off.svg'))
            self.window.muteButton.setIconSize(QtCore.QSize(25,25))
            self.window.muteButton.setStyleSheet ('background-color:transparent;')
        elif volume>0 and volume<=50:
            self.window.muteButton.setIcon(QtGui.QIcon('icons/svg/IconSet2/volume-medium.svg'))
            self.window.muteButton.setIconSize(QtCore.QSize(25,25))
            self.window.muteButton.setStyleSheet ('background-color:transparent;')
        elif volume>50 and volume<=100:
            self.window.muteButton.setIcon(QtGui.QIcon('icons/svg/IconSet2/volume-high.svg'))
            self.window.muteButton.setIconSize(QtCore.QSize(25,25))
            self.window.muteButton.setStyleSheet ('background-color:transparent;')

    def setMedia(self,media):
        # parse the metadata of the file
        media.parse()
        # set the title of the track as window title
        self.setWindowTitle(media.get_meta(0))
        # the media player has to be 'connected' to the QFrame
        # (otherwise a video would be displayed in it's own window)
        # this is platform specific!
        # you have to give the id of the QFrame (or similar object) to
        # vlc, different platforms have different functions for this
        #self.mediaListPlayer.set_media_player(self.mediaPlayer)
        #self.mediaPlayer = self.mediaListPlayer.get_media_player()

        # A hack to make everything to work properly :P
        self.mediaPlayer.set_media(media)
        #self.mediaListPlayer.next()
        if sys.platform.startswith('linux'): # for Linux using the X Server
            self.mediaPlayer.set_xwindow(self.window.mediaView.winId())
        elif sys.platform == "win32": # for Windows
            self.mediaPlayer.set_hwnd(self.window.mediaView.winId())
        elif sys.platform == "darwin": # for MacOS
            self.mediaPlayer.set_nsobject(self.window.mediaView.winId())
        self.setPlayPause()
        self.mediaPlayer.play()
        self.window.timeLeft.setText(self.stringTimeFormat(self.media.get_duration()))
        
    def OpenFile(self,filename = None):
        if filename is None:
            filename = QtGui.QFileDialog.getOpenFileName(self, "Open File", os.path.expanduser('~'))
        if not filename:
            return
        if sys.version < '3':
            filename = unicode(filename)
        
        self.media=self.playlist.setSingleFile(filename)
        self.setMedia(self.media)
        
    def OpenMultipleFiles(self,filenames = None):
        if filenames is None:
            filenames = QtGui.QFileDialog.getOpenFileNames(self, "Open File", os.path.expanduser('~'))
        if not filenames:
            return
        if sys.version < '3':
            for i in range(0,len(filenames),1) :
                filenames[i] = unicode(filenames[i])
        
        self.media=self.playlist.setMultipleFiles(filenames)
        self.setMedia(self.media)       

    def stringTimeFormat(self, time):

        strng = "00:00:00"
        
        if time<0 :
            return strng
        
        hr = floor((time/3600)/1000)
        mnt = floor((time - hr*1000*3600)/60000)
        sec = floor((time - hr*3600*1000 - mnt*60*1000)/1000)
        
        strHr = str(hr)
        strMnt = str(mnt)
        strSec = str(sec)
        
        if hr<10 :
            strHr = "0" + strHr
        if mnt<10 :
            strMnt = "0" + strMnt
        if sec<10 :
            strSec = "0" + strSec

        strng = strHr + ":" + strMnt + ":" + strSec 
        return strng

    def updateUI(self):
        # setting the slider to the desired position
        self.window.seekBar.setValue(self.mediaPlayer.get_position() * 1000)

        if not self.mediaPlayer.is_playing():
            # no need to call this function if nothing is played
            self.timer.stop()
            if not self.isPaused:
                # after the video finished, the play button stills shows
                # "Pause", not the desired behavior of a media player
                # this will fix it
                self.mediaPlayer.stop()
                self.window.playState.setIcon(QtGui.QIcon('icons/svg/IconSet2/play.svg'))
       
        self.window.timeDone.setText(self.stringTimeFormat(int(self.media.get_duration() * self.mediaPlayer.get_position())))
        self.window.timeLeft.setText(self.stringTimeFormat(self.media.get_duration()))

    def showPlaylist(self):
        self.playlist.show()
        self.playlist.connect(self.playlist.window.listAdd,QtCore.SIGNAL("clicked()"),self.addtoPlaylist)

    def addtoPlaylist(self,filenames=None):
        if filenames is None:
            filenames = QtGui.QFileDialog.getOpenFileNames(self, "Open File", os.path.expanduser('~'))
        if not filenames:
            return
        if sys.version < '3':
            for i in range(0,len(filenames),1) :
                filenames[i] = unicode(filenames[i])
        
        if self.mediaPlayer.get_media()==None:
            self.media=self.playlist.setMultipleFiles(filenames)
            self.setMedia(self.media)
        else:
            self.playlist.setMultipleFiles(filenames)

    def stopPlayer(self):
        self.mediaPlayer.stop()

    def toggleMute(self):
        if self.mediaPlayer.audio_get_volume()!=0:
            self.setVolume(0)
            self.window.volumeBar.setValue(0)
        else:
            self.setVolume(50)
            self.window.volumeBar.setValue(50)
    def jumpForward(self):
        self.mediaPlayer.set_time(self.mediaPlayer.get_time()+10000)
        self.updateUI()

    def jumpBackward(self):
        self.mediaPlayer.set_time(self.mediaPlayer.get_time()-10000)
        self.updateUI()

    def jumpToSpecificTime(self):
        self.resetValues()
        self.dialog.show()
        self.dialog.window.goButton.clicked.connect(self.goToTime)
        self.dialog.window.reset.clicked.connect(self.resetValues)

    def goToTime(self):
        time=(self.dialog.window.hours.value()*3600+self.dialog.window.minutes.value()*60+self.dialog.window.seconds.value())*1000
        if time<=self.mediaPlayer.get_length():
            self.mediaPlayer.set_time(time)
            self.updateUI()
            self.dialog.close()
        else:
            self.mediaPlayer.set_time(self.mediaPlayer.get_length())
            self.updateUI()
            self.dialog.close()
    
    def resetValues(self):
        self.dialog.window.hours.setValue(0)
        self.dialog.window.minutes.setValue(0)
        self.dialog.window.seconds.setValue(0)

