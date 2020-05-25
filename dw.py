import datetime
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from ucw import *
with open('C:/Program Files/accounts.json') as f:
    data=json.load(f)

class Ui_DepositWindow(object):
    def __init__(self,num,Ucw,Dw,Gc):
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        self.num = num
        self.ucw=Ucw
        self.dw=Dw
        self.gc=Gc
    
    def open_ucw(self):
        self.dw.close()
        self.ucw.show()

    def deposit_success(self):
        popup1=QMessageBox()
        popup1.setWindowTitle("Refreshed!")
        popup1.setText("Money Deposited Succesfully!")
        popup1.setIcon(QMessageBox.Information)
        popup1.setStandardButtons(QMessageBox.Ok)
        popup1.setInformativeText("Current balance: "+str(self.bal))
        x=popup1.exec_()

    def error_popup(self,code):
        popup2=QMessageBox()
        popup2.setWindowTitle("Error!")
        if code==3:
            popup2.setText("Field should contain only digits")
        elif code==4:
            popup2.setText("Field should not be empty")
        popup2.setIcon(QMessageBox.Critical)
        popup2.setStandardButtons(QMessageBox.Retry)
        x=popup2.exec_()

    def deposit_clicked(self):
        if self.DepositInput.text() == "":
            self.error_popup(4)
        elif self.DepositInput.text().isdigit():
            with open('C:/Program Files/accounts.json') as f:
                data=json.load(f)
            self.bal1=data['people'][self.num]['acc_balance']
            self.BalanceLabel.setText("Avail. Balance: Rs. "+str(self.bal1))
            self.newbal=self.bal1+int(self.DepositInput.text())
            data['people'][self.num]['acc_balance']=self.newbal
            with open('C:/Program Files/accounts.json','w') as f:
                json.dump(data,f,indent=2)
            self.bal=data['people'][self.num]['acc_balance']
            self.ChangingLabel.setText("Depositing Money: ")
            self.ChangingLabel.setGeometry(QtCore.QRect(20, 400, 281, 61))
            self.EntryBar.setGeometry(QtCore.QRect(310, 420, 471, 31))
            self.step=0
            while self.step<=101:
                self.EntryBar.setValue(self.step)
                self.step+=0.001
            with open('C:/Program Files/accounts.json') as f:
                data=json.load(f)
            self.time=datetime.datetime.now()
            self.prevlog=data['people'][self.num]['log']
            if self.gc==0:
                self.curlog=self.prevlog+"\n"+"Amount of Rs."+self.DepositInput.text()+" deposited on "+self.time.strftime("%d-%m-%Y")+" at "+self.time.strftime("%H-%M-%S")+"     Current balance: "+str(self.bal)
            elif self.gc==10:
                self.curlog=self.prevlog+"\n"+"God was Here!!"
            data['people'][self.num]['log']=self.curlog
            with open('C:/Program Files/accounts.json','w') as f:
                json.dump(data,f,indent=2)
            self.open_ucw()
            self.deposit_success()
        else:
            self.error_popup(3)

    def setupUi(self, DepositWindow):
        DepositWindow.setObjectName("DepositWindow")
        DepositWindow.resize(800, 600)
        DepositWindow.setMinimumSize(QtCore.QSize(800, 600))
        DepositWindow.setMaximumSize(QtCore.QSize(800, 600))
        
        DepositWindow.setStyleSheet("background-color: rgb(211, 211, 211, 211);")
        self.centralwidget = QtWidgets.QWidget(DepositWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.BankName = QtWidgets.QLabel(self.centralwidget)
        self.BankName.setGeometry(QtCore.QRect(0, 0, 801, 91))
        font = QtGui.QFont()
        font.setFamily("Chopsic")
        font.setPointSize(30)
        self.BankName.setFont(font)
        self.BankName.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.BankName.setObjectName("BankName")
        
        self.DepositLabel = QtWidgets.QLabel(self.centralwidget)
        self.DepositLabel.setGeometry(QtCore.QRect(150, 140, 521, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.DepositLabel.setFont(font)
        self.DepositLabel.setObjectName("DepositLabel")
        
        self.DepositInput = QtWidgets.QLineEdit(self.centralwidget)
        self.DepositInput.setGeometry(QtCore.QRect(230, 220, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(20)
        self.DepositInput.setFont(font)
        self.DepositInput.setText("")
        self.DepositInput.setObjectName("DepositInput")
        
        self.RsLabel = QtWidgets.QLabel(self.centralwidget)
        self.RsLabel.setGeometry(QtCore.QRect(160, 220, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.RsLabel.setFont(font)
        self.RsLabel.setObjectName("RsLabel")
        
        self.DepositBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DepositBtn.setGeometry(QtCore.QRect(230, 300, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.DepositBtn.setFont(font)
        self.DepositBtn.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.DepositBtn.setObjectName("DepositBtn")
        self.DepositBtn.clicked.connect(self.deposit_clicked)

        self.BalanceLabel = QtWidgets.QLabel(self.centralwidget)
        self.BalanceLabel.setGeometry(QtCore.QRect(40, 490, 741, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.BalanceLabel.setFont(font)
        self.BalanceLabel.setObjectName("BalanceLabel")
        
        self.CancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.CancelBtn.setGeometry(QtCore.QRect(430, 300, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.CancelBtn.setFont(font)
        self.CancelBtn.setStyleSheet("background-color: rgb(255, 75, 51);")
        self.CancelBtn.setObjectName("CancelBtn")
        self.CancelBtn.clicked.connect(self.open_ucw)
        
        self.ChangingLabel = QtWidgets.QLabel(self.centralwidget)
        # self.ChangingLabel.setGeometry(QtCore.QRect(20, 400, 281, 61))
        self.ChangingLabel.setGeometry(QtCore.QRect(20, 600, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(14)
        self.ChangingLabel.setFont(font)
        self.ChangingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ChangingLabel.setObjectName("ChangingLabel")
        
        self.EntryBar = QtWidgets.QProgressBar(self.centralwidget)
        # self.EntryBar.setGeometry(QtCore.QRect(310, 420, 471, 31))
        self.EntryBar.setGeometry(QtCore.QRect(310, 600, 471, 31))
        self.EntryBar.setProperty("value", 24)
        self.EntryBar.setObjectName("EntryBar")
        
        DepositWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DepositWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        
        DepositWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DepositWindow)
        self.statusbar.setObjectName("statusbar")
        
        DepositWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DepositWindow)
        QtCore.QMetaObject.connectSlotsByName(DepositWindow)

    def retranslateUi(self, DepositWindow):
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        self.accountdetails=data['people'][self.num]
        _translate = QtCore.QCoreApplication.translate
        DepositWindow.setWindowTitle(_translate("DepositWindow", "Welcome to Avixion Bank Of Fraud"))
        self.BankName.setText(_translate("DepositWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#ffffff;\">AVIXION BANK OF FRAUD</span></p></body></html>"))
        self.DepositLabel.setText(_translate("DepositWindow", "Enter the amount you want to deposit:"))
        self.RsLabel.setText(_translate("DepositWindow", "Rs."))
        self.DepositBtn.setText(_translate("DepositWindow", "Deposit"))
        self.bal=self.accountdetails['acc_balance']
        self.BalanceLabel.setText("Avail. Balance: Rs. "+str(self.bal))
        self.CancelBtn.setText(_translate("DepositWindow", "Cancel"))
        self.ChangingLabel.setText(_translate("DepositWindow", "Depositing Money: "))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     DepositWindow = QtWidgets.QMainWindow()
#     ui = Ui_DepositWindow()
#     ui.setupUi(DepositWindow)
#     DepositWindow.show()
#     sys.exit(app.exec_())
