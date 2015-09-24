# -*- coding: utf-8 -*-
#python 2.7
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
    searcher = Jp_to_eng_word_search_handler()

    mw.myWidget = widget = QWidget()
    widget.resize(600, 400)


    textbox = QLineEdit(widget)
    #textbox.move(20, 20)
    textbox.resize(280,40)
    button = QPushButton('Click me', widget)
    button.move(300,0)

    @pyqtSlot()
    def on_click():
        #textbox.setText("Button clicked.")
        #table(searcher.search(textbox.text()))
        asd = searcher.get_search_result(textbox.text())

        showInfo(asd.get_expression_number(0))
    button.clicked.connect(on_click)


    # Show window
    widget.show()

def table(search_result):
    mw.table = table = QTableView(mw.myWidget)
    mw.tableitem = tableItem = QListView()

# initiate table
    table.setWindowTitle("QTableWidget Example @pythonspot.com")
    table.move(0,50)
    table.resize(400, 250)

    table.setShowGrid(False)


    #table.hide()
    #table.setTopMargin(0)


action = QAction("test", mw)
mw.connect(action, SIGNAL("triggered()"), testFunction)
mw.form.menuTools.addAction(action)