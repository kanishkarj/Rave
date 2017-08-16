# Rave
Media Player built on `python`, [`libvlc.py`](https://wiki.videolan.org/python_bindings), `pystr` and `pyqt`.

## Requirements
- [Python 3](https://www.python.org/download/releases/3.0/)
- [ptqt4](https://pypi.python.org/pypi/PyQt4)
- [pysrt](https://pypi.python.org/pypi/pysrt)

## Installation
For linux installation can be done by run install script for corresponding distro.
- For Debian based systems execute install script as follows (first give premission) :
    ```bash
        $ chmod +x install_debian.sh
        $ ./install_debian.sh
    ```
- Similarly install script can be run for other distros.
  
## Build instructions
Before building the project ensure that the required packages are installed. Installation instructions for each of them are given below :
- **python 3 :**
    - *[Windows](https://www.python.org/downloads/release/python-362)*
    - *Linux* : python comes preinstalled with most of the Linux distributions. If not then execute the following command in the terminal 
    ```bash
        $ sudo apt-get install python3 python-pip // Debian and derivatives.
        $ sudo pacman -S python3 python-pip // Arch and derivatives.
        $ sudo dnf install python3 python-pip // openSUSE and Red Hat Linux.
    ```
- **pyqt4:**
    - *[Windows](https://riverbankcomputing.com/software/pyqt/download)*
    - *Linux* :
    ```bash
        $ sudo apt-get install python-pyqt4 //Debian and derivatives.
        $ sudo pacman -S python-pyqt4 //arch and derivatives.
        $ sudo dnf install python-pyqt4 //OpenSuse and Redhat distributions.
    ```
- **pysrt:**
    - *Windows* :
    Execute the following statement in the command prompt with administrative privileges.
    ```batch
        pip install pysrt
    ```
    - *Linux* : 
    ```bash
        $ sudo pip install pysrt
    ``` 

# License

This project is licensed under the terms of the GNU GPLv3.


