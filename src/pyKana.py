# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from QuizSettingsDialog import *
from RomanizeWords import *
from VocabularyDialog import *
from AboutDialog import *
from ui.Ui_main import *

class PyKana(QMainWindow):
    """
    Main Window Of The App
    """
    
    def __init__(self, parent=None):
        """
        
        Arguments:
        - `parent`:
        """
        super(PyKana, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.center_on_screen()         

        self.connect(self.ui.quizButton, SIGNAL("clicked()"), self.quiz_clicked)
        self.connect(self.ui.romanizeButton, SIGNAL("clicked()"), self.romanize_clicked)
        self.connect(self.ui.vocabButton, SIGNAL("clicked()"), self.vocabulary_clicked)
        self.connect(self.ui.actionReadme, SIGNAL("triggered()"), self.readme_triggered)


    def center_on_screen(self):
        """
        move the window to the center of the screen

        Arguments:
        - `self`:
        """
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))
        


    def quiz_clicked(self):
        """
        
        Arguments:
        - `self`:
        """
        self.settings = QuizSettingsDlg()
        self.settings.exec_()

    def romanize_clicked(self):
        """
        
        Arguments:
        - `self`:
        """
        self.romanize = RomanizeWords()
        self.romanize.exec_()
        
    def vocabulary_clicked(self):
        """
        
        """
        self.vocabulary = VocabularyDialog()
        self.vocabulary.exec_()


    def readme_triggered(self):
        """
        Opens the readme dialog
        
        Arguments:
        - `self`:
        """
        self.about = AboutDialog()
        self.about.exec_()
        


app = QApplication(sys.argv)
myapp = PyKana()
myapp.show()
sys.exit(app.exec_())


