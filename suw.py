import datetime
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from main import *
with open('C:/Program Files/accounts.json') as f:
    data=json.load(f)

class Ui_SignUpWindow(object):
    def __init__(self,num,LoginWindow,Suw):
        self.num = num
        self.suw=Suw
        self.Log=LoginWindow
    
    def open_log(self):
        self.Log.show()
        self.suw.close()

    def fields_empty_popup(self):
        popup1=QMessageBox()
        popup1.setWindowTitle("Error!")
        popup1.setText("All Field are Mandatory and are to be filled!")
        popup1.setIcon(QMessageBox.Critical)
        popup1.setStandardButtons(QMessageBox.Retry)
        x=popup1.exec_()

    def invalid_input_popup(self,code):
        popup2=QMessageBox()
        popup2.setWindowTitle("Error!")
        popup2.setText("Invalid input!")
        popup2.setIcon(QMessageBox.Critical)
        popup2.setStandardButtons(QMessageBox.Retry)
        if code == 1:
            popup2.setInformativeText("Name contains only alphabets!")
        elif code==2:
            popup2.setInformativeText("Phone Number Contains 10 digits!")
        elif code==3:
            popup2.setInformativeText("Phone number contains only digits!")
        elif code==4:
            popup2.setInformativeText("Entered PINs do not match!!")
        elif code==5:
            popup2.setInformativeText("PIN contains only 4 digits!")
        x=popup2.exec_()

    def signup_succes_popup(self):
        popup3=QMessageBox()
        popup3.setWindowTitle("Account Created Succesfully!")
        popup3.setText("Account Created Succesfully!")
        popup3.setIcon(QMessageBox.Information)
        popup3.setStandardButtons(QMessageBox.Ok)
        popup3.setInformativeText("Welcome "+self.name+" to Avixion Bank Of Fraud!\nYour Account Number is: "+str(self.acc_num))
        x=popup3.exec_()

    def signup_btn(self):
        if self.EnterNameInput.text() == "" or self.EnterPhoneInput.text() == "" or self.EnterPinInput.text() == "" or self.ReEnterPinInput.text() == "" or self.EnterEmailInput.text() == "" or self.EnterAddInput.text() == "":
            self.fields_empty_popup()
        else:
            with open('C:/Program Files/accounts.json') as f:
                data=json.load(f)
            self.new_acc={}
            if self.EnterNameInput.text().isalpha() or self.EnterNameInput.text().count(" ") > 0:
                self.name=self.EnterNameInput.text()
                self.new_acc['name']=self.name
                if self.EnterPhoneInput.text().isdigit():
                    if int(self.EnterPhoneInput.text())>999999999 and int(self.EnterPhoneInput.text())<10000000000:
                        self.phn=self.EnterPhoneInput.text()
                        self.new_acc['phone']=int(self.phn)
                        if self.EnterPinInput.text().isdigit() and self.ReEnterPinInput.text().isdigit():
                            if int(self.EnterPinInput.text())>999 and int(self.EnterPinInput.text())<10000 and int(self.ReEnterPinInput.text())>999 and int(self.ReEnterPinInput.text())<10000:
                                self.pin_enter=int(self.EnterPinInput.text())
                                self.pin_check=int(self.ReEnterPinInput.text())
                                if self.pin_enter == self.pin_check:
                                    self.new_acc['PIN']=self.pin_enter
                                    
                                    self.acc_num=len(data['people'])+1
                                    self.new_acc['acc_number']=self.acc_num

                                    self.bal=0
                                    self.new_acc['acc_balance']=self.bal
                                    
                                    self.email=self.EnterEmailInput.text()
                                    self.new_acc['email']=self.email
                                    
                                    self.add=self.EnterAddInput.text()
                                    self.new_acc['address']=self.add

                                    self.time=datetime.datetime.now()
                                    self.curlog="Account created on "+self.time.strftime("%d-%m-%Y")+" at "+self.time.strftime("%H-%M-%S")
                                    self.new_acc['log']=self.curlog

                                    data['people'].append(self.new_acc)

                                    with open('C:/Program Files/accounts.json','w') as f:
                                        json.dump(data,f,indent=2)
                                    
                                    self.suw.resize(800, 700)
                                    self.suw.setMinimumSize(QtCore.QSize(800, 700))
                                    self.suw.setMaximumSize(QtCore.QSize(800, 700))

                                    self.step=0
                                    while self.step<=101:
                                        self.EntryBar.setValue(self.step)
                                        if self.step<=50:
                                            self.ChangingLabel.setText("Accessing Account...")
                                        else:
                                            self.ChangingLabel.setText("Entering Account...")
                                        self.step+=0.01
                                    
                                    self.suw.setMinimumSize(QtCore.QSize(800, 600))
                                    self.suw.resize(800, 600)
                                    self.suw.setMaximumSize(QtCore.QSize(800, 600))
                                    self.open_log()
                                    self.signup_succes_popup()

                                    
                                else:
                                    self.invalid_input_popup(4)
                            else:
                                self.invalid_input_popup(5)
                        else:
                            self.invalid_input_popup(5)
                    else:
                        self.invalid_input_popup(2)
                else:
                    self.invalid_input_popup(3)
            else:
                self.invalid_input_popup(1)
            
    def setupUi(self, SignUpWindow):
        SignUpWindow.setObjectName("SignUpWindow")
        SignUpWindow.resize(800, 600)
        SignUpWindow.setMinimumSize(QtCore.QSize(800, 600))
        SignUpWindow.setMaximumSize(QtCore.QSize(800, 600))
        SignUpWindow.setMouseTracking(True)
        SignUpWindow.setStyleSheet("background-color: rgb(211, 211, 211);")
        
        self.centralwidget = QtWidgets.QWidget(SignUpWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.BankName = QtWidgets.QLabel(self.centralwidget)
        self.BankName.setGeometry(QtCore.QRect(0, 0, 801, 91))
        font = QtGui.QFont()
        font.setFamily("Chopsic")
        font.setPointSize(30)
        
        self.BankName.setFont(font)
        self.BankName.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.BankName.setObjectName("BankName")
        
        self.EnterNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.EnterNameLabel.setGeometry(QtCore.QRect(20, 110, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.EnterNameLabel.setFont(font)
        self.EnterNameLabel.setObjectName("EnterNameLabel")
        
        self.EnterPhoneLabel = QtWidgets.QLabel(self.centralwidget)
        self.EnterPhoneLabel.setGeometry(QtCore.QRect(20, 170, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.EnterPhoneLabel.setFont(font)
        self.EnterPhoneLabel.setObjectName("EnterPhoneLabel")
        
        self.EnterEmailLabel = QtWidgets.QLabel(self.centralwidget)
        self.EnterEmailLabel.setGeometry(QtCore.QRect(20, 230, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.EnterEmailLabel.setFont(font)
        self.EnterEmailLabel.setObjectName("EnterEmailLabel")
        
        self.EnterPinLabel = QtWidgets.QLabel(self.centralwidget)
        self.EnterPinLabel.setGeometry(QtCore.QRect(20, 440, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.EnterPinLabel.setFont(font)
        self.EnterPinLabel.setObjectName("EnterPinLabel")
        
        self.ReEnterPinLabel = QtWidgets.QLabel(self.centralwidget)
        self.ReEnterPinLabel.setGeometry(QtCore.QRect(20, 500, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.ReEnterPinLabel.setFont(font)
        self.ReEnterPinLabel.setObjectName("ReEnterPinLabel")
        
        self.EnterAddLabel = QtWidgets.QLabel(self.centralwidget)
        self.EnterAddLabel.setGeometry(QtCore.QRect(20, 290, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.EnterAddLabel.setFont(font)
        self.EnterAddLabel.setObjectName("EnterAddLabel")
        
        self.EnterNameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.EnterNameInput.setGeometry(QtCore.QRect(180, 120, 581, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(True)
        self.EnterNameInput.setFont(font)
        self.EnterNameInput.setMouseTracking(False)
        self.EnterNameInput.setFrame(True)
        self.EnterNameInput.setClearButtonEnabled(True)
        self.EnterNameInput.setObjectName("EnterNameInput")
        
        self.EnterPhoneInput = QtWidgets.QLineEdit(self.centralwidget)
        self.EnterPhoneInput.setGeometry(QtCore.QRect(280, 180, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.EnterPhoneInput.setFont(font)
        self.EnterPhoneInput.setClearButtonEnabled(True)
        self.EnterPhoneInput.setObjectName("EnterPhoneInput")
        
        self.EnterEmailInput = QtWidgets.QLineEdit(self.centralwidget)
        self.EnterEmailInput.setGeometry(QtCore.QRect(280, 240, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.EnterEmailInput.setFont(font)
        self.EnterEmailInput.setClearButtonEnabled(True)
        self.EnterEmailInput.setObjectName("EnterEmailInput")
        
        self.EnterPinInput = QtWidgets.QLineEdit(self.centralwidget)
        self.EnterPinInput.setGeometry(QtCore.QRect(210, 440, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.EnterPinInput.setFont(font)
        self.EnterPinInput.setClearButtonEnabled(True)
        self.EnterPinInput.setObjectName("EnterPinInput")
        
        self.ReEnterPinInput = QtWidgets.QLineEdit(self.centralwidget)
        self.ReEnterPinInput.setGeometry(QtCore.QRect(250, 500, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ReEnterPinInput.setFont(font)
        self.ReEnterPinInput.setClearButtonEnabled(True)
        self.ReEnterPinInput.setObjectName("ReEnterPinInput")
        
        self.EnterAddInput = QtWidgets.QLineEdit(self.centralwidget)
        self.EnterAddInput.setGeometry(QtCore.QRect(210, 300, 551, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.EnterAddInput.setFont(font)
        self.EnterAddInput.setClearButtonEnabled(True)
        self.EnterAddInput.setObjectName("EnterAddInput")
        
        self.SignUpButn = QtWidgets.QPushButton(self.centralwidget)
        self.SignUpButn.setGeometry(QtCore.QRect(550, 460, 211, 81))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.SignUpButn.setFont(font)
        self.SignUpButn.setFlat(True)
        self.SignUpButn.setObjectName("SignUpButn")
        self.SignUpButn.clicked.connect(self.signup_btn)
        
        self.ChangingLabel = QtWidgets.QLabel(self.centralwidget)
        self.ChangingLabel.setGeometry(QtCore.QRect(0, 600, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(14)
        self.ChangingLabel.setFont(font)
        self.ChangingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ChangingLabel.setObjectName("ChangingLabel")
        
        self.EntryBar = QtWidgets.QProgressBar(self.centralwidget)
        self.EntryBar.setGeometry(QtCore.QRect(290, 620, 471, 31))
        self.EntryBar.setProperty("value", 24)
        self.EntryBar.setObjectName("EntryBar")
        
        SignUpWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(SignUpWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        SignUpWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(SignUpWindow)
        self.statusbar.setObjectName("statusbar")
        SignUpWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SignUpWindow)
        QtCore.QMetaObject.connectSlotsByName(SignUpWindow)

        


    def retranslateUi(self, SignUpWindow):
        _translate = QtCore.QCoreApplication.translate
        SignUpWindow.setWindowTitle(_translate("SignUpWindow", "Welcome to Avixion Bank Of Fraud"))
        self.BankName.setText(_translate("SignUpWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#ffffff;\">AVIXION BANK OF FRAUD</span></p></body></html>"))
        self.EnterNameLabel.setText(_translate("SignUpWindow", "Enter  Name:"))
        self.EnterPhoneLabel.setText(_translate("SignUpWindow", "Enter  Phone Number:"))
        self.EnterEmailLabel.setText(_translate("SignUpWindow", "Enter  E-mail Address:"))
        self.EnterPinLabel.setText(_translate("SignUpWindow", "Enter New PIN:"))
        self.ReEnterPinLabel.setText(_translate("SignUpWindow", "Re-enter New PIN:"))
        self.EnterAddLabel.setText(_translate("SignUpWindow", "Enter  Address:"))
        self.SignUpButn.setText(_translate("SignUpWindow", "Sign Up"))
        self.ChangingLabel.setText(_translate("SignUpWindow", "Signing Up..."))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     SignUpWindow = QtWidgets.QMainWindow()
#     ui = Ui_SignUpWindow()
#     ui.setupUi(SignUpWindow)
#     SignUpWindow.show()
#     sys.exit(app.exec_())
