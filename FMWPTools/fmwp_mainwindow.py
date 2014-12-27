# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fmwp_mainwindow.ui'
#
# Created: Thu Dec 18 01:03:49 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(320, 320)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.showHistoryWIFIButton = QtGui.QPushButton(self.centralwidget)
        self.showHistoryWIFIButton.setGeometry(QtCore.QRect(20, 10, 121, 23))
        self.showHistoryWIFIButton.setObjectName(_fromUtf8("showHistoryWIFIButton"))
        self.findMissingPasswordButton = QtGui.QPushButton(self.centralwidget)
        self.findMissingPasswordButton.setGeometry(QtCore.QRect(160, 10, 75, 23))
        self.findMissingPasswordButton.setObjectName(_fromUtf8("findMissingPasswordButton"))
        self.showWIFIListView = QtGui.QListView(self.centralwidget)
        self.showWIFIListView.setGeometry(QtCore.QRect(20, 60, 256, 192))
        self.showWIFIListView.setObjectName(_fromUtf8("showWIFIListView"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 181, 16))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.showHistoryWIFIButton.setText(_translate("MainWindow", "顯示歷史WIFI名稱", None))
        self.findMissingPasswordButton.setText(_translate("MainWindow", "找回密碼", None))
        self.label.setText(_translate("MainWindow", "歷史WIFI名稱", None))

