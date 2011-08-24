# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
This class represents the quiz dialog
where users answers questions
"""

import random

from PyQt4 import QtCore
from PyQt4 import QtGui

import ui.Ui_quizDialog 
import alphabet
import resources_rc

class QuizDlg(QtGui.QDialog):
    """
    This class represents the quiz dialog
    where users answers questions
    """
           
    def __init__(self, question_count, char_set, 
                 check_dakuten, check_yoon, parent=None):
        """
        constructer for objects

        Arguments:
        - `question_count`: count of the questions that is going to be asked
        """
        super(QuizDlg, self).__init__(parent)

        # question count
        self.q_count = question_count 
        
        # check's are boolean
        self.char_set = char_set
        self.check_dakuten = check_dakuten
        self.check_yoon = check_yoon
        self.answer = ""
 
        # char array for quiz
        self.chars = []

        # variables
        self.correct_count = 0
        self.wrong_count = 0
        self.q_answered = 0
        self.response = None

        self.interface = ui.Ui_quizDialog.Ui_quizDialog()
        self.interface.setupUi(self)
        
        self.connect(self.interface.btn1, QtCore.SIGNAL("clicked()"), 
                     self.button_clicked)
        self.connect(self.interface.btn2, QtCore.SIGNAL("clicked()"), 
                     self.button_clicked)
        self.connect(self.interface.btn3, QtCore.SIGNAL("clicked()"), 
                     self.button_clicked)
        self.connect(self.interface.btn4, QtCore.SIGNAL("clicked()"), 
                     self.button_clicked)
            
        self.interface.totalCount.setText(
            str(self.q_answered)+"/"+str(self.q_count))
        
        self.set_chars()
        self.start_quiz()


    def set_chars(self):
        """
        set the chars array
        """
        if self.char_set == "Hiragana":
            self.chars = alphabet.HIRAGANA[:]
        elif self.char_set == "Katakana":
            self.chars = alphabet.KATAKANA[:]
        else:
            self.chars = alphabet.HIRAGANA[:]
            for char in alphabet.KATAKANA:
                self.chars.append(char)
        
        if self.check_dakuten == True:
            for char in alphabet.DAKUTEN:
                self.chars.append(char)

        if self.check_yoon == True:
            for char in alphabet.YOON:
                self.chars.append(char)


    def get_random_char(self):
        """
        returns a random character
        """
             
        if self.char_set == "Both":
            arr = ["hiragana","katakana"]
            char_set = random.choice(arr)
        else:
            char_set = str(self.char_set)
            char_set = char_set.lower()


        correct = random.choice(self.chars)
        self.interface.imgLabel.setPixmap(
            QtGui.QPixmap(":/imgs/"+char_set+"/"+correct+".png"))
        
        return correct

    def set_buttons_text(self):
        """
        sets the buttons text's
        """

        char_arr = self.chars[:]
          
        char_arr.remove(self.answer)
        
        rnd1 = random.choice(char_arr)
        char_arr.remove(rnd1)

        rnd2 = random.choice(char_arr)
        char_arr.remove(rnd2)

        rnd3 = random.choice(char_arr)
        char_arr.remove(rnd3)

        rnd4 = random.choice(char_arr)
        char_arr.remove(rnd4)

        buttons = [self.interface.btn1, self.interface.btn2, 
                   self.interface.btn3, self.interface.btn4]
        
        self.interface.btn1.setText(rnd1)
        self.interface.btn2.setText(rnd2)
        self.interface.btn3.setText(rnd3)
        self.interface.btn4.setText(rnd4)

        random.choice(buttons).setText(self.answer)

    def start_quiz(self):
        """
        starts the quiz
        """
        self.answer = self.get_random_char()
        self.set_buttons_text()        

    def button_clicked(self):
        """
        this method called when any answer button
        clicked.
        """
        sender = self.sender()
        self.response = sender.text()        

        self.q_answered += 1
        self.interface.totalCount.setText(
            str(self.q_answered)+"/"+str(self.q_count))

        if(self.answer==self.response):
            self.correct_count += 1
            self.interface.correctCount.setText(
                str(self.correct_count))                    
        else:
            self.wrong_count += 1
            self.interface.wrongCount.setText(str(self.wrong_count))

        if(self.q_answered>=self.q_count):
            self.close()

            msg_box = QtGui.QMessageBox()
            msg_box.setText("You have finished your quiz!")
            msg_box.setInformativeText("You got "+str(self.correct_count)+
                                      " correct answer \nin "+ 
                                      str(self.q_count)+" questions.")

            fark = self.q_answered / 5.0
            range_too_bad = fark
            range_bad = fark * 2
            range_normal = fark * 3
            range_good = fark * 4
            
            if self.correct_count <= range_too_bad:                
                msg_box.setWindowTitle("Y U don't know kana!")
                msg_box.setIconPixmap(QtGui.QPixmap(":/imgs/icons/1.png"))
            elif (self.correct_count > range_too_bad and 
                  self.correct_count <= range_bad):           
                msg_box.setWindowTitle("Sorry but you need to work hard!")
                msg_box.setIconPixmap(QtGui.QPixmap(":/imgs/icons/2.png"))
            elif (self.correct_count > range_bad and 
                  self.correct_count <= range_normal):
                msg_box.setWindowTitle("It's not bad!")
                msg_box.setIconPixmap(QtGui.QPixmap(":/imgs/icons/3.png"))
            elif (self.correct_count > range_normal and 
                  self.correct_count <= range_good):
                msg_box.setWindowTitle("Wow, that is a good score!")
                msg_box.setIconPixmap(QtGui.QPixmap(":/imgs/icons/4.png"))
            else:
                msg_box.setWindowTitle("Y U Know Kana!")
                msg_box.setIconPixmap(QtGui.QPixmap(":/imgs/icons/5.png"))

            msg_box.exec_()

        # ask new question recursively if not finish
        self.start_quiz()
