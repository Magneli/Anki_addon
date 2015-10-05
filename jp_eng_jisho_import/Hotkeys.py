# -*- coding: utf-8 -*-
# python 2.7
# import all of the Qt GUI library
from aqt.qt import *
import anki_api_interface
from aqt.utils import showInfo


class Hotkeys():
    def do_stuff(self, exp, reading, meaning):
        if exp != "":
            if not anki_api_interface.is_card_in_collection(exp, reading):
                anki_api_interface.add_word_card(exp, reading, meaning)
        else:
            if not anki_api_interface.is_card_in_collection(reading, reading):
                anki_api_interface.add_word_card(reading, reading, meaning)

    def __init__(self, parent):
        self.parent = parent

        self.button1()
        self.button2()
        self.button3()
        self.button4()
        self.button5()
        self.button6()
        self.button7()
        self.button8()
        self.button9()
        self.button0()
        self.buttonQ()
        self.buttonW()
        self.buttonE()
        self.buttonR()
        self.buttonT()
        self.buttonY()
        self.buttonU()
        self.buttonI()
        self.buttonO()
        self.buttonP()

    def button1(self):
        button1 = QPushButton('Click me', self.parent.widget)
        button1.resize(0, 0)
        button1.clicked.connect(self.hotkey1)
        button1.setShortcut(QKeySequence("ctrl+1"))

    def hotkey1(self):
        if 0 < self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(
                self.parent.search_result.get_expression_number(0), self.parent.search_result.get_reading_number(0)):
            self.do_stuff(self.parent.search_result.get_expression_number(0),
                          self.parent.search_result.get_reading_number(0),
                          self.parent.search_result.get_meaning_number(0))

    def button2(self):
        button2 = QPushButton('Click me', self.parent.widget)
        button2.resize(0, 0)
        button2.clicked.connect(self.hotkey2)
        button2.setShortcut(QKeySequence("ctrl+2"))

    def hotkey2(self):
        if 1 < self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(
                self.parent.search_result.get_expression_number(1), self.parent.search_result.get_reading_number(1)):
            self.do_stuff(self.parent.search_result.get_expression_number(1),
                          self.parent.search_result.get_reading_number(1),
                          self.parent.search_result.get_meaning_number(1))

    def button3(self):
        button3 = QPushButton('Click me', self.parent.widget)
        button3.resize(0, 0)
        button3.clicked.connect(self.hotkey3)
        button3.setShortcut(QKeySequence("ctrl+3"))

    def hotkey3(self):
        if 2 < self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(
                self.parent.search_result.get_expression_number(2), self.parent.search_result.get_reading_number(2)):
            self.do_stuff(self.parent.search_result.get_expression_number(2),
                          self.parent.search_result.get_reading_number(2),
                          self.parent.search_result.get_meaning_number(2))

    def button4(self):
        button4 = QPushButton('Click me', self.parent.widget)
        button4.resize(0, 0)
        button4.clicked.connect(self.hotkey4)
        button4.setShortcut(QKeySequence("ctrl+4"))

    def hotkey4(self):
        if 3 < self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(
                self.parent.search_result.get_expression_number(3), self.parent.search_result.get_reading_number(3)):
            self.do_stuff(self.parent.search_result.get_expression_number(3),
                          self.parent.search_result.get_reading_number(3),
                          self.parent.search_result.get_meaning_number(3))

    def button5(self):
        button5 = QPushButton('Click me', self.parent.widget)
        button5.resize(0, 0)
        button5.clicked.connect(self.hotkey5)
        button5.setShortcut(QKeySequence("ctrl+5"))

    def hotkey5(self):
        if 4 < self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(
                self.parent.search_result.get_expression_number(4), self.parent.search_result.get_reading_number(4)):
            self.do_stuff(self.parent.search_result.get_expression_number(4),
                          self.parent.search_result.get_reading_number(4),
                          self.parent.search_result.get_meaning_number(4))

    def button6(self):
        button6 = QPushButton('Click me', self.parent.widget)
        button6.resize(0, 0)
        button6.clicked.connect(self.hotkey6)
        button6.setShortcut(QKeySequence("ctrl+6"))

    def hotkey6(self):
        if 5 < self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(
                self.parent.search_result.get_expression_number(5), self.parent.search_result.get_reading_number(5)):
            self.do_stuff(self.parent.search_result.get_expression_number(5),
                          self.parent.search_result.get_reading_number(5),
                          self.parent.search_result.get_meaning_number(5))

    def button7(self):
        button7 = QPushButton('Click me', self.parent.widget)
        button7.resize(0, 0)
        button7.clicked.connect(self.hotkey7)
        button7.setShortcut(QKeySequence("ctrl+7"))

    def hotkey7(self):
        if 6 < self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(
                self.parent.search_result.get_expression_number(6), self.parent.search_result.get_reading_number(6)):
            self.do_stuff(self.parent.search_result.get_expression_number(6),
                          self.parent.search_result.get_reading_number(6),
                          self.parent.search_result.get_meaning_number(6))

    def button8(self):
        button8 = QPushButton('Click me', self.parent.widget)
        button8.resize(0, 0)
        button8.clicked.connect(self.hotkey8)
        button8.setShortcut(QKeySequence("ctrl+8"))

    def hotkey8(self):
        if 7 < self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(
                self.parent.search_result.get_expression_number(7), self.parent.search_result.get_reading_number(7)):
            self.do_stuff(self.parent.search_result.get_expression_number(7),
                          self.parent.search_result.get_reading_number(7),
                          self.parent.search_result.get_meaning_number(7))

    def button9(self):
        button9 = QPushButton('Click me', self.parent.widget)
        button9.resize(0, 0)
        button9.clicked.connect(self.hotkey9)
        button9.setShortcut(QKeySequence("ctrl+9"))

    def hotkey9(self):
        if 8 < self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(
                self.parent.search_result.get_expression_number(8), self.parent.search_result.get_reading_number(8)):
            self.do_stuff(self.parent.search_result.get_expression_number(8),
                          self.parent.search_result.get_reading_number(8),
                          self.parent.search_result.get_meaning_number(8))

    def button0(self):
        button0 = QPushButton('Click me', self.parent.widget)
        button0.resize(0, 0)
        button0.clicked.connect(self.hotkey0)
        button0.setShortcut(QKeySequence("ctrl+0"))

    def hotkey0(self):
        if 9 < self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(
                self.parent.search_result.get_expression_number(9), self.parent.search_result.get_reading_number(9)):
            self.do_stuff(self.parent.search_result.get_expression_number(9),
                          self.parent.search_result.get_reading_number(9),
                          self.parent.search_result.get_meaning_number(9))

    def buttonQ(self):
        buttonQ = QPushButton('Click me', self.parent.widget)
        buttonQ.resize(0, 0)
        buttonQ.clicked.connect(self.hotkeyQ)
        buttonQ.setShortcut(QKeySequence("ctrl+Q"))

    def hotkeyQ(self):
        if 10 < self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(
                self.parent.search_result.get_expression_number(10), self.parent.search_result.get_reading_number(10)):
            self.do_stuff(self.parent.search_result.get_expression_number(10),
                          self.parent.search_result.get_reading_number(10),
                          self.parent.search_result.get_meaning_number(10))

    def buttonW(self):
        buttonW = QPushButton('Click me', self.parent.widget)
        buttonW.resize(0, 0)
        buttonW.clicked.connect(self.hotkeyW)
        buttonW.setShortcut(QKeySequence("ctrl+W"))

    def hotkeyW(self):
        if 11 < self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(
                self.parent.search_result.get_expression_number(11), self.parent.search_result.get_reading_number(11)):
            self.do_stuff(self.parent.search_result.get_expression_number(11),
                          self.parent.search_result.get_reading_number(11),
                          self.parent.search_result.get_meaning_number(11))

    def buttonE(self):
        buttonE = QPushButton('Click me', self.parent.widget)
        buttonE.resize(0, 0)
        buttonE.clicked.connect(self.hotkeyE)
        buttonE.setShortcut(QKeySequence("ctrl+E"))

    def hotkeyE(self):
        if 12 < self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(
                self.parent.search_result.get_expression_number(12), self.parent.search_result.get_reading_number(12)):
            self.do_stuff(self.parent.search_result.get_expression_number(12),
                          self.parent.search_result.get_reading_number(12),
                          self.parent.search_result.get_meaning_number(12))

    def buttonR(self):
        buttonR = QPushButton('Click me', self.parent.widget)
        buttonR.resize(0, 0)
        buttonR.clicked.connect(self.hotkeyR)
        buttonR.setShortcut(QKeySequence("ctrl+R"))

    def hotkeyR(self):
        if 13 < self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(
                self.parent.search_result.get_expression_number(13), self.parent.search_result.get_reading_number(13)):
            self.do_stuff(self.parent.search_result.get_expression_number(13),
                          self.parent.search_result.get_reading_number(13),
                          self.parent.search_result.get_meaning_number(13))

    def buttonT(self):
        buttonT = QPushButton('Click me', self.parent.widget)
        buttonT.resize(0, 0)
        buttonT.clicked.connect(self.hotkeyT)
        buttonT.setShortcut(QKeySequence("ctrl+T"))

    def hotkeyT(self):
        if 14 < self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(
                self.parent.search_result.get_expression_number(14), self.parent.search_result.get_reading_number(14)):
            self.do_stuff(self.parent.search_result.get_expression_number(14),
                          self.parent.search_result.get_reading_number(14),
                          self.parent.search_result.get_meaning_number(14))

    def buttonY(self):
        buttonY = QPushButton('Click me', self.parent.widget)
        buttonY.resize(0, 0)
        buttonY.clicked.connect(self.hotkeyY)
        buttonY.setShortcut(QKeySequence("ctrl+Y"))

    def hotkeyY(self):
        if 15 < self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(
                self.parent.search_result.get_expression_number(15), self.parent.search_result.get_reading_number(15)):
            self.do_stuff(self.parent.search_result.get_expression_number(15),
                          self.parent.search_result.get_reading_number(15),
                          self.parent.search_result.get_meaning_number(15))

    def buttonU(self):
        buttonU = QPushButton('Click me', self.parent.widget)
        buttonU.resize(0, 0)
        buttonU.clicked.connect(self.hotkeyU)
        buttonU.setShortcut(QKeySequence("ctrl+U"))

    def hotkeyU(self):
        if 16 < self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(
                self.parent.search_result.get_expression_number(16), self.parent.search_result.get_reading_number(16)):
            self.do_stuff(self.parent.search_result.get_expression_number(16),
                          self.parent.search_result.get_reading_number(16),
                          self.parent.search_result.get_meaning_number(16))

    def buttonI(self):
        buttonI = QPushButton('Click me', self.parent.widget)
        buttonI.resize(0, 0)
        buttonI.clicked.connect(self.hotkeyI)
        buttonI.setShortcut(QKeySequence("ctrl+I"))

    def hotkeyI(self):
        if 17 < self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(
                self.parent.search_result.get_expression_number(17), self.parent.search_result.get_reading_number(17)):
            self.do_stuff(self.parent.search_result.get_expression_number(17),
                          self.parent.search_result.get_reading_number(17),
                          self.parent.search_result.get_meaning_number(17))

    def buttonO(self):
        buttonO = QPushButton('Click me', self.parent.widget)
        buttonO.resize(0, 0)
        buttonO.clicked.connect(self.hotkeyO)
        buttonO.setShortcut(QKeySequence("ctrl+O"))

    def hotkeyO(self):
        if 18 < self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(
                self.parent.search_result.get_expression_number(18), self.parent.search_result.get_reading_number(18)):
            self.do_stuff(self.parent.search_result.get_expression_number(18),
                          self.parent.search_result.get_reading_number(18),
                          self.parent.search_result.get_meaning_number(18))

    def buttonP(self):
        buttonP = QPushButton('Click me', self.parent.widget)
        buttonP.resize(0, 0)
        buttonP.clicked.connect(self.hotkeyP)
        buttonP.setShortcut(QKeySequence("ctrl+P"))

    def hotkeyP(self):
        if 19 < self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(
                self.parent.search_result.get_expression_number(19), self.parent.search_result.get_reading_number(19)):
            self.do_stuff(self.parent.search_result.get_expression_number(19),
                          self.parent.search_result.get_reading_number(19),
                          self.parent.search_result.get_meaning_number(19))
