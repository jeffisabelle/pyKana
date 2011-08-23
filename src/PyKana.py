# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
Base Dialog
"""

import sys

from PyQt4 import QtCore
from PyQt4 import QtGui

import QuizSettingsDialog
import RomanizeWords
import VocabularyDialog
import AboutDialog
import ui.Ui_main

class PyKana(QtGui.QMainWindow):
    """
    Main Window Of The App
    """
    
    def __init__(self, parent=None):
        """
        
        Arguments:
        - `parent`:
        """
        super(PyKana, self).__init__(parent)

        self.interface = ui.Ui_main.Ui_MainWindow()
        self.interface.setupUi(self)

        self.center_on_screen()         

        self.connect(self.interface.quizButton, QtCore.SIGNAL("clicked()"),
                     quiz_clicked)
        
        self.connect(self.interface.romanizeButton, QtCore.SIGNAL("clicked()"), 
                     romanize_clicked)

        self.connect(self.interface.vocabButton, QtCore.SIGNAL("clicked()"), 
                     vocabulary_clicked)
        
        self.connect(self.interface.actionReadme, QtCore.SIGNAL("triggered()"), 
                     readme_triggered)


    def center_on_screen(self):
        """
        move the window to the center of the screen

        Arguments:
        - `self`:
        """
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))
        


def quiz_clicked():
    """
    Shows the Kana Quiz dialog
    """
    settings = QuizSettingsDialog.QuizSettingsDlg()
    settings.exec_()

def romanize_clicked():
    """
    Shows the Romanize Words dialog
    """
    romanize = RomanizeWords.RomanizeWords()
    romanize.exec_()
        
def vocabulary_clicked():
    """
    Shows the Vocabulary Practice dialog
    """
    vocabulary = VocabularyDialog.VocabularyDialog()
    vocabulary.exec_()

def readme_triggered():
    """
    Opens the readme dialog    
    """
    about = AboutDialog.AboutDialog()
    about.exec_()
        


APP = QtGui.QApplication(sys.argv)
MYAPP = PyKana()
MYAPP.show()
sys.exit(APP.exec_())


