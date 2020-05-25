import json
from PyQt5 import QtCore, QtGui, QtWidgets
from gmw import *
with open('C:/Program Files/accounts.json') as f:
    data=json.load(f)

class Ui_GodTransactionDataWindow(object):
    def __init__(self,index,Gmw,Gtdw):
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        self.index = index
        self.gmw=Gmw
        self.gtdw=Gtdw
    
    def open_gmw(self):
        self.gtdw.close()
        self.gmw.show()
    

    def ref(self):
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        self.accountdetailsN=data['people'][self.index]
        self.log=self.accountdetailsN['log']
        self.textEdit.setText(self.log)

    def done(self):
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        data['people'][self.index]['log']=self.textEdit.toPlainText()
        with open('C:/Program Files/accounts.json','w') as f:
                json.dump(data,f,indent=2)

    def setupUi(self, GodTransactionDataWindow):
        GodTransactionDataWindow.setObjectName("GodTransactionDataWindow")
        GodTransactionDataWindow.resize(1024, 768)
        GodTransactionDataWindow.setMinimumSize(QtCore.QSize(1024, 768))
        GodTransactionDataWindow.setMaximumSize(QtCore.QSize(1024, 768))
        GodTransactionDataWindow.setStyleSheet("background-color: rgb(211, 211, 211);\n")
        
        self.centralwidget = QtWidgets.QWidget(GodTransactionDataWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.RefreshBtn = QtWidgets.QPushButton(self.centralwidget)
        self.RefreshBtn.setGeometry(QtCore.QRect(20, 100, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(13)
        self.RefreshBtn.setFont(font)
        self.RefreshBtn.setObjectName("RefreshBtn")
        self.RefreshBtn.clicked.connect(self.ref)

        self.DoneBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DoneBtn.setGeometry(QtCore.QRect(20, 690, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(12)
        self.DoneBtn.setFont(font)
        self.DoneBtn.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.DoneBtn.setObjectName("DoneBtn")
        self.DoneBtn.clicked.connect(self.done)

        self.GoBackBtn = QtWidgets.QPushButton(self.centralwidget)
        self.GoBackBtn.setGeometry(QtCore.QRect(850, 690, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(12)
        self.GoBackBtn.setFont(font)
        self.GoBackBtn.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.GoBackBtn.setObjectName("GoBackBtn")
        self.GoBackBtn.clicked.connect(self.open_gmw)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 110, 1011, 61))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")
        
        self.BankName = QtWidgets.QLabel(self.centralwidget)
        self.BankName.setGeometry(QtCore.QRect(0, 0, 1021, 91))
        font = QtGui.QFont()
        font.setFamily("Chopsic")
        font.setPointSize(30)
        self.BankName.setFont(font)
        self.BankName.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.BankName.setObjectName("BankName")
        
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 180, 1011, 501))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setObjectName("textEdit")
        
        GodTransactionDataWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(GodTransactionDataWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 26))
        self.menubar.setObjectName("menubar")
        GodTransactionDataWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(GodTransactionDataWindow)
        self.statusbar.setObjectName("statusbar")
        GodTransactionDataWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GodTransactionDataWindow)
        QtCore.QMetaObject.connectSlotsByName(GodTransactionDataWindow)

    def retranslateUi(self, GodTransactionDataWindow):
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        self.accountdetails=data['people'][self.index]
        self.log=self.accountdetails['log']
        self.textEdit.setText(self.log)
        _translate = QtCore.QCoreApplication.translate
        GodTransactionDataWindow.setWindowTitle(_translate("GodTransactionDataWindow", "Welcome Almighty!!"))
        self.GoBackBtn.setText(_translate("GodTransactionDataWindow", "Go Back"))
        self.label.setText(_translate("GodTransactionDataWindow", "Transaction Data"))
        self.BankName.setText(_translate("GodTransactionDataWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#ffffff;\">WELCOME aLMIGHTY!!</span></p></body></html>"))
        self.RefreshBtn.setText(_translate("TransactionDataWindow", "Refresh"))
        self.DoneBtn.setText(_translate("TransactionDataWindow", "Done"))

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     GodTransactionDataWindow = QtWidgets.QMainWindow()
#     ui = Ui_GodTransactionDataWindow()
#     ui.setupUi(GodTransactionDataWindow)
#     GodTransactionDataWindow.show()
#     sys.exit(app.exec_())
