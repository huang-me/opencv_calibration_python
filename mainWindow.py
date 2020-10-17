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
        mainWindow.resize(679, 445)
        self.TEXT_CALIBRATION = QtWidgets.QLabel(mainWindow)
        self.TEXT_CALIBRATION.setGeometry(QtCore.QRect(30, 70, 110, 40))
        self.TEXT_CALIBRATION.setTextFormat(QtCore.Qt.PlainText)
        self.TEXT_CALIBRATION.setObjectName("TEXT_CALIBRATION")
        self.BTN_CORNER = QtWidgets.QPushButton(mainWindow)
        self.BTN_CORNER.setGeometry(QtCore.QRect(40, 120, 150, 70))
        self.BTN_CORNER.setObjectName("BTN_CORNER")
        self.BTN_INTRINSIC = QtWidgets.QPushButton(mainWindow)
        self.BTN_INTRINSIC.setGeometry(QtCore.QRect(40, 210, 150, 70))
        self.BTN_INTRINSIC.setObjectName("BTN_INTRINSIC")
        self.BTN_DISTORTION = QtWidgets.QPushButton(mainWindow)
        self.BTN_DISTORTION.setGeometry(QtCore.QRect(40, 300, 150, 70))
        self.BTN_DISTORTION.setObjectName("BTN_DISTORTION")
        self.TEXT_EXTRINSIC = QtWidgets.QLabel(mainWindow)
        self.TEXT_EXTRINSIC.setGeometry(QtCore.QRect(230, 90, 131, 41))
        self.TEXT_EXTRINSIC.setTextFormat(QtCore.Qt.PlainText)
        self.TEXT_EXTRINSIC.setObjectName("TEXT_EXTRINSIC")
        self.BTN_EXTRINSIC = QtWidgets.QPushButton(mainWindow)
        self.BTN_EXTRINSIC.setGeometry(QtCore.QRect(240, 180, 150, 70))
        self.BTN_EXTRINSIC.setObjectName("BTN_EXTRINSIC")
        self.CLOSE_ALL_WINDOW = QtWidgets.QPushButton(mainWindow)
        self.CLOSE_ALL_WINDOW.setGeometry(QtCore.QRect(240, 340, 140, 35))
        self.CLOSE_ALL_WINDOW.setObjectName("CLOSE_ALL_WINDOW")
        self.ID_IMAGE = QtWidgets.QComboBox(mainWindow)
        self.ID_IMAGE.setGeometry(QtCore.QRect(240, 140, 120, 25))
        self.ID_IMAGE.setCurrentText("")
        self.ID_IMAGE.setObjectName("ID_IMAGE")
        self.TEXT_AUGMENTED = QtWidgets.QLabel(mainWindow)
        self.TEXT_AUGMENTED.setGeometry(QtCore.QRect(450, 40, 165, 25))
        self.TEXT_AUGMENTED.setObjectName("TEXT_AUGMENTED")
        self.BTN_AUGMENTED = QtWidgets.QPushButton(mainWindow)
        self.BTN_AUGMENTED.setGeometry(QtCore.QRect(460, 70, 180, 55))
        self.BTN_AUGMENTED.setObjectName("BTN_AUGMENTED")
        self.TEXT_DISPARITY = QtWidgets.QLabel(mainWindow)
        self.TEXT_DISPARITY.setGeometry(QtCore.QRect(450, 140, 165, 25))
        self.TEXT_DISPARITY.setObjectName("TEXT_DISPARITY")
        self.BTN_DISPARITY = QtWidgets.QPushButton(mainWindow)
        self.BTN_DISPARITY.setGeometry(QtCore.QRect(460, 170, 180, 55))
        self.BTN_DISPARITY.setObjectName("BTN_DISPARITY")
        self.TEXT_SIFT = QtWidgets.QLabel(mainWindow)
        self.TEXT_SIFT.setGeometry(QtCore.QRect(450, 240, 165, 25))
        self.TEXT_SIFT.setObjectName("TEXT_SIFT")
        self.BTN_KEYPOINT = QtWidgets.QPushButton(mainWindow)
        self.BTN_KEYPOINT.setGeometry(QtCore.QRect(460, 270, 180, 55))
        self.BTN_KEYPOINT.setObjectName("BTN_KEYPOINT")
        self.BTN_MATCHKEY = QtWidgets.QPushButton(mainWindow)
        self.BTN_MATCHKEY.setGeometry(QtCore.QRect(460, 340, 180, 55))
        self.BTN_MATCHKEY.setObjectName("BTN_MATCHKEY")
        self.SEP_LINE = QtWidgets.QFrame(mainWindow)
        self.SEP_LINE.setGeometry(QtCore.QRect(410, 40, 20, 365))
        self.SEP_LINE.setFrameShape(QtWidgets.QFrame.VLine)
        self.SEP_LINE.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SEP_LINE.setObjectName("SEP_LINE")

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
        self.TEXT_AUGMENTED.setText(_translate("mainWindow", "2. Augmented Reality"))
        self.BTN_AUGMENTED.setText(_translate("mainWindow", "2.1 Augmented Reality"))
        self.TEXT_DISPARITY.setText(_translate("mainWindow", "3. Stereo Disparity Map"))
        self.BTN_DISPARITY.setText(_translate("mainWindow", "3.1 Stereo Disparity Map"))
        self.TEXT_SIFT.setText(_translate("mainWindow", "4. SIFT"))
        self.BTN_KEYPOINT.setText(_translate("mainWindow", "4.1 Keypoints"))
        self.BTN_MATCHKEY.setText(_translate("mainWindow", "4.2 Matched Keypoints"))
