# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys, random, time, alphabet
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.Ui_quizDialog import *

class QuizDlg(QDialog):
    """
    This class represents the quiz dialog
    where users answers questions
    """
           
    def __init__(self, questionCount, charSet, cDakuten, cYoon, parent=None):
        """
        constructer for objects

        Arguments:
        - `questionCount`: count of the questions that is going to be asked
        """
        super(QuizDlg, self).__init__(parent)

        # question count
        self.qCount = questionCount 
        
        # check's are boolean
        self.charSet = charSet
        self.checkDakuten = cDakuten
        self.checkYoon = cYoon
 
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
            
        self.ui.totalCount.setText(str(self.qAnswered)+"/"+str(self.qCount))
        self.setRangeOfChars()
        self.startQuiz()


    def setRangeOfChars(self):
        """
        
        """
        if self.charSet == "Hiragana":
            self.chars = alphabet.hiragana[:]
        elif self.charSet == "Katakana":
            self.chars = alphabet.katakana[:]
        else:
            self.chars = alphabet.hiragana[:]
            for c in alphabet.katakana:
                self.chars.append(c)
        
        if self.checkDakuten == True:
            for c in alphabet.dakuten:
                self.chars.append(c)

        if self.checkYoon == True:
            for c in alphabet.yoon:
                self.chars.append(c)


    def getRandomChar(self):
        """
        returns a random character
        """
             
        if self.charSet == "Both":
            arr = ["hiragana","katakana"]
            set = random.choice(arr)
        else:
            set = str(self.charSet)
            set = set.lower()


        correct = random.choice(self.chars)
        self.ui.imgLabel.setPixmap(QPixmap("imgs/"+set+"/"+correct+".png"))
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
        self.ui.totalCount.setText(str(self.qAnswered)+"/"+str(self.qCount))

        if(self.answer==self.response):
            self.correctCount += 1
            self.ui.correctCount.setText(str(self.correctCount))                    
        else:
            self.wrongCount += 1
            self.ui.wrongCount.setText(str(self.wrongCount))

        if(self.qAnswered>=self.qCount):
            self.close()

            msgBox = QMessageBox()
            msgBox.setText("You have finished your quiz!")
            msgBox.setInformativeText("You got "+str(self.correctCount)+" correct answer \nin "+ str(self.qCount)+" questions.")
            fark = self.qAnswered / 5.0
            rangeTooBad = fark
            rangeBad = fark * 2
            rangeNormal = fark * 3
            rangeGood = fark * 4
            rangePerfect = fark * 5
            
            if self.correctCount <= rangeTooBad:                
                msgBox.setWindowTitle("Y U don't know kana!")
                msgBox.setIconPixmap(QPixmap("imgs/icons/1.png"))
            elif self.correctCount > rangeTooBad and self.correctCount <= rangeBad:
                print "bad"
                msgBox.setWindowTitle("Sorry but you need to work hard!")
                msgBox.setIconPixmap(QPixmap("imgs/icons/2.png"))
            elif self.correctCount > rangeBad and self.correctCount <= rangeNormal:
                print "normal"
                msgBox.setWindowTitle("It's not bad!")
                msgBox.setIconPixmap(QPixmap("imgs/icons/3.png"))
            elif self.correctCount > rangeNormal and self.correctCount <= rangeGood:
                print "good"
                msgBox.setWindowTitle("Wow, that is a good score!")
                msgBox.setIconPixmap(QPixmap("imgs/icons/4.png"))
            else:
                print "perfect"
                msgBox.setWindowTitle("Y U Know Kana!")
                msgBox.setIconPixmap(QPixmap("imgs/icons/5.png"))

            msgBox.exec_()

        # ask new question recursively if not finish
        self.startQuiz()


            

            
            
