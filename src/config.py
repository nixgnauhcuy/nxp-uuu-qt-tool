import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QSettings

USER_CONFIG_INI = 'user.ini'

configini = QSettings(USER_CONFIG_INI, QSettings.Format.IniFormat)

config_param = {
    "fastboot": '',
    "uboot": '',
    "kernel": '',
    "devicetree": '',
    "rootfs": '',
}


def configLoad():
    for key in configini.allKeys():
        config_param[key] = configini.value(key)


def configCreate():
    for key, value in config_param.items():
        configini.setValue(key, value)

def init():
    if os.path.exists(f'{USER_CONFIG_INI}'):
        configLoad()
    else:
        configCreate()
