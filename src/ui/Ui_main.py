# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_main.ui'
#
# Created: Mon Aug 22 00:01:28 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 240)
        MainWindow.setMinimumSize(QtCore.QSize(600, 240))
        MainWindow.setMaximumSize(QtCore.QSize(600, 240))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imgs/icons/5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.quizButton = QtGui.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imgs/icons/m_quiz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.quizButton.setIcon(icon1)
        self.quizButton.setIconSize(QtCore.QSize(64, 64))
        self.quizButton.setObjectName("quizButton")
        self.gridLayout.addWidget(self.quizButton, 0, 0, 1, 1)
        self.vocabButton = QtGui.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/imgs/icons/m_vocabulary.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vocabButton.setIcon(icon2)
        self.vocabButton.setIconSize(QtCore.QSize(64, 64))
        self.vocabButton.setObjectName("vocabButton")
        self.gridLayout.addWidget(self.vocabButton, 1, 0, 1, 1)
        self.editButton = QtGui.QPushButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/imgs/icons/m_dictionary.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editButton.setIcon(icon3)
        self.editButton.setIconSize(QtCore.QSize(64, 64))
        self.editButton.setObjectName("editButton")
        self.gridLayout.addWidget(self.editButton, 1, 3, 1, 1)
        self.settingsButton = QtGui.QPushButton(self.centralwidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/imgs/icons/m_settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsButton.setIcon(icon4)
        self.settingsButton.setIconSize(QtCore.QSize(55, 64))
        self.settingsButton.setObjectName("settingsButton")
        self.gridLayout.addWidget(self.settingsButton, 1, 2, 1, 1)
        self.cardsButton = QtGui.QPushButton(self.centralwidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/imgs/icons/m_cards.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cardsButton.setIcon(icon5)
        self.cardsButton.setIconSize(QtCore.QSize(64, 64))
        self.cardsButton.setObjectName("cardsButton")
        self.gridLayout.addWidget(self.cardsButton, 0, 2, 1, 1)
        self.romanizeButton = QtGui.QPushButton(self.centralwidget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/imgs/icons/m_romanize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.romanizeButton.setIcon(icon6)
        self.romanizeButton.setIconSize(QtCore.QSize(64, 64))
        self.romanizeButton.setObjectName("romanizeButton")
        self.gridLayout.addWidget(self.romanizeButton, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 25))
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
        QtCore.QObject.connect(self.settingsButton, QtCore.SIGNAL("clicked()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PyKana [under-development]", None, QtGui.QApplication.UnicodeUTF8))
        self.quizButton.setText(QtGui.QApplication.translate("MainWindow", "Kana \n"
"Quiz", None, QtGui.QApplication.UnicodeUTF8))
        self.vocabButton.setText(QtGui.QApplication.translate("MainWindow", "Vocabulary \n"
"Practice", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setText(QtGui.QApplication.translate("MainWindow", "Edit \n"
"Dictionary", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsButton.setText(QtGui.QApplication.translate("MainWindow", "Quit \n"
"Program", None, QtGui.QApplication.UnicodeUTF8))
        self.cardsButton.setText(QtGui.QApplication.translate("MainWindow", "Flash \n"
"Cards", None, QtGui.QApplication.UnicodeUTF8))
        self.romanizeButton.setText(QtGui.QApplication.translate("MainWindow", "Romanize \n"
"Words", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReadme.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
