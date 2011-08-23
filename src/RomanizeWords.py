import random

from PyQt4 import QtCore
from PyQt4 import QtGui

from ui.Ui_romanize import *
import resources_rc
import dictionary

class RomanizeWords(QtGui.QDialog):
    """
    """
    
    def __init__(self, parent=None):
        """
        """        
        super(RomanizeWords, self).__init__(parent)
        self.ui = Ui_romanizeDialog()
        self.ui.setupUi(self)        
        self.ui.lineEdit.setText("romanize it here, and press enter")
        self.ui.lineEdit.selectAll()
        self.ask_question()        
        self.connect(self.ui.checkButton, QtCore.SIGNAL("clicked()"), self.check_answer)

        self.center_on_screen()

    def center_on_screen(self, widget=None):
        """
        
        Arguments:
        - `self`:
        """
        resolution = QtGui.QDesktopWidget().screenGeometry()
        if widget:
            widget.move((resolution.width() / 2) - (widget.sizeHint().width() / 2),
                        (resolution.height() / 2) - (widget.sizeHint().height() / 2))
        else:
            self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                      (resolution.height() / 2) - (self.frameSize().height() / 2))



    def set_the_word(self):
        """
        
        Arguments:
        - `self`:
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
            # print self.picArray[i]

    def ask_question(self):
        """
        this method ask a question.
        called recursively after checking the answer.
        """        
        self.set_the_word()
        self.lenOfWord = self.get_length_of_the_word()
        self.set_labels(self.lenOfWord)            
            

    def check_answer(self):
        """
        
        Arguments:
        """
        msg_box = QtGui.QMessageBox()
        self.given_answer = self.ui.lineEdit.text()

        if self.given_answer == self.correct_answer:

            msg_box.setWindowTitle("Well Done!")
            text = "\nPerfect!\n\nyour answer: '"+self.given_answer+"' \nwas correct!" 
            text += "\n\n\n"+self.correct_answer+" means '"+self.meaning_of_word+"'"
            msg_box.setText(text)
            pic = QPixmap(":/imgs/icons/4resized.png")
            msg_box.setIconPixmap(pic)            
        else:
            msg_box.setWindowTitle("Be More Careful!")
            text = "\nSorry :/ \n\nyour answer: '"+self.given_answer+"' was wrong!" 
            text += "\nthe correct answer was: '"+self.correct_answer+"'" 
            text += "\n\n\n"+self.correct_answer+" means '"+self.meaning_of_word+"'"
            msg_box.setText(text)
            pic = QPixmap(":/imgs/icons/2resized.png")
            msg_box.setIconPixmap(pic)                      

        self.center_on_screen(msg_box)        
        msg_box.exec_()
        self.ask_question()
        self.ui.lineEdit.clear()
