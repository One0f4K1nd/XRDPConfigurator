# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogSize.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dialogSize(object):
    def setupUi(self, dialogSize):
        if not dialogSize.objectName():
            dialogSize.setObjectName(u"dialogSize")
        dialogSize.resize(374, 190)
        dialogSize.setAutoFillBackground(False)
        dialogSize.setStyleSheet(u"background-color: rgba(255, 255, 255, 210);")
        self.label = QLabel(dialogSize)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 10, 181, 35))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setFrameShape(QFrame.StyledPanel)
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setAlignment(Qt.AlignCenter)
        self.closeBtn = QPushButton(dialogSize)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setGeometry(QRect(85, 154, 93, 30))
        self.cancelBtn = QPushButton(dialogSize)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setGeometry(QRect(195, 154, 98, 30))
        self.groupBox_2 = QGroupBox(dialogSize)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(25, 55, 151, 76))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.widthSpinBox = QSpinBox(self.groupBox_2)
        self.widthSpinBox.setObjectName(u"widthSpinBox")
        self.widthSpinBox.setGeometry(QRect(30, 30, 91, 27))
        self.widthSpinBox.setMinimum(50)
        self.widthSpinBox.setMaximum(9999)
        self.groupBox_3 = QGroupBox(dialogSize)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(185, 55, 151, 76))
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.heightSpinBox = QSpinBox(self.groupBox_3)
        self.heightSpinBox.setObjectName(u"heightSpinBox")
        self.heightSpinBox.setGeometry(QRect(30, 30, 91, 27))
        self.heightSpinBox.setMinimum(50)
        self.heightSpinBox.setMaximum(9999)

        self.retranslateUi(dialogSize)

        QMetaObject.connectSlotsByName(dialogSize)
    # setupUi

    def retranslateUi(self, dialogSize):
        dialogSize.setWindowTitle(QCoreApplication.translate("dialogSize", u"Form", None))
        self.label.setText(QCoreApplication.translate("dialogSize", u"Login Dialog Size", None))
        self.closeBtn.setText(QCoreApplication.translate("dialogSize", u"OK", None))
        self.cancelBtn.setText(QCoreApplication.translate("dialogSize", u"Cancel", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("dialogSize", u"Width", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("dialogSize", u"Height", None))
    # retranslateUi

