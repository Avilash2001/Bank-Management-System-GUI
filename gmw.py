import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets  import QMessageBox
from gpcw import *
from gtdw import *
import ucw
with open('C:/Program Files/accounts.json') as f:
    data=json.load(f)

class Ui_GodModeWindow1(object):
    def __init__(self,LoginWindow,Gpcw,Gmw,Gc):
        self.gpcw=Gpcw
        self.Log=LoginWindow 
        self.gmw=Gmw 
        self.gc=Gc

    def open_log(self):
        god_checker=0
        self.Log.show()
        self.gmw.close()

    def open_gtdw(self):
        if self.NameLabel.text() == "Name:":
            self.remind_popup()
        else:
            self.GodTransactionDataWindow = QtWidgets.QMainWindow()
            self.ui = Ui_GodTransactionDataWindow(self.index,self.gmw,self.GodTransactionDataWindow)
            self.ui.setupUi(self.GodTransactionDataWindow)
            self.GodTransactionDataWindow.show()

    def open_ucw(self):
        if self.NameLabel.text() == "Name:":
            self.remind_popup()
        else:
            self.UserChoiceWindow = QtWidgets.QMainWindow()
            self.ui = ucw.Ui_UserChoiceWindow(self.index,self.gmw,self.UserChoiceWindow,self.gc)
            self.ui.setupUi(self.UserChoiceWindow)
            self.UserChoiceWindow.show()
            self.gmw.close() 

    def greet_popup(self,i):
        with open('C:/Program Files/accounts.json') as f:
           data=json.load(f)
        self.AccountSelector.clear()
        for i in data['people']:
           self.name_entry=i['name']
           self.AccountSelector.addItem(self.name_entry)
        
    def remind_popup(self):   
        popup3=QMessageBox()
        popup3.setWindowTitle("Warning")
        popup3.setText("Click the Get Data Button")
        popup3.setIcon(QMessageBox.Warning)
        popup3.setStandardButtons(QMessageBox.Ok)
        x=popup3.exec_() 

    def get_data_clicked(self):
        with open('C:/Program Files/accounts.json') as f:
             data=json.load(f)
        self.index=int(self.AccountSelector.currentIndex())
        self.accountdetailsN=data['people'][self.index]
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
        if self.NameLabel.text() == "Name:":
            self.remind_popup()
        else:
            with open('C:/Program Files/accounts.json') as f:
                data=json.load(f)
            data['people'].pop(self.index)
            with open('C:/Program Files/accounts.json','w') as f:
                json.dump(data,f,indent=2)    
            with open('C:/Program Files/accounts.json') as f:
                data=json.load(f)
            self.AccountSelector.clear()
            for i in data['people']:
                self.name_entry=i['name']
                self.AccountSelector.addItem(self.name_entry)

    def del_confirm(self):
        if self.NameLabel.text() == "Name:":
            self.remind_popup()
        else:
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

    def setupUi(self, GodModeWindow1):
        GodModeWindow1.setObjectName("GodModeWindow1")
        GodModeWindow1.resize(1024, 768)
        GodModeWindow1.setMinimumSize(QtCore.QSize(1024, 768))
        GodModeWindow1.setMaximumSize(QtCore.QSize(1024, 768))
        GodModeWindow1.setStyleSheet("background-color: rgb(211, 211, 211);\n"
"")
        self.centralwidget = QtWidgets.QWidget(GodModeWindow1)
        self.centralwidget.setObjectName("centralwidget")
        
        self.BankName = QtWidgets.QLabel(self.centralwidget)
        self.BankName.setGeometry(QtCore.QRect(0, 0, 1021, 91))
        font = QtGui.QFont()
        font.setFamily("Chopsic")
        font.setPointSize(30)
        self.BankName.setFont(font)
        self.BankName.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.BankName.setObjectName("BankName")
        
        self.GetDataBtn = QtWidgets.QPushButton(self.centralwidget)
        self.GetDataBtn.setGeometry(QtCore.QRect(861, 130, 162, 41))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.GetDataBtn.setFont(font)
        self.GetDataBtn.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.GetDataBtn.setObjectName("GetDataBtn")
        self.GetDataBtn.clicked.connect(self.get_data_clicked)

        self.AccountSelector = QtWidgets.QComboBox(self.centralwidget)
        self.AccountSelector.setGeometry(QtCore.QRect(290, 130, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.AccountSelector.setFont(font)
        for i in data['people']:
                self.name_entry=i['name']
                self.AccountSelector.addItem(self.name_entry)
        self.AccountSelector.setObjectName("AccountSelector")
        
        self.SelectAccountLabel = QtWidgets.QLabel(self.centralwidget)
        self.SelectAccountLabel.setGeometry(QtCore.QRect(20, 120, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(15)
        self.SelectAccountLabel.setFont(font)
        self.SelectAccountLabel.setObjectName("SelectAccountLabel")
        
        self.EnterPinLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.EnterPinLabel_2.setGeometry(QtCore.QRect(10, 360, 981, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.EnterPinLabel_2.setFont(font)
        self.EnterPinLabel_2.setObjectName("EnterPinLabel_2")
        
        self.AccNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.AccNumLabel.setGeometry(QtCore.QRect(10, 280, 971, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.AccNumLabel.setFont(font)
        self.AccNumLabel.setObjectName("AccNumLabel")
        
        self.PinLabel = QtWidgets.QLabel(self.centralwidget)
        self.PinLabel.setGeometry(QtCore.QRect(10, 320, 971, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.PinLabel.setFont(font)
        self.PinLabel.setObjectName("PinLabel")
        
        self.EmailLabel = QtWidgets.QLabel(self.centralwidget)
        self.EmailLabel.setGeometry(QtCore.QRect(10, 400, 961, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.EmailLabel.setFont(font)
        self.EmailLabel.setObjectName("EmailLabel")
        
        self.NameLabel = QtWidgets.QLabel(self.centralwidget)
        self.NameLabel.setGeometry(QtCore.QRect(10, 200, 991, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.NameLabel.setFont(font)
        self.NameLabel.setObjectName("NameLabel")
        
        self.PhoneLabel = QtWidgets.QLabel(self.centralwidget)
        self.PhoneLabel.setGeometry(QtCore.QRect(10, 240, 981, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.PhoneLabel.setFont(font)
        self.PhoneLabel.setObjectName("PhoneLabel")
        
        self.AddLabel = QtWidgets.QLabel(self.centralwidget)
        self.AddLabel.setGeometry(QtCore.QRect(10, 450, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.AddLabel.setFont(font)
        self.AddLabel.setObjectName("AddLabel")
        
        self.AddressLabelData = QtWidgets.QLabel(self.centralwidget)
        self.AddressLabelData.setGeometry(QtCore.QRect(120, 470, 851, 101))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.AddressLabelData.setFont(font)
        self.AddressLabelData.setText("")
        self.AddressLabelData.setObjectName("AddressLabelData")
        
        self.TransactionBtn = QtWidgets.QPushButton(self.centralwidget)
        self.TransactionBtn.setGeometry(QtCore.QRect(30, 600, 271, 101))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.TransactionBtn.setFont(font)
        self.TransactionBtn.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.TransactionBtn.setObjectName("TransactionBtn")
        self.TransactionBtn.clicked.connect(self.open_gtdw)
        
        self.DeleteAccBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteAccBtn.setGeometry(QtCore.QRect(320, 600, 271, 101))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.DeleteAccBtn.setFont(font)
        self.DeleteAccBtn.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.DeleteAccBtn.setObjectName("DeleteAccBtn")
        self.DeleteAccBtn.clicked.connect(self.del_confirm)
        
        self.AccessAccBtn = QtWidgets.QPushButton(self.centralwidget)
        self.AccessAccBtn.setGeometry(QtCore.QRect(610, 600, 271, 101))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.AccessAccBtn.setFont(font)
        self.AccessAccBtn.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.AccessAccBtn.setObjectName("AccessAccBtn")
        self.AccessAccBtn.clicked.connect(self.open_ucw)
        
        self.GoBackBtn = QtWidgets.QPushButton(self.centralwidget)
        self.GoBackBtn.setGeometry(QtCore.QRect(900, 600, 121, 101))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.GoBackBtn.setFont(font)
        self.GoBackBtn.setStyleSheet("background-color: rgb(255, 75, 51);")
        self.GoBackBtn.setObjectName("GoBackBtn")
        self.GoBackBtn.clicked.connect(self.open_log)
        
        GodModeWindow1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GodModeWindow1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 26))
        self.menubar.setObjectName("menubar")
        GodModeWindow1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GodModeWindow1)
        self.statusbar.setObjectName("statusbar")
        GodModeWindow1.setStatusBar(self.statusbar)

        self.retranslateUi(GodModeWindow1)
        QtCore.QMetaObject.connectSlotsByName(GodModeWindow1)

        popup=QMessageBox()
        popup.setWindowTitle("Welcome Almighty")
        popup.setText("You have entered God Mode!")
        popup.setIcon(QMessageBox.Information)
        popup.setStandardButtons(QMessageBox.Ok)
        popup.buttonClicked.connect(self.greet_popup)
        x=popup.exec_()

    def retranslateUi(self, GodModeWindow1):
        _translate = QtCore.QCoreApplication.translate
        GodModeWindow1.setWindowTitle(_translate("GodModeWindow1", "Welcome Almighty!!"))
        self.BankName.setText(_translate("GodModeWindow1", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#ffffff;\">WELCOME aLMIGHTY!!</span></p></body></html>"))
        self.SelectAccountLabel.setText(_translate("GodModeWindow1", "Select Account:"))
        self.EnterPinLabel_2.setText(_translate("GodModeWindow1", "Balance:"))
        self.AccNumLabel.setText(_translate("GodModeWindow1", "Account Number:"))
        self.PinLabel.setText(_translate("GodModeWindow1", "PIN:"))
        self.EmailLabel.setText(_translate("GodModeWindow1", "E-mail Address:"))
        self.NameLabel.setText(_translate("GodModeWindow1", "Name:"))
        self.PhoneLabel.setText(_translate("GodModeWindow1", "Phone Number:"))
        self.AddLabel.setText(_translate("GodModeWindow1", "Address:"))
        self.GetDataBtn.setText(_translate("GodModeWindow1", "Get Data"))
        self.TransactionBtn.setText(_translate("GodModeWindow1", "See and Edit\n"
"Transaction Data"))
        self.DeleteAccBtn.setText(_translate("GodModeWindow1", "Delete\n"
"Account"))
        self.AccessAccBtn.setText(_translate("GodModeWindow1", "Access\n"
"Account"))
        self.GoBackBtn.setText(_translate("GodModeWindow1", "Go\n"
"Back"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     GodModeWindow1 = QtWidgets.QMainWindow()
#     ui = Ui_GodModeWindow1()
#     ui.setupUi(GodModeWindow1)
#     GodModeWindow1.show()
#     sys.exit(app.exec_())
