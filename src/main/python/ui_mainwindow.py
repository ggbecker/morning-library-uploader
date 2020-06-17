# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelApiToken = QtWidgets.QLabel(self.centralwidget)
        self.labelApiToken.setObjectName("labelApiToken")
        self.horizontalLayout.addWidget(self.labelApiToken)
        self.lineEditApiToken = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditApiToken.setObjectName("lineEditApiToken")
        self.horizontalLayout.addWidget(self.lineEditApiToken)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelMusicFolder = QtWidgets.QLabel(self.centralwidget)
        self.labelMusicFolder.setObjectName("labelMusicFolder")
        self.horizontalLayout_2.addWidget(self.labelMusicFolder)
        self.lineEditMusicFolder = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditMusicFolder.setObjectName("lineEditMusicFolder")
        self.horizontalLayout_2.addWidget(self.lineEditMusicFolder)
        self.pushButtonBrowseMusicFolder = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBrowseMusicFolder.setObjectName("pushButtonBrowseMusicFolder")
        self.horizontalLayout_2.addWidget(self.pushButtonBrowseMusicFolder)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButtonCancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout_3.addWidget(self.pushButtonCancel)
        self.pushButtonUpload = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonUpload.setObjectName("pushButtonUpload")
        self.horizontalLayout_3.addWidget(self.pushButtonUpload)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.textBrowserOutput = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowserOutput.setObjectName("textBrowserOutput")
        self.verticalLayout.addWidget(self.textBrowserOutput)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 603, 29))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuAbout.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.labelApiToken.setBuddy(self.lineEditApiToken)
        self.labelMusicFolder.setBuddy(self.lineEditMusicFolder)

        self.retranslateUi(MainWindow)
        self.pushButtonUpload.clicked.connect(MainWindow.uploadTracks)
        self.pushButtonCancel.clicked.connect(MainWindow.close)
        self.pushButtonBrowseMusicFolder.clicked.connect(MainWindow.browse)
        self.actionAbout.triggered.connect(MainWindow.about)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEditApiToken, self.lineEditMusicFolder)
        MainWindow.setTabOrder(self.lineEditMusicFolder, self.pushButtonBrowseMusicFolder)
        MainWindow.setTabOrder(self.pushButtonBrowseMusicFolder, self.pushButtonCancel)
        MainWindow.setTabOrder(self.pushButtonCancel, self.pushButtonUpload)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Morning Library Uploader"))
        self.labelApiToken.setText(_translate("MainWindow", "&API Token:"))
        self.labelMusicFolder.setText(_translate("MainWindow", "&Music Folder:"))
        self.pushButtonBrowseMusicFolder.setText(_translate("MainWindow", "&Browse"))
        self.pushButtonCancel.setText(_translate("MainWindow", "&Cancel"))
        self.pushButtonUpload.setText(_translate("MainWindow", "&Upload"))
        self.menuAbout.setTitle(_translate("MainWindow", "&Help"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))
        self.actionExit.setText(_translate("MainWindow", "&Exit"))
