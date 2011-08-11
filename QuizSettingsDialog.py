# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Ui_quizSettings import *
from QuizDialog import *

class QuizSettingsDlg(QDialog):
    """
    """
    
    def __init__(self, parent=None):
        """
        
        Arguments:
        - `parent`:
        """
        super(QuizSettingsDlg, self).__init__(parent)
        self.ui = Ui_quizSettings()
        self.ui.setupUi(self)
        self.centerOnScreen()
        self.connect(self.ui.startButton, SIGNAL("clicked()"), self.startClicked)
        

    def centerOnScreen(self):
        """
        move the window to the center of the screen

        Arguments:
        - `self`:
        """
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))


    def startClicked(self):
        """
        create a quiz dlg object
        and execute it

        Arguments:
        - `self`:
        """
        
        # these are the settings gathered from user
        # about the quiz
        self.qCount = self.ui.spinBox.value()
        self.hirCheck = self.ui.hirCheck.isChecked()
        self.hirHanCheck = self.ui.hirHanCheck.isChecked()
        self.hirYoonCheck = self.ui.hirYoonCheck.isChecked()
        self.katCheck = self.ui.katCheck.isChecked()
        self.katHanCheck = self.ui.katHanCheck.isChecked()
        self.katYoonCheck = self.ui.katYoonCheck.isChecked()
        
        # -debug-
        # print self.hirCheck , " - " , self.hirHanCheck , " - " , self.hirYoonCheck 
        # print self.katCheck , " - " , self.katHanCheck , " - " , self.katYoonCheck
        
        quiz = QuizDlg(self.qCount, self.hirCheck, self.hirHanCheck, self.hirYoonCheck,
                       self.katCheck, self.katHanCheck, self.katYoonCheck)

        quiz.exec_()

