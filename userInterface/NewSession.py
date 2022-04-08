# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewSession.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NewSession(object):
    def setupUi(self, NewSession):
        if not NewSession.objectName():
            NewSession.setObjectName(u"NewSession")
        NewSession.resize(570, 210)
        NewSession.setMinimumSize(QSize(570, 210))
        NewSession.setMaximumSize(QSize(570, 210))
        self.label = QLabel(NewSession)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(5, 6, 555, 85))
        self.label.setFrameShape(QFrame.StyledPanel)
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setTextFormat(Qt.RichText)
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.newSessionName = QLineEdit(NewSession)
        self.newSessionName.setObjectName(u"newSessionName")
        self.newSessionName.setGeometry(QRect(100, 40, 371, 41))
        self.newSessionName.setAutoFillBackground(True)
        self.newSessionName.setText(u"")
        self.newSessionName.setAlignment(Qt.AlignCenter)
        self.buttonBox = QDialogButtonBox(NewSession)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(380, 180, 180, 28))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label_2 = QLabel(NewSession)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(5, 95, 556, 81))
        self.label_2.setFrameShape(QFrame.StyledPanel)
        self.label_2.setFrameShadow(QFrame.Raised)
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.connectionTypeComboBox = QComboBox(NewSession)
        self.connectionTypeComboBox.addItem("")
        self.connectionTypeComboBox.addItem("")
        self.connectionTypeComboBox.addItem("")
        self.connectionTypeComboBox.addItem("")
        self.connectionTypeComboBox.addItem("")
        self.connectionTypeComboBox.addItem("")
        self.connectionTypeComboBox.addItem("")
        self.connectionTypeComboBox.addItem("")
        self.connectionTypeComboBox.setObjectName(u"connectionTypeComboBox")
        self.connectionTypeComboBox.setGeometry(QRect(100, 130, 371, 36))

        self.retranslateUi(NewSession)

        QMetaObject.connectSlotsByName(NewSession)
    # setupUi

    def retranslateUi(self, NewSession):
        NewSession.setWindowTitle(QCoreApplication.translate("NewSession", u"New Session", None))
        self.label.setText(QCoreApplication.translate("NewSession", u"<html><head/><body><p><span style=\" font-weight:600;\">New session name</span></p></body></html>", None))
        self.newSessionName.setPlaceholderText(QCoreApplication.translate("NewSession", u"New session name", None))
        self.label_2.setText(QCoreApplication.translate("NewSession", u"<html><head/><body><p><span style=\" font-weight:600;\">Connection Type</span></p></body></html>", None))
        self.connectionTypeComboBox.setItemText(0, QCoreApplication.translate("NewSession", u"X11rdp (libxup.so)", None))
        self.connectionTypeComboBox.setItemText(1, QCoreApplication.translate("NewSession", u"sesman-Xvnc (libvnc.so)", None))
        self.connectionTypeComboBox.setItemText(2, QCoreApplication.translate("NewSession", u"console (VNC) (libvnc.so)", None))
        self.connectionTypeComboBox.setItemText(3, QCoreApplication.translate("NewSession", u"vnc-any (VNC) (libvnc.so)", None))
        self.connectionTypeComboBox.setItemText(4, QCoreApplication.translate("NewSession", u"sesman-any (VNC) (libvnc.so)", None))
        self.connectionTypeComboBox.setItemText(5, QCoreApplication.translate("NewSession", u"rdp-any (librdp.so)", None))
        self.connectionTypeComboBox.setItemText(6, QCoreApplication.translate("NewSession", u"freerdp (libxrdpfreerdp1.so)", None))
        self.connectionTypeComboBox.setItemText(7, QCoreApplication.translate("NewSession", u"Neutrinolabs back-end (libxrdpneutrinordp.so)", None))

    # retranslateUi

