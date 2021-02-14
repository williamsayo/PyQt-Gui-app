from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QMainWindow
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QDesktopServices as browser
import qtawesome as qta
import os

static = os.path.join(os.path.split(__file__)[0],'static')

class LandingWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LandingWindow,self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(451, 246)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.body = QtWidgets.QFrame(self.centralwidget)
        self.body.setGeometry(QtCore.QRect(0, 0, 451, 246))
        self.body.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")

        self.header = QtWidgets.QLabel(self.body)
        self.header.setGeometry(QtCore.QRect(160, 20, 141, 45))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setObjectName("header")

        self.progressBar = QtWidgets.QProgressBar(self.body)
        self.progressBar.setGeometry(QtCore.QRect(40, 150, 391, 23))
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 50)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")

        self.creators = QtWidgets.QLabel(self.body)
        self.creators.setGeometry(QtCore.QRect(300, 225, 150, 15))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.creators.setFont(font)
        self.creators.setObjectName("creators")

        self.description = QtWidgets.QLabel(self.body)
        self.description.setGeometry(QtCore.QRect(100, 60, 270, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.description.setFont(font)
        self.description.setObjectName("description")

        self.label = QtWidgets.QLabel(self.body)
        self.label.setGeometry(QtCore.QRect(175, 180, 70, 25))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.setCentralWidget(self.centralwidget)

        # box shadow

        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(2)
        self.shadow.setYOffset(2)
        self.shadow.setColor(QtGui.QColor(0,0,0,60))
        self.body.setGraphicsEffect(self.shadow)

        # timer on the progress bar

        self.progressBar.setValue(0) 
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        # timer in ms
        self.timer.start(15)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        with open(os.path.join(static,'qss/landing.qss'),'r') as stylesheet:
            self.setStyleSheet(stylesheet.read())
        self.show( )


    def progress(self):
        self.progressBar.setValue(self.progressBar.value() + 1)

        if self.progressBar.value() >= 100:
            self.timer.stop()

            login = LoginWindow()
            login.show()

            self.close()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "CODEY TECH"))
        self.creators.setText(_translate("MainWindow", "created Mike & Ayo"))
        self.description.setText(_translate("MainWindow", "A Chat And File Transfer App"))
        self.label.setText(_translate("MainWindow", "Loading..."))


class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow,self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.resize(400, 560)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.login_frame = QtWidgets.QFrame(self)
        self.login_frame.setGeometry(QtCore.QRect(0, 0, 400, 560))
        self.login_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.login_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_frame.setObjectName("login_frame")
        self.login_frame_layout = QtWidgets.QVBoxLayout(self.login_frame)
        self.login_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.login_frame_layout.setObjectName("login_frame_layout")

        self.title_frame = QtWidgets.QFrame(self.login_frame)
        self.title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_frame.setObjectName("title_frame")

        self.title_content = QtWidgets.QFrame(self.title_frame)
        self.title_content.setGeometry(QtCore.QRect(125, 20, 250, 183))
        self.title_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_content.setObjectName("title_content")

        self.titleLabel = QtWidgets.QLabel(self.title_content)
        self.titleLabel.setGeometry(QtCore.QRect(0, 130, 170, 40))
        self.titleLabel.setObjectName("titleLabel")

        self.imageLabel = QtWidgets.QLabel(self.title_content)
        self.imageLabel.setGeometry(QtCore.QRect(-100, 20, 351, 111))
        self.imageLabel.setPixmap(QtGui.QPixmap(os.path.join(static,"images/blog-wp-login.png")))
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setObjectName("imageLabel")

        self.closeBtn = QtWidgets.QPushButton(self.title_frame)
        self.closeBtn.setGeometry(QtCore.QRect(370, 10, 25, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.closeBtn.setFont(font)
        self.closeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeBtn.clicked.connect(lambda: self.close())
        self.closeBtn.setIconSize(QtCore.QSize(16, 16))
        self.closeBtn.setObjectName("closeBtn")

        self.login_frame_layout.addWidget(self.title_frame)

        self.content_frame = QtWidgets.QFrame(self.login_frame)
        self.content_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_frame.setObjectName("content_frame")

        self.usernameEntry = QtWidgets.QLineEdit(self.content_frame)
        self.usernameEntry.addAction(qta.icon("fa5.user-circle"),QLineEdit.TrailingPosition)
        self.usernameEntry.setGeometry(QtCore.QRect(25, 30, 350, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell condensed")
        font.setPointSize(12)
        self.usernameEntry.setFont(font)
        self.usernameEntry.setObjectName("usernameEntry")
        self.usernameEntry.setMaxLength(20)

        self.passwordEntry = QtWidgets.QLineEdit(self.content_frame)
        self.passwordEntry.addAction(qta.icon("mdi.account-lock-outline"),QLineEdit.TrailingPosition)
        self.passwordEntry.setGeometry(QtCore.QRect(25, 90, 350, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell condensed")
        font.setPointSize(12)
        self.passwordEntry.setFont(font)
        self.passwordEntry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEntry.setObjectName("passwordEntry")
        self.passwordEntry.setMaxLength(20)

        self.rememberMe = QtWidgets.QCheckBox(self.content_frame)
        self.rememberMe.setGeometry(QtCore.QRect(30, 140, 110, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rememberMe.setFont(font)
        self.rememberMe.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rememberMe.setObjectName("rememberMe")

        self.login_frame_layout.addWidget(self.content_frame)

        self.footer_frame = QtWidgets.QFrame(self.login_frame)
        self.footer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_frame.setObjectName("footer_frame")

        self.login = QtWidgets.QPushButton(self.footer_frame)
        options = [{'scale-factor':1.5,'color':'#fff','color_active':'black'}]
        self.login.setIcon(qta.icon("mdi.login",options=options))
        self.login.setGeometry(QtCore.QRect(275, 0, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.login.setFont(font)
        self.login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login.setAutoFillBackground(False)
        self.login.setObjectName("login")

        self.signup = QtWidgets.QPushButton(self.footer_frame)
        self.signup.setIcon(qta.icon("fa.user-plus",options=options))
        self.signup.setGeometry(QtCore.QRect(130, 0, 135, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.signup.setFont(font)
        self.signup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signup.setAutoFillBackground(False)
        self.signup.setObjectName("signup")

        self.sociaIs_frame = QtWidgets.QFrame(self.footer_frame)
        self.sociaIs_frame.setGeometry(QtCore.QRect(225, 120, 138, 45))
        self.sociaIs_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sociaIs_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sociaIs_frame.setObjectName("sociaIs_frame")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.sociaIs_frame)
        self.horizontalLayout.setContentsMargins(2, 7, 2, -1)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.instagram = QtWidgets.QLabel(self.sociaIs_frame)
        self.instagram.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.instagram.setPixmap(QtGui.QPixmap(os.path.join(static,"images/1491580635-yumminkysocialmedia26_83102.png")))
        self.instagram.setScaledContents(True)
        self.instagram.setObjectName("instagram")
        self.instagram.mouseReleaseEvent = self.openInstagram

        self.horizontalLayout.addWidget(self.instagram)

        self.youtube = QtWidgets.QLabel(self.sociaIs_frame)
        self.youtube.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.youtube.setPixmap(QtGui.QPixmap(os.path.join(static,"images/1491580651-yumminkysocialmedia28_83061.png")))
        self.youtube.setScaledContents(True)
        self.youtube.setObjectName("youtube")
        self.youtube.mouseReleaseEvent = self.openYoutube

        self.horizontalLayout.addWidget(self.youtube)

        self.facebook = QtWidgets.QLabel(self.sociaIs_frame)
        self.facebook.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.facebook.setPixmap(QtGui.QPixmap(os.path.join(static,"images/facebook_icon-icons.com_59205.png")))
        self.facebook.setScaledContents(True)
        self.facebook.setObjectName("facebook")
        self.facebook.mouseReleaseEvent = self.openFacebook

        self.horizontalLayout.addWidget(self.facebook)

        self.twitter = QtWidgets.QLabel(self.sociaIs_frame)
        self.twitter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.twitter.setPixmap(QtGui.QPixmap(os.path.join(static,"images/1491579542-yumminkysocialmedia22_83078.png")))
        self.twitter.setScaledContents(True)
        self.twitter.setObjectName("twitter")
        self.twitter.mouseReleaseEvent = self.openTwitter

        self.horizontalLayout.addWidget(self.twitter)

        self.login_frame_layout.addWidget(self.footer_frame)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        with open(os.path.join(static,'qss/login.qss'),'r') as stylesheet:
            self.setStyleSheet(stylesheet.read())
        self.show()

    def openInstagram(self, event):
            browser.openUrl(QtCore.QUrl("https://www.instagram.com/williamsayo44/"))
    def openYoutube(self, event):
            browser.openUrl(QtCore.QUrl("https://www.youtube.com"))
    def openFacebook(self, event):
            browser.openUrl(QtCore.QUrl("https://www.facebook.com"))
    def openTwitter(self, event):
            browser.openUrl(QtCore.QUrl("https://www.twitter.com"))


    def mousePressEvent(self, event):
        self.initPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.initPosition)
        self.move(self.pos().x() + delta.x() , self.pos().y() + delta.y())
        self.initPosition = event.globalPos()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLabel.setText(_translate("MainWindow", "LogIn Security"))
        self.closeBtn.setText(_translate("MainWindow", "x"))
        self.usernameEntry.setPlaceholderText(_translate("MainWindow", "Username"))
        self.passwordEntry.setPlaceholderText(_translate("MainWindow", "Password"))
        self.rememberMe.setText(_translate("MainWindow", "Remember Me"))
        self.login.setText(_translate("MainWindow", "LogIn"))
        self.signup.setText(_translate("MainWindow", "Create New Account "))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    landing = LandingWindow()
    sys.exit(app.exec_())
