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
from Add_keybinds import  add_keybinds
from jp_eng_jisho_import.Search_handler import Jp_to_eng_word_search_handler


def runInterface():
    mw.newUi = Interface()


class Interface(QWidget):
    def __init__(self):
        super(Interface, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 550, 550)
        self.setWindowTitle(u'鴨鴨')
        searcher = Jp_to_eng_word_search_handler.Jp_to_eng_word_search_handler()
        self.search_result = searcher.search("鴨")
        makeAreas(self)
        add_keybinds(self)
        self.show()
