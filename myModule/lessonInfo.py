# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\LessonInfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LessonInfo(object):
    def setupUi(self, LessonInfo):
        LessonInfo.setObjectName("LessonInfo")
        LessonInfo.resize(1260, 1000)
        self.centralwidget = QtWidgets.QWidget(LessonInfo)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Window_Title = QtWidgets.QLabel(self.centralwidget)
        self.label_Window_Title.setGeometry(QtCore.QRect(330, 100, 541, 91))
        self.label_Window_Title.setStyleSheet("font-size: 28pt; color: rgb(12, 223, 255);\n"
"font: 36pt \"Papyrus\";")
        self.label_Window_Title.setObjectName("label_Window_Title")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(310, 300, 591, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 50, 0, 75)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.InputClassID = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.InputClassID.setMinimumSize(QtCore.QSize(0, 50))
        self.InputClassID.setObjectName("InputClassID")
        self.verticalLayout.addWidget(self.InputClassID)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.InputLesson = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.InputLesson.setMinimumSize(QtCore.QSize(0, 50))
        self.InputLesson.setObjectName("InputLesson")
        self.verticalLayout.addWidget(self.InputLesson)
        self.ButtonIntoClass = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonIntoClass.setGeometry(QtCore.QRect(510, 740, 201, 61))
        self.ButtonIntoClass.setObjectName("ButtonIntoClass")
        self.commandLinkButton_backhp = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_backhp.setGeometry(QtCore.QRect(10, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.commandLinkButton_backhp.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\UI\\../sources/homepage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_backhp.setIcon(icon)
        self.commandLinkButton_backhp.setObjectName("commandLinkButton_backhp")
        LessonInfo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LessonInfo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1260, 26))
        self.menubar.setObjectName("menubar")
        LessonInfo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LessonInfo)
        self.statusbar.setObjectName("statusbar")
        LessonInfo.setStatusBar(self.statusbar)

        self.retranslateUi(LessonInfo)
        QtCore.QMetaObject.connectSlotsByName(LessonInfo)

    def retranslateUi(self, LessonInfo):
        _translate = QtCore.QCoreApplication.translate
        LessonInfo.setWindowTitle(_translate("LessonInfo", "MainWindow"))
        self.label_Window_Title.setText(_translate("LessonInfo", "Attendance Check"))
        self.label.setText(_translate("LessonInfo", "Class ID"))
        self.label_2.setText(_translate("LessonInfo", "Lesson"))
        self.ButtonIntoClass.setText(_translate("LessonInfo", "Get Into Class"))
        self.commandLinkButton_backhp.setText(_translate("LessonInfo", "Back to Home Page"))
