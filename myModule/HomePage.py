# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\Home Page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomePage(object):
    def setupUi(self, HomePage):
        HomePage.setObjectName("HomePage")
        HomePage.resize(1260, 1000)
        self.centralwidget = QtWidgets.QWidget(HomePage)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Window_Title = QtWidgets.QLabel(self.centralwidget)
        self.label_Window_Title.setGeometry(QtCore.QRect(330, 100, 541, 91))
        self.label_Window_Title.setStyleSheet("font-size: 28pt; color: rgb(12, 223, 255);\n"
"font: 36pt \"Papyrus\";")
        self.label_Window_Title.setObjectName("label_Window_Title")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(430, 300, 321, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 50, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Button_register = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Button_register.setMinimumSize(QtCore.QSize(0, 55))
        self.Button_register.setObjectName("Button_register")
        self.verticalLayout.addWidget(self.Button_register)
        self.Button_Rollcall = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Button_Rollcall.setMinimumSize(QtCore.QSize(0, 55))
        self.Button_Rollcall.setObjectName("Button_Rollcall")
        self.verticalLayout.addWidget(self.Button_Rollcall)
        HomePage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HomePage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1260, 26))
        self.menubar.setObjectName("menubar")
        HomePage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HomePage)
        self.statusbar.setObjectName("statusbar")
        HomePage.setStatusBar(self.statusbar)

        self.retranslateUi(HomePage)
        QtCore.QMetaObject.connectSlotsByName(HomePage)

    def retranslateUi(self, HomePage):
        _translate = QtCore.QCoreApplication.translate
        HomePage.setWindowTitle(_translate("HomePage", "MainWindow"))
        self.label_Window_Title.setText(_translate("HomePage", "Attendance Check"))
        self.Button_register.setText(_translate("HomePage", "Register"))
        self.Button_Rollcall.setText(_translate("HomePage", "Roll Call"))
