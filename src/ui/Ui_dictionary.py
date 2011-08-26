# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_dictionary.ui'
#
# Created: Fri Aug 26 05:09:39 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_dictionaryDialog(object):
    def setupUi(self, dictionaryDialog):
        dictionaryDialog.setObjectName("dictionaryDialog")
        dictionaryDialog.resize(750, 300)
        dictionaryDialog.setMinimumSize(QtCore.QSize(750, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imgs/icons/m_dictionary.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dictionaryDialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(dictionaryDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtGui.QTableWidget(dictionaryDialog)
        self.tableWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(100)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeaderItem(0).setText("Word")
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_button = QtGui.QPushButton(dictionaryDialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imgs/icons/d_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_button.setIcon(icon1)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout.addWidget(self.add_button)
        self.remove_button = QtGui.QPushButton(dictionaryDialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/imgs/icons/d_remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_button.setIcon(icon2)
        self.remove_button.setObjectName("remove_button")
        self.horizontalLayout.addWidget(self.remove_button)
        self.quit_button = QtGui.QPushButton(dictionaryDialog)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/imgs/icons/d_quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.quit_button.setIcon(icon3)
        self.quit_button.setObjectName("quit_button")
        self.horizontalLayout.addWidget(self.quit_button)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(dictionaryDialog)
        QtCore.QObject.connect(self.quit_button, QtCore.SIGNAL("clicked()"), dictionaryDialog.close)
        QtCore.QMetaObject.connectSlotsByName(dictionaryDialog)

    def retranslateUi(self, dictionaryDialog):
        dictionaryDialog.setWindowTitle(QtGui.QApplication.translate("dictionaryDialog", "Dictionary [under-development]", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("dictionaryDialog", "Syllable", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("dictionaryDialog", "Character Set", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("dictionaryDialog", "Meaning", None, QtGui.QApplication.UnicodeUTF8))
        self.add_button.setText(QtGui.QApplication.translate("dictionaryDialog", "Add Word", None, QtGui.QApplication.UnicodeUTF8))
        self.remove_button.setText(QtGui.QApplication.translate("dictionaryDialog", "Remove Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.quit_button.setText(QtGui.QApplication.translate("dictionaryDialog", "Quit", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
