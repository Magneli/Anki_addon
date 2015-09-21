# -*- coding: utf-8 -*-
#  import the main window object (mw) from ankiqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *
from anki import Collection

deck_name = u'語彙'

def get_deck_name(card):
    return card.col.decks.name(card.did)


def is_card_in_deck(expression, reading):
    ids = mw.col.findCards(expression)
    for id in ids:
        card = mw.col.getCard(id)
        if get_deck_name(card) == deck_name:
            note = card.note()
            if expression == note.items()[0][1] and reading == note.items()[1][1]:
                return True

    return False
