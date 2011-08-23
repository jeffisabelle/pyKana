# -*- coding: utf-8 -*-
#!/usr/bin/python

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui.Ui_quizSettings import *
from QuizDialog import *
import icons_rc

class QuizSettingsDlg(QDialog):
    """
    """
    
    def __init__(self, parent=None):
        """
        constructer for settings
        """
        super(QuizSettingsDlg, self).__init__(parent)
        self.ui = Ui_quizSettings()
        self.ui.setupUi(self)
                
        self.center_on_screen()
        self.connect(self.ui.startButton, SIGNAL("clicked()"), self.start_clicked)
        self.setWindowIcon(QIcon(":/imgs/icons/settings.png"))

    def center_on_screen(self):
        """
        move the window to the center of the screen
        """
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))


    def start_clicked(self):
        """
        create a quiz dlg object
        and execute it
        """
        
        # these are the settings gathered from user
        # about the quiz
        
        self.qCount = self.ui.spinBox.value()
        self.charSet = self.ui.comboBox.currentText() 
        self.checkDakuten = self.ui.checkDakuten.isChecked()
        self.checkYoon = self.ui.checkYoon.isChecked()        
                
        quiz = QuizDlg(self.qCount, self.charSet, self.checkDakuten, self.checkYoon)
        quiz.exec_()

