# -.- coding: utf-8 -.-
from aqt.qt import *
import os
from .. import config_parser


def makeAreas(widget):
    make_upper_area(widget)
    make_lower_area(widget)

    layout = QVBoxLayout(widget)
    layout.addWidget(widget.textboxarea)
    layout.addWidget(widget.htmlarea)


def make_lower_area(widget):
    widget.htmlarea = QWebView(widget)
    widget.htmlarea.move(0, 40)
    path = os.path.dirname(__file__) + "\style.css"

    #path = u'C:/Users/Spaceducks/Documents/Anki/addons/jp_eng_jisho_import/Gui/style.css'
    widget.htmlarea.settings().setUserStyleSheetUrl(QUrl.fromLocalFile(path))
    widget.htmlarea.setHtml("<html><head> </head><body><p>Hello</p></body> </html>")


def make_upper_area(widget):
    add_textbox_area(widget)
    add_search_box(widget)
    add_set_deck_field(widget)
    add_labels(widget)
    set_upper_layout(widget)

def set_upper_layout(widget):
    textboxareaLayout = QHBoxLayout(widget.textboxarea)
    textboxareaLayout.addWidget(widget.search_label)
    textboxareaLayout.addWidget(widget.search_box)
    textboxareaLayout.addSpacing(40)
    textboxareaLayout.addWidget(widget.set_deck_label)
    textboxareaLayout.addWidget(widget.setDeck)
    textboxareaLayout.addWidget(widget.current_deck_label)
    textboxareaLayout.setAlignment(widget.current_deck_label, Qt.AlignRight)
    textboxareaLayout.setAlignment(widget.setDeck, Qt.AlignRight)
    textboxareaLayout.setAlignment(widget.set_deck_label, Qt.AlignRight)
    textboxareaLayout.addSpacing(20)

def add_labels(widget):
    font = QFont()
    font.setPixelSize(14)
    widget.current_deck_label = QLabel(widget.textboxarea)
    config_parser.read_config()
    widget.current_deck_label.setText("Current: "+config_parser.deck_name)
    widget.current_deck_label.setFont(font)
    widget.search_label = QLabel(widget.textboxarea)
    widget.search_label.setText("Search:")
    widget.search_label.setFont(font)
    widget.set_deck_label = QLabel(widget.textboxarea)
    widget.set_deck_label.setText("Set Deck:")
    widget.set_deck_label.setFont(font)

def add_search_box(widget):
    widget.search_box = QLineEdit(widget.textboxarea)
    widget.search_box.setMinimumHeight(23)

def add_set_deck_field(widget):
    widget.setDeck = QLineEdit(widget.textboxarea)
    widget.setDeck.setMinimumHeight(23)
    widget.setDeck.setMinimumWidth(80)
    widget.setDeck.setMaximumWidth(80)

def add_textbox_area(widget):
    widget.textboxarea = QWidget(widget)
    widget.textboxarea.setMinimumSize(QSize(100, 35))
    widget.textboxarea.setMaximumHeight(35)
