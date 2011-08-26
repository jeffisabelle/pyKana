"""
This class represents the
Romanize Words section
"""

import random

from PyQt4 import QtCore
from PyQt4 import QtGui

import ui.Ui_romanize
import resources_rc
import dictionary

class RomanizeWords(QtGui.QDialog):
    """
    This class represents the
    Romanize Words section
    """   
    
    def __init__(self, parent=None):
        """
        """        
        super(RomanizeWords, self).__init__(parent)
        self.interface = ui.Ui_romanize.Ui_romanizeDialog()
        self.interface.setupUi(self)    
        self.interface.lineEdit.setText("romanize it here, and press enter")
        self.interface.lineEdit.selectAll()

        self.word_arr = []
        self.correct_answer = ""
        self.syllable_ver = ""
        self.char_set = ""      
        self.meaning_of_word = ""
        self.pic_array = []

        self.ask_question()        
        self.connect(self.interface.checkButton, 
                     QtCore.SIGNAL("clicked()"), self.check_answer)

        self.center_on_screen()


    def center_on_screen(self, widget=None):
        """
        
        Arguments:
        - `self`:
        """
        resolution = QtGui.QDesktopWidget().screenGeometry()
        if widget:
            widget.move((resolution.width() / 2) - 
                        (widget.sizeHint().width() / 2),
                        (resolution.height() / 2) - 
                        (widget.sizeHint().height() / 2))
        else:
            self.move((resolution.width() / 2) - 
                      (self.frameSize().width() / 2),
                      (resolution.height() / 2) - 
                      (self.frameSize().height() / 2))



    def set_the_word(self):
        """
        sets the word
        """
        self.word_arr = random.choice(dictionary.load_array("data.dat"))
        self.correct_answer = self.word_arr[0]
        self.syllable_ver = self.word_arr[1]
        self.char_set = self.word_arr[2]      
        self.meaning_of_word = self.word_arr[3]
        self.pic_array = dictionary.get_picture_array(self.syllable_ver)
        

    def get_length_of_the_word(self):
        """
        returns the number of syllable of the word.
        eg. a-no-hi-to returns 4.
        """        
        return len(self.pic_array)

    def set_labels(self, length):
        """
        this method sets the labels with appropriate
        images by using 'pic_array'
        
        Arguments:
        - `length`: length of the word
        """

        labels = [self.interface.harf1, self.interface.harf2,
                  self.interface.harf3, self.interface.harf4,
                  self.interface.harf5, self.interface.harf6,
                  self.interface.harf7, self.interface.harf8
                  ]

        for label in labels:
            label.clear()
        
        for i in range(length):
            labels[i].setPixmap(
                QtGui.QPixmap(":/imgs/"+self.char_set+
                              "/resized/"+self.pic_array[i]))

    def ask_question(self):
        """
        this method ask a question.
        called recursively after checking the answer.
        """        
        self.set_the_word()        
        len_of_word = self.get_length_of_the_word()
        self.set_labels(len_of_word)            
            

    def check_answer(self):
        """
        
        Arguments:
        """
        msg_box = QtGui.QMessageBox()
        given_answer = self.interface.lineEdit.text()

        if given_answer == self.correct_answer:

            msg_box.setWindowTitle("Well Done!")
            text = "\nPerfect!\n\nyour answer: '" + \
                given_answer+"' \nwas correct!" + \
                "\n\n"+self.correct_answer+" means '" + \
                self.meaning_of_word+"'"

            msg_box.setText(text)
            pic = QtGui.QPixmap(":/imgs/icons/4resized.png")
            msg_box.setIconPixmap(pic)            
        else:
            msg_box.setWindowTitle("Be More Careful!")
            text = "\nSorry :/ \n\nyour answer: '" + \
                given_answer+"' was wrong!" + \
                "\nthe correct answer was: '"+self.correct_answer+"'" + \
                "\n\n"+self.correct_answer+" means '"+self.meaning_of_word+"'"

            msg_box.setText(text)
            pic = QtGui.QPixmap(":/imgs/icons/2resized.png")
            msg_box.setIconPixmap(pic)                      

        self.center_on_screen(msg_box)        
        msg_box.exec_()
        self.ask_question()
        self.interface.lineEdit.clear()
