sudo apt-get install git python3 python3-pyqt4 python3-pysrt;

sudo git clone https://github.com/kanishkarj/Rave.git /opt/rave/

sudo chmod -R 777 /opt/rave/

sudo ln -s /opt/rave/run.py /bin/rave

sudo cp /opt/rave/rave.desktop /usr/share/applications/rave.desktop
