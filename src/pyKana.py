# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys 
from QuizSettingsDialog import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Ui_main import *

class PyKana(QMainWindow):
    """
    """
    
    def __init__(self, parent = None):
        """
        
        Arguments:
        - `parent`:
        """
        super(PyKana, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.centerOnScreen()
        
        self.connect(self.ui.quizButton, SIGNAL("clicked()"), self.quizClicked)
        

    def centerOnScreen(self):
        """
        move the window to the center of the screen

        Arguments:
        - `self`:
        """
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))
        


    def quizClicked(self):
        """
        
        Arguments:
        - `self`:
        """
        self.settings = QuizSettingsDlg()
        self.settings.exec_()


app = QApplication(sys.argv)
myapp = PyKana()
myapp.show()
sys.exit(app.exec_())


