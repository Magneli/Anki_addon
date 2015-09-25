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
    interface = User_Interface()


class User_Interface():
    def __init__(self):
        mw.myWidget = self.widget = QWidget()
        self.add_textbox()
        self.add_insidebox()
        self.add_scroll_area()

        teststring = "asdasdasdasdasdasd"
        # self.listWidget1.resize(teststring.__len__() * 8, 2000)
        # item = QListWidgetItem(teststring)
        # self.listWidget1.addItem(item)

        self.scrollarea.setWidget(self.insidebox)

        self.widget.show()

    def add_insidebox(self):
        self.insidebox = QWidget()
        self.insidebox.resize(900, 2300)

        self.listWidget1 = QListWidget(self.insidebox)
        self.listWidget1.move(0, 0)
        self.listWidget1.resize(300, 2000)

        self.listWidget2 = QListWidget(self.insidebox)
        self.listWidget2.move(320, 0)
        self.listWidget2.resize(300, 2000)

        self.add_main_buttons(self.listWidget2)
        self.listWidget3 = QListWidget(self.insidebox)
        self.listWidget3.move(640, 0)
        self.listWidget3.resize(300, 2000)

    def add_scroll_area(self):
        mw.scrollarea = self.scrollarea = QScrollArea(self.widget)
        self.scrollarea.move(0, 50)
        self.scrollarea.resize(1000, 500)

    def add_textbox(self):
        self.widget.resize(1000, 700)
        mw.textbox = self.textbox = QLineEdit(self.widget)
        self.textbox.resize(400, 30)

    def add_main_buttons(self, listWidget2):
        searcher = Jp_to_eng_word_search_handler()

        self.button = QPushButton('Click me', self.widget)
        self.button.resize(0, 0)
        self.button2 = QPushButton('Click me', self.widget)
        self.button2.resize(0, 0)

        def nothing():
            pass

        def on_click():
            result = searcher.get_search_result(self.textbox.text())
            self.textbox.setText("")
            listWidget2.clear()

            # showInfo(result.get_expression_number(0))
            # listWidget2.resize(1, 1)
            self.listWidget1.clear()
            self.listWidget2.clear()
            self.listWidget3.clear()
            for i in range(0, result.get_result_count()):
                item = QListWidgetItem(str(i+1)+": "+ result.get_expression_number(i)+"\n")
                self.listWidget1.addItem(item)

                item = QListWidgetItem(result.get_reading_number(i)+"\n")
                self.listWidget2.addItem(item)

                item = QListWidgetItem(result.get_meaning_number(i)+"\n")
                self.listWidget3.addItem(item)

        self.button.clicked.connect(on_click)
        self.button2.clicked.connect(nothing)
        self.button2.setShortcut(QKeySequence("tab"))
        self.button.setShortcut(QKeySequence("return"))

    def table(self, search_result):
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
