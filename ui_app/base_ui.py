# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 500)
        MainWindow.setMinimumSize(QSize(750, 400))
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        MainWindow.setAnimated(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, 3, 6, 6)
        self.frm_left_menu = QFrame(self.centralwidget)
        self.frm_left_menu.setObjectName(u"frm_left_menu")
        self.frm_left_menu.setMinimumSize(QSize(110, 400))
        self.frm_left_menu.setMaximumSize(QSize(110, 16777215))
        self.frm_left_menu.setStyleSheet(u"")
        self.frm_left_menu.setFrameShape(QFrame.NoFrame)
        self.frm_left_menu.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frm_left_menu)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 9, 2, 5)
        self.lbl_menu = QLabel(self.frm_left_menu)
        self.lbl_menu.setObjectName(u"lbl_menu")
        self.lbl_menu.setMaximumSize(QSize(16777215, 50))
        self.lbl_menu.setStyleSheet(u"")
        self.lbl_menu.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_menu)

        self.line = QFrame(self.frm_left_menu)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.btn_raw_input = QPushButton(self.frm_left_menu)
        self.btn_raw_input.setObjectName(u"btn_raw_input")
        self.btn_raw_input.setStyleSheet(u"")
        self.btn_raw_input.setFlat(False)

        self.verticalLayout.addWidget(self.btn_raw_input)

        self.btn_file_input = QPushButton(self.frm_left_menu)
        self.btn_file_input.setObjectName(u"btn_file_input")
        self.btn_file_input.setFlat(False)

        self.verticalLayout.addWidget(self.btn_file_input)

        self.btn_key_maker = QPushButton(self.frm_left_menu)
        self.btn_key_maker.setObjectName(u"btn_key_maker")
        self.btn_key_maker.setFlat(False)

        self.verticalLayout.addWidget(self.btn_key_maker)

        self.verticalSpacer = QSpacerItem(20, 159, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.line_2 = QFrame(self.frm_left_menu)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line_2)

        self.btn_exit = QPushButton(self.frm_left_menu)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setFlat(False)

        self.verticalLayout.addWidget(self.btn_exit)


        self.horizontalLayout_6.addWidget(self.frm_left_menu)

        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShadow(QFrame.Plain)
        self.line_7.setFrameShape(QFrame.VLine)

        self.horizontalLayout_6.addWidget(self.line_7)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(600, 485))
        self.stackedWidget.setStyleSheet(u"")
        self.page_raw = QWidget()
        self.page_raw.setObjectName(u"page_raw")
        self.verticalLayout_2 = QVBoxLayout(self.page_raw)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frm_top_page_raw = QFrame(self.page_raw)
        self.frm_top_page_raw.setObjectName(u"frm_top_page_raw")
        self.frm_top_page_raw.setMinimumSize(QSize(600, 30))
        self.frm_top_page_raw.setMaximumSize(QSize(16777215, 30))
        self.frm_top_page_raw.setFrameShape(QFrame.StyledPanel)
        self.frm_top_page_raw.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frm_top_page_raw)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 6, 2, 6)
        self.lbl_top_raw = QLabel(self.frm_top_page_raw)
        self.lbl_top_raw.setObjectName(u"lbl_top_raw")

        self.horizontalLayout.addWidget(self.lbl_top_raw)


        self.verticalLayout_2.addWidget(self.frm_top_page_raw)

        self.line_4 = QFrame(self.page_raw)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setFrameShape(QFrame.HLine)

        self.verticalLayout_2.addWidget(self.line_4)

        self.frm_page_raw = QFrame(self.page_raw)
        self.frm_page_raw.setObjectName(u"frm_page_raw")
        self.frm_page_raw.setMinimumSize(QSize(600, 450))
        self.frm_page_raw.setFrameShape(QFrame.StyledPanel)
        self.frm_page_raw.setFrameShadow(QFrame.Raised)
        self.lyt_page_raw = QVBoxLayout(self.frm_page_raw)
        self.lyt_page_raw.setSpacing(4)
        self.lyt_page_raw.setObjectName(u"lyt_page_raw")
        self.lyt_page_raw.setContentsMargins(2, 2, 2, 4)

        self.verticalLayout_2.addWidget(self.frm_page_raw)

        self.stackedWidget.addWidget(self.page_raw)
        self.page_file = QWidget()
        self.page_file.setObjectName(u"page_file")
        self.verticalLayout_7 = QVBoxLayout(self.page_file)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frm_top_page_file = QFrame(self.page_file)
        self.frm_top_page_file.setObjectName(u"frm_top_page_file")
        self.frm_top_page_file.setMinimumSize(QSize(600, 30))
        self.frm_top_page_file.setMaximumSize(QSize(16777215, 30))
        self.frm_top_page_file.setFrameShape(QFrame.StyledPanel)
        self.frm_top_page_file.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frm_top_page_file)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(2, 6, 2, 6)
        self.lbl_top_file = QLabel(self.frm_top_page_file)
        self.lbl_top_file.setObjectName(u"lbl_top_file")

        self.horizontalLayout_4.addWidget(self.lbl_top_file)


        self.verticalLayout_7.addWidget(self.frm_top_page_file)

        self.line_5 = QFrame(self.page_file)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setFrameShape(QFrame.HLine)

        self.verticalLayout_7.addWidget(self.line_5)

        self.frm_page_file = QFrame(self.page_file)
        self.frm_page_file.setObjectName(u"frm_page_file")
        self.frm_page_file.setMinimumSize(QSize(600, 450))
        self.frm_page_file.setFrameShape(QFrame.StyledPanel)
        self.frm_page_file.setFrameShadow(QFrame.Raised)
        self.lyt_page_file = QVBoxLayout(self.frm_page_file)
        self.lyt_page_file.setSpacing(4)
        self.lyt_page_file.setObjectName(u"lyt_page_file")
        self.lyt_page_file.setContentsMargins(2, 2, 2, 4)

        self.verticalLayout_7.addWidget(self.frm_page_file)

        self.stackedWidget.addWidget(self.page_file)
        self.page_key_maker = QWidget()
        self.page_key_maker.setObjectName(u"page_key_maker")
        self.verticalLayout_5 = QVBoxLayout(self.page_key_maker)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frm_top_page_key_maker = QFrame(self.page_key_maker)
        self.frm_top_page_key_maker.setObjectName(u"frm_top_page_key_maker")
        self.frm_top_page_key_maker.setMinimumSize(QSize(600, 30))
        self.frm_top_page_key_maker.setMaximumSize(QSize(16777215, 30))
        self.frm_top_page_key_maker.setFrameShape(QFrame.StyledPanel)
        self.frm_top_page_key_maker.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frm_top_page_key_maker)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 6, 2, 6)
        self.lbl_top_key_maker = QLabel(self.frm_top_page_key_maker)
        self.lbl_top_key_maker.setObjectName(u"lbl_top_key_maker")

        self.horizontalLayout_3.addWidget(self.lbl_top_key_maker)


        self.verticalLayout_5.addWidget(self.frm_top_page_key_maker)

        self.line_6 = QFrame(self.page_key_maker)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setFrameShape(QFrame.HLine)

        self.verticalLayout_5.addWidget(self.line_6)

        self.frm_page_key_maker = QFrame(self.page_key_maker)
        self.frm_page_key_maker.setObjectName(u"frm_page_key_maker")
        self.frm_page_key_maker.setMinimumSize(QSize(600, 450))
        self.frm_page_key_maker.setFrameShape(QFrame.StyledPanel)
        self.frm_page_key_maker.setFrameShadow(QFrame.Raised)
        self.lyt_page_key = QVBoxLayout(self.frm_page_key_maker)
        self.lyt_page_key.setSpacing(4)
        self.lyt_page_key.setObjectName(u"lyt_page_key")
        self.lyt_page_key.setContentsMargins(2, 2, 2, 4)

        self.verticalLayout_5.addWidget(self.frm_page_key_maker)

        self.stackedWidget.addWidget(self.page_key_maker)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.verticalLayout_9 = QVBoxLayout(self.page_setting)
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frm_top_page_setting = QFrame(self.page_setting)
        self.frm_top_page_setting.setObjectName(u"frm_top_page_setting")
        self.frm_top_page_setting.setMinimumSize(QSize(600, 30))
        self.frm_top_page_setting.setMaximumSize(QSize(16777215, 30))
        self.frm_top_page_setting.setFrameShape(QFrame.StyledPanel)
        self.frm_top_page_setting.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frm_top_page_setting)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(2, 6, 2, 6)
        self.lbl_top_setting = QLabel(self.frm_top_page_setting)
        self.lbl_top_setting.setObjectName(u"lbl_top_setting")

        self.horizontalLayout_5.addWidget(self.lbl_top_setting)


        self.verticalLayout_9.addWidget(self.frm_top_page_setting)

        self.line_3 = QFrame(self.page_setting)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setFrameShape(QFrame.HLine)

        self.verticalLayout_9.addWidget(self.line_3)

        self.frm_page_setting = QFrame(self.page_setting)
        self.frm_page_setting.setObjectName(u"frm_page_setting")
        self.frm_page_setting.setMinimumSize(QSize(600, 450))
        self.frm_page_setting.setFrameShape(QFrame.StyledPanel)
        self.frm_page_setting.setFrameShadow(QFrame.Raised)
        self.lyt_page_setting = QVBoxLayout(self.frm_page_setting)
        self.lyt_page_setting.setSpacing(4)
        self.lyt_page_setting.setObjectName(u"lyt_page_setting")
        self.lyt_page_setting.setContentsMargins(2, 2, 2, 4)

        self.verticalLayout_9.addWidget(self.frm_page_setting)

        self.stackedWidget.addWidget(self.page_setting)

        self.horizontalLayout_6.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Nested Foam", None))
        self.lbl_menu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.btn_raw_input.setText(QCoreApplication.translate("MainWindow", u"Raw Input", None))
        self.btn_file_input.setText(QCoreApplication.translate("MainWindow", u"File Input", None))
        self.btn_key_maker.setText(QCoreApplication.translate("MainWindow", u"Key Maker", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.lbl_top_raw.setText(QCoreApplication.translate("MainWindow", u"Raw Input", None))
        self.lbl_top_file.setText(QCoreApplication.translate("MainWindow", u"File Input", None))
        self.lbl_top_key_maker.setText(QCoreApplication.translate("MainWindow", u"Key Maker", None))
        self.lbl_top_setting.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
    # retranslateUi

