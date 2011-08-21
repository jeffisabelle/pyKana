# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_about.ui'
#
# Created: Sun Aug 21 18:56:43 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 255)
        Dialog.setWindowOpacity(1.0)
        Dialog.setAutoFillBackground(True)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 10, 461, 201))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.labelImg = QtGui.QLabel(self.frame)
        self.labelImg.setGeometry(QtCore.QRect(270, 0, 261, 211))
        self.labelImg.setText("")
        self.labelImg.setPixmap(QtGui.QPixmap("imgs/icons/avatar.png"))
        self.labelImg.setObjectName("labelImg")
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(5, 10, 311, 181))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(5, 100, 271, 17))
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 215, 141, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "About PyKana", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "PyKana is licensed under GNU/GPL v3\n"
"You are totally free to share, modify and\n"
"redistribute it under the terms of GNU GPL.\n"
"\n"
"To get the source code, please see below;\n"
"\n"
"\n"
"Please feel safe to cantact me if you need\n"
"any help or if you got any feedback.\n"
"muhammet[at]muhammetcan.net", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/jeffisabelle/pyKana\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/jeffisabelle/pyKana</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "See License", None, QtGui.QApplication.UnicodeUTF8))

