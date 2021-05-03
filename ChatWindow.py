from PyQt5.QtWidgets import QMainWindow, QMenu, QSizePolicy, QSystemTrayIcon
from PyQt5 import QtCore, QtGui, QtWidgets
import qtawesome as qta
import os
import socket
import threading
from random import randrange
from win10toast import ToastNotifier

static = os.path.join(os.path.split(__file__)[0],'static')
cwd = os.path.split(__file__)[0]
media = os.path.join(cwd,'media')

host = socket.gethostbyname(socket.gethostname())
port = 2424

username = input("Enter a username for the chatroom: ")
time = QtCore.QDateTime.currentDateTime().toString("h:mm ap")

class ThreadClass(QtCore.QThread):
    any_signal = QtCore.pyqtSignal(str)
    def __init__(self, parent=None,info=''):
        super(ThreadClass,self).__init__(parent)
        self.info = info
        self.is_running = True

    def run(self):
        self.any_signal.emit(self.info)

class ChatScreen(QMainWindow):

    def __init__(self,host,port,username):
        super(ChatScreen,self).__init__()
        self.setupUi()
        self.systemTray()
        self.username = username
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect((host,port))
        self.notifier = ToastNotifier()

        t1 = threading.Thread(target=self.receive_message)
        t1.start()

    def receive_message(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8') 
                if message == 'username':
                    self.client.send(self.username.encode('utf-8'))
                else:
                    self.thread = ThreadClass(parent=None,info=message)
                    self.thread.start()
                    self.thread.any_signal.connect(self.receiveMessage)
        
            except:
                self.client.close()
                print( f'You have left the chatroom!')
                break

    def systemTray(self):
        self.trayIcon = QSystemTrayIcon(QtGui.QIcon(os.path.join(static,'images/conversation_icon.ico')),parent=self)
        self.trayIcon.setToolTip("Quickchat messenger")
        self.trayIcon.messageClicked.connect(self.showNormal)

        self.trayIcon.show()

        self.menu = QMenu()
        openAction = self.menu.addAction(qta.icon("fa5.smile-wink"),"Quickchat messenger")
        openAction.triggered.connect(self.showNormal)
        exitAction = self.menu.addAction(qta.icon("mdi.exit-run"),"Exit")
        exitAction.triggered.connect(self.closeWindow)

        self.trayIcon.setContextMenu(self.menu)

    def setupUi(self):
        white = "#fff"
        self.setObjectName("MainWindow")
        self.resize(866, 568)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setMinimumSize(QtCore.QSize(650, 470))
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.windowFrame = QtWidgets.QFrame(self.centralwidget)
        self.windowFrame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.windowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.windowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.windowFrame.setObjectName("windowFrame")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.windowFrame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.closeFrame = QtWidgets.QFrame(self.windowFrame)
        self.closeFrame.setMinimumSize(QtCore.QSize(100, 0))
        self.closeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.closeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.closeFrame.setObjectName("closeFrame")

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.closeFrame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.minimizeBtn = QtWidgets.QPushButton(self.closeFrame)
        self.minimizeBtn.setMinimumSize(QtCore.QSize(15, 15))
        self.minimizeBtn.setMaximumSize(QtCore.QSize(15, 15))
        self.minimizeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimizeBtn.setObjectName("minimizeBtn")
        self.minimizeBtn.clicked.connect(lambda : self.showMinimized())

        self.horizontalLayout_5.addWidget(self.minimizeBtn)

        self.maximizeBtn = QtWidgets.QPushButton(self.closeFrame)
        self.maximizeBtn.setMinimumSize(QtCore.QSize(15, 15))
        self.maximizeBtn.setMaximumSize(QtCore.QSize(15, 15))
        self.maximizeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.maximizeBtn.setObjectName("maximizeBtn")
        self.maximizeBtn.clicked.connect(lambda : self.maximizeFunc())

        self.horizontalLayout_5.addWidget(self.maximizeBtn)

        self.closeBtn = QtWidgets.QPushButton(self.closeFrame)
        self.closeBtn.setMinimumSize(QtCore.QSize(15, 15))
        self.closeBtn.setMaximumSize(QtCore.QSize(15, 15))
        self.closeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeBtn.setObjectName("closeBtn")
        self.closeBtn.clicked.connect(lambda : self.closeWindow())

        self.horizontalLayout_5.addWidget(self.closeBtn)
        self.horizontalLayout_4.addWidget(self.closeFrame, 0, QtCore.Qt.AlignRight)

        self.verticalLayout_3.addWidget(self.windowFrame)

        self.headerContainer = QtWidgets.QFrame(self.centralwidget)
        self.headerContainer.setMaximumSize(QtCore.QSize(16777215, 50))
        self.headerContainer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.headerContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerContainer.setObjectName("headerContainer")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.headerContainer)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.chatName = QtWidgets.QPushButton(self.headerContainer)
        self.chatName.setIconSize(QtCore.QSize(50,40))
        self.chatName.setIcon(qta.icon("fa5.smile-wink",color=white))
        self.chatName.setMinimumSize(QtCore.QSize(130, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.chatName.setFont(font)
        self.chatName.setObjectName("chatName")

        self.horizontalLayout_2.addWidget(self.chatName)

        self.leaveBtn = QtWidgets.QPushButton(self.headerContainer)
        self.leaveBtn.setIconSize(QtCore.QSize(25,21))
        self.leaveBtn.setIcon(qta.icon("mdi.exit-run",color=white))
        self.leaveBtn.setMinimumSize(QtCore.QSize(120, 30))
        self.leaveBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.leaveBtn.clicked.connect(lambda: self.closeWindow())
        self.leaveBtn.setObjectName("leaveBtn")

        self.horizontalLayout_2.addWidget(self.leaveBtn, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.headerContainer)

        self.bodyContainer = QtWidgets.QFrame(self.centralwidget)
        self.bodyContainer.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.bodyContainer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bodyContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bodyContainer.setObjectName("bodyContainer")

        self.bodyLayout = QtWidgets.QHBoxLayout(self.bodyContainer)
        self.bodyLayout.setContentsMargins(0, 0, 0, 0)
        self.bodyLayout.setSpacing(0)
        self.bodyLayout.setObjectName("bodyLayout")

        self.side_bar = QtWidgets.QFrame(self.bodyContainer)
        self.side_bar.setMaximumSize(QtCore.QSize(273, 16777215))
        
        self.side_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_bar.setObjectName("side_bar")

        self.side_barLayout = QtWidgets.QVBoxLayout(self.side_bar)
        self.side_barLayout.setContentsMargins(0, 0, 0, 0)
        self.side_barLayout.setSpacing(0)
        self.side_barLayout.setObjectName("side_barLayout")

        self.side_bar_box = QtWidgets.QFrame(self.side_bar)
        self.side_bar_box.setMinimumSize(QtCore.QSize(0, 100))
        self.side_bar_box.setMaximumSize(QtCore.QSize(16777215, 500))
        self.side_bar_box.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_bar_box.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_bar_box.setObjectName("side_bar_box")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.side_bar_box)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.roomContainer = QtWidgets.QFrame(self.side_bar_box)
        self.roomContainer.setMinimumSize(QtCore.QSize(0, 100))
        self.roomContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.roomContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.roomContainer.setObjectName("roomContainer")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.roomContainer)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.roomtitleContainer = QtWidgets.QFrame(self.roomContainer)
        self.roomtitleContainer.setMaximumSize(QtCore.QSize(16777215, 50))
        self.roomtitleContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.roomtitleContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.roomtitleContainer.setObjectName("roomtitleContainer")

        self.roomTitle = QtWidgets.QPushButton(self.roomtitleContainer)
        self.roomTitle.setIcon(qta.icon("fa.wechat",color=white))
        self.roomTitle.setGeometry(QtCore.QRect(15, 0, 250, 50))
        self.roomTitle.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.roomTitle.setFont(font)
        self.roomTitle.setObjectName("roomTitle")

        self.verticalLayout_2.addWidget(self.roomtitleContainer)

        self.roomName = QtWidgets.QFrame(self.roomContainer)
        self.roomName.setMinimumSize(QtCore.QSize(0, 50))
        self.roomName.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.roomName.setFrameShadow(QtWidgets.QFrame.Raised)
        self.roomName.setObjectName("roomName")
        
        self.room = QtWidgets.QLabel(self.roomName)
        self.room.setGeometry(QtCore.QRect(15, 0, 250, 50))
        self.room.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.room.setFont(font)
        self.room.setObjectName("room")

        self.verticalLayout_2.addWidget(self.roomName)

        self.verticalLayout.addWidget(self.roomContainer)

        self.usersContainer = QtWidgets.QFrame(self.side_bar_box)
        self.usersContainer.setMinimumSize(QtCore.QSize(0, 100))
        self.usersContainer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.usersContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.usersContainer.setObjectName("usersContainer")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.usersContainer)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.userstitleContainer = QtWidgets.QFrame(self.usersContainer)
        self.userstitleContainer.setMaximumSize(QtCore.QSize(16777215, 50))
        self.userstitleContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userstitleContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userstitleContainer.setObjectName("userstitleContainer")

        self.usersTitle = QtWidgets.QPushButton(self.userstitleContainer)
        self.usersTitle.setIcon(qta.icon("fa.users",color=white))
        self.usersTitle.setGeometry(QtCore.QRect(15, 0, 250, 50))
        self.usersTitle.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.usersTitle.setFont(font)
        self.usersTitle.setObjectName("usersTitle")

        self.verticalLayout_4.addWidget(self.userstitleContainer)

        self.usersName = QtWidgets.QFrame(self.usersContainer)
        self.usersName.setStyleSheet("padding-bottom:30px;")
        self.usersName.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.usersName.setFrameShadow(QtWidgets.QFrame.Raised)
        self.usersName.setObjectName("usersName")

        self.user = QtWidgets.QLabel(self.usersName)
        self.user.setGeometry(QtCore.QRect(15, 0, 250, 50))
        self.user.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.user.setFont(font)
        self.user.setObjectName("user")

        self.verticalLayout_4.addWidget(self.usersName)
        self.verticalLayout.addWidget(self.usersContainer)

        self.side_barLayout.addWidget(self.side_bar_box, 0, QtCore.Qt.AlignTop)

        self.bodyLayout.addWidget(self.side_bar)

        self.chatScreen = QtWidgets.QScrollArea(self.bodyContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatScreen.sizePolicy().hasHeightForWidth())
        self.chatScreen.setSizePolicy(sizePolicy)
        self.chatScreen.setMinimumSize(QtCore.QSize(500, 0))
        self.chatScreen.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.chatScreen.setWidgetResizable(True)
        self.chatScreen.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)

        self.chatScreen.setMinimumSize(QtCore.QSize(500, 0))
        self.chatScreen.setFrameShape(QtWidgets.QFrame.Panel)
        self.chatScreen.setFrameShadow(QtWidgets.QFrame.Plain)
        self.chatScreen.setObjectName("chatScreen")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1076, 638))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.chatsFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.chatsFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.chatsFrame.setBaseSize(QtCore.QSize(600, 50))
        self.chatsFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.chatsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chatsFrame.setObjectName("chatsFrame")

        self.chatsFrame_layout = QtWidgets.QVBoxLayout(self.chatsFrame)
        self.chatsFrame_layout.setSpacing(10)
        self.chatsFrame_layout.setObjectName("chatsFrame_layout")

        self.receivedMessageContainer = QtWidgets.QFrame(self.chatsFrame)
        self.receivedMessageContainer.setBaseSize(QtCore.QSize(200, 50))
        self.receivedMessageContainer.setMinimumSize(QtCore.QSize(100, 50))
        self.receivedMessageContainer.setMaximumSize(QtCore.QSize(600, 1657750))
        self.receivedMessageContainer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.receivedMessageContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.receivedMessageContainer.setObjectName("receivedMessageContainer")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.receivedMessageContainer)
        self.horizontalLayout_3.setContentsMargins(5, 2, 0, 2)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.profilePic = QtWidgets.QLabel(self.receivedMessageContainer)
        self.profilePic.setMinimumSize(QtCore.QSize(40, 35))
        self.profilePic.setMaximumSize(QtCore.QSize(40, 35))
        self.profilePic.setObjectName("profilePic")

        self.horizontalLayout_3.addWidget(self.profilePic)

        self.receivedFrame = QtWidgets.QFrame(self.receivedMessageContainer)
        self.receivedFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.receivedFrame.setMinimumSize(QtCore.QSize(100, 50))
        self.receivedFrame.setMaximumSize(QtCore.QSize(600, 1657750))
        self.receivedFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.receivedFrame.setObjectName("receivedFrame")

        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.receivedFrame)
        self.verticalLayout_8.setContentsMargins(25, 2, 25, 2)
        self.verticalLayout_8.setSpacing(1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        self.sender = QtWidgets.QLabel(self.receivedFrame)
        self.sender.setMinimumSize(QtCore.QSize(0, 20))
        self.sender.setObjectName("sender")

        self.verticalLayout_8.addWidget(self.sender)

        self.receivedMessage = QtWidgets.QLabel(self.receivedFrame)
        self.receivedMessage.setMinimumSize(QtCore.QSize(0, 20))
        self.receivedMessage.setWordWrap(True)
        self.receivedMessage.setSizeIncrement(QtCore.QSize(200, 500))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.receivedMessage.setFont(font)
        self.receivedMessage.setObjectName("message")

        self.verticalLayout_8.addWidget(self.receivedMessage)

        self.horizontalLayout_3.addWidget(self.receivedFrame)

        self.chatsFrame_layout.addWidget(self.receivedMessageContainer,0, QtCore.Qt.AlignLeft)

        self.verticalLayout_6.addWidget(self.chatsFrame, 0, QtCore.Qt.AlignTop)

        self.chatScreen.setWidget(self.scrollAreaWidgetContents)
        self.bodyLayout.addWidget(self.chatScreen)

        self.verticalLayout_3.addWidget(self.bodyContainer)

        self.sendContainer = QtWidgets.QFrame(self.centralwidget)
        self.sendContainer.setMaximumSize(QtCore.QSize(16777215, 50))
        self.sendContainer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sendContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sendContainer.setObjectName("sendContainer")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.sendContainer)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.entryFrame = QtWidgets.QFrame(self.sendContainer)
        self.entryFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.entryFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.entryFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.entryFrame.setObjectName("entryFrame")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.entryFrame)
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.messageEntry = QtWidgets.QLineEdit(self.entryFrame)
        self.messageEntry.setMinimumSize(QtCore.QSize(0, 25))
        self.messageEntry.setMaximumSize(QtCore.QSize(16777215, 35))
        validator = QtGui.QRegExpValidator(QtCore.QRegExp(".+"))
        self.messageEntry.setValidator(validator)
        self.messageEntry.returnPressed.connect(lambda:self.sendMessage())
        self.messageEntry.setPlaceholderText("Type a message")
        self.messageEntry.setObjectName("messageEntry")

        self.horizontalLayout.addWidget(self.messageEntry)

        self.sendBtn = QtWidgets.QPushButton(self.entryFrame)
        self.sendBtn.setIconSize(QtCore.QSize(50,25))
        self.sendBtn.setIcon(qta.icon("mdi.send",color='#fff'))
        self.sendBtn.setMinimumSize(QtCore.QSize(35, 35))
        self.sendBtn.setMaximumSize(QtCore.QSize(35, 35))
        self.sendBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendBtn.clicked.connect(lambda:self.sendMessage())
        self.sendBtn.setObjectName("sendBtn")

        self.horizontalLayout.addWidget(self.sendBtn)

        self.verticalLayout_5.addWidget(self.entryFrame)

        self.verticalLayout_3.addWidget(self.sendContainer)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        with open(os.path.join(static,'qss/chat.qss'),'r') as sheet:
            self.setStyleSheet(sheet.read())

        self.initPosition = self.pos()
        self.show()

    def receiveMessage(self,received_message):
        time = QtCore.QDateTime.currentDateTime().toString("h:mm ap")
        
        if received_message.find(':') >= 0:
            message = received_message.split(':')[1]
            sender = "%s %s"%(received_message.split(":")[0].upper(),time)
        
        else:
            message = received_message
            sender = "QuickChat Bot %s"%(time)

        self.receivedMessageContainer = QtWidgets.QFrame(self.chatsFrame)
        self.receivedMessageContainer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.receivedMessageContainer.setBaseSize(QtCore.QSize(200, 100))
        self.receivedMessageContainer.setMinimumSize(QtCore.QSize(100, 50))
        self.receivedMessageContainer.setMaximumSize(QtCore.QSize(1500, 1657750))
        self.receivedMessageContainer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.receivedMessageContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.receivedMessageContainer.setObjectName("receivedMessageContainer")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.receivedMessageContainer)
        self.horizontalLayout_3.setContentsMargins(5, 2, 0, 2)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.profilePic = QtWidgets.QLabel(self.receivedMessageContainer)
        self.profilePic.setMinimumSize(QtCore.QSize(40, 35))
        self.profilePic.setMaximumSize(QtCore.QSize(40, 35))
        self.profilePic.setObjectName("profilePic")

        self.horizontalLayout_3.addWidget(self.profilePic)

        self.receivedFrame = QtWidgets.QFrame(self.receivedMessageContainer)
        self.receivedFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.receivedFrame.setMinimumSize(QtCore.QSize(100, 50))
        self.receivedFrame.setMaximumSize(QtCore.QSize(600, 1657750))
        self.receivedFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.receivedFrame.setObjectName("receivedFrame")

        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.receivedFrame)
        self.verticalLayout_8.setContentsMargins(25, 2, 25, 2)
        self.verticalLayout_8.setSpacing(1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        self.sender = QtWidgets.QLabel(self.receivedFrame)
        self.sender.setMinimumSize(QtCore.QSize(0, 20))
        self.sender.setObjectName("sender")
        self.sender.setText(sender)

        self.verticalLayout_8.addWidget(self.sender)

        self.receivedMessage = QtWidgets.QLabel(self.receivedFrame)
        self.receivedMessage.setMinimumSize(QtCore.QSize(0, 20))
        self.receivedMessage.setWordWrap(True)
        self.receivedMessage.setSizeIncrement(QtCore.QSize(200, 500))
        self.receivedMessage.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.receivedMessage.adjustSize()
        font = QtGui.QFont()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.receivedMessage.setFont(font)
        self.receivedMessage.setObjectName("message")
        self.receivedMessage.setText(message)

        self.verticalLayout_8.addWidget(self.receivedMessage)

        self.horizontalLayout_3.addWidget(self.receivedFrame)

        self.chatsFrame_layout.addWidget(self.receivedMessageContainer,0,QtCore.Qt.AlignLeft)

        self.verticalLayout_6.addWidget(self.chatsFrame, 0, QtCore.Qt.AlignTop)

        vScroll = self.chatScreen.verticalScrollBar()
        vScroll.setValue(vScroll.maximum()+66)

        if self.isMinimized():
            self.trayIcon.showMessage(sender.split(' ')[0],message,QtGui.QIcon(os.path.join(static,'images/chat.png')),5000)

    def sendMessage(self):
        message = self.messageEntry.text()
        client_message = f'{self.username}: {message}'.encode('utf-8')
        self.client.send(client_message)

        time = QtCore.QDateTime.currentDateTime().toString("h:mm ap")
        self.messageEntry.setText("")

        self.sentMessageContainer = QtWidgets.QFrame(self.chatsFrame)
        self.sentMessageContainer.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.sentMessageContainer.setMinimumSize(QtCore.QSize(100, 50))
        self.sentMessageContainer.setMaximumSize(QtCore.QSize(600, 1657750))
        self.sentMessageContainer.setSizeIncrement(QSizePolicy.Preferred,QSizePolicy.Preferred)
        self.sentMessageContainer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sentMessageContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sentMessageContainer.setObjectName("sentMessageContainer")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.sentMessageContainer)
        self.horizontalLayout_3.setContentsMargins(5, 2, 0, 2)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.sentFrame = QtWidgets.QFrame(self.sentMessageContainer)
        self.sentFrame.setMinimumSize(QtCore.QSize(100, 50))
        self.sentFrame.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.sentFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sentFrame.setObjectName("sentFrame")

        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.sentFrame)
        self.verticalLayout_8.setContentsMargins(15, 5, 15, 5)
        self.verticalLayout_8.setSpacing(1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        self.sender = QtWidgets.QLabel(self.sentFrame)
        self.sender.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.sender.setMinimumSize(QtCore.QSize(0, 20))
        self.sender.setMaximumSize(QtCore.QSize(80, 20))
        self.sender.setText("You %s"%(time))
        self.sender.setObjectName("sender")

        self.verticalLayout_8.insertWidget(0,self.sender)

        self.sentMessage = QtWidgets.QLabel(self.sentFrame)
        self.sentMessage.setText(message)
        self.sentMessage.setAlignment(QtCore.Qt.AlignLeft)
        self.sentMessage.setIndent(True)
        self.sentMessage.setWordWrap(True)
        self.sentMessage.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.sentMessage.adjustSize()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sentMessage.setFont(font)
        self.sentMessage.setObjectName("sentMessage")

        self.verticalLayout_8.insertWidget(1,self.sentMessage)

        self.horizontalLayout_3.insertWidget(0,self.sentFrame)

        self.profilePic = QtWidgets.QLabel(self.sentMessageContainer)
        self.profilePic.setMinimumSize(QtCore.QSize(40, 35))
        self.profilePic.setMaximumSize(QtCore.QSize(40, 35))
        self.profilePic.setObjectName("profilePic")

        self.horizontalLayout_3.insertWidget(1,self.profilePic)

        self.chatsFrame_layout.insertWidget(-1,self.sentMessageContainer ,0, QtCore.Qt.AlignRight)

        vScroll = self.chatScreen.verticalScrollBar()
        vScroll.setValue(vScroll.maximum()+66)

    def closeWindow(self):
        self.client.close()
        self.close()

    def maximizeFunc(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def mousePressEvent(self, event):
        self.initPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.initPosition)
        self.move(self.pos().x() + delta.x() , self.pos().y() + delta.y())
        self.initPosition = event.globalPos()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chatName.setText(_translate("MainWindow", "QuickChat Messenger"))
        self.leaveBtn.setText(_translate("MainWindow", "Leave Room"))
        self.roomTitle.setText(_translate("MainWindow", "Room Name"))
        self.room.setText(_translate("MainWindow", "General"))
        self.usersTitle.setText(_translate("MainWindow", "Users"))
        self.user.setText(_translate("MainWindow", "somebody"))
        self.sender.setText(_translate("MainWindow", "QuickChat Bot %s"%(time)))
        self.receivedMessage.setText(_translate("MainWindow", "Hello %s"%(username)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    if username == "":
        username = socket.gethostname() + str(randrange(1,100))
    ui = ChatScreen(host,port,username)
    sys.exit(app.exec_())