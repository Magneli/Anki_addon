# -*- coding: utf-8 -*-
# python 2.7
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


def get_card(id):
    return mw.col.getCard(id)


def find_cards(search_term):
    return mw.col.findCards(search_term)


def is_card_in_collection(expression, reading):
    ids = find_cards(expression)
    for id in ids:
        card = get_card(id)
        # if get_deck_name(card) == deck_name:
        note = card.note()
        if expression == note.items()[0][1] and reading == note.items()[1][1]:
            return True
    return False


def add_word_card(expression, reading, meaning):
    card = _find_sample_card_for_card_creation()
    note = card.col.newNote()
    new_card_data = (expression, reading, meaning)
    i = 0
    for (name, value) in note.items():
        if i < 3:
            note[name] = value + new_card_data[i]
        else:
            note[name] = value + ""
        i += 1
    card.col.addNote(note)
    note.flush()


def _find_sample_card_for_card_creation():
    ids = find_cards("deck:current")
    for id in ids:
        # if get_deck_name(get_card(id)) == deck_name:
        return get_card(id)


def reset_card_due_stats(card):
    card.queue = 2
    card.type = 2
    card.due = mw.col.sched.today
    card.ivl = 1
    card.factor = 1000
    card.col.sched._updateStats(card, 'rev')
    card.flushSched()
