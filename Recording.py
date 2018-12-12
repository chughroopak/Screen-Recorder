# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Recording.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!
import signal
import subprocess

import os

import Main
import psutil
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def __init__(self,file_location,file_name,audio):
        Dialog = QtWidgets.QDialog()
        self.dlg = Dialog
        self.setupUi(Dialog)
        self.file_location = file_location
        self.file_name = file_name
        if(audio == 2):
            self.audio = "Stereo Mix (Realtek High Definition Audio)"
        else:
            self.audio = "Microphone (Realtek High Definition Audio)"
        Dialog.show()
        print("test 1")
        self.recording = True
        self.start_recording()
        sys.exit(Dialog.exec_())


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(290, 131)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 50, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 50, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Screen Recorder"))
        self.pushButton.setText(_translate("Dialog", "PAUSE"))
        self.pushButton_2.setText(_translate("Dialog", "STOP"))
        self.label.setText(_translate("Dialog", "RECORDING!"))

        # self.pushButton.clicked.connect(self.pause_resume)
        self.pushButton_2.clicked.connect(self.stop_recording)

    def start_recording(self):
        print("test 2")
        cmd = "ffmpeg -y -f dshow  -i audio=\""+self.audio+"\" -f gdigrab -i desktop -framerate 15 -vcodec h264 \""+self.file_location+"/"+self.file_name+"\""
        print(cmd)
        self.P = subprocess.Popen(cmd)
        self.recording = True
       # self.psProcess = psutil.Process(pid=self.P.pid)

    # def pause_resume(self):
    #     if self.recording == True:
    #         #self.psProcess.suspend()
    #         os.kill(self.P.pid, signal.SIGSTOP)
    #         print("Paused")
    #         self.recording = False
    #     else:
    #         #self.psProcess.resume()
    #         os.kill(P.pid, signal.SIGCONT)
    #         print("Resumed")
    #         self.recording = True

    def stop_recording(self):
        import time
# #        stdout_data = self.P.communicate(input='q')[0]
# #        print("q\n")
        os.kill(self.P.pid, signal.CTRL_C_EVENT)
        time.sleep(1)
        self.dlg.close()
#         # if self.P.poll() is None:  # Force kill if process is still alive
#         #     time.sleep(3)
#         #     os.kill(self.P.pid, signal.SIGTERM)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

