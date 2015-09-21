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

def testFunction():

    ids = anki_api_interface.find_cards("exp123")
    card = anki_api_interface.get_card(ids[0])
    note = card.note()

    showInfo(note.items()[0][0])
    showInfo(note.items()[1][0])
    showInfo(note.items()[2][0])

    showInfo(note.items()[0][1]) #exp
    showInfo(note.items()[1][1]) #read
    showInfo(note.items()[2][1]) #mean










action = QAction("test", mw)
mw.connect(action, SIGNAL("triggered()"), testFunction)
mw.form.menuTools.addAction(action)