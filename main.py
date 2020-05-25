import os
from elevate import elevate
import datetime
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets  import QMessageBox
from ucw import *
from suw import *
from gpcw import *
with open('C:/Program Files/accounts.json') as f:
    data=json.load(f)

LoginWindow = None
Gc=0

class Ui_LoginWindow(object):
    
    def open_ucw(self):
        self.UserChoiceWindow = QtWidgets.QMainWindow()
        self.ui = Ui_UserChoiceWindow(self.num,LoginWindow,self.UserChoiceWindow,self.gc)
        self.ui.setupUi(self.UserChoiceWindow)
        self.UserChoiceWindow.show()
        LoginWindow.close()

    def open_suw(self):
        self.SignUpWindow = QtWidgets.QMainWindow()
        self.ui = Ui_SignUpWindow(self.num,LoginWindow,self.SignUpWindow)
        self.ui.setupUi(self.SignUpWindow)
        self.SignUpWindow.show()
        LoginWindow.close()

    def open_gpcw(self):
        self.GodPassCheckerWindow = QtWidgets.QMainWindow()
        self.ui = Ui_GodPassCheckerWindow(LoginWindow,self.GodPassCheckerWindow,self.gc)
        self.ui.setupUi(self.GodPassCheckerWindow)
        self.GodPassCheckerWindow.show()
        LoginWindow.close()

    def god_entry(self):
        print(self.gc)
        if self.gc == 10:
            self.open_gpcw()
            self.gc=0
        else:
            self.gc+=1
    
    def setupUi(self, LoginWindow):
        self.gc=Gc
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.setEnabled(True)
        LoginWindow.resize(800, 600)
        LoginWindow.setMinimumSize(QtCore.QSize(800, 600))
        LoginWindow.setMaximumSize(QtCore.QSize(800, 600))
        LoginWindow.setStyleSheet("background-color: rgb(211, 211, 211);")
        LoginWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        
        
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.LoginLabel = QtWidgets.QLabel(self.centralwidget)
        self.LoginLabel.setGeometry(QtCore.QRect(110, 110, 591, 71))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.LoginLabel.setFont(font)
        self.LoginLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LoginLabel.setObjectName("LoginLabel")
        
        self.LoginBtn = QtWidgets.QPushButton(self.centralwidget)
        # self.LoginBtn.setGeometry(QtCore.QRect(200, 400, 181, 41))
        self.LoginBtn.setGeometry(QtCore.QRect(200, 600, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.LoginBtn.setFont(font)
        self.LoginBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LoginBtn.setDefault(True)
        self.LoginBtn.setFlat(False)
        self.LoginBtn.setObjectName("LoginBtn")
        self.LoginBtn.clicked.connect(self.LoginBtn_click)

        self.CancelBtn = QtWidgets.QPushButton(self.centralwidget)
        # self.CancelBtn.setGeometry(QtCore.QRect(420, 400, 181, 41))
        self.CancelBtn.setGeometry(QtCore.QRect(420, 600, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.CancelBtn.setFont(font)
        self.CancelBtn.setStyleSheet("background-color: rgb(255, 75, 51);")
        self.CancelBtn.setDefault(True)
        self.CancelBtn.setFlat(False)
        self.CancelBtn.setObjectName("LoginBtn")
        self.CancelBtn.clicked.connect(self.CancelBtn_click)
        
        self.NewUserLabel = QtWidgets.QLabel(self.centralwidget)
        self.NewUserLabel.setGeometry(QtCore.QRect(10, 500, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Sweet Sensations Personal Use")
        font.setPointSize(16)
        self.NewUserLabel.setFont(font)
        self.NewUserLabel.setObjectName("NewUserLabel")
        
        self.SignUpBtn = QtWidgets.QPushButton(self.centralwidget)
        self.SignUpBtn.setGeometry(QtCore.QRect(150, 500, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(18)
        font.setItalic(True)
        font.setUnderline(True)
        self.SignUpBtn.setFont(font)
        self.SignUpBtn.setFlat(True)
        self.SignUpBtn.setObjectName("SignUpBtn")
        self.SignUpBtn.clicked.connect(self.open_suw)
        
        self.BankNameG = QtWidgets.QPushButton(self.centralwidget)
        self.BankNameG.setGeometry(QtCore.QRect(0, 0, 801, 91))
        font = QtGui.QFont()
        font.setFamily("Chopsic")
        font.setPointSize(28)
        self.BankNameG.setFont(font)
        self.BankNameG.setStyleSheet("background-color: rgb(52, 52, 52);\n""color: rgb(255, 255, 255);")
        self.BankNameG.setFlat(False)
        self.BankNameG.setObjectName("BankNameG")
        self.BankNameG.clicked.connect(self.god_entry)
        
        self.AccountNumInput = QtWidgets.QLineEdit(self.centralwidget)
        self.AccountNumInput.setGeometry(QtCore.QRect(160, 180, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.AccountNumInput.setFont(font)
        self.AccountNumInput.setAlignment(QtCore.Qt.AlignCenter)
        self.AccountNumInput.setObjectName("AccountNumInput")
        
        self.LoginLabel_2 = QtWidgets.QLabel(self.centralwidget)
        # self.LoginLabel_2.setGeometry(QtCore.QRect(100, 270, 591, 61))
        self.LoginLabel_2.setGeometry(QtCore.QRect(100, 600, 591, 61))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.LoginLabel_2.setFont(font)
        self.LoginLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.LoginLabel_2.setObjectName("LoginLabel_2")
        
        self.AccountNumInput_2 = QtWidgets.QLineEdit(self.centralwidget)
        # self.AccountNumInput_2.setGeometry(QtCore.QRect(160, 340, 471, 41))
        self.AccountNumInput_2.setGeometry(QtCore.QRect(160, 600, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.AccountNumInput_2.setFont(font)
        self.AccountNumInput_2.setAlignment(QtCore.Qt.AlignCenter)
        self.AccountNumInput_2.setObjectName("AccountNumInput_2")
        
        self.ChangingLabel = QtWidgets.QLabel(self.centralwidget)
        # self.ChangingLabel.setGeometry(QtCore.QRect(20, 440, 281, 61))
        self.ChangingLabel.setGeometry(QtCore.QRect(20, 600, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(14)
        self.ChangingLabel.setFont(font)
        self.ChangingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ChangingLabel.setObjectName("ChangingLabel")
        
        self.EntryBar = QtWidgets.QProgressBar(self.centralwidget)
        # self.EntryBar.setGeometry(QtCore.QRect(310, 460, 471, 31))
        self.EntryBar.setGeometry(QtCore.QRect(310, 600, 471, 31))
        self.EntryBar.setProperty("value", 24)
        self.EntryBar.setObjectName("EntryBar")
        
        self.NextBtn = QtWidgets.QPushButton(self.centralwidget)
        self.NextBtn.setGeometry(QtCore.QRect(300, 230, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.NextBtn.setFont(font)
        self.NextBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NextBtn.setDefault(True)
        self.NextBtn.setFlat(False)
        self.NextBtn.setObjectName("NextBtn")
        self.NextBtn.clicked.connect(self.NextBtn_click)
        
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)
        self.num=0
        self.accountdetails=data['people'][self.num]


    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Welcome to Avixion Bank Of Fraud"))
        self.LoginLabel.setText(_translate("LoginWindow", "ENTER ACCOUNT NUMBER:"))
        self.LoginBtn.setText(_translate("LoginWindow", "LOGIN"))
        self.CancelBtn.setText(_translate("LoginWindow", "CANCEL"))
        self.NewUserLabel.setText(_translate("LoginWindow", "NEW USER? "))
        self.SignUpBtn.setText(_translate("LoginWindow", "SIGN UP"))
        self.BankNameG.setText(_translate("LoginWindow", "AVIXION BANK OF FRAUD"))
        self.LoginLabel_2.setText(_translate("LoginWindow", "ENTER PIN TO LOGIN:"))
        self.ChangingLabel.setText(_translate("LoginWindow", "Acessing Account..."))
        self.NextBtn.setText(_translate("LoginWindow", "NEXT"))

    def acc_num_wrong_popup(self):
        popup1=QMessageBox()
        popup1.setWindowTitle("Error!")
        popup1.setText("Invaid / Wrong Account Number")
        popup1.setIcon(QMessageBox.Critical)
        popup1.setStandardButtons(QMessageBox.Retry)
        x=popup1.exec_()

    def pin_invalid_popup(self):
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        self.time=datetime.datetime.now()
        self.prevlog=data['people'][self.num]['log']
        self.curlog=self.prevlog+"\nFailed Login Attempt on "+self.time.strftime("%d-%m-%Y")+" at "+self.time.strftime("%H-%M-%S")
        data['people'][self.num]['log']=self.curlog
        with open('C:/Program Files/accounts.json','w') as f:
            json.dump(data,f,indent=2)
        popup2=QMessageBox()
        popup2.setWindowTitle("Error!")
        popup2.setText("Invaid PIN")
        popup2.setIcon(QMessageBox.Critical)
        popup2.setStandardButtons(QMessageBox.Retry)
        popup2.setInformativeText("PIN should contain 4 digits!")
        x=popup2.exec_()

    def pin_wrong_popup(self):
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        self.time=datetime.datetime.now()
        self.prevlog=data['people'][self.num]['log']
        self.curlog=self.prevlog+"\nFailed Login Attempt on "+self.time.strftime("%d-%m-%Y")+" at "+self.time.strftime("%H-%M-%S")
        data['people'][self.num]['log']=self.curlog
        with open('C:/Program Files/accounts.json','w') as f:
            json.dump(data,f,indent=2)
        popup3=QMessageBox()
        popup3.setWindowTitle("Error!")
        popup3.setText("Wrong PIN")
        popup3.setIcon(QMessageBox.Critical)
        popup3.setStandardButtons(QMessageBox.Retry)
        x=popup3.exec_()

    

    def NextBtn_click(self):
        self.gc=0
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        if self.AccountNumInput.text() != "" and self.AccountNumInput.text().isdigit() :
            for i in range(len(data['people'])):
                if int(self.AccountNumInput.text()) == data['people'][i]['acc_number']:
                    self.num=i
                    break
            if int(self.AccountNumInput.text())==data['people'][self.num]['acc_number']:
                self.AccountNumInput.setEnabled(False)
                name=data['people'][self.num]['name']
                self.LoginLabel_2.setText(name+" Enter PIN")    
                self.LoginLabel_2.setGeometry(QtCore.QRect(100, 270, 591, 61))
                self.AccountNumInput_2.setGeometry(QtCore.QRect(160, 340, 471, 41))
                self.LoginBtn.setGeometry(QtCore.QRect(200, 400, 181, 41))
                self.CancelBtn.setGeometry(QtCore.QRect(420, 400, 181, 41))
                self.accountdetails=data['people'][self.num]
            else:
                self.acc_num_wrong_popup()
        else:
            self.acc_num_wrong_popup()
            
    def LoginBtn_click(self):
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        if self.AccountNumInput_2.text()!="" and self.AccountNumInput_2.text().isdigit()and int(self.AccountNumInput_2.text())>999 and int(self.AccountNumInput_2.text())<10000:
            self.pin=int(self.AccountNumInput_2.text())
            if  self.pin== data['people'][self.num]['PIN']:
                self.ChangingLabel.setGeometry(QtCore.QRect(20, 440, 281, 61))
                self.EntryBar.setGeometry(QtCore.QRect(310, 460, 471, 31))
                
                self.step=0
                while self.step<=101:
                    self.EntryBar.setValue(self.step)
                    if self.step<=50:
                        self.ChangingLabel.setText("Accessing Account...")
                    else:
                        self.ChangingLabel.setText("Entering Account...")
                    self.step+=0.01
                with open('C:/Program Files/accounts.json') as f:
                    data=json.load(f)
                self.time=datetime.datetime.now()
                self.prevlog=data['people'][self.num]['log']
                self.curlog=self.prevlog+"\nLogged in on "+self.time.strftime("%d-%m-%Y")+" at "+self.time.strftime("%H-%M-%S")
                data['people'][self.num]['log']=self.curlog
                with open('C:/Program Files/accounts.json','w') as f:
                    json.dump(data,f,indent=2)
            else:
                self.pin_wrong_popup()
            number=self.num
            self.AccountNumInput.setText("")
            self.AccountNumInput_2.setText("")
            self.LoginBtn.setGeometry(QtCore.QRect(200, 600, 181, 41))
            self.CancelBtn.setGeometry(QtCore.QRect(420, 600, 181, 41))
            self.LoginLabel_2.setGeometry(QtCore.QRect(100, 600, 591, 61))
            self.AccountNumInput_2.setGeometry(QtCore.QRect(160, 600, 471, 41))
            self.ChangingLabel.setGeometry(QtCore.QRect(20, 600, 281, 61))
            self.EntryBar.setGeometry(QtCore.QRect(310, 600, 471, 31))
            self.AccountNumInput.setEnabled(True)
            if self.pin == data['people'][self.num]['PIN']:
                self.open_ucw()
        else:
            self.pin_invalid_popup()

    def CancelBtn_click(self):
        self.AccountNumInput.setEnabled(True)
        self.AccountNumInput.setText("")
        self.AccountNumInput_2.setText("")
        self.LoginBtn.setGeometry(QtCore.QRect(200, 600, 181, 41))
        self.CancelBtn.setGeometry(QtCore.QRect(420, 600, 181, 41))
        self.LoginLabel_2.setGeometry(QtCore.QRect(100, 600, 591, 61))
        self.AccountNumInput_2.setGeometry(QtCore.QRect(160, 600, 471, 41))
        self.ChangingLabel.setGeometry(QtCore.QRect(20, 600, 281, 61))
        self.EntryBar.setGeometry(QtCore.QRect(310, 600, 471, 31))


if __name__ == "__main__":
    elevate()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow= QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
    