import sys
import os.path
from packages.libvlc import vlc
from PyQt4 import QtCore, QtGui
from main_design import Ui_MainWindow

class VlcPlayer :

    def __init__(self,window,mainWindow):
        # creating a basic vlc instance
        self.vlcInstance = vlc.Instance()
        # creating an empty vlc media player
        self.mediaPlayer = self.vlcInstance.media_player_new()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(200)
        self.isPaused = False
        self.window = window
        self.mainWindow = mainWindow

        self.connectControllers()
        self.setUI();
        

    def connectControllers(self):
        self.mainWindow.connect(self.window.actionOpen_File, QtCore.SIGNAL("triggered()"), self.OpenFile)
        self.mainWindow.connect(self.window.actionExit, QtCore.SIGNAL("triggered()"), sys.exit)
        self.mainWindow.connect(self.timer, QtCore.SIGNAL("timeout()"),self.updateUI)
        self.mainWindow.connect(self.window.seekBar,QtCore.SIGNAL("sliderMoved(int)"),self.setSeekPosition)
        self.mainWindow.connect(self.window.playState, QtCore.SIGNAL("clicked()"),self.setPlayPause)
        self.mainWindow.connect(self.window.volumeBar,QtCore.SIGNAL("valueChanged(int)"),self.setVolume)
        

    def setUI(self):

        self.window.playState.setIcon(QtGui.QIcon('icons/svg/play-2.svg'))
        self.window.playState.setIconSize(QtCore.QSize(65,65))
        self.window.playState.setStyleSheet ('background-color:transparent;')

        self.window.previous.setIcon(QtGui.QIcon('icons/svg/backward-3.svg'))
        self.window.previous.setIconSize(QtCore.QSize(50,50))
        self.window.previous.setStyleSheet ('background-color:transparent;')

        self.window.next.setIcon(QtGui.QIcon('icons/svg/forward-2.svg'))
        self.window.next.setIconSize(QtCore.QSize(50,50))
        self.window.next.setStyleSheet ('background-color:transparent;')

        self.window.palette = self.window.mediaView.palette()
        self.window.palette.setColor(QtGui.QPalette.Window,QtGui.QColor(7,54,66))
        self.window.mediaView.setPalette(self.window.palette)
        self.window.mediaView.setAutoFillBackground(True)
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
            self.window.playState.setIcon(QtGui.QIcon('icons/svg/play-2.svg'))
            self.isPaused = True
        else:
            if self.mediaPlayer.play() == -1:
                self.OpenFile()
                return
            self.mediaPlayer.play()
            self.window.playState.setIcon(QtGui.QIcon('icons/svg/pause-2.svg'))
            self.timer.start()
            self.isPaused = False

    def setVolume(self, volume):
        self.mediaPlayer.audio_set_volume(volume)

    def OpenFile(self,filename = None):
        if filename is None:
            filename = QtGui.QFileDialog.getOpenFileName(self.mainWindow, "Open File", os.path.expanduser('~'))
        if not filename:
            return
            
        # create the media
        if sys.version < '3':
            filename = unicode(filename)
        self.media = self.vlcInstance.media_new(filename)
        # put the media in the media player
        self.mediaPlayer.set_media(self.media)

        # parse the metadata of the file
        self.media.parse()
        # set the title of the track as window title
        self.mainWindow.setWindowTitle(self.media.get_meta(0))

        # the media player has to be 'connected' to the QFrame
        # (otherwise a video would be displayed in it's own window)
        # this is platform specific!
        # you have to give the id of the QFrame (or similar object) to
        # vlc, different platforms have different functions for this
        if sys.platform.startswith('linux'): # for Linux using the X Server
            self.mediaPlayer.set_xwindow(self.window.mediaView.winId())
        elif sys.platform == "win32": # for Windows
            self.mediaPlayer.set_hwnd(self.window.mediaView.winId())
        elif sys.platform == "darwin": # for MacOS
            self.mediaPlayer.set_nsobject(self.window.mediaView.winId())
        self.setPlayPause()
        self.mediaPlayer.stop()
        self.mediaPlayer.play()

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


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    player = VlcPlayer(ui,MainWindow)
    #initMediaPlayer(ui,MainWindow)
    #setUI(ui,MainWindow)
    #initMenu(ui,MainWindow)
    

    MainWindow.show()
    sys.exit(app.exec_())

