# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PreviewWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import XRDPConfigurator_resources_rc

class Ui_PreviewWindow(object):
    def setupUi(self, PreviewWindow):
        if not PreviewWindow.objectName():
            PreviewWindow.setObjectName(u"PreviewWindow")
        PreviewWindow.resize(635, 709)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PreviewWindow.sizePolicy().hasHeightForWidth())
        PreviewWindow.setSizePolicy(sizePolicy)
        PreviewWindow.setMinimumSize(QSize(635, 709))
        PreviewWindow.setMaximumSize(QSize(635, 709))
        self.previewBrowser = QPlainTextEdit(PreviewWindow)
        self.previewBrowser.setObjectName(u"previewBrowser")
        self.previewBrowser.setGeometry(QRect(0, 117, 636, 555))
        self.previewBrowser.setAcceptDrops(False)
        self.previewBrowser.setReadOnly(True)
        self.previewBrowser.setPlainText(u"")
        self.previewBrowser.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.previewBrowser.setBackgroundVisible(True)
        self.previewOKButton = QDialogButtonBox(PreviewWindow)
        self.previewOKButton.setObjectName(u"previewOKButton")
        self.previewOKButton.setGeometry(QRect(270, 676, 96, 29))
        self.previewOKButton.setStandardButtons(QDialogButtonBox.Ok)
        self.previewOKButton.setCenterButtons(True)
        self.label = QLabel(PreviewWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(306, 6, 327, 107))
        self.label.setPixmap(QPixmap(u":/Logo/images/logos/XRDPConfiguratorLogoSmall.png"))
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(PreviewWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(44, 28, 187, 57))
        font = QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QFrame.StyledPanel)
        self.label_2.setFrameShadow(QFrame.Raised)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.retranslateUi(PreviewWindow)
        self.previewOKButton.accepted.connect(PreviewWindow.accept)

        QMetaObject.connectSlotsByName(PreviewWindow)
    # setupUi

    def retranslateUi(self, PreviewWindow):
        PreviewWindow.setWindowTitle(QCoreApplication.translate("PreviewWindow", u"Preview", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("PreviewWindow", u"INI File Preview", None))
    # retranslateUi

