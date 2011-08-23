# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
This module creates the dialog
for Quiz Settings
"""

from PyQt4 import QtCore
from PyQt4 import QtGui

import ui.Ui_quizSettings
import QuizDialog

class QuizSettingsDlg(QtGui.QDialog):
    """
    Creates the Settings Dialog Object
    """
    
    def __init__(self, parent=None):
        """
        constructer for settings
        """
        super(QuizSettingsDlg, self).__init__(parent)
        self.interface = ui.Ui_quizSettings.Ui_quizSettings()
        self.interface.setupUi(self)
                
        self.center_on_screen()
        self.connect(self.interface.startButton, QtCore.SIGNAL("clicked()"), 
                     self.start_clicked)
        
        self.setWindowIcon(QtGui.QIcon(":/imgs/icons/settings.png"))

        self.q_count = 0
        self.char_set = ""
        self.check_dakuten = False
        self.check_yoon = False
        

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
        
        self.q_count = self.interface.spinBox.value()
        self.char_set = self.interface.comboBox.currentText() 
        self.check_dakuten = self.interface.checkDakuten.isChecked()
        self.check_yoon = self.interface.checkYoon.isChecked()        
                
        quiz = QuizDialog.QuizDlg(self.q_count, self.char_set, 
                       self.check_dakuten, self.check_yoon)

        quiz.exec_()

