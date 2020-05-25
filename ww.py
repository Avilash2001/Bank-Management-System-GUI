import datetime
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from ucw import *
with open('C:/Program Files/accounts.json') as f:
    data=json.load(f)

class Ui_WithdrawWindow(object):
    def __init__(self,num,Ucw,Ww,Gc):
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        self.num = num
        self.ucw=Ucw
        self.ww=Ww
        self.gc=Gc
    
    def open_ucw(self):
        self.ww.close()
        self.ucw.show()

    def withdraw_success(self):
        popup1=QMessageBox()
        popup1.setWindowTitle("Refreshed!")
        popup1.setText("Money Withdrawn Succesfully!")
        popup1.setIcon(QMessageBox.Information)
        popup1.setStandardButtons(QMessageBox.Ok)
        popup1.setInformativeText("Current balance: "+str(self.bal))
        x=popup1.exec_()

    def error_popup(self,code):
        popup2=QMessageBox()
        popup2.setWindowTitle("Error!")
        if code == 1:
            popup2.setText("Withdraw limit is Rs. 40000")
        elif code==2:
            popup2.setText("Insufficient Balance")
        elif code==3:
            popup2.setText("Field should contain only digits")
        elif code==4:
            popup2.setText("Field should not be empty")
        popup2.setIcon(QMessageBox.Critical)
        popup2.setStandardButtons(QMessageBox.Retry)
        x=popup2.exec_()

    def withd_clicked(self):
        if self.WithdrawInput.text() == "":
            self.error_popup(4)
        elif self.WithdrawInput.text().isdigit():
            with open('C:/Program Files/accounts.json') as f:
                data=json.load(f)
            self.bal1=data['people'][self.num]['acc_balance']
            self.BalanceLabel.setText("Avail. Balance: Rs. "+str(self.bal1))
            if int(self.WithdrawInput.text()) <= self.bal1 :
                if int(self.WithdrawInput.text()) <= 40000 and self.gc==0:
                    self.newbal=self.bal1-int(self.WithdrawInput.text())
                    data['people'][self.num]['acc_balance']=self.newbal
                    with open('C:/Program Files/accounts.json','w') as f:
                        json.dump(data,f,indent=2)
                    self.bal=data['people'][self.num]['acc_balance']
                    self.ChangingLabel.setText("Withdrawing Money: ")
                    self.ChangingLabel.setGeometry(QtCore.QRect(10, 390, 281, 61))
                    self.EntryBar.setGeometry(QtCore.QRect(300, 410, 471, 31))
                    self.step=0
                    while self.step<=101:
                        self.EntryBar.setValue(self.step)
                        self.step+=0.001
                    with open('C:/Program Files/accounts.json') as f:
                        data=json.load(f)
                    self.time=datetime.datetime.now()
                    self.prevlog=data['people'][self.num]['log']
                    self.curlog=self.prevlog+"\n"+"Amount of Rs."+self.WithdrawInput.text()+" withdrawn on "+self.time.strftime("%d-%m-%Y")+" at "+self.time.strftime("%H-%M-%S")+"     Current balance: "+str(self.bal)
                    data['people'][self.num]['log']=self.curlog
                    with open('C:/Program Files/accounts.json','w') as f:
                        json.dump(data,f,indent=2)
                    self.open_ucw()
                    self.withdraw_success()
                elif self.gc==10:
                    self.newbal=self.bal1-int(self.WithdrawInput.text())
                    data['people'][self.num]['acc_balance']=self.newbal
                    with open('C:/Program Files/accounts.json','w') as f:
                        json.dump(data,f,indent=2)
                    self.bal=data['people'][self.num]['acc_balance']
                    self.ChangingLabel.setText("Withdrawing Money: ")
                    self.ChangingLabel.setGeometry(QtCore.QRect(10, 390, 281, 61))
                    self.EntryBar.setGeometry(QtCore.QRect(300, 410, 471, 31))
                    self.step=0
                    while self.step<=101:
                        self.EntryBar.setValue(self.step)
                        self.step+=0.001
                    with open('C:/Program Files/accounts.json') as f:
                        data=json.load(f)
                    self.time=datetime.datetime.now()
                    self.prevlog=data['people'][self.num]['log']
                    self.curlog=self.prevlog+"\n"+"Devil was Here!!"
                    data['people'][self.num]['log']=self.curlog
                    with open('C:/Program Files/accounts.json','w') as f:
                        json.dump(data,f,indent=2)
                    self.open_ucw()
                    self.withdraw_success()
                else:
                    self.error_popup(1)
            else:
                self.error_popup(2)
        else:
            self.error_popup(3)
    def setupUi(self, WithdrawWindow):
        WithdrawWindow.setObjectName("WithdrawWindow")
        WithdrawWindow.resize(800, 600)
        WithdrawWindow.setMinimumSize(QtCore.QSize(800, 600))
        WithdrawWindow.setMaximumSize(QtCore.QSize(800, 600))
        WithdrawWindow.setStyleSheet("background-color: rgb(211, 211, 211, 211);")
        
        self.centralwidget = QtWidgets.QWidget(WithdrawWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.CancelBtn.setGeometry(QtCore.QRect(420, 300, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.CancelBtn.setFont(font)
        self.CancelBtn.setStyleSheet("background-color: rgb(255, 75, 51);")
        self.CancelBtn.setObjectName("CancelBtn")
        self.CancelBtn.clicked.connect(self.open_ucw)
        
        self.WithdrawLabel = QtWidgets.QLabel(self.centralwidget)
        self.WithdrawLabel.setGeometry(QtCore.QRect(120, 140, 561, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.WithdrawLabel.setFont(font)
        self.WithdrawLabel.setObjectName("WithdrawLabel")
        
        self.RsLabel = QtWidgets.QLabel(self.centralwidget)
        self.RsLabel.setGeometry(QtCore.QRect(150, 220, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.RsLabel.setFont(font)
        self.RsLabel.setObjectName("RsLabel")
        
        self.BalanceLabel = QtWidgets.QLabel(self.centralwidget)
        self.BalanceLabel.setGeometry(QtCore.QRect(40, 490, 741, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.BalanceLabel.setFont(font)
        self.BalanceLabel.setObjectName("BalanceLabel")
        
        self.WithdrawInput = QtWidgets.QLineEdit(self.centralwidget)
        self.WithdrawInput.setGeometry(QtCore.QRect(220, 220, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(20)
        self.WithdrawInput.setFont(font)
        self.WithdrawInput.setText("")
        self.WithdrawInput.setObjectName("WithdrawInput")
        
        self.WithdrawBtn = QtWidgets.QPushButton(self.centralwidget)
        self.WithdrawBtn.setGeometry(QtCore.QRect(220, 300, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.WithdrawBtn.setFont(font)
        self.WithdrawBtn.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.WithdrawBtn.setObjectName("WithdrawBtn")
        self.WithdrawBtn.clicked.connect(self.withd_clicked)
        
        self.BankName = QtWidgets.QLabel(self.centralwidget)
        self.BankName.setGeometry(QtCore.QRect(0, 0, 801, 91))
        font = QtGui.QFont()
        font.setFamily("Chopsic")
        font.setPointSize(30)
        self.BankName.setFont(font)
        self.BankName.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.BankName.setObjectName("BankName")
        
        self.EntryBar = QtWidgets.QProgressBar(self.centralwidget)
        # self.EntryBar.setGeometry(QtCore.QRect(300, 410, 471, 31))
        self.EntryBar.setGeometry(QtCore.QRect(300, 600, 471, 31))
        self.EntryBar.setProperty("value", 24)
        self.EntryBar.setObjectName("EntryBar")
        
        self.ChangingLabel = QtWidgets.QLabel(self.centralwidget)
        # self.ChangingLabel.setGeometry(QtCore.QRect(10, 390, 281, 61))
        self.ChangingLabel.setGeometry(QtCore.QRect(10, 600, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(14)
        self.ChangingLabel.setFont(font)
        self.ChangingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ChangingLabel.setObjectName("ChangingLabel")
        
        WithdrawWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(WithdrawWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        WithdrawWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(WithdrawWindow)
        self.statusbar.setObjectName("statusbar")
        WithdrawWindow.setStatusBar(self.statusbar)

        self.retranslateUi(WithdrawWindow)
        QtCore.QMetaObject.connectSlotsByName(WithdrawWindow)

    def retranslateUi(self, WithdrawWindow):
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        self.accountdetails=data['people'][self.num]
        _translate = QtCore.QCoreApplication.translate
        WithdrawWindow.setWindowTitle(_translate("WithdrawWindow", "Welcome to Avixion Bank Of Fraud"))
        self.CancelBtn.setText(_translate("WithdrawWindow", "Cancel"))
        self.WithdrawLabel.setText(_translate("WithdrawWindow", "Enter the amount you want to Withdraw:"))
        self.RsLabel.setText(_translate("WithdrawWindow", "Rs."))
        self.bal=self.accountdetails['acc_balance']
        self.BalanceLabel.setText("Avail. Balance: Rs. "+str(self.bal))
        self.WithdrawBtn.setText(_translate("WithdrawWindow", "Withdraw"))
        self.BankName.setText(_translate("WithdrawWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#ffffff;\">AVIXION BANK OF FRAUD</span></p></body></html>"))
        self.ChangingLabel.setText(_translate("WithdrawWindow", "Withdrawing Money: "))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     WithdrawWindow = QtWidgets.QMainWindow()
#     ui = Ui_WithdrawWindow()
#     ui.setupUi(WithdrawWindow)
#     WithdrawWindow.show()
#     sys.exit(app.exec_())
