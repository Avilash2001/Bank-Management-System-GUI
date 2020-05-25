import datetime
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from acw import *

class Ui_EditDetailsWindow(object):
    def __init__(self,num,Acw,Edw):
        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        self.num = num
        self.edw=Edw
        self.acw=Acw

    def open_acw(self):
        self.edw.close()
        self.acw.show()

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

    def edit_success(self):
        popup1=QMessageBox()
        popup1.setWindowTitle("Success!!")
        popup1.setText("Account Details Updated!!")
        popup1.setIcon(QMessageBox.Information)
        popup1.setStandardButtons(QMessageBox.Ok)
        x=popup1.exec_()

    def done_btn(self):
        if self.EnterNameInput.text() == "" or self.EnterPhoneInput.text() == "" or self.EnterEmailInput.text() == "" or self.EnterAddInput.text() == "":
            self.fields_empty_popup()
        else:
            with open('C:/Program Files/accounts.json') as f:
                data=json.load(f)
            if self.EnterNameInput.text().isalpha() or self.EnterNameInput.text().count(" ") > 0:
                self.name=self.EnterNameInput.text()
                data['people'][self.num]['name']=self.name
                if self.EnterPhoneInput.text().isdigit():
                    if int(self.EnterPhoneInput.text())>999999999 and int(self.EnterPhoneInput.text())<10000000000:
                        self.phn=self.EnterPhoneInput.text()
                        data['people'][self.num]['phone']=int(self.phn)
                        data['people'][self.num]['email']=self.EnterEmailInput.text()      
                        data['people'][self.num]['address']=self.EnterAddInput.text()
                        if self.EnterPinInput.text() == "" and self.ReEnterPinInput.text() =="":
                            self.time=datetime.datetime.now()
                            self.prevlog=data['people'][self.num]['log']
                            self.curlog=self.prevlog+"\n"+"Account details edited on "+self.time.strftime("%d-%m-%Y")+" at "+self.time.strftime("%H-%M-%S")
                            data['people'][self.num]['log']=self.curlog
                            with open('C:/Program Files/accounts.json','w') as f:
                                json.dump(data,f,indent=2)
                            self.edw.setMinimumSize(QtCore.QSize(800, 680))
                            self.edw.resize(800, 680)
                            self.edw.setMaximumSize(QtCore.QSize(800, 680))
                            self.step=0
                            while self.step<=101:
                                self.EntryBar.setValue(self.step)
                                self.ChangingLabel.setText("Saving Edits...")
                                self.step+=0.01
                            self.open_acw()
                            self.edit_success()
                        else:
                            if self.EnterPinInput.text().isdigit() and self.ReEnterPinInput.text().isdigit():
                                if int(self.EnterPinInput.text())>999 and int(self.EnterPinInput.text())<10000 and int(self.ReEnterPinInput.text())>999 and int(self.ReEnterPinInput.text())<10000:
                                    if int(self.EnterPinInput.text()) == int(self.ReEnterPinInput.text()):
                                        data['people'][self.num]['PIN'] = int(self.EnterPinInput.text())
                                        self.time=datetime.datetime.now()
                                        self.prevlog=data['people'][self.num]['log']
                                        self.curlog=self.prevlog+"\n"+"Account details edited on "+self.time.strftime("%d-%m-%Y")+" at "+self.time.strftime("%H-%M-%S")
                                        data['people'][self.num]['log']=self.curlog
                                        with open('C:/Program Files/accounts.json','w') as f:
                                            json.dump(data,f,indent=2)
                                        self.edw.setMinimumSize(QtCore.QSize(800, 680))
                                        self.edw.resize(800, 680)
                                        self.edw.setMaximumSize(QtCore.QSize(800, 680))
                                        self.step=0
                                        while self.step<=101:
                                            self.EntryBar.setValue(self.step)
                                            self.ChangingLabel.setText("Saving Edits...")
                                            self.step+=0.01
                                        self.open_acw()
                                        self.edit_success()
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
                
    def setupUi(self, EditDetailsWindow):
        EditDetailsWindow.setObjectName("EditDetailsWindow")
        EditDetailsWindow.resize(800, 600)
        EditDetailsWindow.setMinimumSize(QtCore.QSize(800, 600))
        EditDetailsWindow.setMaximumSize(QtCore.QSize(800, 600))
        EditDetailsWindow.setStyleSheet("background-color: rgb(211, 211, 211);")
        
        self.centralwidget = QtWidgets.QWidget(EditDetailsWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.EditDetailsLabel = QtWidgets.QLabel(self.centralwidget)
        self.EditDetailsLabel.setGeometry(QtCore.QRect(290, 100, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(20)
        self.EditDetailsLabel.setFont(font)
        self.EditDetailsLabel.setObjectName("EditDetailsLabel")
       
        self.BankName = QtWidgets.QLabel(self.centralwidget)
        self.BankName.setGeometry(QtCore.QRect(0, 0, 801, 91))
        font = QtGui.QFont()
        font.setFamily("Chopsic")
        font.setPointSize(30)
        self.BankName.setFont(font)
        self.BankName.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.BankName.setObjectName("BankName")
       
        self.EnterEmailLabel = QtWidgets.QLabel(self.centralwidget)
        self.EnterEmailLabel.setGeometry(QtCore.QRect(10, 260, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.EnterEmailLabel.setFont(font)
        self.EnterEmailLabel.setObjectName("EnterEmailLabel")
       
        self.ReEnterPinLabel = QtWidgets.QLabel(self.centralwidget)
        self.ReEnterPinLabel.setGeometry(QtCore.QRect(10, 510, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.ReEnterPinLabel.setFont(font)
        self.ReEnterPinLabel.setObjectName("ReEnterPinLabel")
        self.ReEnterPinInput = QtWidgets.QLineEdit(self.centralwidget)
        self.ReEnterPinInput.setGeometry(QtCore.QRect(240, 510, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ReEnterPinInput.setFont(font)
        self.ReEnterPinInput.setClearButtonEnabled(True)
        self.ReEnterPinInput.setObjectName("ReEnterPinInput")
       
        self.EnterEmailInput = QtWidgets.QLineEdit(self.centralwidget)
        self.EnterEmailInput.setGeometry(QtCore.QRect(270, 270, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.EnterEmailInput.setFont(font)
        self.EnterEmailInput.setClearButtonEnabled(True)
        self.EnterEmailInput.setObjectName("EnterEmailInput")
       
        self.EnterPinInput = QtWidgets.QLineEdit(self.centralwidget)
        self.EnterPinInput.setGeometry(QtCore.QRect(200, 460, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.EnterPinInput.setFont(font)
        self.EnterPinInput.setClearButtonEnabled(True)
        self.EnterPinInput.setObjectName("EnterPinInput")
       
        self.EnterAddInput = QtWidgets.QLineEdit(self.centralwidget)
        self.EnterAddInput.setGeometry(QtCore.QRect(200, 320, 551, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.EnterAddInput.setFont(font)
        self.EnterPinInput.setClearButtonEnabled(True)
        self.EnterAddInput.setObjectName("EnterAddInput")
       
        self.EnterPhoneInput = QtWidgets.QLineEdit(self.centralwidget)
        self.EnterPhoneInput.setGeometry(QtCore.QRect(270, 220, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.EnterPhoneInput.setFont(font)
        self.EnterPhoneInput.setClearButtonEnabled(True)
        self.EnterPhoneInput.setObjectName("EnterPhoneInput")
        
        self.EnterAddLabel = QtWidgets.QLabel(self.centralwidget)
        self.EnterAddLabel.setGeometry(QtCore.QRect(10, 310, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.EnterAddLabel.setFont(font)
        self.EnterAddLabel.setObjectName("EnterAddLabel")
        
        self.EnterNameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.EnterNameInput.setGeometry(QtCore.QRect(170, 170, 581, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(True)
        self.EnterNameInput.setFont(font)
        self.EnterNameInput.setMouseTracking(False)
        self.EnterNameInput.setFrame(True)
        self.EnterNameInput.setClearButtonEnabled(True)
        self.EnterNameInput.setObjectName("EnterNameInput")
        
        self.CancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.CancelBtn.setGeometry(QtCore.QRect(610, 510, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.CancelBtn.setFont(font)
        self.CancelBtn.setStyleSheet("background-color: rgb(255, 75, 51);")
        self.CancelBtn.setFlat(False)
        self.CancelBtn.setObjectName("CancelBtn")
        self.CancelBtn.clicked.connect(self.open_acw)
        
        self.EnterPhoneLabel = QtWidgets.QLabel(self.centralwidget)
        self.EnterPhoneLabel.setGeometry(QtCore.QRect(10, 210, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.EnterPhoneLabel.setFont(font)
        self.EnterPhoneLabel.setObjectName("EnterPhoneLabel")
        
        self.EnterPinLabel = QtWidgets.QLabel(self.centralwidget)
        self.EnterPinLabel.setGeometry(QtCore.QRect(10, 460, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.EnterPinLabel.setFont(font)
        self.EnterPinLabel.setObjectName("EnterPinLabel")
        self.EnterNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.EnterNameLabel.setGeometry(QtCore.QRect(10, 160, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(16)
        self.EnterNameLabel.setFont(font)
        self.EnterNameLabel.setObjectName("EnterNameLabel")
        
        self.DoneBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DoneBtn.setGeometry(QtCore.QRect(610, 460, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Kaushan Script")
        font.setPointSize(20)
        self.DoneBtn.setFont(font)
        self.DoneBtn.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.DoneBtn.setFlat(False)
        self.DoneBtn.setObjectName("DoneBtn")
        self.DoneBtn.clicked.connect(self.done_btn)
        
        self.EntryBar = QtWidgets.QProgressBar(self.centralwidget)
        self.EntryBar.setGeometry(QtCore.QRect(290, 600, 471, 31))
        self.EntryBar.setProperty("value", 24)
        self.EntryBar.setObjectName("EntryBar")
        
        self.ChangingLabel = QtWidgets.QLabel(self.centralwidget)
        self.ChangingLabel.setGeometry(QtCore.QRect(0, 580, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Bite Chocolate")
        font.setPointSize(14)
        self.ChangingLabel.setFont(font)
        self.ChangingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ChangingLabel.setObjectName("ChangingLabel")

        popup2=QMessageBox()
        popup2.setWindowTitle("Information!!")
        popup2.setText("How to edit: ")
        popup2.setInformativeText("1. Only change the details you want to edit\n2. If you want to change the PIN fill the field else leave it empty.")
        popup2.setIcon(QMessageBox.Information)
        popup2.setStandardButtons(QMessageBox.Ok)
        y=popup2.exec_()
        
        self.EditDetailsLabel.raise_()
        self.BankName.raise_()
        self.EnterEmailLabel.raise_()
        self.ReEnterPinLabel.raise_()
        self.ReEnterPinInput.raise_()
        self.EnterEmailInput.raise_()
        self.EnterAddInput.raise_()
        self.EnterAddLabel.raise_()
        self.CancelBtn.raise_()
        self.EnterPhoneLabel.raise_()
        self.EnterPinLabel.raise_()
        self.EnterNameLabel.raise_()
        self.EnterPhoneInput.raise_()
        self.EnterNameInput.raise_()
        self.EnterPinInput.raise_()
        self.DoneBtn.raise_()
        self.EntryBar.raise_()
        self.ChangingLabel.raise_()
        
        EditDetailsWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(EditDetailsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        EditDetailsWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(EditDetailsWindow)
        self.statusbar.setObjectName("statusbar")
        EditDetailsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EditDetailsWindow)
        QtCore.QMetaObject.connectSlotsByName(EditDetailsWindow)

        with open('C:/Program Files/accounts.json') as f:
            data=json.load(f)
        
        self.accountdetails=data['people'][self.num]
        self.name=self.accountdetails['name']
        self.EnterNameInput.setText(self.name)
        self.email=self.accountdetails['email']
        self.EnterEmailInput.setText(self.email)
        self.phn=self.accountdetails['phone']
        self.EnterPhoneInput.setText(str(self.phn))
        self.add=self.accountdetails['address']
        self.EnterAddInput.setText(str(self.add))

    def retranslateUi(self, EditDetailsWindow):
        
        _translate = QtCore.QCoreApplication.translate
        EditDetailsWindow.setWindowTitle(_translate("EditDetailsWindow", "Welcome to Avixion Bank Of Fraud"))
        self.EditDetailsLabel.setText(_translate("EditDetailsWindow", "Edit Details"))
        self.BankName.setText(_translate("EditDetailsWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#ffffff;\">AVIXION BANK OF FRAUD</span></p></body></html>"))
        self.EnterEmailLabel.setText(_translate("EditDetailsWindow", "Enter  E-mail Address:"))
        self.ReEnterPinLabel.setText(_translate("EditDetailsWindow", "Re-enter New PIN:"))
        self.EnterAddLabel.setText(_translate("EditDetailsWindow", "Enter  Address:"))
        self.CancelBtn.setText(_translate("EditDetailsWindow", "Cancel"))
        self.EnterPhoneLabel.setText(_translate("EditDetailsWindow", "Enter  Phone Number:"))
        self.EnterPinLabel.setText(_translate("EditDetailsWindow", "Enter New PIN:"))
        self.EnterNameLabel.setText(_translate("EditDetailsWindow", "Enter  Name:"))
        self.DoneBtn.setText(_translate("EditDetailsWindow", "Done"))
        self.ChangingLabel.setText(_translate("EditDetailsWindow", "Saving Edits..."))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     EditDetailsWindow = QtWidgets.QMainWindow()
#     ui = Ui_EditDetailsWindow()
#     ui.setupUi(EditDetailsWindow)
#     EditDetailsWindow.show()
#     sys.exit(app.exec_())
