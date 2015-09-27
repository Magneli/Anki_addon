# -*- coding: utf-8 -*-
# python 2.7
# import the main window object (mw) from ankiqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, getText
# import all of the Qt GUI library
from aqt.qt import *
from anki import Collection
import os
import sys

from platform import system

import anki_api_interface

from Hotkeys import Hotkeys
from Jp_to_eng_word_search_handler import Jp_to_eng_word_search_handler


def testFunction():
    interface = User_Interface()


class User_Interface():
    def __init__(self):
        self.search_result = None
        self.small_font = 9
        self.big_font = 16
        mw.myWidget = self.widget = QWidget()
        self.widget.resize(1020, 700)
        self.add_input_textbox()
        self.add_inner_box()
        self.add_scroll_area()
        self.add_main_buttons()
        self.add_hotkeys()
        self.widget.show()

    def add_inner_box(self):
        self.inner_box = QWidget()
        self.inner_box.resize(1000, 2300)

        self.numbercolumn = QListWidget(self.inner_box)
        self.numbercolumn.move(0, 0)
        self.numbercolumn.resize(25, 500)

        self.column1 = QListWidget(self.inner_box)
        self.column1.move(28, 0)
        self.column1.resize(300, 500)

        self.column2 = QListWidget(self.inner_box)
        self.column2.move(348, 0)
        self.column2.resize(300, 500)

        self.column3 = QListWidget(self.inner_box)
        self.column3.move(668, 0)
        self.column3.resize(300, 500)

    def add_scroll_area(self):
        mw.scrollarea = self.scrollarea = QScrollArea(self.widget)
        self.scrollarea.move(0, 50)
        self.scrollarea.resize(1020, 650)
        self.scrollarea.setWidget(self.inner_box)

    def add_input_textbox(self):

        mw.textbox = self.textbox = QLineEdit(self.widget)
        self.textbox.move(300, 0)
        self.textbox.resize(400, 30)

    def add_main_buttons(self):

        self.searcher = Jp_to_eng_word_search_handler()
        self.search_button = QPushButton('Click me', self.widget)
        self.search_button.resize(0, 0)
        self.search_button.clicked.connect(self.on_search)
        self.search_button.setShortcut(QKeySequence("return"))

    def on_search(self):

        self.search_result = self.searcher.get_search_result(self.textbox.text())
        if self.search_result.get_result_count() > 0:
            self.textbox.setText("")
            self.column1.clear()
            self.column2.clear()
            self.column3.clear()
            self.numbercolumn.clear()
            self.realign_columns()
            for i in range(0, self.search_result.get_result_count()):
                self.add_to_third_column(i, self.search_result)
                self.add_to_number_column(i, self.search_result)
                self.add_to_first_column(i, self.search_result)
                self.add_to_second_column(i, self.search_result)

    def realign_columns(self):
        column_height = self.get_column3_height()
        self.resize_column_heights(column_height)
        self.move_columns()

    def column12_width(self):
        width_in_pixels = 150
        for i in range(0, self.search_result.get_result_count()):
            if self.search_result.get_reading_number(i).__len__() * 22 > width_in_pixels:
                width_in_pixels = self.search_result.get_reading_number(i).__len__() * 22
            if self.search_result.get_expression_number(i).__len__() * 22 > width_in_pixels:
                width_in_pixels = self.search_result.get_expression_number(i).__len__() * 22
        return width_in_pixels

    def move_columns(self):
        self.column2.move(25 + self.column12_width(), 0)
        self.column3.move(25 + (self.column12_width() * 2), 0)

    def resize_column_heights(self, new_height):
        self.column1.resize(self.column12_width(), new_height)
        self.column2.resize(self.column12_width(), new_height)
        self.column3.resize(1200 - self.column12_width() - self.column12_width(), new_height)
        self.numbercolumn.resize(50, new_height)

        self.inner_box.resize(1000, new_height + 50)

    def get_column3_height(self):
        total_lines = 0
        for i in range(0, self.search_result.get_result_count()):
            total_lines += self.count_lines(self.search_result.get_meaning_number(i))
        return total_lines * 13 + 40 + (self.search_result.get_result_count() * 30)

    def add_to_third_column(self, i, result):
        self.add_string_to_list(self.column3, result.get_meaning_number(i), self.small_font)

        self.column3_line_count = self.count_lines(result.get_meaning_number(i))

        self.add_padding_column3()
        self.add_padding_other_columns()

    def add_padding_column3(self):
        if self.column3_line_count == 1:
            self.add_string_to_list(self.column3, "\n", self.small_font)
        else:
            self.add_string_to_list(self.column3, "", self.small_font)

    def add_padding_other_columns(self):
        if self.column3_line_count < 3:
            self.lines_off_padding = self.make_newlines(0)
        else:
            self.lines_off_padding = self.make_newlines(self.column3_line_count - 1)

    def add_to_number_column(self, i, result):
        shortcut_list = (
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P")

        self.add_string_to_list(self.numbercolumn, shortcut_list[i], self.big_font)
        self.add_string_to_list(self.numbercolumn, self.lines_off_padding, self.small_font)

    def add_to_first_column(self, i, result):

        self.add_string_to_list(self.column1, result.get_expression_number(i), self.big_font)
        self.add_string_to_list(self.column1, self.lines_off_padding, self.small_font)

    def add_to_second_column(self, i, result):
        self.add_string_to_list(self.column2, result.get_reading_number(i), self.big_font)
        self.add_string_to_list(self.column2, self.lines_off_padding, self.small_font)

    def add_string_to_list(self, itemlist, string, fontsize):
        item = QListWidgetItem(string)
        font = QFont()
        #font.setFamily("Lucida")
        font.setPointSize(fontsize)
        item.setFont(font)
        itemlist.addItem(item)

    def make_newlines(self, number):
        result = " "
        for i in range(0, number - 1):
            result += "\n"
        return result

    def count_lines(self, string):
        counter = 1
        for char in string:
            if char == '\n':
                counter += 1
        return counter

    def add_hotkeys(self):
        self.hk = Hotkeys(self)
