# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(547, 468)
        self.TEXT_CALIBRATION = QtWidgets.QLabel(mainWindow)
        self.TEXT_CALIBRATION.setGeometry(QtCore.QRect(60, 50, 111, 41))
        self.TEXT_CALIBRATION.setTextFormat(QtCore.Qt.PlainText)
        self.TEXT_CALIBRATION.setObjectName("TEXT_CALIBRATION")
        self.BTN_CORNER = QtWidgets.QPushButton(mainWindow)
        self.BTN_CORNER.setGeometry(QtCore.QRect(70, 100, 151, 71))
        self.BTN_CORNER.setObjectName("BTN_CORNER")
        self.BTN_INTRINSIC = QtWidgets.QPushButton(mainWindow)
        self.BTN_INTRINSIC.setGeometry(QtCore.QRect(70, 190, 151, 71))
        self.BTN_INTRINSIC.setObjectName("BTN_INTRINSIC")
        self.BTN_DISTORTION = QtWidgets.QPushButton(mainWindow)
        self.BTN_DISTORTION.setGeometry(QtCore.QRect(70, 280, 151, 71))
        self.BTN_DISTORTION.setObjectName("BTN_DISTORTION")
        self.TEXT_EXTRINSIC = QtWidgets.QLabel(mainWindow)
        self.TEXT_EXTRINSIC.setGeometry(QtCore.QRect(300, 70, 131, 41))
        self.TEXT_EXTRINSIC.setTextFormat(QtCore.Qt.PlainText)
        self.TEXT_EXTRINSIC.setObjectName("TEXT_EXTRINSIC")
        self.BTN_EXTRINSIC = QtWidgets.QPushButton(mainWindow)
        self.BTN_EXTRINSIC.setGeometry(QtCore.QRect(310, 190, 151, 71))
        self.BTN_EXTRINSIC.setObjectName("BTN_EXTRINSIC")
        self.BOX_FILE = QtWidgets.QComboBox(mainWindow)
        self.BOX_FILE.setGeometry(QtCore.QRect(310, 140, 151, 25))
        self.BOX_FILE.setCurrentText("")
        self.BOX_FILE.setObjectName("BOX_FILE")
        self.CLOSE_ALL_WINDOW = QtWidgets.QPushButton(mainWindow)
        self.CLOSE_ALL_WINDOW.setGeometry(QtCore.QRect(350, 420, 131, 31))
        self.CLOSE_ALL_WINDOW.setObjectName("CLOSE_ALL_WINDOW")

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Main Window"))
        self.TEXT_CALIBRATION.setText(_translate("mainWindow", "1. Calibration"))
        self.BTN_CORNER.setText(_translate("mainWindow", "1.1 Find Corners"))
        self.BTN_INTRINSIC.setText(_translate("mainWindow", "1.2 Find Intrinsic"))
        self.BTN_DISTORTION.setText(_translate("mainWindow", "1.4 Find Distortion"))
        self.TEXT_EXTRINSIC.setText(_translate("mainWindow", "1.3 Find Extrinsic"))
        self.BTN_EXTRINSIC.setText(_translate("mainWindow", "1.3 Find Extrinsic"))
        self.CLOSE_ALL_WINDOW.setText(_translate("mainWindow", "Close All Windows"))
