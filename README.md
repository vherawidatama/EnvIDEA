# EnvIDEA

## Troubleshoot Error WebSocket IDEA Compatibility Using Debian 9.9.0

1. Wajib Update & Upgrade dengan perintah apt update && apt upgrade
2. sudo apt-get install python2.7 build-essential autoconf libtool pkg-config python-opengl python-pil python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev libssl-dev python-pip python-setuptools git unzip
3. Install pycrypto-2.0.1 compare pycrypto-2.6.1
   - tar -zxvf pycrypto2.0.1.tar.gz
   - python setup.py install
   - pip uninstall pycrypto
4. Install pycrypto-2.6.1
   - tar -zxvf pycrypto2.6.1.tar.gz
   - python setup.py install
5. Install Pycryptoplus
   - unzip pycryptoplus
   - python setup.py install
   
## HAPPY USING TUTORIAL FOR TROUBLESHOOT ERROR WEBSOCKET IDEA
