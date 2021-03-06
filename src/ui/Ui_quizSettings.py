# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_quizSettings.ui'
#
# Created: Sun Aug 21 23:57:32 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_quizSettings(object):
    def setupUi(self, quizSettings):
        quizSettings.setObjectName("quizSettings")
        quizSettings.resize(350, 280)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(quizSettings.sizePolicy().hasHeightForWidth())
        quizSettings.setSizePolicy(sizePolicy)
        quizSettings.setMinimumSize(QtCore.QSize(350, 280))
        quizSettings.setMaximumSize(QtCore.QSize(350, 280))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imgs/icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        quizSettings.setWindowIcon(icon)
        self.startButton = QtGui.QPushButton(quizSettings)
        self.startButton.setGeometry(QtCore.QRect(240, 240, 100, 30))
        self.startButton.setObjectName("startButton")
        self.cancelButton = QtGui.QPushButton(quizSettings)
        self.cancelButton.setGeometry(QtCore.QRect(130, 240, 100, 30))
        self.cancelButton.setObjectName("cancelButton")
        self.frame = QtGui.QFrame(quizSettings)
        self.frame.setGeometry(QtCore.QRect(10, 90, 330, 141))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtGui.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 312, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.specifyContent = QtGui.QLabel(self.layoutWidget)
        self.specifyContent.setObjectName("specifyContent")
        self.gridLayout.addWidget(self.specifyContent, 0, 0, 1, 1)
        self.checkDakuten = QtGui.QCheckBox(self.layoutWidget)
        self.checkDakuten.setObjectName("checkDakuten")
        self.gridLayout.addWidget(self.checkDakuten, 1, 0, 1, 1)
        self.checkYoon = QtGui.QCheckBox(self.layoutWidget)
        self.checkYoon.setCheckable(True)
        self.checkYoon.setObjectName("checkYoon")
        self.gridLayout.addWidget(self.checkYoon, 2, 0, 1, 1)
        self.gorsel1 = QtGui.QLabel(self.layoutWidget)
        self.gorsel1.setText("")
        self.gorsel1.setPixmap(QtGui.QPixmap(":/imgs/icons/handaku.png"))
        self.gorsel1.setObjectName("gorsel1")
        self.gridLayout.addWidget(self.gorsel1, 1, 1, 1, 1)
        self.gorsel2 = QtGui.QLabel(self.layoutWidget)
        self.gorsel2.setText("")
        self.gorsel2.setPixmap(QtGui.QPixmap(":/imgs/icons/yoon.png"))
        self.gorsel2.setObjectName("gorsel2")
        self.gridLayout.addWidget(self.gorsel2, 2, 1, 1, 1)
        self.layoutWidget1 = QtGui.QWidget(quizSettings)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 1, 331, 91))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.setContent = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.setContent.setFont(font)
        self.setContent.setObjectName("setContent")
        self.gridLayout_2.addWidget(self.setContent, 0, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.layoutWidget1)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 27))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.layoutWidget1)
        self.spinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox.setSuffix("")
        self.spinBox.setMinimum(5)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 1, 1, 1, 1)

        self.retranslateUi(quizSettings)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), quizSettings.close)
        QtCore.QMetaObject.connectSlotsByName(quizSettings)

    def retranslateUi(self, quizSettings):
        quizSettings.setWindowTitle(QtGui.QApplication.translate("quizSettings", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setText(QtGui.QApplication.translate("quizSettings", "Start Quiz", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("quizSettings", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.specifyContent.setText(QtGui.QApplication.translate("quizSettings", "Specify the content of the quiz       ", None, QtGui.QApplication.UnicodeUTF8))
        self.checkDakuten.setText(QtGui.QApplication.translate("quizSettings", "Include (han)dakuten\n"
"characters to quiz", None, QtGui.QApplication.UnicodeUTF8))
        self.checkYoon.setText(QtGui.QApplication.translate("quizSettings", "Include yōon \n"
"characters to quiz", None, QtGui.QApplication.UnicodeUTF8))
        self.setContent.setText(QtGui.QApplication.translate("quizSettings", "Select Character Set", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("quizSettings", "Hiragana", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("quizSettings", "Katakana", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("quizSettings", "Both", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("quizSettings", "How many questions \n"
"do you want to take?", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
