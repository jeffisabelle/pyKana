# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
Represents the about dialog
"""

from PyQt4 import QtGui

import ui.Ui_about 

class AboutDialog(QtGui.QDialog):
    """
    Represents the about dialog
    """
    
    def __init__(self, parent=None):
        """
        Constructer
        """
        super(AboutDialog, self).__init__(parent)
        self.interface = ui.Ui_about.Ui_Dialog()
        self.interface.setupUi(self)
        self.interface.labelImg.setPixmap(
            QtGui.QPixmap(":/imgs/icons/avatar.png"))
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
