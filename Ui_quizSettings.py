# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_quizSettings.ui'
#
# Created: Fri Aug 12 01:04:17 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_quizSettings(object):
    def setupUi(self, quizSettings):
        quizSettings.setObjectName("quizSettings")
        quizSettings.resize(350, 265)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(quizSettings.sizePolicy().hasHeightForWidth())
        quizSettings.setSizePolicy(sizePolicy)
        quizSettings.setMinimumSize(QtCore.QSize(350, 265))
        quizSettings.setMaximumSize(QtCore.QSize(350, 265))
        self.startButton = QtGui.QPushButton(quizSettings)
        self.startButton.setGeometry(QtCore.QRect(240, 225, 100, 30))
        self.startButton.setObjectName("startButton")
        self.cancelButton = QtGui.QPushButton(quizSettings)
        self.cancelButton.setGeometry(QtCore.QRect(130, 225, 100, 30))
        self.cancelButton.setObjectName("cancelButton")
        self.frame = QtGui.QFrame(quizSettings)
        self.frame.setGeometry(QtCore.QRect(10, 30, 330, 140))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtGui.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 310, 120))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.hirCheck = QtGui.QCheckBox(self.layoutWidget)
        self.hirCheck.setChecked(True)
        self.hirCheck.setTristate(False)
        self.hirCheck.setObjectName("hirCheck")
        self.gridLayout.addWidget(self.hirCheck, 0, 0, 1, 1)
        self.katCheck = QtGui.QCheckBox(self.layoutWidget)
        self.katCheck.setObjectName("katCheck")
        self.gridLayout.addWidget(self.katCheck, 0, 1, 1, 1)
        self.hirHanCheck = QtGui.QCheckBox(self.layoutWidget)
        self.hirHanCheck.setObjectName("hirHanCheck")
        self.gridLayout.addWidget(self.hirHanCheck, 1, 0, 1, 1)
        self.katHanCheck = QtGui.QCheckBox(self.layoutWidget)
        self.katHanCheck.setObjectName("katHanCheck")
        self.gridLayout.addWidget(self.katHanCheck, 1, 1, 1, 1)
        self.hirYoonCheck = QtGui.QCheckBox(self.layoutWidget)
        self.hirYoonCheck.setCheckable(False)
        self.hirYoonCheck.setObjectName("hirYoonCheck")
        self.gridLayout.addWidget(self.hirYoonCheck, 2, 0, 1, 1)
        self.katYoonCheck = QtGui.QCheckBox(self.layoutWidget)
        self.katYoonCheck.setCheckable(False)
        self.katYoonCheck.setObjectName("katYoonCheck")
        self.gridLayout.addWidget(self.katYoonCheck, 2, 1, 1, 1)
        self.layoutWidget1 = QtGui.QWidget(quizSettings)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 170, 331, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox = QtGui.QSpinBox(self.layoutWidget1)
        self.spinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox.setSuffix("")
        self.spinBox.setMinimum(5)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.setContent = QtGui.QLabel(quizSettings)
        self.setContent.setGeometry(QtCore.QRect(10, 0, 330, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.setContent.setFont(font)
        self.setContent.setObjectName("setContent")

        self.retranslateUi(quizSettings)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), quizSettings.close)
        QtCore.QMetaObject.connectSlotsByName(quizSettings)

    def retranslateUi(self, quizSettings):
        quizSettings.setWindowTitle(QtGui.QApplication.translate("quizSettings", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setText(QtGui.QApplication.translate("quizSettings", "Start Quiz", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("quizSettings", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.hirCheck.setText(QtGui.QApplication.translate("quizSettings", "Hiragana", None, QtGui.QApplication.UnicodeUTF8))
        self.katCheck.setText(QtGui.QApplication.translate("quizSettings", "Katakana", None, QtGui.QApplication.UnicodeUTF8))
        self.hirHanCheck.setText(QtGui.QApplication.translate("quizSettings", "Hiragana with\n"
"handakuten", None, QtGui.QApplication.UnicodeUTF8))
        self.katHanCheck.setText(QtGui.QApplication.translate("quizSettings", "Katakana with \n"
"handakuten", None, QtGui.QApplication.UnicodeUTF8))
        self.hirYoonCheck.setText(QtGui.QApplication.translate("quizSettings", "Hiragana with \n"
" yōon", None, QtGui.QApplication.UnicodeUTF8))
        self.katYoonCheck.setText(QtGui.QApplication.translate("quizSettings", "Katakana with \n"
"yōon", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("quizSettings", "How many questions \n"
"do you want to take?", None, QtGui.QApplication.UnicodeUTF8))
        self.setContent.setText(QtGui.QApplication.translate("quizSettings", "Please select your quiz content", None, QtGui.QApplication.UnicodeUTF8))

