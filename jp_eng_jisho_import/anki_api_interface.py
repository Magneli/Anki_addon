# -*- coding: utf-8 -*-
# python 2.7
#  import the main window object (mw) from ankiqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *
from anki import Collection

deck_name = u'Words'
model_name = u'Default plugin template'


# deck_name = u'語彙'
# model_name = u'Japonaise example_sentence'



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


def reset_card_due_stats(card):
    card.queue = 2
    card.type = 2
    card.due = mw.col.sched.today
    card.ivl = 1
    card.factor = 1000
    card.col.sched._updateStats(card, 'rev')
    card.flushSched()


def add_word_card(expression, reading, meaning):
    deck = find_deck()
    model = find_model(deck)
    set_deck_id(model, deck['id'])
    select_model(model)
    note = make_note()
    add_info_to_note(note, expression, reading, meaning)
    mw.col.addNote(note)
    note.flush()


def add_info_to_note(note, expression, reading, meaning):
    new_card_data = (expression, reading, meaning)
    i = 0
    for (name, value) in note.items():
        if i < 3:
            note[name] = value + new_card_data[i]
        else:
            note[name] = value + ""
        i += 1


def make_note():
    return mw.col.newNote(False)


def select_model(model):
    mw.col.models.setCurrent(model)


def find_deck():
    deck = mw.col.decks.byName(deck_name)
    if deck == None:
        mw.col.decks.id(deck_name)
    deck = mw.col.decks.byName(deck_name)
    return deck


def find_model(deck):
    model = mw.col.models.byName(model_name)
    if model == None:
        add_model(model_name, deck['id'])
    model = mw.col.models.byName(model_name)
    return model


def set_deck_id(model, did):
    model['tmpls'][0]['did'] = did


def add_model(name, id):
    m = mw.col.models.new(name)
    newfield = mw.col.models.newField("Expression")
    newfield2 = mw.col.models.newField("Reading")
    newfield3 = mw.col.models.newField("Meaning")
    mw.col.models.addField(m, newfield)
    mw.col.models.addField(m, newfield2)
    mw.col.models.addField(m, newfield3)
    template = mw.col.models.newTemplate("template")
    template[
        'qfmt'] = "<span style=\"font-family: Kozuka Gothic Pr6N M;   \"><span style=\"font-family: Kozuka Gothic Pr6N M; font-size: 40px; \">{{Expression}}</span></span>"
    template[
        'afmt'] = "{{FrontSide}} <hr id=answer> <span style=\"font-family: Kozuka Gothic Pr6N M;   \">{{Reading}}<br>{{Meaning}}<br><p align=\"left\">"
    template['did'] = id
    mw.col.models.addTemplate(m, template)
    mw.col.models.add(m)
