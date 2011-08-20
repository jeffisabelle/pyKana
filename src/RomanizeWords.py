import dictionary, random
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.Ui_romanize import *


class RomanizeWords(QDialog):
    """
    """
    
    def __init__(self, parent = None):
        """
        """        
        super(RomanizeWords, self).__init__(parent)
        self.ui = Ui_romanizeDialog()
        self.ui.setupUi(self)        
        self.centerOnScreen()
        
        self.askQuestion()
        
        self.connect(self.ui.checkButton, SIGNAL("clicked()"), self.checkAnswer)

    def centerOnScreen(self):
        """
        move the window to the center of the screen

        Arguments:
        - `self`:
        """
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))



    def setTheWord(self):
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
        

    def getLengthOfTheWord(self):
        """
        returns the number of syllable of the word.
        eg. a-no-hi-to returns 4.
        Arguments:
        - `self`:
        """        
        return len(self.pic_array)

    def setLabels(self, len):
        """
        
        Arguments:
        - `self`:
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
            self.labels[i].setPixmap(QPixmap("imgs/"+self.char_set+"/resized/"+self.pic_array[i]))
            # print self.picArray[i]

    def askQuestion(self):
        """
        
        Arguments:
        - `self`:
        """        
        self.ui.lineEdit.clear()
        self.setTheWord()
        self.lenOfWord = self.getLengthOfTheWord()
        self.setLabels(self.lenOfWord)            
            

    def checkAnswer(self):
        """
        
        Arguments:
        - `self`:
        """
        self.given_answer = self.ui.lineEdit.text()
        if self.given_answer == self.correct_answer:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Well Done!")
            text = "\nPerfect!\n\nyour answer: '"+self.given_answer+"' \nwas correct!" 
            msgBox.setText(text)
            pic = QPixmap("imgs/icons/4resized.png")
            msgBox.setIconPixmap(pic)
            msgBox.exec_()
            self.askQuestion()
        else:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Be More Careful!")
            text = "\nSorry :/ \n\nyour answer: '"+self.given_answer+"' was wrong! \nthe correct answer was: '"+self.correct_answer+"'" 
            msgBox.setText(text)
            pic = QPixmap("imgs/icons/2resized.png")
            msgBox.setIconPixmap(pic)
            msgBox.exec_()
            self.askQuestion()
