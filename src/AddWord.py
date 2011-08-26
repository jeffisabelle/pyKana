# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
Represents the adding
new words dialog
"""

from PyQt4 import QtGui
from PyQt4 import QtCore

import ui.Ui_addDict
import dictionary

class AddWord(QtGui.QDialog):
    """
    Represents the adding
    new words dialog
    """
    
    def __init__(self, parent=None):
        """
        Constructer
        """
        super(AddWord, self).__init__(parent)
        self.interface = ui.Ui_addDict.Ui_Dialog()
        self.interface.setupUi(self)
        self.interface.lineEdit.selectAll()
        
        self.connect(self.interface.addButton, QtCore.SIGNAL("clicked()"),
                     self.add_clicked)

        self.center_on_screen()
        self.dictionary_array = dictionary.load_array("data.dat")

    def center_on_screen(self):
        """
        move the window to the center of the screen

        Arguments:
        - `self`:
        """
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

        
    def add_clicked(self):
        """
        Adds the word to dictionary
        """
        word = str(self.interface.lineEdit.text())
        syllable = str(self.interface.lineEdit_2.text())
        meaning = str(self.interface.lineEdit_3.text())
        char_set = str(self.interface.comboBox.currentText()).lower()

        new_word = [word, syllable, char_set, meaning]

        msg_box = QtGui.QMessageBox()                
        if dictionary.has_this_word(word, self.dictionary_array):
            msg_box.setText("\nThis word is already \n in your dictionary!")
            msg_box.setIconPixmap(QtGui.QPixmap(":/imgs/icons/d_already.png"))
            msg_box.exec_()
        else:
            msg_box.setText("\nThe word has been added \n to your dictionary!")
            msg_box.setIconPixmap(QtGui.QPixmap(":/imgs/icons/d_added.png"))
            msg_box.exec_()
            dictionary.add_new_word(new_word, self.dictionary_array, "data.dat")
        
        
