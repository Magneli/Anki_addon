# -*- coding: utf-8 -*-
# python 2.7

from aqt import mw
from aqt.utils import showInfo, getText
from aqt.qt import *
from anki import Collection

import os
import sys

from platform import system

from MakeAreas import makeAreas


def runInterface():
    mw.newUi = Interface()


class Interface(QWidget):
    def __init__(self):
        super(Interface, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 550, 550)
        self.setWindowTitle(u'鴨鴨')
        makeAreas(self)
        self.htmlarea.setHtml(
            "<html> <head> </head> <body> <p>yay </p> </body> </html>")
        self.show()
