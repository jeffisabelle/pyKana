# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys, random, time, alphabet
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Ui_quizDialog import *

class QuizDlg(QDialog):
    """
    """
           
    def __init__(self, questionCount, cHiragana, cHiraganaDakuten, cHiraganaYoon, 
                 cKatakana, cKatakanaDakuten, cKatakanaYoon, parent=None):
        """
        constructer for objects

        Arguments:
        - `questionCount`: count of the questions that is going to be asked
        """
        super(QuizDlg, self).__init__(parent)

        # question count
        self.qCount = questionCount 
        
        # check's are boolean
        self.hirCheck = cHiragana 
        self.hirDakutenCheck = cHiraganaDakuten
        self.hirYoonCheck = cHiraganaYoon
        self.katCheck = cKatakana
        self.katDakutenCheck = cKatakanaDakuten
        self.katYoonCheck = cKatakanaYoon
        
        # char array for quiz
        self.chars = []

        # variables
        self.correctCount = 0
        self.wrongCount = 0
        self.qAnswered = 0
        self.response = None

        self.ui = Ui_quizDialog()
        self.ui.setupUi(self)
        
        self.connect(self.ui.btn1, SIGNAL("clicked()"), self.buttonClicked)
        self.connect(self.ui.btn2, SIGNAL("clicked()"), self.buttonClicked)
        self.connect(self.ui.btn3, SIGNAL("clicked()"), self.buttonClicked)
        self.connect(self.ui.btn4, SIGNAL("clicked()"), self.buttonClicked)
                
        self.setRangeOfChars()
        self.startQuiz()


    def setRangeOfChars(self):
        """
        
        Arguments:
        - `self`:
        """
        self.set = []
        if self.hirCheck == True:
            self.set.append("hiragana")
            for c in alphabet.hiragana:
                self.chars.append(c)
        
        if self.hirDakutenCheck == True:
            self.set.append("hiragana")
            for c in alphabet.hiraganaDakuten:
                self.chars.append(c)

        if self.hirYoonCheck == True:
            self.set.append("hiragana")
            for c in alphabet.hiraganaYoon:
                self.chars.append(c)
        
        if self.katCheck == True:
            self.set.append("katakana")
            for c in alphabet.katakana:
                self.chars.append(c)

    def getRandomChar(self):
        """
        returns a random hiragana character
        """
        set = random.choice(self.set)
        correct = random.choice(self.chars)
        self.ui.imgLabel.setPixmap(QPixmap(set+"/"+correct+".png"))
        return correct

    def setButtonsText(self):
        """
        sets the buttons text's
        """

        charArr = self.chars[:]
          
        charArr.remove(self.answer)
        
        rnd1 = random.choice(charArr)
        charArr.remove(rnd1)

        rnd2 = random.choice(charArr)
        charArr.remove(rnd2)

        rnd3 = random.choice(charArr)
        charArr.remove(rnd3)

        rnd4 = random.choice(charArr)
        charArr.remove(rnd4)

        buttons = [self.ui.btn1,self.ui.btn2,self.ui.btn3,self.ui.btn4]
        
        self.ui.btn1.setText(rnd1)
        self.ui.btn2.setText(rnd2)
        self.ui.btn3.setText(rnd3)
        self.ui.btn4.setText(rnd4)

        random.choice(buttons).setText(self.answer)

    def startQuiz(self):
        """
        starts the quiz
        """
        self.answer = self.getRandomChar()
        self.setButtonsText()        

    def buttonClicked(self):
        sender = self.sender()
        self.response = sender.text()        

        self.qAnswered += 1

        if(self.answer==self.response):
            self.correctCount += 1
            s = "your response '"+self.response+"' was correct!"
            self.ui.iconLabel.setPixmap(QPixmap("icons/qdlg_correct.png"))
            self.ui.responseLabel.setText(s)            
        
        else:
            self.wrongCount += 1
            s = "your response '"+self.response+"' was wrong!"
            self.ui.iconLabel.setPixmap(QPixmap("icons/qdlg_wrong.png"))
            self.ui.responseLabel.setText(s)

        if(self.qAnswered>=self.qCount):
            self.close()
            msgBox = QMessageBox()
            msgBox.setText("You have finished your quiz!")
            msgBox.setInformativeText("You got "+str(self.correctCount)+" correct answer \nin "+ str(self.qCount)+" questions.")
        
            if self.wrongCount >= self.correctCount:
                msgBox.setWindowTitle("Y U don't know kana!")
                msgBox.setIconPixmap(QPixmap("icons/angryIcon.png"))
            else:
                msgBox.setWindowTitle("You got a nice score!")
                msgBox.setIconPixmap(QPixmap("icons/happyIcon.png"))
            
            msgBox.exec_()


                    
        self.startQuiz()
        
