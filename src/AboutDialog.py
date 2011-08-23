# -*- coding: utf-8 -*-
#!/usr/bin/python

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui.Ui_about import *

class AboutDialog(QDialog):
    """
    """
    
    def __init__(self, parent=None):
        """
        """
        super(AboutDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.labelImg.setPixmap(QPixmap(":/imgs/icons/avatar.png"))
        self.center_on_screen()
        
    def center_on_screen(self):
        """
        move the window to the center of the screen

        Arguments:
        - `self`:
        """
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))
