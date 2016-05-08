from ..Search_handler import Jp_to_eng_word_search_handler
from html_factory import display_search_result
from aqt.qt import *
from ..API import anki_api_interface
from .. import config_parser

shortcut_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "Q", "W", "E", "R", "T", "Y", "U", "I", "O",
                         "P"]

def add_keybinds(widget):
    widget.search_box.returnPressed.connect(make_search_function(widget))
    widget.setDeck.returnPressed.connect(make_deck_select_function(widget))

    for i in range(0, 20):
            shortcut =QAction(widget)
            widget.addAction(shortcut)
            shortcut.triggered.connect(makehotkeyfunction(widget, shortcut_list[i], i))
            shortcut.setShortcut(QKeySequence("ctrl+" + shortcut_list[i]))




def make_deck_select_function(widget):
    return lambda: on_deck_select_press(widget)

def on_deck_select_press(widget):
    widget.current_deck_label.setText("Current: "+widget.setDeck.text())
    config_parser.deck_name = widget.setDeck.text()
    config_parser.write_config()



def makehotkeyfunction(widget, hotkey, number):
    return lambda:makehotkey(widget, hotkey, number)

def makehotkey(widget, hotkey,number):
    if widget.search_result is not None and number < widget.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(
            widget.search_result.get_expression_number(number), widget.search_result.get_reading_number(number)):
        add_card_to_anki(widget.search_result.get_expression_number(number),
                      widget.search_result.get_reading_number(number),
                      widget.search_result.get_meaning_number(number))

def add_card_to_anki(exp, reading, meaning):
        if exp != "":
            if not anki_api_interface.is_card_in_collection(exp, reading):
                anki_api_interface.add_word_card(exp, reading, meaning)
        else:
            if not anki_api_interface.is_card_in_collection(reading, reading):
                anki_api_interface.add_word_card(reading, reading, meaning)

def make_search_function(widget):
    return lambda: on_search(widget)
def on_search(widget):
    searcher = Jp_to_eng_word_search_handler.Jp_to_eng_word_search_handler()
    widget.search_result = searcher.search(widget.search_box.text())
    display_search_result(widget)
