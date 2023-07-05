import sys
import platform
import subprocess
import os
import config
import resources_rc

from Ui_main import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt6.QtCore import QTimer, QThread, pyqtSignal
from PyQt6.QtGui import QTextCursor


class BurnTaskThread(QThread):
    uiUpdateSignal = pyqtSignal(str)

    def __init__(self, parent):
        super(BurnTaskThread, self).__init__()
        self.parent = parent
        self.cmd = None
        self.running = False

    def isRunning(self):
        return self.running
    
    def setRunCmd(self, cmd):
        self.cmd = cmd
    
    def run(self):
        if self.running == True:
            return
        
        try:
            self.running = True
            self.uiUpdateSignal.emit("\n------ Star Burn! ------\n")
            p = subprocess.Popen(self.cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            
            while p.poll() is None:
                line = p.stdout.readline()
                p.stdout.flush()
                self.uiUpdateSignal.emit(line)
            self.running = False
        except Exception as e:
            self.running = False
            print(e)



class MyPyQT_Form(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.warningMsgBox = QMessageBox()
        self.warningMsgBox.setIcon(QMessageBox.Icon.Warning)
        self.warningMsgBox.setWindowTitle("Warning")
        self.warningMsgBox.setStandardButtons(QMessageBox.StandardButton.Ok)

        self.fastbootPathPushButton.clicked.connect(self.PathPushButtonCb)
        self.ubootPathPushButton.clicked.connect(self.PathPushButtonCb)
        self.kernelPathPushButton.clicked.connect(self.PathPushButtonCb)
        self.deviceTreePathPushButton.clicked.connect(self.PathPushButtonCb)
        self.rootfsPathPushButton.clicked.connect(self.PathPushButtonCb)

        self.fastbootBurnPushButton.clicked.connect(self.BurnPushButtonCb)
        self.ubootBurnPushButton.clicked.connect(self.BurnPushButtonCb)
        self.kernelBurnPushButton.clicked.connect(self.BurnPushButtonCb)
        self.deviceTreeBurnPushButton.clicked.connect(self.BurnPushButtonCb)
        self.rootfsBurnPushButton.clicked.connect(self.BurnPushButtonCb)

        self.clearLogPushButton.clicked.connect(self.ClearLogPushButtonCb)

        self.burnTaskThread = BurnTaskThread(self)
        self.burnTaskThread.uiUpdateSignal.connect(self.LogPrint)
        self.burnTaskThread.finished.connect(self.BurnTaskThreadFinished)

        self.usbMonitorTimer = QTimer()
        self.usbMonitorTimer.timeout.connect(self.CheckUsbMonitorCb)
        
        
        self.SystemInit()


    def SystemInit(self):
        self.curSystem = platform.system()
        if self.curSystem == "Linux":
            self.uuuTool = "uuu"
        else:
            self.uuuTool = "uuu.exe"

        self.fastbootPathLineEdit.setText(config.config_param["fastboot"])
        self.ubootPathLineEdit.setText(config.config_param["uboot"])
        self.kernelPathLineEdit.setText(config.config_param["kernel"])
        self.deviceTreePathLineEdit.setText(config.config_param["devicetree"])
        self.rootfsPathLineEdit.setText(config.config_param["rootfs"])

        self.CheckUsbMonitorCb()

        self.usbMonitorTimer.start(1000)

    def LogPrint(self, log):
        self.logPlainTextEdit.moveCursor(QTextCursor.MoveOperation.End)
        self.logPlainTextEdit.insertPlainText(log)

    def BurnTaskThreadFinished(self):
        self.LogPrint("\n------ Burn Completed! ------\n")


    def BurnPushButtonCb(self):
        curObjectName = self.sender().objectName()
        
        _target = ""
        _targetPath = ""
        _extendArg = ""
        strWarningText = ""
        if curObjectName == "fastbootBurnPushButton":
            _target = "fastboot"
            _targetPath = self.fastbootPathLineEdit.text()
            if ".imx" not in _targetPath:
                strWarningText = "Please check the fastboot path!"
                _targetPath = ""
        elif curObjectName == "ubootBurnPushButton":
            _target = "uboot"
            _targetPath = self.ubootPathLineEdit.text()
            if ".imx" not in _targetPath:
                strWarningText = "Please check the uboot path!"
                _targetPath = ""
        elif curObjectName == "kernelBurnPushButton":
            _target = "kernel"
            _targetPath = self.kernelPathLineEdit.text()
            _extendArg = os.path.basename(_targetPath)
            if "zImage" not in _targetPath:
                strWarningText = "Please check the kernel path!"
                _targetPath = ""
        elif curObjectName == "deviceTreeBurnPushButton": 
            _target = "devicetree"
            _targetPath = self.deviceTreePathLineEdit.text()
            _extendArg = os.path.basename(_targetPath)
            if ".dtb" not in _targetPath:
                strWarningText = "Please check the devicetree path!"
                _targetPath = ""
        else:
            _target = "rootfs"
            _targetPath = self.rootfsPathLineEdit.text()
            if ".ext4" not in _targetPath:
                strWarningText = "Please check the rootfs path!"
                _targetPath = ""

        
        if _targetPath != "":
            _flashMemory = self.flashMemoryComboBox.currentText()
            _targetBurnPath = _targetPath
            _targetBurn = _target
            _extendCmdArg = _extendArg

            _scriptsPath = os.path.join('scripts', _flashMemory, _targetBurn + '.lst')
            _cmd = self.uuuTool + ' -v -b ' + _scriptsPath + ' ' + _targetBurnPath + ' ' + _extendCmdArg
            self.burnTaskThread.setRunCmd(_cmd)
            self.burnTaskThread.start()
        else:
            self.warningMsgBox.setText(strWarningText)
            self.warningMsgBox.exec()


    def PathPushButtonCb(self):
        curObjectName = self.sender().objectName()
        
        if (curObjectName == "fastbootPathPushButton"):
            _curFirmware = "fastboot"
            _type = "(*.imx)"
            _path = self.fastbootPathLineEdit
        elif (curObjectName == "ubootPathPushButton"):
            _curFirmware = "uboot"
            _type = "imx files(*.imx)"
            _path = self.ubootPathLineEdit
        elif (curObjectName == "kernelPathPushButton"):
            _curFirmware = "kernel"
            _type = "zImage files(zImage)"
            _path = self.kernelPathLineEdit
        elif (curObjectName == "deviceTreePathPushButton"):
            _curFirmware = "devicetree"
            _type = "dtb files(*.dtb)"
            _path = self.deviceTreePathLineEdit
        else:
            _curFirmware = "rootfs"
            _type = "rootfs files(*.ext4)"
            _path = self.rootfsPathLineEdit
        file = QFileDialog.getOpenFileName(self, "Please select the " + _curFirmware + " file", "", _type)
        if file[0] != "":
            _path.setText(file[0])
            config.configini.setValue(_curFirmware, file[0])


    def ClearLogPushButtonCb(self):
        self.logPlainTextEdit.clear()

    def CheckUsbMonitorCb(self):
        p = subprocess.Popen(self.uuuTool + " " + "-lsusb",
                            shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p.wait()

        _status = 0
        device = ''
        lines = p.communicate()[0].decode('utf-8').split('\n')

        for line in lines:
            if 'MX' in line and 'SDP' in line:
                _status = 1
                device = line.split()[1]
                self.chipLineEdit.setText(device)
                self.statusCurLabel.setText("Neew burn fastboot!")
                self.normalGroupBox.setEnabled(False)
            elif 'FB' in line:
                _status = 2
                self.statusCurLabel.setText("Ready!")
                self.normalGroupBox.setEnabled(True)
        
        if _status == 0:
            self.chipLineEdit.setText("")
            self.statusCurLabel.setText("No connect device!")
            self.normalGroupBox.setEnabled(False)
        




if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Initialize or load configuration
    config.init()

    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec())
