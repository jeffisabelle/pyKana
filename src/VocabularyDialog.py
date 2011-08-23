# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
Represents the vocabulary practice
dialog
"""

import random

from PyQt4 import QtCore
from PyQt4 import QtGui

import ui.Ui_vocabulary 
import resources_rc
import dictionary

class VocabularyDialog(QtGui.QDialog):
    """
    Represents the vocabulary practice
    dialog
    """
    
    def __init__(self, parent=None):
        """
        constructer for vocabulary dialog objects
        """

        super(VocabularyDialog, self).__init__(parent)
        self.interface = ui.Ui_vocabulary.Ui_vocabularyDialog()
        self.interface.setupUi(self)
       
        self.ask_new_word()
        self.center_on_screen()        

        self.connect(self.interface.cevap1Button, 
                     QtCore.SIGNAL("clicked()"), self.button_clicked)
        self.connect(self.interface.cevap2Button, 
                     QtCore.SIGNAL("clicked()"), self.button_clicked)
        self.connect(self.interface.cevap3Button, 
                     QtCore.SIGNAL("clicked()"), self.button_clicked)
        self.connect(self.interface.cevap4Button, 
                     QtCore.SIGNAL("clicked()"), self.button_clicked)

        self.word_arr = []
        self.correct_answer = ""
        self.syllable_ver = ""
        self.char_set = ""
        self.meaning_of_word = ""
        self.pic_array = []
        self.labels = []
        self.len_of_word = 0
        self.response_of_user = ""

    def center_on_screen(self):
        """
        move the window to the center of the screen
        """
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

    def set_the_word(self):
        """
        sets the word
        """
        self.word_arr = random.choice(dictionary.romanize)
        self.correct_answer = self.word_arr[0]
        self.syllable_ver = self.word_arr[1]
        self.char_set = self.word_arr[2]      
        self.meaning_of_word = self.word_arr[3]
        self.pic_array = dictionary.getPictureArray(self.syllable_ver)
        

    def get_length_of_the_word(self):
        """
        returns the number of syllable of the word.
        eg. a-no-hi-to returns 4.
        Arguments:
        - `self`:
        """        
        return len(self.pic_array)


    def set_labels(self, length):
        """
        this method sets the labels with appropriate
        images by using 'pic_array'
        
        Arguments:
        - `length`: length of the word
        """
        self.labels = [self.interface.harf1, self.interface.harf2,
                       self.interface.harf3, self.interface.harf4,
                       self.interface.harf5, self.interface.harf6,
                       self.interface.harf7, self.interface.harf8
                       ]

        for label in self.labels:
            label.clear()
        
        for i in range(length):
            self.labels[i].setPixmap(QtGui.QPixmap(
                    ":/imgs/"+self.char_set+"/resized/"+self.pic_array[i]))

        self.interface.romanizedLabel.setText("chose your answer from below")

    def ask_new_word(self):
        """
        asks new words.
        called recursively after response
        """
        self.set_the_word()
        self.len_of_word = self.get_length_of_the_word()
        self.set_labels(self.len_of_word)    
        self.set_button_labels()
    
    def set_button_labels(self):
        """
        sets the labels of buttons.
        """
        answers_arr = []
        for row in dictionary.romanize:
            answers_arr.append(row[3])
        
        answers_arr.remove(self.meaning_of_word)
        
        rnd1 = random.choice(answers_arr)
        answers_arr.remove(rnd1)
        
        rnd2 = random.choice(answers_arr)
        answers_arr.remove(rnd2)

        rnd3 = random.choice(answers_arr)
        answers_arr.remove(rnd3)

        rnd4 = random.choice(answers_arr)
        answers_arr.remove(rnd4)

        buttons = [self.interface.cevap1Button, self.interface.cevap2Button,
                   self.interface.cevap3Button, self.interface.cevap4Button]
 
        self.interface.cevap1Button.setText(rnd1)
        self.interface.cevap2Button.setText(rnd2)
        self.interface.cevap3Button.setText(rnd3)
        self.interface.cevap4Button.setText(rnd4)

        random.choice(buttons).setText(self.meaning_of_word)
        
    def button_clicked(self):
        """
        this method called when any answer button
        clicked.
        """
        sender = self.sender()
        self.response_of_user = sender.text()


        msg_box = QtGui.QMessageBox()
        
        if self.response_of_user == self.meaning_of_word:
            msg_box.setText("you did it! \nthat answer was correct (O_o)/")
            msg_box.setIconPixmap(QtGui.QPixmap(":/imgs/icons/4resized.png"))
        else:
            msg_box.setText("sorry but that was a wrong choice!"+
                            " \nkeep working!")
            msg_box.setIconPixmap(QtGui.QPixmap(":/imgs/icons/2resized.png"))


        msg_box.exec_()
        self.ask_new_word()
