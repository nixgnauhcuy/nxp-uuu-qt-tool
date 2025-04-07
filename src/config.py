import os
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QSettings, QStandardPaths

APP_NAME = "nxp-uuu-qt-tool"

if sys.platform == "win32":
    config_dir = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
else:
    config_dir = os.path.expanduser("~/.config")

config_path = os.path.join(config_dir, APP_NAME, "user.ini")

os.makedirs(os.path.dirname(config_path), exist_ok=True)

USER_CONFIG_INI = config_path

configini = QSettings(USER_CONFIG_INI, QSettings.Format.IniFormat)

config_param = {
    "fastboot": "",
    "uboot": "",
    "kernel": "",
    "devicetree": "",
    "rootfs": "",
    "file": "",
}


def configLoad():
    for key in configini.allKeys():
        config_param[key] = configini.value(key)


def configCreate():
    for key, value in config_param.items():
        configini.setValue(key, value)


def init():
    if os.path.exists(f"{USER_CONFIG_INI}"):
        configLoad()
    else:
        configCreate()
