import datetime
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from ucw import *
from edw import *
with open('C:/Program Files/accounts.json') as f:
    data=json.load(f)


class Ui_AccountDetailsWindow(object):
    def __init__(self,num,Ucw,Acw):
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        self.num = num
        self.ucw=Ucw
        self.acw=Acw

    def open_ucw(self):
        self.acw.close()
        self.ucw.show()

    def open_edw(self):
        self.EditDetailsWindow = QtWidgets.QMainWindow()
        self.ui = Ui_EditDetailsWindow(self.num,self.acw,self.EditDetailsWindow)
        self.ui.setupUi(self.EditDetailsWindow)
        self.EditDetailsWindow.show()
        self.acw.close()

    def ref_clicked(self):
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        self.accountdetailsN=data['people'][self.num]
        self.email=self.accountdetailsN['email']
        self.EmailLabel.setText("E-mail Address: "+str(self.email))
        self.add=self.accountdetailsN['address']
        self.AddressLabelData.setText(str(self.add))
        self.phn=self.accountdetailsN['phone']
        self.PhoneLabel.setText("Phone Number: "+str(self.phn))
        self.pin=self.accountdetailsN['PIN']
        self.PinLabel.setText("Pin: "+str(self.pin))
        self.name=self.accountdetailsN['name']
        self.NameLabel.setText("Name: "+str(self.name))
        self.accnum=self.accountdetailsN['acc_number']
        self.AccNumLabel.setText("Account Number: "+str(self.accnum))
        self.bal=self.accountdetailsN['acc_balance']
        self.EnterPinLabel_2.setText("Balance: "+str(self.bal))

    def deleteacc(self):
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        data['people'].pop(self.num)
        with open('C:/Program Files/accounts.json','w') as f:
            json.dump(data,f,indent=2)
        self.acw.close()
        self.ucw.close()    

    def del_confirm(self):
        popup1=QMessageBox()
        popup1.setWindowTitle("Warning")
        popup1.setText("Deleting your account is permanant and all of your data will be lost forever!\nAre you Sure?")
        popup1.setIcon(QMessageBox.Warning)
        popup1.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        popup1.buttonClicked.connect(self.input_confirm)
        x=popup1.exec_()

    def input_confirm(self,i):
        if i.text() == "&Yes":
            popup2=QMessageBox()
            popup2.setWindowTitle("Final Warning")
            popup2.setText("Are you Absolutly Sure?")
            popup2.setIcon(QMessageBox.Warning)
            popup2.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            popup2.buttonClicked.connect(self.input_confirm_final)
            x=popup2.exec_()
       
    def input_confirm_final(self,i):
        if i.text() == "&Yes":
            self.deleteacc()

    def setupUi(self, AccountDetailsWindow):
        AccountDetailsWindow.setObjectName("AccountDetailsWindow")
        AccountDetailsWindow.resize(800, 600)
        AccountDetailsWindow.setMinimumSize(QtCore.QSize(800, 600))
        AccountDetailsWindow.setMaximumSize(QtCore.QSize(800, 600))
        AccountDetailsWindow.setStyleSheet("background-color: rgb(211, 211, 211, 211);")
        
        self.centralwidget = QtWidgets.QWidget(AccountDetailsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BankName = QtWidgets.QLabel(self.centralwidget)
        self.BankName.setGeometry(QtCore.QRect(0, 0, 801, 91))
        font = QtGui.QFont()
        font.setFamily("Chopsic")
        font.setPointSize(30)
        self.BankName.setFont(font)
        self.BankName.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.BankName.setObjectName("BankName")
        
        self.AccountDetailsLabel = QtWidgets.QLabel(self.centralwidget)
        self.AccountDetailsLabel.setGeometry(QtCore.QRect(250, 100, 331, 71))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(20)
        self.AccountDetailsLabel.setFont(font)
        self.AccountDetailsLabel.setObjectName("AccountDetailsLabel")
        
        self.EmailLabel = QtWidgets.QLabel(self.centralwidget)
        self.EmailLabel.setGeometry(QtCore.QRect(10, 370, 771, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.EmailLabel.setFont(font)
        self.EmailLabel.setObjectName("EmailLabel")
        
        self.AddLabel = QtWidgets.QLabel(self.centralwidget)
        self.AddLabel.setGeometry(QtCore.QRect(10, 420, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.AddLabel.setFont(font)
        self.AddLabel.setObjectName("AddLabel")
        
        self.PhoneLabel = QtWidgets.QLabel(self.centralwidget)
        self.PhoneLabel.setGeometry(QtCore.QRect(10, 210, 771, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.PhoneLabel.setFont(font)
        self.PhoneLabel.setObjectName("PhoneLabel")
        
        self.PinLabel = QtWidgets.QLabel(self.centralwidget)
        self.PinLabel.setGeometry(QtCore.QRect(10, 290, 771, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.PinLabel.setFont(font)
        self.PinLabel.setObjectName("PinLabel")
        
        self.NameLabel = QtWidgets.QLabel(self.centralwidget)
        self.NameLabel.setGeometry(QtCore.QRect(10, 170, 771, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.NameLabel.setFont(font)
        self.NameLabel.setObjectName("NameLabel")
        
        self.AccNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.AccNumLabel.setGeometry(QtCore.QRect(10, 250, 761, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.AccNumLabel.setFont(font)
        self.AccNumLabel.setObjectName("AccNumLabel")
        
        self.EnterPinLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.EnterPinLabel_2.setGeometry(QtCore.QRect(10, 330, 771, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.EnterPinLabel_2.setFont(font)
        self.EnterPinLabel_2.setObjectName("EnterPinLabel_2")
        
        self.AddressLabelData = QtWidgets.QLabel(self.centralwidget)
        self.AddressLabelData.setGeometry(QtCore.QRect(120, 430, 671, 71))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(15)
        self.AddressLabelData.setFont(font)
        self.AddressLabelData.setText("")
        self.AddressLabelData.setObjectName("AddressLabelData")
        
        self.EditDetailsBtn = QtWidgets.QPushButton(self.centralwidget)
        self.EditDetailsBtn.setGeometry(QtCore.QRect(20, 520, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(12)
        self.EditDetailsBtn.setFont(font)
        self.EditDetailsBtn.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.EditDetailsBtn.setObjectName("EditDetailsBtn")
        self.EditDetailsBtn.clicked.connect(self.open_edw)

        self.RefreshBtn = QtWidgets.QPushButton(self.centralwidget)
        self.RefreshBtn.setGeometry(QtCore.QRect(10, 110, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(12)
        self.RefreshBtn.setFont(font)
        self.RefreshBtn.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.RefreshBtn.setObjectName("RefreshBtn")
        self.RefreshBtn.clicked.connect(self.ref_clicked)
        
        self.GoBackBtn = QtWidgets.QPushButton(self.centralwidget)
        self.GoBackBtn.setGeometry(QtCore.QRect(620, 520, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(12)
        self.GoBackBtn.setFont(font)
        self.GoBackBtn.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.GoBackBtn.setObjectName("GoBackBtn")
        self.GoBackBtn.clicked.connect(self.open_ucw)
        
        self.DeleteAccountBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteAccountBtn.setGeometry(QtCore.QRect(290, 520, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(12)
        self.DeleteAccountBtn.setFont(font)
        self.DeleteAccountBtn.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"")
        self.DeleteAccountBtn.setObjectName("DeleteAccountBtn")
        self.DeleteAccountBtn.clicked.connect(self.del_confirm)

        AccountDetailsWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(AccountDetailsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        AccountDetailsWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(AccountDetailsWindow)
        self.statusbar.setObjectName("statusbar")
        AccountDetailsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AccountDetailsWindow)
        QtCore.QMetaObject.connectSlotsByName(AccountDetailsWindow)

    def retranslateUi(self, AccountDetailsWindow):
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        self.accountdetails=data['people'][self.num]
        _translate = QtCore.QCoreApplication.translate
        AccountDetailsWindow.setWindowTitle(_translate("AccountDetailsWindow", "Welcome to Avixion Bank Of Fraud"))
        self.BankName.setText(_translate("AccountDetailsWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#ffffff;\">AVIXION BANK OF FRAUD</span></p></body></html>"))
        self.AccountDetailsLabel.setText(_translate("AccountDetailsWindow", "Account Details"))
        self.AddLabel.setText(_translate("AccountDetailsWindow", "Address:"))
        self.email=self.accountdetails['email']
        self.EmailLabel.setText("E-mail Address: "+str(self.email))
        self.add=self.accountdetails['address']
        self.AddressLabelData.setText(str(self.add))
        self.phn=self.accountdetails['phone']
        self.PhoneLabel.setText("Phone Number: "+str(self.phn))
        self.pin=self.accountdetails['PIN']
        self.PinLabel.setText("Pin: "+str(self.pin))
        self.name=self.accountdetails['name']
        self.NameLabel.setText("Name: "+str(self.name))
        self.accnum=self.accountdetails['acc_number']
        self.AccNumLabel.setText("Account Number: "+str(self.accnum))
        self.bal=self.accountdetails['acc_balance']
        self.EnterPinLabel_2.setText("Balance: "+str(self.bal))
        self.RefreshBtn.setText(_translate("AccountDetailsWindow", "Refresh"))
        self.EditDetailsBtn.setText(_translate("AccountDetailsWindow", "Edit Details"))
        self.GoBackBtn.setText(_translate("AccountDetailsWindow", "Go Back"))
        self.DeleteAccountBtn.setText(_translate("AccountDetailsWindow", "Delete Account"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     AccountDetailsWindow = QtWidgets.QMainWindow()
#     ui = Ui_AccountDetailsWindow()
#     ui.setupUi(AccountDetailsWindow)
#     AccountDetailsWindow.show()
#     sys.exit(app.exec_())
