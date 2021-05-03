# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat_window(scrollable).ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.minimizeBtn.setStyleSheet("border-radius:7px;\n"
"background-color: #ffbd44;")
        self.minimizeBtn.setText("")
        self.minimizeBtn.setObjectName("minimizeBtn")
        self.horizontalLayout_5.addWidget(self.minimizeBtn)
        self.maximizeBtn = QtWidgets.QPushButton(self.closeFrame)
        self.maximizeBtn.setMinimumSize(QtCore.QSize(15, 15))
        self.maximizeBtn.setMaximumSize(QtCore.QSize(15, 15))
        self.maximizeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.maximizeBtn.setStyleSheet("border-radius:7px;\n"
"background-color:#00ca4e;")
        self.maximizeBtn.setText("")
        self.maximizeBtn.setObjectName("maximizeBtn")
        self.horizontalLayout_5.addWidget(self.maximizeBtn)
        self.closeBtn = QtWidgets.QPushButton(self.closeFrame)
        self.closeBtn.setMinimumSize(QtCore.QSize(15, 15))
        self.closeBtn.setMaximumSize(QtCore.QSize(15, 15))
        self.closeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeBtn.setStyleSheet("border-radius: 7px;\n"
"background-color: #ff605c;")
        self.closeBtn.setText("")
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout_5.addWidget(self.closeBtn)
        self.horizontalLayout_4.addWidget(self.closeFrame, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addWidget(self.windowFrame)
        self.headerContainer = QtWidgets.QFrame(self.centralwidget)
        self.headerContainer.setMaximumSize(QtCore.QSize(16777215, 50))
        self.headerContainer.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.headerContainer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.headerContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerContainer.setObjectName("headerContainer")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.headerContainer)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chatName = QtWidgets.QLabel(self.headerContainer)
        self.chatName.setMinimumSize(QtCore.QSize(130, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.chatName.setFont(font)
        self.chatName.setStyleSheet("color: rgb(255, 255, 255);")
        self.chatName.setObjectName("chatName")
        self.horizontalLayout_2.addWidget(self.chatName)
        self.leaveBtn = QtWidgets.QPushButton(self.headerContainer)
        self.leaveBtn.setMinimumSize(QtCore.QSize(120, 30))
        self.leaveBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.leaveBtn.setStyleSheet("border:1px solid gray;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(76, 76, 76);")
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
        self.side_bar.setStyleSheet("background-color: rgb(202, 202, 202);")
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
        self.label = QtWidgets.QLabel(self.roomtitleContainer)
        self.label.setGeometry(QtCore.QRect(15, 0, 250, 50))
        self.label.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.roomtitleContainer)
        self.roomName = QtWidgets.QFrame(self.roomContainer)
        self.roomName.setMinimumSize(QtCore.QSize(0, 50))
        self.roomName.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.roomName.setFrameShadow(QtWidgets.QFrame.Raised)
        self.roomName.setObjectName("roomName")
        self.label_2 = QtWidgets.QLabel(self.roomName)
        self.label_2.setGeometry(QtCore.QRect(15, 0, 250, 50))
        self.label_2.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("padding-bottom:30px;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.roomName)
        self.verticalLayout.addWidget(self.roomContainer)
        self.usersContainer = QtWidgets.QFrame(self.side_bar_box)
        self.usersContainer.setMinimumSize(QtCore.QSize(0, 100))
        self.usersContainer.setStyleSheet("padding-bottom:10px;")
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
        self.label_4 = QtWidgets.QLabel(self.userstitleContainer)
        self.label_4.setGeometry(QtCore.QRect(15, 0, 250, 50))
        self.label_4.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.userstitleContainer)
        self.usersName = QtWidgets.QFrame(self.usersContainer)
        self.usersName.setStyleSheet("padding-bottom:30px;")
        self.usersName.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.usersName.setFrameShadow(QtWidgets.QFrame.Raised)
        self.usersName.setObjectName("usersName")
        self.label_3 = QtWidgets.QLabel(self.usersName)
        self.label_3.setGeometry(QtCore.QRect(15, 0, 250, 50))
        self.label_3.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("padding-bottom:30px;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.usersName)
        self.verticalLayout.addWidget(self.usersContainer)
        self.side_barLayout.addWidget(self.side_bar_box, 0, QtCore.Qt.AlignTop)
        self.bodyLayout.addWidget(self.side_bar)

        self.scrollArea = QtWidgets.QScrollArea(self.bodyContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(500, 0))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1076, 638))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.messageContainer = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.messageContainer.setMinimumSize(QtCore.QSize(0, 50))
        self.messageContainer.setMaximumSize(QtCore.QSize(600, 50))
        self.messageContainer.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(223, 223, 223);")
        self.messageContainer.setObjectName("messageContainer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.messageContainer)
        self.horizontalLayout_3.setContentsMargins(10, 2, 0, 2)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.profilePic = QtWidgets.QLabel(self.messageContainer)
        self.profilePic.setMaximumSize(QtCore.QSize(40, 35))
        self.profilePic.setStyleSheet("border-radius:10px;")
        self.profilePic.setText("")
        self.profilePic.setPixmap(QtGui.QPixmap("media/profile_pics/default.jpg"))
        self.profilePic.setScaledContents(True)
        self.profilePic.setObjectName("profilePic")
        self.horizontalLayout_3.addWidget(self.profilePic)
        self.frame = QtWidgets.QFrame(self.messageContainer)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_8.setContentsMargins(0, 2, 0, 2)
        self.verticalLayout_8.setSpacing(1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.sender = QtWidgets.QLabel(self.frame)
        self.sender.setMinimumSize(QtCore.QSize(0, 20))
        self.sender.setStyleSheet("color: rgb(0, 170, 255);\n"
"")
        self.sender.setObjectName("sender")
        self.verticalLayout_8.addWidget(self.sender)
        self.message = QtWidgets.QLabel(self.frame)
        self.message.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.message.setFont(font)
        self.message.setObjectName("message")
        self.verticalLayout_8.addWidget(self.message)
        self.horizontalLayout_3.addWidget(self.frame)
        self.verticalLayout_6.addWidget(self.messageContainer, 0, QtCore.Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.bodyLayout.addWidget(self.scrollArea)
        
        self.verticalLayout_3.addWidget(self.bodyContainer)
        self.sendContainer = QtWidgets.QFrame(self.centralwidget)
        self.sendContainer.setMaximumSize(QtCore.QSize(16777215, 50))
        self.sendContainer.setStyleSheet("background-color: rgb(223, 223, 223);")
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
        self.messageEntry.setStyleSheet("border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"padding-left:20px;")
        self.messageEntry.setObjectName("messageEntry")
        self.horizontalLayout.addWidget(self.messageEntry)
        self.sendBtn = QtWidgets.QPushButton(self.entryFrame)
        self.sendBtn.setMinimumSize(QtCore.QSize(35, 35))
        self.sendBtn.setMaximumSize(QtCore.QSize(35, 35))
        self.sendBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendBtn.setStyleSheet("border:1px solid gray;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"background-color: rgb(76, 76, 76);")
        self.sendBtn.setObjectName("sendBtn")
        self.horizontalLayout.addWidget(self.sendBtn)
        self.verticalLayout_5.addWidget(self.entryFrame)
        self.verticalLayout_3.addWidget(self.sendContainer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chatName.setText(_translate("MainWindow", "VagueChat"))
        self.leaveBtn.setText(_translate("MainWindow", "Leave Room"))
        self.label.setText(_translate("MainWindow", "Room Name"))
        self.label_2.setText(_translate("MainWindow", "General"))
        self.label_4.setText(_translate("MainWindow", "Users"))
        self.label_3.setText(_translate("MainWindow", "somebody"))
        self.sender.setText(_translate("MainWindow", "Dave 2:50 pm"))
        self.message.setText(_translate("MainWindow", "Hello everyone"))
        self.sendBtn.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())