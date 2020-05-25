import json
from PyQt5 import QtCore, QtGui, QtWidgets
from ucw import *
with open('C:/Program Files/accounts.json') as f:
    data=json.load(f)

class Ui_TransactionDataWindow(object):
    def __init__(self,num,Ucw,Tdw):
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        self.num = num
        self.ucw=Ucw
        self.tdw=Tdw

    def open_ucw(self):
        self.tdw.close()
        self.ucw.show()

    def acc_refreshed_popup(self):
        popup1=QMessageBox()
        popup1.setWindowTitle("Refreshed!")
        popup1.setText("Transactions Refreshed Succesfully!")
        popup1.setIcon(QMessageBox.Information)
        popup1.setStandardButtons(QMessageBox.Ok)
        x=popup1.exec_()
    
    def ref(self):
        self.ChangingLabel.setGeometry(QtCore.QRect(0, 490, 281, 61))
        self.EntryBar.setGeometry(QtCore.QRect(290, 510, 291, 31))
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        self.accountdetailsN=data['people'][self.num]
        self.log=self.accountdetailsN['log']
        self.textBrowser.setText(self.log)
        self.step=0
        while self.step<=101:
            self.EntryBar.setValue(self.step)
            self.step+=0.001
        self.ChangingLabel.setGeometry(QtCore.QRect(0, 600, 281, 61))
        self.EntryBar.setGeometry(QtCore.QRect(290, 600, 291, 31))
        self.acc_refreshed_popup()

    def setupUi(self, TransactionDataWindow):
        TransactionDataWindow.setObjectName("TransactionDataWindow")
        TransactionDataWindow.resize(800, 600)
        TransactionDataWindow.setMinimumSize(QtCore.QSize(800, 600))
        TransactionDataWindow.setMaximumSize(QtCore.QSize(800, 600))
        TransactionDataWindow.setStyleSheet("background-color: rgb(211, 211, 211);")
        
        self.centralwidget = QtWidgets.QWidget(TransactionDataWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BankName = QtWidgets.QLabel(self.centralwidget)
        self.BankName.setGeometry(QtCore.QRect(0, 0, 801, 91))
        font = QtGui.QFont()
        font.setFamily("Chopsic")
        font.setPointSize(30)
        
        self.BankName.setFont(font)
        self.BankName.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.BankName.setObjectName("BankName")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 110, 511, 61))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 170, 771, 311))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser.setObjectName("textBrowser")
        
        self.GoBackBtn = QtWidgets.QPushButton(self.centralwidget)
        self.GoBackBtn.setGeometry(QtCore.QRect(610, 500, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(12)
        self.GoBackBtn.setFont(font)
        self.GoBackBtn.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.GoBackBtn.setObjectName("GoBackBtn")
        self.GoBackBtn.clicked.connect(self.open_ucw)
        
        self.EntryBar = QtWidgets.QProgressBar(self.centralwidget)
        # self.EntryBar.setGeometry(QtCore.QRect(290, 510, 291, 31))
        self.EntryBar.setGeometry(QtCore.QRect(290, 610, 291, 31))
        self.EntryBar.setProperty("value", 24)
        self.EntryBar.setObjectName("EntryBar")
        
        self.ChangingLabel = QtWidgets.QLabel(self.centralwidget)
        # self.ChangingLabel.setGeometry(QtCore.QRect(0, 490, 281, 61))
        self.ChangingLabel.setGeometry(QtCore.QRect(0, 600, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(12)
        self.ChangingLabel.setFont(font)
        self.ChangingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ChangingLabel.setObjectName("ChangingLabel")
        
        self.RefreshBtn = QtWidgets.QPushButton(self.centralwidget)
        self.RefreshBtn.setGeometry(QtCore.QRect(20, 100, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(13)
        self.RefreshBtn.setFont(font)
        self.RefreshBtn.setObjectName("RefreshBtn")
        self.RefreshBtn.clicked.connect(self.ref)
        
        TransactionDataWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(TransactionDataWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        TransactionDataWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(TransactionDataWindow)
        self.statusbar.setObjectName("statusbar")
        TransactionDataWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TransactionDataWindow)
        QtCore.QMetaObject.connectSlotsByName(TransactionDataWindow)

    def retranslateUi(self, TransactionDataWindow):
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        self.accountdetails=data['people'][self.num]
        self.log=self.accountdetails['log']
        self.textBrowser.setText(self.log)
        _translate = QtCore.QCoreApplication.translate
        TransactionDataWindow.setWindowTitle(_translate("TransactionDataWindow", "Welcome to Avixion Bank Of Fraud"))
        self.BankName.setText(_translate("TransactionDataWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#ffffff;\">AVIXION BANK OF FRAUD</span></p></body></html>"))
        self.label.setText(_translate("TransactionDataWindow", "Transaction Data"))
        self.GoBackBtn.setText(_translate("TransactionDataWindow", "Go Back"))
        self.ChangingLabel.setText(_translate("TransactionDataWindow", "Refreshing Transactions"))
        self.RefreshBtn.setText(_translate("TransactionDataWindow", "Refresh"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     TransactionDataWindow = QtWidgets.QMainWindow()
#     ui = Ui_TransactionDataWindow()
#     ui.setupUi(TransactionDataWindow)
#     TransactionDataWindow.show()
#     sys.exit(app.exec_())
