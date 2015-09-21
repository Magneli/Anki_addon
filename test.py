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
from anki.utils import intTime, timestampID

def testFunction():
    card = mw.col.sched.getCard()
    cardCount = mw.col.cardCount()
    # show a message box

    search_term = "exp123"#.decode(encoding='UTF-8',errors='strict')

    ids = mw.col.findCards(search_term)
    #showInfo(search_term)
    card = mw.col.getCard(ids[0])

    note = card.note()
    searcher = Search_handler.Search_handler()
    taberu = searcher.search("taberu")
    ducks  = searcher.search("kiku")


    result =""
    card = mw.col.getCard(ids[0])
    card.due = 10000
   # card.type = 0
    card.flushSched()
    note = card.note()
    #showInfo(note.items())

    #newnote = card.col.newNote()

    list= ("1","2", "3", "", "" )
    i = 0
   # for (name, value) in newnote.items():
   #     newnote[name] = value + list[i]
   #     i+=1
   # newnote.flush()

   # card.col.addNote(newnote)
    for (name, value) in note.items():
        result+=name+value
    #showInfo(result)
    #showInfo(note.items()[0][0])
    #showInfo(note.items()[1][0])
    #showInfo(note.items()[2][0])
    if anki_api_interface.is_card_in_deck(taberu.get_expression_number(0), taberu.get_reading_number(0)):
        showInfo("yay")
    #showInfo(note.items()[0][1])
    #showInfo(note.items()[1][1])
    #showInfo(note.items()[2][1])





action = QAction("test", mw)
mw.connect(action, SIGNAL("triggered()"), testFunction)
mw.form.menuTools.addAction(action)