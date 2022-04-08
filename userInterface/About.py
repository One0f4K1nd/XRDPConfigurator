# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'About.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import XRDPConfigurator_resources_rc

class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName(u"About")
        About.resize(940, 750)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(About.sizePolicy().hasHeightForWidth())
        About.setSizePolicy(sizePolicy)
        About.setMinimumSize(QSize(940, 750))
        About.setMaximumSize(QSize(940, 750))
        About.setModal(True)
        self.WALLPAPER_3 = QLabel(About)
        self.WALLPAPER_3.setObjectName(u"WALLPAPER_3")
        self.WALLPAPER_3.setGeometry(QRect(-5, -5, 1141, 756))
        self.WALLPAPER_3.setPixmap(QPixmap(u":/backgrounds/images/backgrounds/StackedWidgetBackground.png"))
        self.WALLPAPER_3.setScaledContents(True)
        self.version_label = QLabel(About)
        self.version_label.setObjectName(u"version_label")
        self.version_label.setGeometry(QRect(885, 10, 36, 35))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.version_label.setFont(font)
        self.version_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.textBrowser = QTextBrowser(About)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(5, 165, 931, 551))
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setStyleSheet(u"background-color: rgba(230, 230, 230, 160);")
        self.label = QLabel(About)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(255, 20, 411, 121))
        self.label.setMaximumSize(QSize(605, 187))
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setLineWidth(3)
        self.label.setText(u"")
        self.label.setPixmap(QPixmap(u":/Logo/images/logos/XRDPConfiguratorLogoLarge.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.buttonBox = QDialogButtonBox(About)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(430, 720, 81, 28))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.version_label_2 = QLabel(About)
        self.version_label_2.setObjectName(u"version_label_2")
        self.version_label_2.setGeometry(QRect(790, 10, 86, 35))
        self.version_label_2.setFont(font)
        self.version_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"About...", None))
        self.WALLPAPER_3.setText("")
        self.version_label.setText(QCoreApplication.translate("About", u"1.0", None))
        self.textBrowser.setHtml(QCoreApplication.translate("About", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'DejaVu Sans'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.version_label_2.setText(QCoreApplication.translate("About", u"<html><head/><body><p>Version :</p></body></html>", None))
    # retranslateUi

