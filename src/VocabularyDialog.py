# -*- coding: utf-8 -*-
#!/usr/bin/python

import random

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui.Ui_vocabulary import *
import icons_rc
import dictionary

class VocabularyDialog(QDialog):
    """
    """
    
    def __init__(self, parent=None):
        """
        
        Arguments:
        """
        super(VocabularyDialog, self).__init__(parent)
        self.ui = Ui_vocabularyDialog()
        self.ui.setupUi(self)
        self.ask_new_word()
        self.center_on_screen()        

        self.connect(self.ui.cevap1Button, SIGNAL("clicked()"), self.button_clicked)
        self.connect(self.ui.cevap2Button, SIGNAL("clicked()"), self.button_clicked)
        self.connect(self.ui.cevap3Button, SIGNAL("clicked()"), self.button_clicked)
        self.connect(self.ui.cevap4Button, SIGNAL("clicked()"), self.button_clicked)


    def center_on_screen(self):
        """
        move the window to the center of the screen

        Arguments:
        - `self`:
        """
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

    def set_the_word(self):
        """
        
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


    def set_labels(self, len):
        """
        this method sets the labels with appropriate
        images by using 'pic_array'
        
        Arguments:
        - `len`: length of the word
        """


        self.labels = [self.ui.harf1,self.ui.harf2,
                       self.ui.harf3,self.ui.harf4,
                       self.ui.harf5,self.ui.harf6,
                       self.ui.harf7,self.ui.harf8
                       ]

        for label in self.labels:
            label.clear()
        
        for i in range(len):
            self.labels[i].setPixmap(QPixmap(":/imgs/"+self.char_set+"/resized/"+self.pic_array[i]))

        self.ui.romanizedLabel.setText("chose your answer from below")

    def ask_new_word(self):
        """
        
        """
        self.set_the_word()
        self.lenOfWord = self.get_length_of_the_word()
        self.set_labels(self.lenOfWord)    
        self.set_button_labels()
    
    def set_button_labels(self):
        """
        
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

        buttons = [self.ui.cevap1Button, self.ui.cevap2Button,
                   self.ui.cevap3Button, self.ui.cevap4Button]
 
        self.ui.cevap1Button.setText(rnd1)
        self.ui.cevap2Button.setText(rnd2)
        self.ui.cevap3Button.setText(rnd3)
        self.ui.cevap4Button.setText(rnd4)

        random.choice(buttons).setText(self.meaning_of_word)
        
    def button_clicked(self):
        """
        
        """
        sender = self.sender()
        self.response_of_user = sender.text()


        msg_box = QMessageBox()
        
        if self.response_of_user == self.meaning_of_word:
            msg_box.setText("you did it! \nthat answer was correct (O_o)/")
            msg_box.setIconPixmap(QPixmap(":/imgs/icons/4resized.png"))
        else:
            msg_box.setText("sorry but that was a wrong choice! \nkeep working!")
            msg_box.setIconPixmap(QPixmap(":/imgs/icons/2resized.png"))


        msg_box.exec_()
        self.ask_new_word()
