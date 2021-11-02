# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pH_1.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(931, 512)
        self.adress=1
        self.verticalLayout_8 = QVBoxLayout(Form)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.LineEdit_2 = QLineEdit(Form)
        self.LineEdit_2.setObjectName(u"LineEdit_2")
        self.LineEdit_2.setMaximumSize(QSize(150, 16777215))
        self.LineEdit_2.setReadOnly(True)

        self.gridLayout.addWidget(self.LineEdit_2, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 2, 1, 1)

        self.Label_4 = QLabel(Form)
        self.Label_4.setObjectName(u"Label_4")

        self.gridLayout.addWidget(self.Label_4, 5, 0, 1, 1)

        self.Label_2 = QLabel(Form)
        self.Label_2.setObjectName(u"Label_2")

        self.gridLayout.addWidget(self.Label_2, 3, 0, 1, 1)

        self.LineEdit = QLineEdit(Form)
        self.LineEdit.setObjectName(u"LineEdit")
        self.LineEdit.setMaximumSize(QSize(150, 16777215))
        self.LineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.LineEdit, 2, 1, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        self.label_3.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(13)
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.Label_3 = QLabel(Form)
        self.Label_3.setObjectName(u"Label_3")

        self.gridLayout.addWidget(self.Label_3, 4, 0, 1, 1)

        self.Label = QLabel(Form)
        self.Label.setObjectName(u"Label")

        self.gridLayout.addWidget(self.Label, 2, 0, 1, 1)

        self.LineEdit_3 = QLineEdit(Form)
        self.LineEdit_3.setObjectName(u"LineEdit_3")
        self.LineEdit_3.setMaximumSize(QSize(150, 16777215))
        self.LineEdit_3.setReadOnly(True)

        self.gridLayout.addWidget(self.LineEdit_3, 4, 1, 1, 1)

        self.LineEdit_4 = QLineEdit(Form)
        self.LineEdit_4.setObjectName(u"LineEdit_4")
        self.LineEdit_4.setMaximumSize(QSize(150, 16777215))
        self.LineEdit_4.setReadOnly(True)

        self.gridLayout.addWidget(self.LineEdit_4, 5, 1, 1, 1)

        self.line_4 = QFrame(Form)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 1, 0, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.con = QPushButton(Form)
        self.con.setObjectName(u"con")

        self.horizontalLayout.addWidget(self.con)

        self.uncon = QPushButton(Form)
        self.uncon.setObjectName(u"uncon")

        self.horizontalLayout.addWidget(self.uncon)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.line_5 = QFrame(Form)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_5)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_2.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(9999999, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(9999999, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.verticalLayout_6.addWidget(self.label_6)

        self.textBrowser_2 = QTextBrowser(Form)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.verticalLayout_6.addWidget(self.textBrowser_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_7.addWidget(self.label_5)
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        font1 = QFont()
        font1.setBold(False)
        font1.setKerning(False)
        self.textBrowser.setFont(font1)
        self.verticalLayout_7.addWidget(self.textBrowser)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.retranslateUi(Form)

        # 弹窗UI文件
        self.diglog=QDialog()
        self.diglog.edit = QLineEdit()

        self.diglog.button = QPushButton("连接")
        self.diglog.la = QLabel()
        self.diglog.la.setText("请输入从机地址")
        self.diglog.setWindowTitle("建立连接")
        layout = QVBoxLayout()
        layout.addWidget(self.diglog.la)
        layout.addWidget(self.diglog.edit)
        layout.addWidget(self.diglog.button)
        self.diglog.setLayout(layout)
        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Label_4.setText(QCoreApplication.translate("Form", u"\u6821\u51c6\u8fc7\u7a0b\u72b6\u6001\u503c", None))
        self.Label_2.setText(QCoreApplication.translate("Form", u"\u7535\u5bfc\u7387\u503c", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u8bbe\u5907\u901a\u8baf\u503c", None))
        self.Label_3.setText(QCoreApplication.translate("Form", u"\u53d8\u9001\u5668\u5730\u5740", None))
        self.Label.setText(QCoreApplication.translate("Form", u"\u6821\u51c6\u6807\u51c6\u6db2\u5bf9\u5e94\u503c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8fde\u63a5\u8bbe\u5907", None))
        self.con.setText(QCoreApplication.translate("Form", u"\u8fde\u63a5", None))
        self.uncon.setText(QCoreApplication.translate("Form", u"\u65ad\u5f00", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u4fee\u6539\u53d8\u9001\u5668\u5730\u5740", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u4fee\u6539", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u590d\u4f4d", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u4e00\u952e\u6821\u51c6", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u5f00\u542f", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u7ec8\u6b62", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u8bbe\u5907\u4fe1\u606f", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#000000;\">\u8bbe\u5907\u53c2\u6570</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">EC \u91cf\u7a0b \u53ef\u9009\uff1a0-440uS/cm\u30010-4400uS/cm\u30010-44000uS/cm </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">EC \u7cbe\u5ea6 \u2264\u00b12% F.S </span></p>\n"
"<p style=\""
                        " margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">TDS \u91cf\u7a0b \u53ef\u9009\uff1a0-200PPM\u30010-2000PPM\u30010-20000PPM </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">TDS \u7cbe\u5ea6 \u2264\u00b12% F.S </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u4f9b\u7535\u7535\u6e90 DC:12V\uff5e24V </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u6ce2\u7279\u7387\u8303\u56f4 9600\uff08\u6682\u65f6\u4e0d\u652f\u6301\u8bbe\u5b9a\uff09 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:"
                        "0px;\"><span style=\" font-size:10pt;\">\u901a\u8baf\u7aef\u53e3 RS485 \u901a\u8baf\u957f\u5ea6 \u22641200 \u7c73 </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#000000;\">\u6821\u51c6\u6b65\u9aa4\uff08\u624b\u52a8\uff09</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1\u3001\u7528\u65e0CO2\u84b8\u998f\u6c34\u5c06\u7535\u6781\u6e05\u6d17\u5e72\u51c0\u5e76\u7528\u67d4\u7eb8\u5dfe\u62ed\u5e72\u3002 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2\u3001\u6b63\u786e\u63a5\u597d"
                        "\u53d8\u9001\u5668\u7535\u6e90\u548c\u7535\u6781\u3002 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3\u3001\u957f\u6309\u6821\u51c6\u6309\u952e\u76f4\u5230\u6821\u51c6\u6307\u793a\u706f\u4eae\u9ec4\u8272\uff0c\u7136\u540e\u677e\u5f00\u6309\u952e\u3002 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4\u3001\u5feb\u901f\u6309\u538b\u6821\u51c6\u6309\u952e\u4e24\u6b21\u76f4\u5230\u6821\u51c6\u6307\u793a\u706f\u7ea2\u8272\u95ea\u70c1\uff0c\u6b64\u65f6\u53d8\u9001\u5668\u8fdb\u5165\u96f6\u70b9\u6821\u51c6\u8fc7\u7a0b\u4e2d \uff08\u6b64\u8fc7\u7a0b\u65f6\u957f\u4e3a30\u79d2\uff09\uff0c\u6821\u51c6\u5b8c\u540e\u6821\u51c6\u6307\u793a\u706f\u7ea2\u8272\u5e38\u4eae\u3002 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block"
                        "-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">5\u3001\u6821\u51c6\u6307\u793a\u706f\u7ea2\u8272\u5e38\u4eae\u540e\u5c06\u7535\u6781\u6d78\u5165\u5230\u51c6\u5907\u597d\u7684\u6807\u51c6\u6db2\u4e2d\uff0c\u4e0d\u540c\u91cf\u7a0b\u548c\u5bf9\u5e94\u6807\u51c6\u6db2\u5982\u4e0b\uff1a 0-440uS\u91cf\u7a0b\u5bf9\u5e94\u6807\u51c6\u6db2\uff1a 146.5uS/cm 0-4400uS\u548c0-2000ppm\u91cf\u7a0b\u5bf9\u5e94\u6807\u51c6\u6db2\uff1a1413uS/cm 0-44000uS\u91cf\u7a0b\u5bf9\u5e94\u6807\u51c6\u6db2\uff1a12.88mS/cm </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">6\u3001\u5feb\u901f\u6309\u538b\u6821\u51c6\u6309\u952e\u4e00\u6b21\u6b64\u65f6\u6821\u51c6\u6307\u793a\u706f\u7eff\u8272\u95ea\u70c1\uff0c\u53d8\u9001\u5668\u8fdb\u5165\u6821\u51c6\u6807\u51c6\u70b9\u8fc7\u7a0b\u4e2d \uff08\u6b64\u8fc7\u7a0b\u65f6\u957f\u4e3a30\u79d2\uff09\uff0c\u6821\u51c6\u5b8c\u540e\u6821\u51c6\u6307\u793a\u706f\u7eff"
                        "\u8272\u5e38\u4eae20\u79d2\uff0c\u7136\u540e\u9ec4\u8272\u95ea\u70c120\u79d2\u63d0\u793a\u5373 \u5c06\u8fdb\u884c\u6821\u51c6\u6570\u636e\u4fdd\u5b58\u3002 </span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u64cd\u4f5c\u65e5\u5fd7", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi


# class Dialog(QDialog):
#     def __init__(self, parent=None):
#         super(Dialog, self).__init__(parent)
#         # Create widgets
#         self.edit = QLineEdit()
#         self.button = QPushButton("Show Greetings")
#         self.la=QLabel()
#         self.la.setText("请输入从机地址")
#         self.button.clicked.connect(self.getText)
#         self.button.clicked.connect(self.accept)
#         self.setWindowTitle("建立连接")
#         # Create layout and add widgets
#         layout= QVBoxLayout()
#         layout.addWidget(self.la)
#         layout.addWidget(self.edit)
#         layout.addWidget(self.button)
#         self.setLayout(layout)
#     def getText(self):
#         return self.la.text()

