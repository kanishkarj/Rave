yaourt -S git python3 python-pyqt4 python-pip;
sudo pip install pysrt;
sudo git clone https://github.com/kanishkarj/Rave.git /opt/rave

sudo chmod +x /opt/rave/run.py
sudo chmod -r /opt/rave/run.py

sudo ln -s /opt/rave/run.py /bin/rave

sudo cp /opt/rave/rave.desktop /usr/share/applications/rave.desktop
