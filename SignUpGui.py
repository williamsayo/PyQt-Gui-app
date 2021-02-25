from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QLineEdit, QMainWindow, QWidget
import qtawesome as qta
from db import Database
import os
import re

static = os.path.join(os.path.split(__file__)[0],'static')
cwd = os.path.split(__file__)[0]


class SignUp(QMainWindow):
    def __init__(self):
        super(SignUp,self).__init__()
        self.setupUi()
        self.invalid_color = 'red'
        self.valid_color = 'green'

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(400, 600)
        self.setWindowFlags( QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.signUp = QtWidgets.QFrame(self.centralwidget)
        self.signUp.setGeometry(QtCore.QRect(0, 0, 400, 600))
        self.signUp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.signUp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.signUp.setObjectName("signUp")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.signUp)
        self.verticalLayout.setObjectName("verticalLayout")

        self.details_container = QtWidgets.QFrame(self.signUp)
        self.details_container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.details_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.details_container.setObjectName("details_container")
        self.details = QtWidgets.QFrame(self.details_container)
        self.details.setGeometry(QtCore.QRect(100, 10, 200, 130))
        self.details.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.details.setFrameShadow(QtWidgets.QFrame.Raised)
        self.details.setObjectName("details")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.details)
        self.verticalLayout_3.setContentsMargins(-1, 2, -1, -1)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.register_label = QtWidgets.QLabel(self.details)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.register_label.setFont(font)
        self.register_label.setObjectName("register_label")

        self.verticalLayout_3.addWidget(self.register_label, 0, QtCore.Qt.AlignHCenter)

        self.socials = QtWidgets.QFrame(self.details)
        self.socials.setMinimumSize(QtCore.QSize(150, 50))
        self.socials.setMaximumSize(QtCore.QSize(150, 16777215))
        self.socials.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.socials.setFrameShadow(QtWidgets.QFrame.Raised)
        self.socials.setObjectName("socials")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.socials)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 9)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.facebook = QtWidgets.QLabel(self.socials)
        self.facebook.setTextFormat(QtCore.Qt.AutoText)
        self.facebook.setPixmap(QtGui.QPixmap(os.path.join(static,"images/1491579542-yumminkysocialmedia22_83078.png")))
        self.facebook.setScaledContents(True)
        self.facebook.setObjectName("facebook")

        self.horizontalLayout.addWidget(self.facebook)

        self.instagram = QtWidgets.QLabel(self.socials)
        self.instagram.setTextFormat(QtCore.Qt.AutoText)
        self.instagram.setPixmap(QtGui.QPixmap(os.path.join(static,"images/1491580635-yumminkysocialmedia26_83102.png")))
        self.instagram.setScaledContents(True)
        self.instagram.setObjectName("instagram")

        self.horizontalLayout.addWidget(self.instagram)

        self.twitter = QtWidgets.QLabel(self.socials)
        self.twitter.setTextFormat(QtCore.Qt.AutoText)
        self.twitter.setPixmap(QtGui.QPixmap(os.path.join(static,"images/facebook_icon-icons.com_59205.png")))
        self.twitter.setScaledContents(True)
        self.twitter.setObjectName("twitter")

        self.horizontalLayout.addWidget(self.twitter)

        self.verticalLayout_3.addWidget(self.socials, 0, QtCore.Qt.AlignHCenter)

        self.other_details_label = QtWidgets.QLabel(self.details)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.other_details_label.setFont(font)
        self.other_details_label.setObjectName("other_details_label")

        self.verticalLayout_3.addWidget(self.other_details_label)

        self.close_frame = QtWidgets.QFrame(self.details_container)
        self.close_frame.setGeometry(QtCore.QRect(330, -5, 60, 30))
        self.close_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.close_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.close_frame.setObjectName("close_frame")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.close_frame)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.shadow_minimize = QGraphicsDropShadowEffect()
        self.shadow_minimize.setBlurRadius(4)
        self.shadow_minimize.setOffset(1,1)
        self.shadow_minimize.setColor(QtGui.QColor(105,105,105))

        self.minimize_btn = QtWidgets.QPushButton(self.close_frame)
        self.minimize_btn.setGraphicsEffect(self.shadow_minimize)
        self.minimize_btn.setMinimumSize(QtCore.QSize(15, 15))
        self.minimize_btn.setMaximumSize(QtCore.QSize(15, 15))
        self.minimize_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimize_btn.setObjectName("minimize_btn")
        self.minimize_btn.clicked.connect(lambda: self.showMinimized())

        self.horizontalLayout_2.addWidget(self.minimize_btn)

        self.shadow_close = QGraphicsDropShadowEffect()
        self.shadow_close.setBlurRadius(4)
        self.shadow_close.setOffset(1,1)
        self.shadow_close.setColor(QtGui.QColor(105,105,105))

        self.close_btn = QtWidgets.QPushButton(self.close_frame)
        self.close_btn.setGraphicsEffect(self.shadow_close)
        self.close_btn.setMinimumSize(QtCore.QSize(15, 15))
        self.close_btn.setMaximumSize(QtCore.QSize(15, 15))
        self.close_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close_btn.setObjectName("close_btn")
        self.close_btn.clicked.connect(lambda: self.close())

        self.horizontalLayout_2.addWidget(self.close_btn)

        self.verticalLayout.addWidget(self.details_container)

        self.central_container = QtWidgets.QFrame(self.signUp)
        self.central_container.setMinimumSize(QtCore.QSize(0, 280))
        self.central_container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.central_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.central_container.setObjectName("central_container")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.central_container)
        self.verticalLayout_2.setContentsMargins(15, 5, 15, 5)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.first_name = QtWidgets.QLineEdit(self.central_container)
        self.first_name.addAction(qta.icon("mdi.format-text"),QLineEdit.LeadingPosition)
        self.first_name.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.first_name.setFont(font)
        self.first_name.setMaxLength(20)
        self.first_name.setClearButtonEnabled(True)
        self.first_name.setObjectName("first_name")

        self.verticalLayout_2.addWidget(self.first_name)

        self.last_name = QtWidgets.QLineEdit(self.central_container)
        self.last_name.addAction(qta.icon("mdi.format-text"),QLineEdit.LeadingPosition)
        self.last_name.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.last_name.setFont(font)
        self.last_name.setMaxLength(20)
        self.last_name.setClearButtonEnabled(True)
        self.last_name.setObjectName("last_name")

        self.verticalLayout_2.addWidget(self.last_name)

        self.username = QtWidgets.QLineEdit(self.central_container)
        self.username.setMinimumSize(QtCore.QSize(0, 35))
        self.username.addAction(qta.icon("fa.user-circle-o"),QLineEdit.LeadingPosition)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setMaxLength(20)
        self.username.setObjectName("username")
        self.username.textChanged.connect(lambda: self.ValidateUsername())

        self.verticalLayout_2.addWidget(self.username)

        self.email = QtWidgets.QLineEdit(self.central_container)
        self.email.addAction(qta.icon("mdi.email-outline"),QLineEdit.LeadingPosition)
        self.email.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.email.setFont(font)
        self.email.setMaxLength(50)
        self.email.setObjectName("email")
        self.email.textChanged.connect(lambda: self.validateEmail())

        self.verticalLayout_2.addWidget(self.email)

        self.password1 = QtWidgets.QLineEdit(self.central_container)
        self.password1.addAction(qta.icon("mdi.account-lock-outline"),QLineEdit.LeadingPosition)
        self.password1.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.password1.setFont(font)
        self.password1.setMaxLength(25)
        self.password1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password1.setObjectName("password1")
        self.password1.textChanged.connect(lambda: self.validatePassword())

        self.verticalLayout_2.addWidget(self.password1)

        self.password2 = QtWidgets.QLineEdit(self.central_container)
        self.password2.addAction(qta.icon("mdi.account-lock-outline"),QLineEdit.LeadingPosition)
        self.password2.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.password2.setFont(font)
        self.password2.setMaxLength(25)
        self.password2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password2.setObjectName("password2")
        self.password2.textChanged.connect(lambda: self.validatePassword())

        self.verticalLayout_2.addWidget(self.password2)
        self.verticalLayout.addWidget(self.central_container)

        self.footer_container = QtWidgets.QFrame(self.signUp)
        self.footer_container.setStyleSheet("")
        self.footer_container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.footer_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_container.setObjectName("footer_container")

        self.terms_and_conditions = QtWidgets.QCheckBox(self.footer_container)
        self.terms_and_conditions.setGeometry(QtCore.QRect(30, 0, 230, 17))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.terms_and_conditions.setFont(font)
        self.terms_and_conditions.setObjectName("terms_and_conditions")

        self.shadow_register = QGraphicsDropShadowEffect()
        self.shadow_register.setBlurRadius(15)
        self.shadow_register.setOffset(5,5)
        self.shadow_register.setColor(QtGui.QColor(105,105,105))

        self.register_btn = QtWidgets.QPushButton(self.footer_container)
        self.register_btn.setGraphicsEffect(self.shadow_register)
        self.register_btn.setGeometry(QtCore.QRect(110, 85, 180, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(14)
        self.register_btn.setFont(font)
        self.register_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.register_btn.setObjectName("register_btn")
        self.register_btn.clicked.connect(self.createUser)

        self.verticalLayout.addWidget(self.footer_container)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        with open(os.path.join(static,'qss/signup.qss'),'r') as sheet:
            self.setStyleSheet(sheet.read())

        self.initPosition = self.pos()
        self.show()

    def ValidateUsername(self):
        username = self.username.text()
        username = username.rstrip()

        database = Database()
        users = database.UserValidation(username)

        if len(self.username.actions()) > 1:self.username.removeAction(self.username.actions()[1])

        if users:
            if len(username) > 0:
                self.username.addAction(qta.icon("mdi.close-circle-outline",color=self.invalid_color),QLineEdit.TrailingPosition)
        
        else:
            self.username.addAction(qta.icon("fa5s.check",color=self.valid_color),QLineEdit.TrailingPosition)
            self.validUsername = True
            return 

        self.validUsername = False

    def validateEmail(self):
        email = self.email.text()
        email_format = re.search(r'[\w.%_]{1,20}@\w{2,20}\.[a-zA-Z]{2,3}',str(email))

        if len(self.email.actions()) > 1:self.email.removeAction(self.email.actions()[1])

        if email_format:
            self.email.addAction(qta.icon("fa5s.check",color=self.valid_color),QLineEdit.TrailingPosition)
            self.validEmail = True
            return
        else:
            if len(email):
                self.email.addAction(qta.icon("mdi.close-circle-outline",color=self.invalid_color),QLineEdit.TrailingPosition)

        self.validEmail = False

    def validatePassword(self):
        password1 = self.password1.text()
        password2 = self.password2.text()
        password_format = re.search('(?=.*[a-z])(?=.*[0-9])(?=.*[a-z0-9]{8,20})',password1)

        if len(self.password1.actions()) > 1:self.password1.removeAction(self.password1.actions()[1])
        if len(self.password2.actions()) > 1:self.password2.removeAction(self.password2.actions()[1])

        if password_format:
            self.password1.addAction(qta.icon("fa5s.check",color=self.valid_color),QLineEdit.TrailingPosition)
            if password1 == password2:
                self.password2.addAction(qta.icon("fa5s.check",color=self.valid_color),QLineEdit.TrailingPosition)
                self.validPassword = True
                return
            elif len(password2) > 0:
                self.password2.addAction(qta.icon("mdi.close-circle-outline",color=self.invalid_color),QLineEdit.TrailingPosition)
        else:
            if len(password1) > 0:
                self.password1.addAction(qta.icon("mdi.close-circle-outline",color=self.invalid_color),QLineEdit.TrailingPosition)
            if len(password2) > 0:
                self.password2.addAction(qta.icon("mdi.close-circle-outline",color=self.invalid_color),QLineEdit.TrailingPosition)

        self.validPassword = False

    def createUser(self):
        first_name = self.first_name.text()
        last_name = self.last_name.text()
        username = self.username.text()
        email = self.email.text()
        password1 = self.password1.text()


        text_format = re.search('.+',first_name and last_name and username)

        if text_format and self.validEmail and self.validPassword and self.validUsername:
            database = Database()
            database.createUser(first_name,last_name,username,email,password1)
        
            self.first_name.setText('')
            self.last_name.setText('')
            self.username.setText('')
            self.email.setText('')
            self.password1.setText('')
            self.password2.setText('')

    def mousePressEvent(self, event):
        self.initPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.initPosition)
        self.move(self.pos().x() + delta.x() , self.pos().y() + delta.y())
        self.initPosition = event.globalPos()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.register_label.setText(_translate("MainWindow", "Register"))
        self.other_details_label.setText(_translate("MainWindow", "or be classical"))
        self.first_name.setPlaceholderText(_translate("MainWindow", "First Name..."))
        self.last_name.setPlaceholderText(_translate("MainWindow", "Last Name..."))
        self.username.setPlaceholderText(_translate("MainWindow", "Username..."))
        self.email.setPlaceholderText(_translate("MainWindow", "Your Email..."))
        self.password1.setPlaceholderText(_translate("MainWindow", "Password..."))
        self.password2.setPlaceholderText(_translate("MainWindow", "Confirm Password..."))
        self.terms_and_conditions.setText(_translate("MainWindow", "I agree to the terms and conditions."))
        self.register_btn.setText(_translate("MainWindow", "Get Started"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registration = SignUp()
    sys.exit(app.exec_())