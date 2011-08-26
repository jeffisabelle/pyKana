# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
Represents the dictionary
dialog
"""

from PyQt4 import QtCore
from PyQt4 import QtGui

import ui.Ui_dictionary
import AddWord
import dictionary

class DictionaryDialog(QtGui.QDialog):

    """
    Represents the dictionary
    dialog
    """      
    def __init__(self, parent=None):
        """
        Constructer for Dictionary Dialog objects
        """
        
        super(DictionaryDialog, self).__init__(parent)
        self.interface = ui.Ui_dictionary.Ui_dictionaryDialog()
        self.interface.setupUi(self)
        self.dictionary_array = dictionary.load_array("data.dat")

        self.display_table_widget(self.dictionary_array)
        self.center_on_screen()

        self.connect(self.interface.remove_button, QtCore.SIGNAL("clicked()"),
                     self.remove_clicked)
        
        self.connect(self.interface.add_button, QtCore.SIGNAL("clicked()"),
                     self.add_clicked)

    def center_on_screen(self):
        """
        move the window to the center of the screen

        Arguments:
        - `self`:
        """
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))
        
    def display_table_widget(self, dict_arr):
        """
        
        Arguments:
        - `dict_arr`: the array that is going to be
        showed on the tabel
        """
        self.interface.tableWidget.setRowCount(len(dict_arr))
        for row in range(len(dict_arr)):
            for col in range(4):
                item = QtGui.QTableWidgetItem(dict_arr[row][col])
                self.interface.tableWidget.setItem(row, col, item)

    def remove_clicked(self):
        """
        Removes the selected item
        from dictionary
        """

        selected = self.interface.tableWidget.selectedItems()
        dictionary.remove_word(selected[0].text(), 
                               self.dictionary_array, "data.dat")
        self.display_table_widget(self.dictionary_array)

    def add_clicked(self):
        """
        Shows the add new words dialog
        After executing finish, it refresh the 
        dictionary_array and refresh the table_widget
        """
        add_dialog = AddWord.AddWord()
        add_dialog.exec_()
        self.dictionary_array = dictionary.load_array("data.dat")
        self.display_table_widget(self.dictionary_array)
