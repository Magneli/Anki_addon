# -*- coding: utf-8 -*-
# python 2.7
# import the main window object (mw) from ankiqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, getText
# import all of the Qt GUI library
from aqt.qt import *
from anki import Collection
import sys
import anki_api_interface

from Jp_to_eng_word_search_handler import Jp_to_eng_word_search_handler



def testFunction():

    mw.myWidget = widget = QWidget()
    add_textbox()
    add_main_buttons()
    widget.show()


def add_textbox():
    widget = mw.myWidget
    widget.resize(600, 400)
    mw.myWidget.textbox =textbox= QLineEdit(widget)
    textbox.resize(400, 30)


def add_main_buttons():
    widget = mw.myWidget
    textbox = mw.myWidget.textbox
    searcher = Jp_to_eng_word_search_handler()

    mw.myWidget.button = button = QPushButton('Click me', widget)
    button.resize(0, 0)
    mw.myWidget.button2 = button2 = QPushButton('Click me', widget)
    button2.resize(0, 0)

    def nothing():
        pass

    def on_click():
        asd = searcher.get_search_result(textbox.text())
        textbox.setText("")
        showInfo(asd.get_expression_number(0))

    button.clicked.connect(on_click)
    button2.clicked.connect(nothing)
    button2.setShortcut(QKeySequence("tab"))
    button.setShortcut(QKeySequence("return"))


def table(search_result):
    mw.table = table = QTableView(mw.myWidget)
    mw.tableitem = tableItem = QListView()

    # initiate table
    table.setWindowTitle("QTableWidget Example @pythonspot.com")
    table.move(0, 50)
    table.resize(400, 250)

    table.setShowGrid(False)


    # table.hide()
    # table.setTopMargin(0)


action = QAction("test", mw)
mw.connect(action, SIGNAL("triggered()"), testFunction)
mw.form.menuTools.addAction(action)
