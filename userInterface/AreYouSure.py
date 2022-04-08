# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AreYouSure.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AreYouSure(object):
    def setupUi(self, AreYouSure):
        if not AreYouSure.objectName():
            AreYouSure.setObjectName(u"AreYouSure")
        AreYouSure.resize(530, 173)
        AreYouSure.setMinimumSize(QSize(530, 173))
        AreYouSure.setMaximumSize(QSize(530, 173))
        self.label = QLabel(AreYouSure)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(5, 10, 521, 81))
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
        self.buttonBox = QDialogButtonBox(AreYouSure)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(210, 95, 136, 71))
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(True)

        self.retranslateUi(AreYouSure)

        QMetaObject.connectSlotsByName(AreYouSure)
    # setupUi

    def retranslateUi(self, AreYouSure):
        AreYouSure.setWindowTitle(QCoreApplication.translate("AreYouSure", u"Unsaved changes...", None))
        self.label.setText(QCoreApplication.translate("AreYouSure", u"<html><head/><body><p>You have unsaved changes.</p><p>Are you sure you want to quit?</p></body></html>", None))
    # retranslateUi

