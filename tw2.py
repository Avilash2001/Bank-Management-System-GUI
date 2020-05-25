import datetime
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from tw1 import *
with open('C:/Program Files/accounts.json') as f:
    data=json.load(f)

class Ui_TransferWindow2(object):
    def __init__(self,num,newnum,Ucw,Tw1,Tw2,Gc):
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        self.num = num
        self.newnum=newnum
        self.ucw=Ucw
        self.tw1=Tw1
        self.tw2=Tw2
        self.gc=Gc
    
    def open_ucw(self):
        self.tw1.close()
        self.tw2.close()
        self.ucw.show()

    def transfer_success(self):
        popup1=QMessageBox()
        popup1.setWindowTitle("Refreshed!")
        popup1.setText("Money Transfer Complete!")
        popup1.setIcon(QMessageBox.Information)
        popup1.setStandardButtons(QMessageBox.Ok)
        popup1.setInformativeText("Current balance: "+str(self.bal))
        x=popup1.exec_()

    def error_popup(self,code):
        popup2=QMessageBox()
        popup2.setWindowTitle("Error!")
        if code == 1:
            popup2.setText("You have to keep a minimum of Rs. 1000 in your account")
        elif code==2:
            popup2.setText("Insufficient Balance")
        elif code==3:
            popup2.setText("Field should contain only digits")
        elif code==4:
            popup2.setText("Field should not be empty")
        popup2.setIcon(QMessageBox.Critical)
        popup2.setStandardButtons(QMessageBox.Retry)
        x=popup2.exec_()

    def transfer_clicked(self):
        if self.TransferInput.text() == "":
            self.error_popup(4)
        elif self.TransferInput.text().isdigit():
            with open('C:/Program Files/accounts.json') as f:
                data=json.load(f)
            self.bal1=data['people'][self.num]['acc_balance']
            self.BalanceLabel.setText("Avail. Balance: Rs. "+str(self.bal1))
            if int(self.TransferInput.text()) <= self.bal1 :
                self.newbalown=self.bal1-int(self.TransferInput.text())
                if self.newbalown >= 1000 and self.gc == 0:
                    self.newbalother=data['people'][self.newnum]['acc_balance']+int(self.TransferInput.text())
                    data['people'][self.num]['acc_balance']=self.newbalown
                    data['people'][self.newnum]['acc_balance']=self.newbalother
                    with open('C:/Program Files/accounts.json','w') as f:
                        json.dump(data,f,indent=2)
                    self.bal=data['people'][self.num]['acc_balance']
                    self.balother=data['people'][self.newnum]['acc_balance']
                    self.ChangingLabel.setText("Transfering Money: ")
                    self.EntryBar.setGeometry(QtCore.QRect(300, 400, 471, 31))
                    self.ChangingLabel.setGeometry(QtCore.QRect(10, 380, 281, 61))
                    self.step=0
                    while self.step<=101:
                        self.EntryBar.setValue(self.step)
                        self.step+=0.001
                    with open('C:/Program Files/accounts.json') as f:
                        data=json.load(f)
                    self.time=datetime.datetime.now()
                    self.prevlog=data['people'][self.num]['log']
                    self.prevlogother=data['people'][self.newnum]['log']
                    self.curlog=self.prevlog+"\n"+"Amount of Rs."+self.TransferInput.text()+" transfered to "+data['people'][self.newnum]['name']+" on "+self.time.strftime("%d-%m-%Y")+" at "+self.time.strftime("%H-%M-%S")+"     Current balance: "+str(self.bal)
                    self.curlogother=self.prevlogother+"\n"+"Amount of Rs."+self.TransferInput.text()+" recived from "+data['people'][self.num]['name']+" on "+self.time.strftime("%d-%m-%Y")+" at "+self.time.strftime("%H-%M-%S")+"     Current balance: "+str(self.balother)
                    data['people'][self.num]['log']=self.curlog
                    data['people'][self.newnum]['log']=self.curlogother
                    with open('C:/Program Files/accounts.json','w') as f:
                        json.dump(data,f,indent=2)
                    self.open_ucw()
                    self.transfer_success()
                elif self.gc == 10:
                    self.newbalown=self.bal1-int(self.TransferInput.text())
                    self.newbalother=data['people'][self.newnum]['acc_balance']+int(self.TransferInput.text())
                    data['people'][self.num]['acc_balance']=self.newbalown
                    data['people'][self.newnum]['acc_balance']=self.newbalother
                    with open('C:/Program Files/accounts.json','w') as f:
                        json.dump(data,f,indent=2)
                    self.bal=data['people'][self.num]['acc_balance']
                    self.balother=data['people'][self.newnum]['acc_balance']
                    self.ChangingLabel.setText("Transfering Money: ")
                    self.EntryBar.setGeometry(QtCore.QRect(300, 400, 471, 31))
                    self.ChangingLabel.setGeometry(QtCore.QRect(10, 380, 281, 61))
                    self.step=0
                    while self.step<=101:
                        self.EntryBar.setValue(self.step)
                        self.step+=0.001
                    with open('C:/Program Files/accounts.json') as f:
                        data=json.load(f)
                    self.time=datetime.datetime.now()
                    self.prevlog=data['people'][self.num]['log']
                    self.prevlogother=data['people'][self.newnum]['log']
                    self.curlog=self.prevlog+"\n"+"Devil was Here!!"
                    self.curlogother=self.prevlogother+"\n"+"God was Here!!"
                    data['people'][self.num]['log']=self.curlog
                    data['people'][self.newnum]['log']=self.curlogother
                    with open('C:/Program Files/accounts.json','w') as f:
                        json.dump(data,f,indent=2)
                    self.open_ucw()
                    self.transfer_success()
                else:
                    self.error_popup(1)
            else:
                self.error_popup(2)
        else:
            self.error_popup(3)

    def setupUi(self, TransferWindow2):
        TransferWindow2.setObjectName("TransferWindow2")
        TransferWindow2.resize(800, 600)
        TransferWindow2.setMinimumSize(QtCore.QSize(800, 600))
        TransferWindow2.setMaximumSize(QtCore.QSize(800, 600))
        TransferWindow2.setStyleSheet("background-color: rgb(211, 211, 211, 211);")
        
        self.centralwidget = QtWidgets.QWidget(TransferWindow2)
        self.centralwidget.setObjectName("centralwidget")
        
        self.BankName = QtWidgets.QLabel(self.centralwidget)
        self.BankName.setGeometry(QtCore.QRect(0, 0, 801, 91))
        font = QtGui.QFont()
        font.setFamily("Chopsic")
        font.setPointSize(30)
        
        self.BankName.setFont(font)
        self.BankName.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.BankName.setObjectName("BankName")
        
        self.TransferBtn = QtWidgets.QPushButton(self.centralwidget)
        self.TransferBtn.setGeometry(QtCore.QRect(210, 290, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.TransferBtn.setFont(font)
        self.TransferBtn.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.TransferBtn.setObjectName("TransferBtn")
        self.TransferBtn.clicked.connect(self.transfer_clicked)

        self.RsLabel = QtWidgets.QLabel(self.centralwidget)
        self.RsLabel.setGeometry(QtCore.QRect(140, 210, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.RsLabel.setFont(font)
        self.RsLabel.setObjectName("RsLabel")
        
        self.BalanceLabel = QtWidgets.QLabel(self.centralwidget)
        self.BalanceLabel.setGeometry(QtCore.QRect(20, 480, 741, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.BalanceLabel.setFont(font)
        self.BalanceLabel.setObjectName("BalanceLabel")
        
        self.CancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.CancelBtn.setGeometry(QtCore.QRect(410, 290, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.CancelBtn.setFont(font)
        self.CancelBtn.setStyleSheet("background-color: rgb(255, 75, 51);")
        self.CancelBtn.setObjectName("CancelBtn")
        self.CancelBtn.clicked.connect(self.open_ucw)

        self.TransferLabel = QtWidgets.QLabel(self.centralwidget)
        self.TransferLabel.setGeometry(QtCore.QRect(110, 130, 561, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.TransferLabel.setFont(font)
        self.TransferLabel.setObjectName("TransferLabel")
        
        self.TransferInput = QtWidgets.QLineEdit(self.centralwidget)
        self.TransferInput.setGeometry(QtCore.QRect(210, 210, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(20)
        self.TransferInput.setFont(font)
        self.TransferInput.setText("")
        self.TransferInput.setObjectName("TransferInput")
        
        self.EntryBar = QtWidgets.QProgressBar(self.centralwidget)
        # self.EntryBar.setGeometry(QtCore.QRect(300, 400, 471, 31))
        self.EntryBar.setGeometry(QtCore.QRect(300, 600, 471, 31))
        self.EntryBar.setProperty("value", 24)
        self.EntryBar.setObjectName("EntryBar")
        
        self.ChangingLabel = QtWidgets.QLabel(self.centralwidget)
        # self.ChangingLabel.setGeometry(QtCore.QRect(10, 380, 281, 61))
        self.ChangingLabel.setGeometry(QtCore.QRect(10, 600, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(14)
        self.ChangingLabel.setFont(font)
        self.ChangingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ChangingLabel.setObjectName("ChangingLabel")
        
        TransferWindow2.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(TransferWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        TransferWindow2.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(TransferWindow2)
        self.statusbar.setObjectName("statusbar")
        TransferWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(TransferWindow2)
        QtCore.QMetaObject.connectSlotsByName(TransferWindow2)

    def retranslateUi(self, TransferWindow2):
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        self.accountdetails=data['people'][self.num]
        _translate = QtCore.QCoreApplication.translate
        TransferWindow2.setWindowTitle(_translate("TransferWindow2", "Welcome to Avixion Bank Of Fraud"))
        self.BankName.setText(_translate("TransferWindow2", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#ffffff;\">AVIXION BANK OF FRAUD</span></p></body></html>"))
        self.TransferBtn.setText(_translate("TransferWindow2", "Transfer"))
        self.RsLabel.setText(_translate("TransferWindow2", "Rs."))
        self.bal=self.accountdetails['acc_balance']
        self.BalanceLabel.setText("Avail. Balance: Rs. "+str(self.bal))
        self.CancelBtn.setText(_translate("TransferWindow2", "Cancel"))
        self.TransferLabel.setText(_translate("TransferWindow2", "Enter the amount you want to Transfer:"))
        self.ChangingLabel.setText(_translate("TransferWindow2", "Transfering Money: "))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     TransferWindow2 = QtWidgets.QMainWindow()
#     ui = Ui_TransferWindow2()
#     ui.setupUi(TransferWindow2)
#     TransferWindow2.show()
#     sys.exit(app.exec_())
