# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!
import Recording
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Dialog(object):
    def __init__(self):
        Dialog = QtWidgets.QDialog()
        self.dlg = Dialog
        self.new_recording = None
        self.setupUi(Dialog)
        Dialog.show()
        if Dialog.exec_():
            Dialog.close()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(413, 253)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 81, 211, 29))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(360, 80, 41, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 120, 191, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(340, 120, 61, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(10, 170, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(220, 170, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 210, 191, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 210, 191, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Screen Recorder"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Click Button To Choose!"))
        self.label.setText(_translate("Dialog", "Screen Recorder"))
        self.label_2.setText(_translate("Dialog", "File Location:"))
        self.pushButton.setText(_translate("Dialog", "..."))
        self.label_3.setText(_translate("Dialog", "File name:"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Enter File Name!"))
        self.comboBox.setItemText(0, _translate("Dialog", ".mp4"))
        self.comboBox.setItemText(1, _translate("Dialog", ".mkv"))
        self.checkBox.setText(_translate("Dialog", "Record Microphone"))
        self.checkBox_2.setText(_translate("Dialog", "Record System Audio"))
        self.pushButton_2.setText(_translate("Dialog", "Start Recording"))
        self.pushButton_3.setText(_translate("Dialog", "Cancel"))

        #Values
        import os
        self.lineEdit.setText(os.path.expanduser(r'~\Desktop'))

        # Connections
        self.pushButton.clicked.connect(self.open_dir)
        self.pushButton_2.clicked.connect(self.start_recording)
        self.pushButton_3.clicked.connect(sys.exit)
        self.checkBox.clicked.connect(self.check)
        self.checkBox_2.clicked.connect(self.check2)


# Dev Defined Functions begin here

    def check(self):
            self.checkBox_2.setChecked(False)
            self.audio = 1

    def check2(self):
            self.checkBox.setChecked(False)
            self.audio = 2

    def open_dir(self):
        import os
        dig = QtWidgets.QFileDialog()
        dig.setFileMode(QtWidgets.QFileDialog.Directory)
        direc = dig.getExistingDirectory(None, "Select Save Directory", os.path.expanduser(r'~\Desktop'))
        if direc != '':
            self.lineEdit.setText(direc)

    def start_recording(self):
        print("teat3")
        self.file_location = str(self.lineEdit.text())
        self.file_name = str(self.lineEdit_2.text()) + str(self.comboBox.currentText())
        print(self.file_name)
        print(self.file_location)
        import os
        if os.path.exists(self.file_location+"/"+self.file_name):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("File Already Exists")
            msg.setWindowTitle("File Already Exists")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            msg.buttonClicked.connect(self.record)
        else:
            print("record")
            self.record()

    def record(self):
        self.dlg.setHidden(True)
        print("new")
        new_recording = Recording.Ui_Dialog(self.file_location, self.file_name, self.audio)

# Dev Defined Functions end here

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()

