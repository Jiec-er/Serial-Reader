# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Equ_mian.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Equitmen(object):
    def setupUi(self, Equitmen):
        if not Equitmen.objectName():
            Equitmen.setObjectName(u"Equitmen")
        Equitmen.resize(698, 317)
        Equitmen.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Academy Engraved LET"])
        font.setPointSize(10)
        Equitmen.setFont(font)
        Equitmen.setMouseTracking(True)
        self.action = QAction(Equitmen)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(Equitmen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.PH_text = QLabel(self.centralwidget)
        self.PH_text.setObjectName(u"PH_text")
        font1 = QFont()
        font1.setFamilies([u"\u9ed1\u4f53"])
        font1.setPointSize(12)
        self.PH_text.setFont(font1)

        self.horizontalLayout.addWidget(self.PH_text)

        self.pH_2 = QPushButton(self.centralwidget)
        self.pH_2.setObjectName(u"pH_2")
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(10)
        self.pH_2.setFont(font2)

        self.horizontalLayout.addWidget(self.pH_2)

        self.pH_1 = QPushButton(self.centralwidget)
        self.pH_1.setObjectName(u"pH_1")
        self.pH_1.setFont(font2)

        self.horizontalLayout.addWidget(self.pH_1)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.EC_text = QLabel(self.centralwidget)
        self.EC_text.setObjectName(u"EC_text")
        self.EC_text.setFont(font1)

        self.horizontalLayout_4.addWidget(self.EC_text)

        self.EC_2 = QPushButton(self.centralwidget)
        self.EC_2.setObjectName(u"EC_2")
        self.EC_2.setFont(font2)

        self.horizontalLayout_4.addWidget(self.EC_2)

        self.EC_1 = QPushButton(self.centralwidget)
        self.EC_1.setObjectName(u"EC_1")
        self.EC_1.setFont(font2)

        self.horizontalLayout_4.addWidget(self.EC_1)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Title = QLabel(self.centralwidget)
        self.Title.setObjectName(u"Title")
        self.Title.setMinimumSize(QSize(0, 53))
        self.Title.setMaximumSize(QSize(16777215, 200))
        font3 = QFont()
        font3.setFamilies([u"\u9ed1\u4f53"])
        font3.setPointSize(22)
        self.Title.setFont(font3)

        self.horizontalLayout_2.addWidget(self.Title)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout_2.addWidget(self.textBrowser)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Water_text = QLabel(self.centralwidget)
        self.Water_text.setObjectName(u"Water_text")
        self.Water_text.setFont(font1)

        self.horizontalLayout_6.addWidget(self.Water_text)

        self.Water_01 = QPushButton(self.centralwidget)
        self.Water_01.setObjectName(u"Water_01")
        self.Water_01.setFont(font2)

        self.horizontalLayout_6.addWidget(self.Water_01)


        self.gridLayout.addLayout(self.horizontalLayout_6, 4, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_11)

        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font2)

        self.horizontalLayout_8.addWidget(self.pushButton_11)


        self.gridLayout.addLayout(self.horizontalLayout_8, 5, 0, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 6, 0, 1, 1)

        Equitmen.setCentralWidget(self.centralwidget)

        self.retranslateUi(Equitmen)

        QMetaObject.connectSlotsByName(Equitmen)
    # setupUi

    def retranslateUi(self, Equitmen):
        Equitmen.setWindowTitle(QCoreApplication.translate("Equitmen", u"Equipment  Center", None))
        self.action.setText(QCoreApplication.translate("Equitmen", u"\u4f7f\u7528", None))
#if QT_CONFIG(tooltip)
        self.action.setToolTip(QCoreApplication.translate("Equitmen", u"<html><head/><body><p>\u963f\u8428\u5fb7\u963f\u8fbe\u6536\u5230\u963f\u8fbe\u7684\u963f\u8fbe\u6492\u963f\u8428\u5fb7</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.PH_text.setText(QCoreApplication.translate("Equitmen", u"pH\u4f20\u611f\u5668", None))
        self.pH_2.setText(QCoreApplication.translate("Equitmen", u"pH 20_2", None))
        self.pH_1.setText(QCoreApplication.translate("Equitmen", u"pH 21_1", None))
        self.EC_text.setText(QCoreApplication.translate("Equitmen", u"\u7535\u5bfc\u7387\u4f20\u611f\u5668", None))
        self.EC_2.setText(QCoreApplication.translate("Equitmen", u"CON 20_1", None))
        self.EC_1.setText(QCoreApplication.translate("Equitmen", u"CON 21_1", None))
        self.Title.setText(QCoreApplication.translate("Equitmen", u"QQM\u8bbe\u5907\u5217\u8868", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Equitmen", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Academy Engraved LET'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:'Arial'; font-size:12.8pt; color:#a9b7c6; background-color:#2b2b2b;\">Welcom to Root of Equ</span><span style=\" font-family:'Arial'; font-size:12.8pt; color:#a9b7c6;\"><br /></span><span style=\" font-family:'Droid Sans Mono Slashed'; font-size:12.8pt; color:#a9b7c6;\">AUTHOR:GJ<br />DATA:</span><span style=\" font-family:'Droid Sans Mono Slashed'; font-size:12.8pt; color:#6897bb;\">2021</span><span style=\" font-family:'"
                        "Droid Sans Mono Slashed'; font-size:12.8pt; color:#a9b7c6;\">/</span><span style=\" font-family:'Droid Sans Mono Slashed'; font-size:12.8pt; color:#6897bb;\">8</span><span style=\" font-family:'Droid Sans Mono Slashed'; font-size:12.8pt; color:#a9b7c6;\">/</span><span style=\" font-family:'Droid Sans Mono Slashed'; font-size:12.8pt; color:#6897bb;\">8<br /></span><span style=\" font-family:'Droid Sans Mono Slashed'; font-size:12.8pt; color:#a9b7c6;\">VERSION:</span><span style=\" font-family:'Droid Sans Mono Slashed'; font-size:12.8pt; color:#6897bb;\">1.0<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /></span></p></body></html>", None))
        self.Water_text.setText(QCoreApplication.translate("Equitmen", u"\u6db2\u4f4d\u8ba1\u4f20\u611f\u5668", None))
        self.Water_01.setText(QCoreApplication.translate("Equitmen", u"SLP21_1", None))
        self.label_11.setText(QCoreApplication.translate("Equitmen", u"...", None))
        self.pushButton_11.setText(QCoreApplication.translate("Equitmen", u"...", None))
    # retranslateUi

