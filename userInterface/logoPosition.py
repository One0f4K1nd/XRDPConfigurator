# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logoPosition.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_logoPosition(object):
    def setupUi(self, logoPosition):
        if not logoPosition.objectName():
            logoPosition.setObjectName(u"logoPosition")
        logoPosition.resize(374, 190)
        logoPosition.setAutoFillBackground(False)
        logoPosition.setStyleSheet(u"background-color: rgba(255, 255, 255, 210);")
        self.label = QLabel(logoPosition)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(95, 5, 181, 35))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setFrameShape(QFrame.StyledPanel)
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setAlignment(Qt.AlignCenter)
        self.okBtn = QPushButton(logoPosition)
        self.okBtn.setObjectName(u"okBtn")
        self.okBtn.setGeometry(QRect(80, 154, 93, 30))
        self.cancelBtn = QPushButton(logoPosition)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setGeometry(QRect(189, 154, 98, 30))
        self.groupBox_5 = QGroupBox(logoPosition)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(185, 55, 151, 76))
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.ySpinBox = QSpinBox(self.groupBox_5)
        self.ySpinBox.setObjectName(u"ySpinBox")
        self.ySpinBox.setGeometry(QRect(30, 30, 91, 27))
        self.ySpinBox.setMinimum(25)
        self.ySpinBox.setMaximum(2000)
        self.groupBox_4 = QGroupBox(logoPosition)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(20, 55, 151, 76))
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.xSpinBox = QSpinBox(self.groupBox_4)
        self.xSpinBox.setObjectName(u"xSpinBox")
        self.xSpinBox.setGeometry(QRect(30, 30, 91, 27))
        self.xSpinBox.setMinimum(5)
        self.xSpinBox.setMaximum(2000)

        self.retranslateUi(logoPosition)

        QMetaObject.connectSlotsByName(logoPosition)
    # setupUi

    def retranslateUi(self, logoPosition):
        logoPosition.setWindowTitle(QCoreApplication.translate("logoPosition", u"Form", None))
        self.label.setText(QCoreApplication.translate("logoPosition", u"Logo Position", None))
        self.okBtn.setText(QCoreApplication.translate("logoPosition", u"OK", None))
        self.cancelBtn.setText(QCoreApplication.translate("logoPosition", u"Cancel", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("logoPosition", u"Y", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("logoPosition", u"X", None))
    # retranslateUi

