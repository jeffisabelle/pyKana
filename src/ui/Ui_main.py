# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_main.ui'
#
# Created: Thu Aug 11 03:16:53 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 240)
        MainWindow.setMinimumSize(QtCore.QSize(520, 240))
        MainWindow.setMaximumSize(QtCore.QSize(520, 240))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.romanizeButton = QtGui.QPushButton(self.centralwidget)
        self.romanizeButton.setGeometry(QtCore.QRect(350, 10, 160, 81))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/m_romanize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.romanizeButton.setIcon(icon)
        self.romanizeButton.setIconSize(QtCore.QSize(64, 64))
        self.romanizeButton.setObjectName("romanizeButton")
        self.quizButton = QtGui.QPushButton(self.centralwidget)
        self.quizButton.setGeometry(QtCore.QRect(10, 10, 160, 81))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/m_quiz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.quizButton.setIcon(icon1)
        self.quizButton.setIconSize(QtCore.QSize(64, 64))
        self.quizButton.setObjectName("quizButton")
        self.cardsButton = QtGui.QPushButton(self.centralwidget)
        self.cardsButton.setGeometry(QtCore.QRect(180, 10, 160, 81))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/m_cards.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cardsButton.setIcon(icon2)
        self.cardsButton.setIconSize(QtCore.QSize(64, 64))
        self.cardsButton.setObjectName("cardsButton")
        self.vocabButton = QtGui.QPushButton(self.centralwidget)
        self.vocabButton.setGeometry(QtCore.QRect(10, 100, 250, 81))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/m_vocabulary.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vocabButton.setIcon(icon3)
        self.vocabButton.setIconSize(QtCore.QSize(64, 64))
        self.vocabButton.setObjectName("vocabButton")
        self.editButton = QtGui.QPushButton(self.centralwidget)
        self.editButton.setGeometry(QtCore.QRect(270, 100, 240, 81))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/m_dictionary.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editButton.setIcon(icon4)
        self.editButton.setIconSize(QtCore.QSize(64, 64))
        self.editButton.setObjectName("editButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionReadme = QtGui.QAction(MainWindow)
        self.actionReadme.setObjectName("actionReadme")
        self.menuFile.addAction(self.actionReadme)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PyKana Beta", None, QtGui.QApplication.UnicodeUTF8))
        self.romanizeButton.setText(QtGui.QApplication.translate("MainWindow", "Romanize \n"
"Words", None, QtGui.QApplication.UnicodeUTF8))
        self.quizButton.setText(QtGui.QApplication.translate("MainWindow", "Kana \n"
"Quiz", None, QtGui.QApplication.UnicodeUTF8))
        self.cardsButton.setText(QtGui.QApplication.translate("MainWindow", "Flash \n"
"Cards", None, QtGui.QApplication.UnicodeUTF8))
        self.vocabButton.setText(QtGui.QApplication.translate("MainWindow", "Vocabulary \n"
"Practice", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setText(QtGui.QApplication.translate("MainWindow", "Edit \n"
"Dictionary", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReadme.setText(QtGui.QApplication.translate("MainWindow", "Readme", None, QtGui.QApplication.UnicodeUTF8))

