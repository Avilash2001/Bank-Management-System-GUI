import datetime
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from main import *
from acw import *
from dw import *
from ww import *
from tw1 import *
from tdw import *

with open('C:/Program Files/accounts.json') as f:
    data=json.load(f)


class Ui_UserChoiceWindow(object):
    def __init__(self,num,LoginWindow,Ucw,Gc):
        self.num = num
        self.ucw=Ucw
        self.Log=LoginWindow
        self.gc=Gc
    
    def open_log(self):
        self.Log.show()
        self.ucw.close()
    
    def logout_btn(self):
        # with open('C:/Program Files/accounts.json') as f:
        #     data1=json.load(f)
        # self.time=datetime.datetime.now()
        # self.prevlog=data1['people'][self.num]['log']
        # self.curlog=self.prevlog+"\nLogged out on "+self.time.strftime("%d-%m-%Y")+" at "+self.time.strftime("%H-%M-%S")
        # data['people'][self.num]['log']=self.curlog
        # with open('C:/Program Files/accounts.json','w') as f:
        #     json.dump(data,f,indent=2)
        self.open_log()

    def open_acw(self):
        self.AccountDetailsWindow = QtWidgets.QMainWindow()
        self.ui = Ui_AccountDetailsWindow(self.num,self.ucw,self.AccountDetailsWindow)
        self.ui.setupUi(self.AccountDetailsWindow)
        self.AccountDetailsWindow.show()
        self.ucw.close()

    def open_dw(self):
        self.DepositWindow = QtWidgets.QMainWindow()
        self.ui1 = Ui_DepositWindow(self.num,self.ucw,self.DepositWindow,self.gc)
        self.ui1.setupUi(self.DepositWindow)
        self.DepositWindow.show()
        self.ucw.close()
    
    def open_ww(self):
        self.WithdrawWindow = QtWidgets.QMainWindow()
        self.ui2 = Ui_WithdrawWindow(self.num,self.ucw,self.WithdrawWindow,self.gc)
        self.ui2.setupUi(self.WithdrawWindow)
        self.WithdrawWindow.show()
        self.ucw.close()

    def open_tw1(self):
        self.TransferWindow1 = QtWidgets.QMainWindow()
        self.ui = Ui_TransferWindow1(self.num,self.ucw,self.TransferWindow1,self.gc)
        self.ui.setupUi(self.TransferWindow1)
        self.TransferWindow1.show()
        self.ucw.close()
    
    def open_tdw(self):
        self.TransactionDataWindow = QtWidgets.QMainWindow()
        self.ui = Ui_TransactionDataWindow(self.num,self.ucw,self.TransactionDataWindow)
        self.ui.setupUi(self.TransactionDataWindow)
        self.TransactionDataWindow.show()
        self.ucw.close()

    def setupUi(self, UserChoiceWindow):
        print(self.gc)
        UserChoiceWindow.setObjectName("UserChoiceWindow")
        UserChoiceWindow.resize(800, 600)
        UserChoiceWindow.setMinimumSize(QtCore.QSize(800, 600))
        UserChoiceWindow.setMaximumSize(QtCore.QSize(800, 600))
        UserChoiceWindow.setStyleSheet("background-color: rgb(211, 211, 211, 211);")
        
        self.centralwidget = QtWidgets.QWidget(UserChoiceWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BankName = QtWidgets.QLabel(self.centralwidget)
        self.BankName.setGeometry(QtCore.QRect(0, 0, 801, 91))
        font = QtGui.QFont()
        font.setFamily("Chopsic")
        font.setPointSize(30)
        self.BankName.setFont(font)
        self.BankName.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.BankName.setObjectName("BankName")
        
        self.WelcomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.WelcomeLabel.setGeometry(QtCore.QRect(0, 150, 800, 41))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(25)
        self.WelcomeLabel.setFont(font)
        self.WelcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.WelcomeLabel.setObjectName("WelcomeLabel")
        
        self.TransactionLogBtn = QtWidgets.QPushButton(self.centralwidget)
        self.TransactionLogBtn.setGeometry(QtCore.QRect(0, 260, 300, 71))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(12)
        self.TransactionLogBtn.setFont(font)
        self.TransactionLogBtn.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.TransactionLogBtn.setObjectName("TransactionLogBtn")
        self.TransactionLogBtn.clicked.connect(self.open_tdw)
        
        self.AccDetailBtn = QtWidgets.QPushButton(self.centralwidget)
        self.AccDetailBtn.setGeometry(QtCore.QRect(0, 370, 300, 71))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(12)
        self.AccDetailBtn.setFont(font)
        self.AccDetailBtn.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.AccDetailBtn.setObjectName("AccDetailBtn")
        self.AccDetailBtn.clicked.connect(self.open_acw)
        
        self.LogoutBtn = QtWidgets.QPushButton(self.centralwidget)
        self.LogoutBtn.setGeometry(QtCore.QRect(0, 480, 300, 71))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(16)
        self.LogoutBtn.setFont(font)
        self.LogoutBtn.setStyleSheet("background-color: rgb(255, 75, 51);")
        self.LogoutBtn.setObjectName("LogoutBtn")
        self.LogoutBtn.clicked.connect(self.logout_btn)
        
        self.DepositBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DepositBtn.setGeometry(QtCore.QRect(500, 260, 300, 71))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(16)
        self.DepositBtn.setFont(font)
        self.DepositBtn.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.DepositBtn.setObjectName("DepositBtn")
        self.DepositBtn.clicked.connect(self.open_dw)
        
        self.WithdrawBtn = QtWidgets.QPushButton(self.centralwidget)
        self.WithdrawBtn.setGeometry(QtCore.QRect(500, 370, 300, 71))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(16)
        self.WithdrawBtn.setFont(font)
        self.WithdrawBtn.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.WithdrawBtn.setObjectName("WithdrawBtn")
        self.WithdrawBtn.clicked.connect(self.open_ww)
        
        self.TransferBtn = QtWidgets.QPushButton(self.centralwidget)
        self.TransferBtn.setGeometry(QtCore.QRect(500, 480, 300, 71))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(16)
        self.TransferBtn.setFont(font)
        self.TransferBtn.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.TransferBtn.setObjectName("TransferBtn")
        self.TransferBtn.clicked.connect(self.open_tw1)
        
        UserChoiceWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(UserChoiceWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        UserChoiceWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(UserChoiceWindow)
        self.statusbar.setObjectName("statusbar")
        UserChoiceWindow.setStatusBar(self.statusbar)

        self.retranslateUi(UserChoiceWindow)
        QtCore.QMetaObject.connectSlotsByName(UserChoiceWindow)

    def retranslateUi(self, UserChoiceWindow):
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        self.accountdetails=data['people'][self.num]
        _translate = QtCore.QCoreApplication.translate
        UserChoiceWindow.setWindowTitle(_translate("UserChoiceWindow", "Welcome to Avixion Bank Of Fraud"))
        self.BankName.setText(_translate("UserChoiceWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#ffffff;\">AVIXION BANK OF FRAUD</span></p></body></html>"))
        self.WelcomeLabel.setText(_translate("UserChoiceWindow", "Welcome XYZ"))
        self.name=self.accountdetails['name']
        self.WelcomeLabel.setText(f"Welcome {self.name}")
        self.TransactionLogBtn.setText(_translate("UserChoiceWindow", "View Transactions Log"))
        self.AccDetailBtn.setText(_translate("UserChoiceWindow", "View Account Details"))
        self.LogoutBtn.setText(_translate("UserChoiceWindow", "Logout"))
        self.DepositBtn.setText(_translate("UserChoiceWindow", "Deposit"))
        self.WithdrawBtn.setText(_translate("UserChoiceWindow", "Withdraw"))
        self.TransferBtn.setText(_translate("UserChoiceWindow", "Transfer"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     UserChoiceWindow = QtWidgets.QMainWindow()
#     ui = Ui_UserChoiceWindow()
#     ui.setupUi(UserChoiceWindow)
#     UserChoiceWindow.show()
#     sys.exit(app.exec_())
