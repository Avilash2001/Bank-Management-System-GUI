import datetime
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from ucw import *
from tw2 import *
with open('C:/Program Files/accounts.json') as f:
    data=json.load(f)

class Ui_TransferWindow1(object):
    def __init__(self,num,Ucw,Tw1,Gc):
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        self.num = num
        self.ucw=Ucw
        self.tw1=Tw1
        self.gc=Gc

    def open_ucw(self):
        self.tw1.close()
        self.ucw.show()

    def error_popup(self,code):
        popup2=QMessageBox()
        popup2.setWindowTitle("Error!")
        if code==2:
            popup2.setText("Invalid Account Number")
        elif code==3:
            popup2.setText("Field should contain only digits")
        elif code==4:
            popup2.setText("Field should not be empty")
        popup2.setIcon(QMessageBox.Critical)
        popup2.setStandardButtons(QMessageBox.Retry)
        x=popup2.exec_()

    def open_tw2(self):
        self.TransferWindow2 = QtWidgets.QMainWindow()
        self.ui = Ui_TransferWindow2(self.num,self.newnum,self.ucw, self.tw1,self.TransferWindow2,self.gc)
        self.ui.setupUi(self.TransferWindow2)
        self.TransferWindow2.show()
        self.tw1.close()

    def Ok_click(self):
        if self.TransAccNumInput.text() == "":
            self.error_popup(4)
        elif self.TransAccNumInput.text().isdigit():
            with open('C:/Program Files/accounts.json') as f:
                data=json.load(f)
            for i in range(len(data['people'])):
                if int(self.TransAccNumInput.text()) == data['people'][i]['acc_number']:
                    self.newnum=i
                    break
            if int(self.TransAccNumInput.text())==data['people'][self.newnum]['acc_number'] and self.num != self.newnum:
                self.TransAccNumInput.setEnabled(False)
                self.newname=data['people'][self.newnum]['name']
                self.ConfirmLabel.setText("Do you want to transfer to "+self.newname+"?")
                self.ConfirmLabel.setGeometry(QtCore.QRect(0, 390, 801, 91))
                self.YesBtn.setGeometry(QtCore.QRect(180, 470, 171, 61))
                self.No.setGeometry(QtCore.QRect(420, 470, 171, 61))
            else:
                self.error_popup(2)
        else:
            self.error_popup(3)

    def No_click(self):
        self.TransAccNumInput.setEnabled(True)
        self.ConfirmLabel.setGeometry(QtCore.QRect(0, 600, 801, 91))
        self.YesBtn.setGeometry(QtCore.QRect(180, 600, 171, 61))
        self.No.setGeometry(QtCore.QRect(420, 600, 171, 61))

    def setupUi(self, TransferWindow1):
        TransferWindow1.setObjectName("TransferWindow1")
        TransferWindow1.resize(800, 600)
        TransferWindow1.setMinimumSize(QtCore.QSize(800, 600))
        TransferWindow1.setMaximumSize(QtCore.QSize(800, 600))
        TransferWindow1.setStyleSheet("background-color: rgb(211, 211, 211, 211);")
        
        self.centralwidget = QtWidgets.QWidget(TransferWindow1)
        self.centralwidget.setObjectName("centralwidget")
        
        self.BankName = QtWidgets.QLabel(self.centralwidget)
        self.BankName.setGeometry(QtCore.QRect(0, 0, 801, 91))
        font = QtGui.QFont()
        font.setFamily("Chopsic")
        font.setPointSize(30)
        self.BankName.setFont(font)
        self.BankName.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.BankName.setObjectName("BankName")
        
        self.TransAccNumLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.TransAccNumLabel1.setGeometry(QtCore.QRect(0, 90, 791, 91))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.TransAccNumLabel1.setFont(font)
        self.TransAccNumLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.TransAccNumLabel1.setObjectName("TransAccNumLabel1")
        
        self.TransAccNumInput = QtWidgets.QLineEdit(self.centralwidget)
        self.TransAccNumInput.setGeometry(QtCore.QRect(120, 260, 551, 41))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.TransAccNumInput.setFont(font)
        self.TransAccNumInput.setAlignment(QtCore.Qt.AlignCenter)
        self.TransAccNumInput.setObjectName("TransAccNumInput")
        
        self.OkBtn = QtWidgets.QPushButton(self.centralwidget)
        self.OkBtn.setGeometry(QtCore.QRect(190, 320, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.OkBtn.setFont(font)
        self.OkBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.OkBtn.setDefault(True)
        self.OkBtn.setFlat(False)
        self.OkBtn.setObjectName("OkBtn")
        self.OkBtn.clicked.connect(self.Ok_click) 
        
        self.TransAccNumLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.TransAccNumLabel2.setGeometry(QtCore.QRect(10, 160, 791, 91))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.TransAccNumLabel2.setFont(font)
        self.TransAccNumLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.TransAccNumLabel2.setObjectName("TransAccNumLabel2")
        
        self.CancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.CancelBtn.setGeometry(QtCore.QRect(410, 320, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.CancelBtn.setFont(font)
        self.CancelBtn.setStyleSheet("background-color: rgb(255, 75, 51);")
        self.CancelBtn.setDefault(True)
        self.CancelBtn.setFlat(False)
        self.CancelBtn.setObjectName("CancelBtn")
        self.CancelBtn.clicked.connect(self.open_ucw)
        
        self.ConfirmLabel = QtWidgets.QLabel(self.centralwidget)
        # self.ConfirmLabel.setGeometry(QtCore.QRect(0, 390, 801, 91))
        self.ConfirmLabel.setGeometry(QtCore.QRect(0, 600, 801, 91))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.ConfirmLabel.setFont(font)
        self.ConfirmLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ConfirmLabel.setObjectName("ConfirmLabel")
        
        self.YesBtn = QtWidgets.QPushButton(self.centralwidget)
        # self.YesBtn.setGeometry(QtCore.QRect(180, 470, 171, 61))
        self.YesBtn.setGeometry(QtCore.QRect(180, 600, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.YesBtn.setFont(font)
        self.YesBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.YesBtn.setDefault(True)
        self.YesBtn.setFlat(False)
        self.YesBtn.setObjectName("YesBtn")
        self.YesBtn.clicked.connect(self.open_tw2)
        
        self.No = QtWidgets.QPushButton(self.centralwidget)
        # self.No.setGeometry(QtCore.QRect(420, 470, 171, 61))
        self.No.setGeometry(QtCore.QRect(420, 600, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.No.setFont(font)
        self.No.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.No.setDefault(True)
        self.No.setFlat(False)
        self.No.setObjectName("No")
        self.No.clicked.connect(self.No_click)
        
        TransferWindow1.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(TransferWindow1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        TransferWindow1.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(TransferWindow1)
        self.statusbar.setObjectName("statusbar")
        TransferWindow1.setStatusBar(self.statusbar)

        self.retranslateUi(TransferWindow1)
        QtCore.QMetaObject.connectSlotsByName(TransferWindow1)

        self.newnum=0

    def retranslateUi(self, TransferWindow1):
        _translate = QtCore.QCoreApplication.translate
        TransferWindow1.setWindowTitle(_translate("TransferWindow1", "Welcome to Avixion Bank Of Fraud"))
        self.BankName.setText(_translate("TransferWindow1", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#ffffff;\">AVIXION BANK OF FRAUD</span></p></body></html>"))
        self.TransAccNumLabel1.setText(_translate("TransferWindow1", "ENTER ACCOUNT NUMBER OF THE PERSON"))
        self.OkBtn.setText(_translate("TransferWindow1", "OK"))
        self.TransAccNumLabel2.setText(_translate("TransferWindow1", "YOU WANT TO TRANSFER FUNDS:"))
        self.CancelBtn.setText(_translate("TransferWindow1", "Cancel"))
        self.ConfirmLabel.setText(_translate("TransferWindow1", "Do you want to transfer to XYZ?"))
        self.YesBtn.setText(_translate("TransferWindow1", "Yes"))
        self.No.setText(_translate("TransferWindow1", "No"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     TransferWindow1 = QtWidgets.QMainWindow()
#     ui = Ui_TransferWindow1()
#     ui.setupUi(TransferWindow1)
#     TransferWindow1.show()
#     sys.exit(app.exec_())
