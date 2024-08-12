# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import re



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 847)
        MainWindow.setStyleSheet("background-color: rgb(36, 31, 49)")
        MainWindow.setDocumentMode(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.textBrowser = QtWidgets.QTextBrowser(parent=self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(90, 30, 401, 131))
        self.textBrowser.setStyleSheet("background-color: rgb(97, 53, 131)")
        self.textBrowser.setObjectName("textBrowser")

        self.Username_field = QtWidgets.QFrame(parent=self.frame)
        self.Username_field.setGeometry(QtCore.QRect(40, 200, 471, 91))
        self.Username_field.setStyleSheet("border: none;")
        self.Username_field.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Username_field.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Username_field.setObjectName("Username_field")

        self.field = QtWidgets.QLineEdit(parent=self.Username_field)
        self.field.setGeometry(QtCore.QRect(10, 20, 451, 31))
        self.field.setStyleSheet("background-color: rgb(48, 25, 99)")
        self.field.setText("")
        self.field.setClearButtonEnabled(False)
        self.field.setObjectName("field")

        self.ErrorTextEdit = QtWidgets.QPlainTextEdit(parent=self.Username_field)
        self.ErrorTextEdit.setEnabled(False)
        self.ErrorTextEdit.setGeometry(QtCore.QRect(10, 50, 451, 41))
        self.ErrorTextEdit.setAcceptDrops(True)
        self.ErrorTextEdit.setAutoFillBackground(False)
        self.ErrorTextEdit.setStyleSheet("color: rgb(165, 29, 45);\n"
"font: 75 italic 8pt \"Ubuntu\";\n"
"border: none;")
        self.ErrorTextEdit.setLineWidth(0)
        self.ErrorTextEdit.setReadOnly(True)
        self.ErrorTextEdit.setPlainText("")
        self.ErrorTextEdit.setOverwriteMode(True)
        self.ErrorTextEdit.setBackgroundVisible(False)
        self.ErrorTextEdit.setObjectName("ErrorTextEdit")

        self.email_field = QtWidgets.QFrame(parent=self.frame)
        self.email_field.setGeometry(QtCore.QRect(40, 310, 471, 91))
        self.email_field.setStyleSheet("border: none;")
        self.email_field.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.email_field.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.email_field.setObjectName("email_field")

        self.ErrorTextEdit_2 = QtWidgets.QPlainTextEdit(parent=self.email_field)
        self.ErrorTextEdit_2.setGeometry(QtCore.QRect(10, 50, 451, 41))
        self.ErrorTextEdit_2.setAutoFillBackground(False)
        self.ErrorTextEdit_2.setStyleSheet("color: rgb(165, 29, 45);\n"
"font: 75 italic 8pt \"Ubuntu\";\n"
"border: none;")
        self.ErrorTextEdit_2.setReadOnly(True)
        self.ErrorTextEdit_2.setPlainText("")
        self.ErrorTextEdit_2.setOverwriteMode(True)
        self.ErrorTextEdit_2.setBackgroundVisible(False)
        self.ErrorTextEdit_2.setObjectName("ErrorTextEdit_2")

        self.field_2 = QtWidgets.QLineEdit(parent=self.email_field)
        self.field_2.setGeometry(QtCore.QRect(10, 20, 451, 31))
        self.field_2.setStyleSheet("background-color: rgb(48, 25, 99);")
        self.field_2.setText("")
        self.field_2.setClearButtonEnabled(False)
        self.field_2.setObjectName("field_2")

        self.psswrd_field = QtWidgets.QFrame(parent=self.frame)
        self.psswrd_field.setGeometry(QtCore.QRect(39, 419, 471, 131))
        self.psswrd_field.setStyleSheet("border: none;")
        self.psswrd_field.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.psswrd_field.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.psswrd_field.setObjectName("psswrd_field")

        self.field_3 = QtWidgets.QLineEdit(parent=self.psswrd_field)
        self.field_3.setGeometry(QtCore.QRect(10, 10, 451, 31))
        self.field_3.setStyleSheet("background-color: rgb(48, 25, 99)")
        self.field_3.setText("")
        self.field_3.setClearButtonEnabled(False)
        self.field_3.setObjectName("field_3")

        self.field_4 = QtWidgets.QLineEdit(parent=self.psswrd_field)
        self.field_4.setGeometry(QtCore.QRect(10, 50, 451, 31))
        self.field_4.setStyleSheet("background-color: rgb(48, 25, 99)")
        self.field_4.setText("")
        self.field_4.setClearButtonEnabled(False)
        self.field_4.setObjectName("field_4")

        self.ErrorTextEdit_3 = QtWidgets.QPlainTextEdit(parent=self.psswrd_field)
        self.ErrorTextEdit_3.setGeometry(QtCore.QRect(10, 90, 451, 41))
        self.ErrorTextEdit_3.setAutoFillBackground(False)
        self.ErrorTextEdit_3.setStyleSheet("color: rgb(165, 29, 45);\n"
"font: 75 italic 8pt \"Ubuntu\";\n"
"border: none;")
        self.ErrorTextEdit_3.setReadOnly(True)
        self.ErrorTextEdit_3.setPlainText("")
        self.ErrorTextEdit_3.setOverwriteMode(True)
        self.ErrorTextEdit_3.setBackgroundVisible(False)
        self.ErrorTextEdit_3.setObjectName("ErrorTextEdit_3")

        self.change_create_user = QtWidgets.QFrame(parent=self.frame)
        self.change_create_user.setGeometry(QtCore.QRect(30, 550, 471, 51))
        self.change_create_user.setStyleSheet("border: none;")
        self.change_create_user.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.change_create_user.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.change_create_user.setObjectName("change_create_user")

        self.createbutton = QtWidgets.QPushButton(parent=self.change_create_user)
        self.createbutton.setGeometry(QtCore.QRect(10, 10, 191, 31))
        self.createbutton.setStyleSheet("background-color: rgb(38, 13, 80);")
        self.createbutton.setObjectName("createbutton")
        self.createbutton.clicked.connect(self.create_account)

        self.ad_field = QtWidgets.QFrame(parent=self.frame)
        self.ad_field.setGeometry(QtCore.QRect(50, 600, 451, 211))
        self.ad_field.setStyleSheet("border: none;")
        self.ad_field.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.ad_field.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ad_field.setObjectName("ad_field")

        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(220, 170, 141, 17))
        self.label.setStyleSheet("color:rgb(154, 153, 150);\n"
        
"font: 75 16pt \"Ubuntu\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:600; color:#241f31;\">Create user </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:600; color:#241f31;\">or</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:600; color:#241f31;\">Start Sesion</span></p></body></html>"))
        self.field.setPlaceholderText(_translate("MainWindow", "Username"))
        self.field_2.setPlaceholderText(_translate("MainWindow", "Email"))
        self.field_3.setPlaceholderText(_translate("MainWindow", "Password"))
        self.field_4.setPlaceholderText(_translate("MainWindow", "Confirm Password"))
        self.createbutton.setText(_translate("MainWindow", "Create User."))
        self.label.setText(_translate("MainWindow", "Create account"))
    
    def create_account(self):
        def usernameParams(self):
                noAvailableCharacters = "^[a-zA-Z0-9]*$"
                minLen, maxLen = 2, 20 
                username = self.field.text()
                if len(username) < minLen or len(username) > maxLen or not re.match(noAvailableCharacters, username):
                    self.ErrorTextEdit.setPlainText("Username must be between " + str(minLen) + "-" + str(maxLen) + ', username shouldnt have characters: '+ noAvailableCharacters + 'please use other username.')
                    return False
                else:
                    self.ErrorTextEdit.setPlainText("")
                    return username
                
        def emailParams(self):
                validateEmail = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
                emailDirection = self.field_2.text()
                if not re.match(validateEmail, emailDirection):
                    self.ErrorTextEdit_2.setPlainText("This email not have a domain")
                    return False
                else:
                    self.ErrorTextEdit_2.setPlainText("")
                    return emailDirection
                
        def passwordConfirm(self):
                password = self.field_3.text()
                confirm = self.field_4.text()
                if password is None:
                    self.ErrorTextEdit_3.setPlainText("Password is empty")
                    return False
                if password != confirm:
                    self.ErrorTextEdit_3.setPlainText("Passwords dont match, please try again")
                    return False
                else:
                    self.ErrorTextEdit_3.setPlainText("")
                    return password
                
        username = usernameParams(self)
        email = emailParams(self)
        psswrd = passwordConfirm(self)
        from conection3 import addUser 
        try:
            addUser(username, email, psswrd)
            self.ErrorTextEdit_3.setPlainText("User created successfully")
        except Exception as e:
            print(f'error: {e}')

             



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())