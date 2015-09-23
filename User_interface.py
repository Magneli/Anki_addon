# -*- coding: utf-8 -*-
#python 2.7
# import the main window object (mw) from ankiqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *
from anki import Collection
import sys
import anki_api_interface
from Search_handler import Search_handler
def testFunction():
    searcher = Search_handler()


    # The QWidget widget is the base class of all user interface objects in PyQt4.
    mw.myWidget = widget = QWidget()

    # Set window size.
    widget.resize(320, 240)

    # Set window title
    widget.setWindowTitle("Hello World!")

    textbox = QLineEdit(widget)
    textbox.move(20, 20)
    textbox.resize(280,40)
    button = QPushButton('Click me', widget)
    button.move(20,80)

    result = QMessageBox.question(widget, 'Message', "Do you like Python?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

    if result == QMessageBox.Yes:
        print 'Yes.'
    else:
        print 'No.'

    table()
    def on_click():
        taberu = searcher.search("taberu")
        textbox.setText(taberu.get_expression_number(0))

    button.clicked.connect(on_click)
    # Show window
    widget.show()

def table():
    mw.table = table = QTableWidget()
    mw.tableitem = tableItem = QTableWidgetItem()

# initiate table
    table.setWindowTitle("QTableWidget Example @pythonspot.com")
    table.resize(400, 250)
    table.setRowCount(4)
    table.setColumnCount(2)

    # set data
    table.setItem(0,0, QTableWidgetItem("Item (1,1)"))
    table.setItem(0,1, QTableWidgetItem("Item (1,2)"))
    table.setItem(1,0, QTableWidgetItem("Item (2,1)"))
    table.setItem(1,1, QTableWidgetItem("Item (2,2)"))
    table.setItem(2,0, QTableWidgetItem("Item (3,1)"))
    table.setItem(2,1, QTableWidgetItem("Item (3,2)"))
    table.setItem(3,0, QTableWidgetItem("Item (4,1)"))
    table.setItem(3,1, QTableWidgetItem("Item (4,2)"))
    #table.show()


action = QAction("test", mw)
mw.connect(action, SIGNAL("triggered()"), testFunction)
mw.form.menuTools.addAction(action)