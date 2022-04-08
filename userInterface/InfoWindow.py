# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InfoWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_InfoWindow(object):
    def setupUi(self, InfoWindow):
        if not InfoWindow.objectName():
            InfoWindow.setObjectName(u"InfoWindow")
        InfoWindow.resize(530, 173)
        InfoWindow.setMinimumSize(QSize(530, 173))
        InfoWindow.setMaximumSize(QSize(530, 173))
        self.label = QLabel(InfoWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(5, 10, 521, 121))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QFrame.StyledPanel)
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setTextFormat(Qt.RichText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.buttonBox = QDialogButtonBox(InfoWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(198, 132, 136, 41))
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.retranslateUi(InfoWindow)

        QMetaObject.connectSlotsByName(InfoWindow)
    # setupUi

    def retranslateUi(self, InfoWindow):
        InfoWindow.setWindowTitle(QCoreApplication.translate("InfoWindow", u"Information", None))
    # retranslateUi

