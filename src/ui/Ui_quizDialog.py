# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_quizDialog.ui'
#
# Created: Fri Aug 12 18:36:19 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_quizDialog(object):
    def setupUi(self, quizDialog):
        quizDialog.setObjectName("quizDialog")
        quizDialog.resize(540, 600)
        quizDialog.setMinimumSize(QtCore.QSize(540, 600))
        quizDialog.setMaximumSize(QtCore.QSize(540, 600))
        self.responseLabel = QtGui.QLabel(quizDialog)
        self.responseLabel.setGeometry(QtCore.QRect(130, 550, 330, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.responseLabel.setFont(font)
        self.responseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.responseLabel.setObjectName("responseLabel")
        self.iconLabel = QtGui.QLabel(quizDialog)
        self.iconLabel.setGeometry(QtCore.QRect(90, 556, 30, 32))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iconLabel.sizePolicy().hasHeightForWidth())
        self.iconLabel.setSizePolicy(sizePolicy)
        self.iconLabel.setText("")
        self.iconLabel.setPixmap(QtGui.QPixmap("imgs/icons/qdlg_get.png"))
        self.iconLabel.setObjectName("iconLabel")
        self.btn1 = QtGui.QPushButton(quizDialog)
        self.btn1.setGeometry(QtCore.QRect(40, 520, 110, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy)
        self.btn1.setObjectName("btn1")
        self.btn2 = QtGui.QPushButton(quizDialog)
        self.btn2.setGeometry(QtCore.QRect(152, 520, 110, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy)
        self.btn2.setObjectName("btn2")
        self.btn3 = QtGui.QPushButton(quizDialog)
        self.btn3.setGeometry(QtCore.QRect(264, 520, 110, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy)
        self.btn3.setObjectName("btn3")
        self.btn4 = QtGui.QPushButton(quizDialog)
        self.btn4.setGeometry(QtCore.QRect(375, 520, 110, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy)
        self.btn4.setObjectName("btn4")
        self.frame = QtGui.QFrame(quizDialog)
        self.frame.setGeometry(QtCore.QRect(20, 9, 500, 500))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.imgLabel = QtGui.QLabel(self.frame)
        self.imgLabel.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.imgLabel.setMaximumSize(QtCore.QSize(500, 500))
        self.imgLabel.setText("")
        self.imgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imgLabel.setObjectName("imgLabel")

        self.retranslateUi(quizDialog)
        QtCore.QMetaObject.connectSlotsByName(quizDialog)

    def retranslateUi(self, quizDialog):
        quizDialog.setWindowTitle(QtGui.QApplication.translate("quizDialog", "Ganbatte!", None, QtGui.QApplication.UnicodeUTF8))
        self.responseLabel.setText(QtGui.QApplication.translate("quizDialog", "you can get your response from here", None, QtGui.QApplication.UnicodeUTF8))
        self.btn1.setText(QtGui.QApplication.translate("quizDialog", "Ka", None, QtGui.QApplication.UnicodeUTF8))
        self.btn2.setText(QtGui.QApplication.translate("quizDialog", "Ri", None, QtGui.QApplication.UnicodeUTF8))
        self.btn3.setText(QtGui.QApplication.translate("quizDialog", "So", None, QtGui.QApplication.UnicodeUTF8))
        self.btn4.setText(QtGui.QApplication.translate("quizDialog", "U", None, QtGui.QApplication.UnicodeUTF8))

