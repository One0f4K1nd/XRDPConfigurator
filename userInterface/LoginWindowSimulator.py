# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginWindowSimulator.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LoginWindowSimulator(object):
    def setupUi(self, LoginWindowSimulator):
        if not LoginWindowSimulator.objectName():
            LoginWindowSimulator.setObjectName(u"LoginWindowSimulator")
        LoginWindowSimulator.setWindowModality(Qt.NonModal)
        LoginWindowSimulator.setEnabled(True)
        LoginWindowSimulator.resize(1384, 909)
        LoginWindowSimulator.setMinimumSize(QSize(1384, 909))
        LoginWindowSimulator.setWindowTitle(u"Login Window Simulator")
#if QT_CONFIG(tooltip)
        LoginWindowSimulator.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        LoginWindowSimulator.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        LoginWindowSimulator.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        LoginWindowSimulator.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        LoginWindowSimulator.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.gridLayout_2 = QGridLayout(LoginWindowSimulator)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.xrdp_window = QGraphicsView(LoginWindowSimulator)
        self.xrdp_window.setObjectName(u"xrdp_window")
        self.xrdp_window.setSizeIncrement(QSize(1, 1))
        self.xrdp_window.setContextMenuPolicy(Qt.PreventContextMenu)
        self.xrdp_window.setAcceptDrops(False)
        self.xrdp_window.setFrameShape(QFrame.StyledPanel)
        self.xrdp_window.setFrameShadow(QFrame.Raised)
        self.xrdp_window.setLineWidth(4)
        self.xrdp_window.setMidLineWidth(4)
        self.xrdp_window.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.xrdp_window.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        self.xrdp_window.setBackgroundBrush(brush)
        self.xrdp_window.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.xrdp_window.setCacheMode(QGraphicsView.CacheNone)
        self.xrdp_window.setViewportUpdateMode(QGraphicsView.SmartViewportUpdate)

        self.gridLayout_2.addWidget(self.xrdp_window, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.miscGroupBox = QGroupBox(LoginWindowSimulator)
        self.miscGroupBox.setObjectName(u"miscGroupBox")
        self.miscGroupBox.setMinimumSize(QSize(140, 0))
        self.closeWinSimBtn = QPushButton(self.miscGroupBox)
        self.closeWinSimBtn.setObjectName(u"closeWinSimBtn")
        self.closeWinSimBtn.setGeometry(QRect(12, 70, 121, 31))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.closeWinSimBtn.setFont(font)
        self.previewINIBtn = QPushButton(self.miscGroupBox)
        self.previewINIBtn.setObjectName(u"previewINIBtn")
        self.previewINIBtn.setGeometry(QRect(12, 20, 121, 31))
        self.previewINIBtn.setFont(font)

        self.gridLayout.addWidget(self.miscGroupBox, 0, 4, 1, 1)

        self.ColoursGroupBox = QGroupBox(LoginWindowSimulator)
        self.ColoursGroupBox.setObjectName(u"ColoursGroupBox")
        self.ColoursGroupBox.setMinimumSize(QSize(801, 121))
        self.ColoursGroupBox.setMaximumSize(QSize(801, 121))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(14)
        self.ColoursGroupBox.setFont(font1)
        self.ColoursGroupBox.setFlat(False)
        self.ColoursGroupBox.setCheckable(False)
        self.ColoursGroupBox.setChecked(False)
        self.resetWindowButton = QPushButton(self.ColoursGroupBox)
        self.resetWindowButton.setObjectName(u"resetWindowButton")
        self.resetWindowButton.setGeometry(QRect(11, 58, 61, 26))
        self.resetWindowButton.setMinimumSize(QSize(61, 26))
        self.resetWindowButton.setMaximumSize(QSize(61, 26))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        self.resetWindowButton.setFont(font2)
        self.grey_Pushbutton = QPushButton(self.ColoursGroupBox)
        self.grey_Pushbutton.setObjectName(u"grey_Pushbutton")
        self.grey_Pushbutton.setGeometry(QRect(78, 56, 145, 30))
        self.grey_Pushbutton.setMinimumSize(QSize(145, 30))
        self.grey_Pushbutton.setMaximumSize(QSize(145, 30))
        self.grey_Pushbutton.setFont(font2)
        self.grey_Pushbutton.setAutoFillBackground(False)
        self.windowView = QGraphicsView(self.ColoursGroupBox)
        self.windowView.setObjectName(u"windowView")
        self.windowView.setGeometry(QRect(229, 58, 35, 25))
        self.windowView.setMinimumSize(QSize(35, 25))
        self.windowView.setMaximumSize(QSize(35, 25))
        self.windowView.setFrameShadow(QFrame.Raised)
        self.backgroundView = QGraphicsView(self.ColoursGroupBox)
        self.backgroundView.setObjectName(u"backgroundView")
        self.backgroundView.setGeometry(QRect(229, 28, 35, 25))
        self.backgroundView.setMinimumSize(QSize(35, 25))
        self.backgroundView.setMaximumSize(QSize(35, 25))
        self.backgroundView.setFrameShadow(QFrame.Raised)
        self.resetBackgroundButton = QPushButton(self.ColoursGroupBox)
        self.resetBackgroundButton.setObjectName(u"resetBackgroundButton")
        self.resetBackgroundButton.setGeometry(QRect(11, 28, 61, 26))
        self.resetBackgroundButton.setMinimumSize(QSize(61, 26))
        self.resetBackgroundButton.setMaximumSize(QSize(61, 26))
        self.resetBackgroundButton.setFont(font2)
        self.background_Pushbutton = QPushButton(self.ColoursGroupBox)
        self.background_Pushbutton.setObjectName(u"background_Pushbutton")
        self.background_Pushbutton.setGeometry(QRect(78, 26, 145, 30))
        self.background_Pushbutton.setMinimumSize(QSize(145, 30))
        self.background_Pushbutton.setMaximumSize(QSize(145, 30))
        self.background_Pushbutton.setFont(font2)
        self.background_Pushbutton.setAutoFillBackground(False)
        self.resetTitleBgndButton = QPushButton(self.ColoursGroupBox)
        self.resetTitleBgndButton.setObjectName(u"resetTitleBgndButton")
        self.resetTitleBgndButton.setGeometry(QRect(11, 88, 61, 26))
        self.resetTitleBgndButton.setMinimumSize(QSize(61, 26))
        self.resetTitleBgndButton.setMaximumSize(QSize(61, 26))
        self.resetTitleBgndButton.setFont(font2)
        self.blue_Pushbutton = QPushButton(self.ColoursGroupBox)
        self.blue_Pushbutton.setObjectName(u"blue_Pushbutton")
        self.blue_Pushbutton.setGeometry(QRect(78, 86, 145, 30))
        self.blue_Pushbutton.setMinimumSize(QSize(145, 30))
        self.blue_Pushbutton.setMaximumSize(QSize(145, 30))
        self.blue_Pushbutton.setFont(font2)
        self.blue_Pushbutton.setAutoFillBackground(False)
        self.titleBgndView = QGraphicsView(self.ColoursGroupBox)
        self.titleBgndView.setObjectName(u"titleBgndView")
        self.titleBgndView.setGeometry(QRect(229, 88, 35, 25))
        self.titleBgndView.setMinimumSize(QSize(35, 25))
        self.titleBgndView.setMaximumSize(QSize(35, 25))
        self.titleBgndView.setFrameShadow(QFrame.Raised)
        self.black_Pushbutton = QPushButton(self.ColoursGroupBox)
        self.black_Pushbutton.setObjectName(u"black_Pushbutton")
        self.black_Pushbutton.setGeometry(QRect(343, 26, 145, 30))
        self.black_Pushbutton.setMinimumSize(QSize(145, 30))
        self.black_Pushbutton.setMaximumSize(QSize(145, 30))
        self.black_Pushbutton.setFont(font2)
        self.black_Pushbutton.setAutoFillBackground(False)
        self.resetTextButton = QPushButton(self.ColoursGroupBox)
        self.resetTextButton.setObjectName(u"resetTextButton")
        self.resetTextButton.setGeometry(QRect(276, 28, 61, 26))
        self.resetTextButton.setMinimumSize(QSize(61, 26))
        self.resetTextButton.setMaximumSize(QSize(61, 26))
        self.resetTextButton.setFont(font2)
        self.textView = QGraphicsView(self.ColoursGroupBox)
        self.textView.setObjectName(u"textView")
        self.textView.setGeometry(QRect(494, 28, 35, 25))
        self.textView.setMinimumSize(QSize(35, 25))
        self.textView.setMaximumSize(QSize(35, 25))
        self.textView.setFrameShadow(QFrame.Raised)
        self.resetSessionBoxHilightBtn = QPushButton(self.ColoursGroupBox)
        self.resetSessionBoxHilightBtn.setObjectName(u"resetSessionBoxHilightBtn")
        self.resetSessionBoxHilightBtn.setGeometry(QRect(276, 58, 61, 26))
        self.resetSessionBoxHilightBtn.setMinimumSize(QSize(61, 26))
        self.resetSessionBoxHilightBtn.setMaximumSize(QSize(61, 26))
        self.resetSessionBoxHilightBtn.setFont(font2)
        self.dark_blue_Pushbutton = QPushButton(self.ColoursGroupBox)
        self.dark_blue_Pushbutton.setObjectName(u"dark_blue_Pushbutton")
        self.dark_blue_Pushbutton.setGeometry(QRect(343, 56, 145, 30))
        self.dark_blue_Pushbutton.setMinimumSize(QSize(145, 30))
        self.dark_blue_Pushbutton.setMaximumSize(QSize(145, 30))
        self.dark_blue_Pushbutton.setFont(font2)
        self.darkBlueView = QGraphicsView(self.ColoursGroupBox)
        self.darkBlueView.setObjectName(u"darkBlueView")
        self.darkBlueView.setGeometry(QRect(494, 58, 35, 25))
        self.darkBlueView.setMinimumSize(QSize(35, 25))
        self.darkBlueView.setMaximumSize(QSize(35, 25))
        self.darkBlueView.setFrameShadow(QFrame.Raised)
        self.resetTopLeftTitleBoxesBtn = QPushButton(self.ColoursGroupBox)
        self.resetTopLeftTitleBoxesBtn.setObjectName(u"resetTopLeftTitleBoxesBtn")
        self.resetTopLeftTitleBoxesBtn.setGeometry(QRect(542, 30, 61, 26))
        self.resetTopLeftTitleBoxesBtn.setMinimumSize(QSize(61, 26))
        self.resetTopLeftTitleBoxesBtn.setMaximumSize(QSize(61, 26))
        self.resetTopLeftTitleBoxesBtn.setFont(font2)
        self.white_Pushbutton = QPushButton(self.ColoursGroupBox)
        self.white_Pushbutton.setObjectName(u"white_Pushbutton")
        self.white_Pushbutton.setGeometry(QRect(609, 28, 145, 30))
        self.white_Pushbutton.setMinimumSize(QSize(145, 30))
        self.white_Pushbutton.setMaximumSize(QSize(145, 30))
        self.white_Pushbutton.setFont(font2)
        self.boxesView = QGraphicsView(self.ColoursGroupBox)
        self.boxesView.setObjectName(u"boxesView")
        self.boxesView.setGeometry(QRect(760, 30, 35, 25))
        self.boxesView.setMinimumSize(QSize(35, 25))
        self.boxesView.setMaximumSize(QSize(35, 25))
        self.boxesView.setFrameShadow(QFrame.Raised)
        self.resetBottomRightBtn = QPushButton(self.ColoursGroupBox)
        self.resetBottomRightBtn.setObjectName(u"resetBottomRightBtn")
        self.resetBottomRightBtn.setGeometry(QRect(542, 60, 61, 26))
        self.resetBottomRightBtn.setMinimumSize(QSize(61, 26))
        self.resetBottomRightBtn.setMaximumSize(QSize(61, 26))
        self.resetBottomRightBtn.setFont(font2)
        self.dark_grey_Pushbutton = QPushButton(self.ColoursGroupBox)
        self.dark_grey_Pushbutton.setObjectName(u"dark_grey_Pushbutton")
        self.dark_grey_Pushbutton.setGeometry(QRect(609, 58, 145, 30))
        self.dark_grey_Pushbutton.setMinimumSize(QSize(145, 30))
        self.dark_grey_Pushbutton.setMaximumSize(QSize(145, 30))
        self.dark_grey_Pushbutton.setFont(font2)
        self.botRightView = QGraphicsView(self.ColoursGroupBox)
        self.botRightView.setObjectName(u"botRightView")
        self.botRightView.setGeometry(QRect(760, 60, 35, 25))
        self.botRightView.setMinimumSize(QSize(35, 25))
        self.botRightView.setMaximumSize(QSize(35, 25))
        self.botRightView.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.ColoursGroupBox, 0, 0, 1, 1)

        self.DialogGroupBox = QGroupBox(LoginWindowSimulator)
        self.DialogGroupBox.setObjectName(u"DialogGroupBox")
        self.DialogGroupBox.setMinimumSize(QSize(270, 121))
        self.DialogGroupBox.setMaximumSize(QSize(545, 121))
        self.DialogGroupBox.setFont(font1)
        self.resizeDialogBtn = QPushButton(self.DialogGroupBox)
        self.resizeDialogBtn.setObjectName(u"resizeDialogBtn")
        self.resizeDialogBtn.setGeometry(QRect(140, 70, 121, 31))
        self.resizeDialogBtn.setMinimumSize(QSize(121, 31))
        self.resizeDialogBtn.setMaximumSize(QSize(121, 31))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(12)
        font3.setItalic(False)
        self.resizeDialogBtn.setFont(font3)
        self.boxesLocationBtn = QPushButton(self.DialogGroupBox)
        self.boxesLocationBtn.setObjectName(u"boxesLocationBtn")
        self.boxesLocationBtn.setGeometry(QRect(140, 30, 121, 31))
        self.boxesLocationBtn.setMinimumSize(QSize(121, 31))
        self.boxesLocationBtn.setMaximumSize(QSize(121, 31))
        font4 = QFont()
        font4.setPointSize(12)
        self.boxesLocationBtn.setFont(font4)
        self.logoPositionBtn = QPushButton(self.DialogGroupBox)
        self.logoPositionBtn.setObjectName(u"logoPositionBtn")
        self.logoPositionBtn.setGeometry(QRect(10, 70, 121, 31))
        self.logoPositionBtn.setMinimumSize(QSize(121, 31))
        self.logoPositionBtn.setMaximumSize(QSize(121, 31))
        self.logoPositionBtn.setFont(font4)
        self.buttonsLocationBtn = QPushButton(self.DialogGroupBox)
        self.buttonsLocationBtn.setObjectName(u"buttonsLocationBtn")
        self.buttonsLocationBtn.setGeometry(QRect(10, 30, 121, 31))
        self.buttonsLocationBtn.setMinimumSize(QSize(121, 31))
        self.buttonsLocationBtn.setMaximumSize(QSize(121, 31))
        self.buttonsLocationBtn.setFont(font4)

        self.gridLayout.addWidget(self.DialogGroupBox, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 5, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(LoginWindowSimulator)

        QMetaObject.connectSlotsByName(LoginWindowSimulator)
    # setupUi

    def retranslateUi(self, LoginWindowSimulator):
        self.miscGroupBox.setTitle("")
        self.closeWinSimBtn.setText(QCoreApplication.translate("LoginWindowSimulator", u"Close WinSim", None))
        self.previewINIBtn.setText(QCoreApplication.translate("LoginWindowSimulator", u"Preview INI", None))
        self.ColoursGroupBox.setTitle(QCoreApplication.translate("LoginWindowSimulator", u"Colours", None))
        self.resetWindowButton.setText(QCoreApplication.translate("LoginWindowSimulator", u"Default", None))
#if QT_CONFIG(tooltip)
        self.grey_Pushbutton.setToolTip(QCoreApplication.translate("LoginWindowSimulator", u"Sets the colour of the xrdp dialog windows", None))
#endif // QT_CONFIG(tooltip)
        self.grey_Pushbutton.setText(QCoreApplication.translate("LoginWindowSimulator", u"Dialogs", None))
        self.resetBackgroundButton.setText(QCoreApplication.translate("LoginWindowSimulator", u"Default", None))
#if QT_CONFIG(tooltip)
        self.background_Pushbutton.setToolTip(QCoreApplication.translate("LoginWindowSimulator", u"Sets the colour of the xrdp login screen background.", None))
#endif // QT_CONFIG(tooltip)
        self.background_Pushbutton.setText(QCoreApplication.translate("LoginWindowSimulator", u"Background", None))
        self.resetTitleBgndButton.setText(QCoreApplication.translate("LoginWindowSimulator", u"Default", None))
#if QT_CONFIG(tooltip)
        self.blue_Pushbutton.setToolTip(QCoreApplication.translate("LoginWindowSimulator", u"<html><head/><body><p>Sets the background colour of the dialog titles.</p><p>Also sets the highlight colour of the login module drop-down box.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.blue_Pushbutton.setText(QCoreApplication.translate("LoginWindowSimulator", u"Title Background", None))
#if QT_CONFIG(tooltip)
        self.black_Pushbutton.setToolTip(QCoreApplication.translate("LoginWindowSimulator", u"Sets the colour of the dialog text.", None))
#endif // QT_CONFIG(tooltip)
        self.black_Pushbutton.setText(QCoreApplication.translate("LoginWindowSimulator", u"Text", None))
        self.resetTextButton.setText(QCoreApplication.translate("LoginWindowSimulator", u"Default", None))
        self.resetSessionBoxHilightBtn.setText(QCoreApplication.translate("LoginWindowSimulator", u"Default", None))
#if QT_CONFIG(tooltip)
        self.dark_blue_Pushbutton.setToolTip(QCoreApplication.translate("LoginWindowSimulator", u"<html><head/><body><p>Sets the background colour of the module<br/>drop-down box's currently selected module.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dark_blue_Pushbutton.setText(QCoreApplication.translate("LoginWindowSimulator", u"Session Box Hilight", None))
        self.resetTopLeftTitleBoxesBtn.setText(QCoreApplication.translate("LoginWindowSimulator", u"Default", None))
#if QT_CONFIG(tooltip)
        self.white_Pushbutton.setToolTip(QCoreApplication.translate("LoginWindowSimulator", u"<html><head/><body><p>Sets the colour of the top and left &quot;shade&quot; lines of the dialogs.</p><p>Also sets the dialog title foreground colour, and the colour of<br/>the dialog input widgets/boxes.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.white_Pushbutton.setText(QCoreApplication.translate("LoginWindowSimulator", u"Title/Shading #1", None))
        self.resetBottomRightBtn.setText(QCoreApplication.translate("LoginWindowSimulator", u"Default", None))
#if QT_CONFIG(tooltip)
        self.dark_grey_Pushbutton.setToolTip(QCoreApplication.translate("LoginWindowSimulator", u"<html><head/><body><p>Sets the colour of the bottom and right &quot;shade&quot; lines of the login dialog window, and the buttons.</p><p>Also sets the colour of the left and top &quot;shade&quot; lines of the input boxes/widgets of the dialogs.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dark_grey_Pushbutton.setText(QCoreApplication.translate("LoginWindowSimulator", u"Shading #2", None))
        self.DialogGroupBox.setTitle(QCoreApplication.translate("LoginWindowSimulator", u"Dialog Customization", None))
        self.resizeDialogBtn.setText(QCoreApplication.translate("LoginWindowSimulator", u"Resize Dialog", None))
        self.boxesLocationBtn.setText(QCoreApplication.translate("LoginWindowSimulator", u"Boxes Location", None))
        self.logoPositionBtn.setText(QCoreApplication.translate("LoginWindowSimulator", u"Logo Position", None))
        self.buttonsLocationBtn.setText(QCoreApplication.translate("LoginWindowSimulator", u"Buttons", None))
        pass
    # retranslateUi

