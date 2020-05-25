import json
from PyQt5 import QtCore, QtGui, QtWidgets
from main import *
from gmw import *

class Ui_GodPassCheckerWindow(object):
    def __init__(self,LoginWindow,Gpcw,Gc):
        self.gpcw=Gpcw
        self.Log=LoginWindow
        self.gc=Gc

    def open_log(self):
        self.Log.show()
        self.gpcw.close()

    def open_gmw(self):
        self.GodModeWindow1 = QtWidgets.QMainWindow()
        self.ui = Ui_GodModeWindow1(self.Log,self.gpcw,self.GodModeWindow1,self.gc)
        self.ui.setupUi(self.GodModeWindow1)
        self.GodModeWindow1.show()
        self.gpcw.close()

    def reject_popup(self):
        popup1=QMessageBox()
        popup1.setWindowTitle("You are not Worthy!")
        popup1.setText("You are not Worthy!")
        popup1.setIcon(QMessageBox.Critical)
        popup1.setStandardButtons(QMessageBox.Ok)
        x=popup1.exec_()
        self.open_log()

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

    def enter_clicked(self):
        if self.GodPassInp.text() == "":
            self.error_popup(4)
        elif self.GodPassInp.text().isdigit():
            if int(self.GodPassInp.text())==123456:
                self.ChangingLabel.setGeometry(QtCore.QRect(0, 270, 401, 81))
                self.EntryBar.setGeometry(QtCore.QRect(0, 220, 401, 31))
                self.gpcw.setMinimumSize(QtCore.QSize(400, 370))
                self.gpcw.resize(400, 370)
                self.gpcw.setMaximumSize(QtCore.QSize(400, 370))
                self.step=0
                while self.step<=101:
                    self.EntryBar.setValue(self.step)
                    if self.step<=50:
                        self.ChangingLabel.setText("Accessing Database...")
                    else:
                        self.ChangingLabel.setText("Decrypting Database...")
                    self.step+=0.01
                self.open_gmw()
            else:
                self.reject_popup()
        else:
            self.error_popup(3)
    
    def setupUi(self, GodPassCheckerWindow):
        GodPassCheckerWindow.setObjectName("GodPassCheckerWindow")
        GodPassCheckerWindow.resize(400, 250)
        GodPassCheckerWindow.setMinimumSize(QtCore.QSize(400, 250))
        GodPassCheckerWindow.setMaximumSize(QtCore.QSize(400, 250))
        GodPassCheckerWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.centralwidget = QtWidgets.QWidget(GodPassCheckerWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.EnterLabel = QtWidgets.QLabel(self.centralwidget)
        self.EnterLabel.setGeometry(QtCore.QRect(10, 0, 391, 81))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(15)
        
        self.EnterLabel.setFont(font)
        self.EnterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.EnterLabel.setObjectName("EnterLabel")
        
        self.GodPassInp = QtWidgets.QLineEdit(self.centralwidget)
        self.GodPassInp.setGeometry(QtCore.QRect(50, 90, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.GodPassInp.setFont(font)
        self.GodPassInp.setAlignment(QtCore.Qt.AlignCenter)
        self.GodPassInp.setObjectName("GodPassInp")
        
        self.EnterBtn = QtWidgets.QPushButton(self.centralwidget)
        self.EnterBtn.setGeometry(QtCore.QRect(130, 150, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.EnterBtn.setFont(font)
        self.EnterBtn.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.EnterBtn.setObjectName("EnterBtn")
        self.EnterBtn.clicked.connect(self.enter_clicked)
        
        self.EntryBar = QtWidgets.QProgressBar(self.centralwidget)
        # self.EntryBar.setGeometry(QtCore.QRect(0, 220, 401, 31))
        self.EntryBar.setGeometry(QtCore.QRect(0, 300, 401, 31))
        self.EntryBar.setProperty("value", 24)
        self.EntryBar.setObjectName("EntryBar")
        
        self.ChangingLabel = QtWidgets.QLabel(self.centralwidget)
        # self.ChangingLabel.setGeometry(QtCore.QRect(0, 270, 401, 81))
        self.ChangingLabel.setGeometry(QtCore.QRect(0, 300, 401, 81))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(15)
        self.ChangingLabel.setFont(font)
        self.ChangingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ChangingLabel.setObjectName("ChangingLabel")
        
        GodPassCheckerWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(GodPassCheckerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menubar.setObjectName("menubar")
        
        GodPassCheckerWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(GodPassCheckerWindow)
        self.statusbar.setObjectName("statusbar")
        
        GodPassCheckerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GodPassCheckerWindow)
        QtCore.QMetaObject.connectSlotsByName(GodPassCheckerWindow)

    def retranslateUi(self, GodPassCheckerWindow):
        _translate = QtCore.QCoreApplication.translate
        GodPassCheckerWindow.setWindowTitle(_translate("GodPassCheckerWindow", "Enter God Password"))
        self.EnterLabel.setText(_translate("GodPassCheckerWindow", "Enter the God Password:"))
        self.EnterBtn.setText(_translate("GodPassCheckerWindow", "Enter!!"))
        self.ChangingLabel.setText(_translate("GodPassCheckerWindow", "Acessing Account..."))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     GodPassCheckerWindow = QtWidgets.QMainWindow()
#     ui = Ui_GodPassCheckerWindow()
#     ui.setupUi(GodPassCheckerWindow)
#     GodPassCheckerWindow.show()
#     sys.exit(app.exec_())
