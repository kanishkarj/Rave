#!/usr/bin/env python3
#!/usr/local/bin/python
#!/usr/bin/env python
''' import all modules and run media player '''
import sys
import os.path
from packages.libvlc import vlc
from PyQt4 import QtCore, QtGui
from math import floor
from Qt_Designer_files.main_design import Ui_MainWindow
from VlcPlayer import VlcPlayer

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    w = VlcPlayer(app) #create VlcPlayer instance
    w.show()
    sys.exit(app.exec_())
