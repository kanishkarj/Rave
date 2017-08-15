yaourt -S git python3 python-pyqt4 python-pip;
sudo pip install pysrt;
echo "
[Desktop Entry]
Version=1.0
Name=Test        
Comment=Cross-platform media player built on libvlc and qt.
Exec= python3 ~/Development/rave/run.py
Icon=utilities-terminal
Terminal=false
Type=Application
Categories=Application;
" > /usr/share/applications/rave.desktop
