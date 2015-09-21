# -*- coding: utf-8 -*-
# import the main window object (mw) from ankiqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *
from anki import Collection
import Search_handler
import anki_api_interface
import time


def testFunction():
    #anki_api_interface.add_word_card("yay", "space","ducks")











action = QAction("test", mw)
mw.connect(action, SIGNAL("triggered()"), testFunction)
mw.form.menuTools.addAction(action)