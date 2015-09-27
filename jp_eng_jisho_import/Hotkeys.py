# -*- coding: utf-8 -*-
# python 2.7
# import all of the Qt GUI library
from aqt.qt import *
from anki import Collection
import anki_api_interface


class Hotkeys():
    def do_stuff(self, exp, reading, meaning):
        if exp != "":
            anki_api_interface.add_word_card(exp, reading, meaning)
        else:
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
        self.parent.button1 = QPushButton('Click me', self.parent.widget)
        self.parent.button1.resize(0, 0)
        self.parent.button1.clicked.connect(self.hotkey1)
        self.parent.button1.setShortcut(QKeySequence("ctrl+1"))

    def hotkey1(self):
        if 0<self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(self.parent.search_result.get_expression_number(0),self.parent.search_result.get_reading_number(0)):
            self.do_stuff(self.parent.search_result.get_expression_number(0),
                                             self.parent.search_result.get_reading_number(0),
                                             self.parent.search_result.get_meaning_number(0))

    def button2(self):
        self.parent.button2 = QPushButton('Click me', self.parent.widget)
        self.parent.button2.resize(0, 0)
        self.parent.button2.clicked.connect(self.hotkey2)
        self.parent.button2.setShortcut(QKeySequence("ctrl+2"))

    def hotkey2(self):
        if 1<self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(self.parent.search_result.get_expression_number(1),self.parent.search_result.get_reading_number(1)):
            self.do_stuff(self.parent.search_result.get_expression_number(1),
                                             self.parent.search_result.get_reading_number(1),
                                             self.parent.search_result.get_meaning_number(1))

    def button3(self):
        self.parent.button3 = QPushButton('Click me', self.parent.widget)
        self.parent.button3.resize(0, 0)
        self.parent.button3.clicked.connect(self.hotkey3)
        self.parent.button3.setShortcut(QKeySequence("ctrl+3"))

    def hotkey3(self):
        if 2<self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(self.parent.search_result.get_expression_number(2),self.parent.search_result.get_reading_number(2)):
            self.do_stuff(self.parent.search_result.get_expression_number(2),
                                             self.parent.search_result.get_reading_number(2),
                                             self.parent.search_result.get_meaning_number(2))

    def button4(self):
        self.parent.button4 = QPushButton('Click me', self.parent.widget)
        self.parent.button4.resize(0, 0)
        self.parent.button4.clicked.connect(self.hotkey4)
        self.parent.button4.setShortcut(QKeySequence("ctrl+4"))

    def hotkey4(self):
        if 3<self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(self.parent.search_result.get_expression_number(3),self.parent.search_result.get_reading_number(3)):
            self.do_stuff(self.parent.search_result.get_expression_number(3),
                                             self.parent.search_result.get_reading_number(3),
                                             self.parent.search_result.get_meaning_number(3))

    def button5(self):
        self.parent.button5 = QPushButton('Click me', self.parent.widget)
        self.parent.button5.resize(0, 0)
        self.parent.button5.clicked.connect(self.hotkey5)
        self.parent.button5.setShortcut(QKeySequence("ctrl+5"))

    def hotkey5(self):
        if 4<self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(self.parent.search_result.get_expression_number(4),self.parent.search_result.get_reading_number(4)):
            self.do_stuff(self.parent.search_result.get_expression_number(4),
                                             self.parent.search_result.get_reading_number(4),
                                             self.parent.search_result.get_meaning_number(4))

    def button6(self):
        self.parent.button6 = QPushButton('Click me', self.parent.widget)
        self.parent.button6.resize(0, 0)
        self.parent.button6.clicked.connect(self.hotkey6)
        self.parent.button6.setShortcut(QKeySequence("ctrl+6"))

    def hotkey6(self):
        if 5<self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(self.parent.search_result.get_expression_number(5),self.parent.search_result.get_reading_number(5)):
            self.do_stuff(self.parent.search_result.get_expression_number(5),
                                             self.parent.search_result.get_reading_number(5),
                                             self.parent.search_result.get_meaning_number(5))

    def button7(self):
        self.parent.button7 = QPushButton('Click me', self.parent.widget)
        self.parent.button7.resize(0, 0)
        self.parent.button7.clicked.connect(self.hotkey7)
        self.parent.button7.setShortcut(QKeySequence("ctrl+7"))

    def hotkey7(self):
        if 6<self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(self.parent.search_result.get_expression_number(6),self.parent.search_result.get_reading_number(6)):
            self.do_stuff(self.parent.search_result.get_expression_number(6),
                                             self.parent.search_result.get_reading_number(6),
                                             self.parent.search_result.get_meaning_number(6))

    def button8(self):
        self.parent.button8 = QPushButton('Click me', self.parent.widget)
        self.parent.button8.resize(0, 0)
        self.parent.button8.clicked.connect(self.hotkey8)
        self.parent.button8.setShortcut(QKeySequence("ctrl+8"))

    def hotkey8(self):
        if 7<self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(self.parent.search_result.get_expression_number(7),self.parent.search_result.get_reading_number(7)):
            self.do_stuff(self.parent.search_result.get_expression_number(7),
                                             self.parent.search_result.get_reading_number(7),
                                             self.parent.search_result.get_meaning_number(7))

    def button9(self):
        self.parent.button9 = QPushButton('Click me', self.parent.widget)
        self.parent.button9.resize(0, 0)
        self.parent.button9.clicked.connect(self.hotkey9)
        self.parent.button9.setShortcut(QKeySequence("ctrl+9"))

    def hotkey9(self):
        if 8<self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(self.parent.search_result.get_expression_number(8),self.parent.search_result.get_reading_number(8)):
            self.do_stuff(self.parent.search_result.get_expression_number(8),
                                             self.parent.search_result.get_reading_number(8),
                                             self.parent.search_result.get_meaning_number(8))

    def button0(self):
        self.parent.button0 = QPushButton('Click me', self.parent.widget)
        self.parent.button0.resize(0, 0)
        self.parent.button0.clicked.connect(self.hotkey0)
        self.parent.button0.setShortcut(QKeySequence("ctrl+0"))

    def hotkey0(self):
        if 9<self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(self.parent.search_result.get_expression_number(9),self.parent.search_result.get_reading_number(9)):
            self.do_stuff(self.parent.search_result.get_expression_number(9),
                                             self.parent.search_result.get_reading_number(9),
                                             self.parent.search_result.get_meaning_number(9))

    def buttonQ(self):
        self.parent.buttonQ = QPushButton('Click me', self.parent.widget)
        self.parent.buttonQ.resize(0, 0)
        self.parent.buttonQ.clicked.connect(self.hotkeyQ)
        self.parent.buttonQ.setShortcut(QKeySequence("ctrl+Q"))

    def hotkeyQ(self):
        if 10<self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(self.parent.search_result.get_expression_number(10),self.parent.search_result.get_reading_number(10)):
            self.do_stuff(self.parent.search_result.get_expression_number(10),
                                             self.parent.search_result.get_reading_number(10),
                                             self.parent.search_result.get_meaning_number(10))

    def buttonW(self):
        self.parent.buttonW = QPushButton('Click me', self.parent.widget)
        self.parent.buttonW.resize(0, 0)
        self.parent.buttonW.clicked.connect(self.hotkeyW)
        self.parent.buttonW.setShortcut(QKeySequence("ctrl+W"))

    def hotkeyW(self):
        if 11<self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(self.parent.search_result.get_expression_number(11),self.parent.search_result.get_reading_number(11)):
            self.do_stuff(self.parent.search_result.get_expression_number(11),
                                             self.parent.search_result.get_reading_number(11),
                                             self.parent.search_result.get_meaning_number(11))

    def buttonE(self):
        self.parent.buttonE = QPushButton('Click me', self.parent.widget)
        self.parent.buttonE.resize(0, 0)
        self.parent.buttonE.clicked.connect(self.hotkeyE)
        self.parent.buttonE.setShortcut(QKeySequence("ctrl+E"))

    def hotkeyE(self):
        if 12<self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(self.parent.search_result.get_expression_number(12),self.parent.search_result.get_reading_number(12)):
            self.do_stuff(self.parent.search_result.get_expression_number(12),
                                             self.parent.search_result.get_reading_number(12),
                                             self.parent.search_result.get_meaning_number(12))

    def buttonR(self):
        self.parent.buttonR = QPushButton('Click me', self.parent.widget)
        self.parent.buttonR.resize(0, 0)
        self.parent.buttonR.clicked.connect(self.hotkeyR)
        self.parent.buttonR.setShortcut(QKeySequence("ctrl+R"))

    def hotkeyR(self):
        if 13<self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(self.parent.search_result.get_expression_number(13),self.parent.search_result.get_reading_number(13)):
            self.do_stuff(self.parent.search_result.get_expression_number(13),
                                             self.parent.search_result.get_reading_number(13),
                                             self.parent.search_result.get_meaning_number(13))

    def buttonT(self):
        self.parent.buttonT = QPushButton('Click me', self.parent.widget)
        self.parent.buttonT.resize(0, 0)
        self.parent.buttonT.clicked.connect(self.hotkeyT)
        self.parent.buttonT.setShortcut(QKeySequence("ctrl+T"))

    def hotkeyT(self):
        if 14<self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(self.parent.search_result.get_expression_number(14),self.parent.search_result.get_reading_number(14)):
            self.do_stuff(self.parent.search_result.get_expression_number(14),
                                             self.parent.search_result.get_reading_number(14),
                                             self.parent.search_result.get_meaning_number(14))

    def buttonY(self):
        self.parent.buttonY = QPushButton('Click me', self.parent.widget)
        self.parent.buttonY.resize(0, 0)
        self.parent.buttonY.clicked.connect(self.hotkeyY)
        self.parent.buttonY.setShortcut(QKeySequence("ctrl+Y"))

    def hotkeyY(self):
        if 15<self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(self.parent.search_result.get_expression_number(15),self.parent.search_result.get_reading_number(15)):
            self.do_stuff(self.parent.search_result.get_expression_number(15),
                                             self.parent.search_result.get_reading_number(15),
                                             self.parent.search_result.get_meaning_number(15))

    def buttonU(self):
        self.parent.buttonU = QPushButton('Click me', self.parent.widget)
        self.parent.buttonU.resize(0, 0)
        self.parent.buttonU.clicked.connect(self.hotkeyU)
        self.parent.buttonU.setShortcut(QKeySequence("ctrl+U"))

    def hotkeyU(self):
        if 16<self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(self.parent.search_result.get_expression_number(16),self.parent.search_result.get_reading_number(16)):
            self.do_stuff(self.parent.search_result.get_expression_number(16),
                                             self.parent.search_result.get_reading_number(16),
                                             self.parent.search_result.get_meaning_number(16))

    def buttonI(self):
        self.parent.buttonI = QPushButton('Click me', self.parent.widget)
        self.parent.buttonI.resize(0, 0)
        self.parent.buttonI.clicked.connect(self.hotkeyI)
        self.parent.buttonI.setShortcut(QKeySequence("ctrl+I"))

    def hotkeyI(self):
        if 17<self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(self.parent.search_result.get_expression_number(17),self.parent.search_result.get_reading_number(17)):
            self.do_stuff(self.parent.search_result.get_expression_number(17),
                                             self.parent.search_result.get_reading_number(17),
                                             self.parent.search_result.get_meaning_number(17))

    def buttonO(self):
        self.parent.buttonO = QPushButton('Click me', self.parent.widget)
        self.parent.buttonO.resize(0, 0)
        self.parent.buttonO.clicked.connect(self.hotkeyO)
        self.parent.buttonO.setShortcut(QKeySequence("ctrl+O"))

    def hotkeyO(self):
        if 18<self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(self.parent.search_result.get_expression_number(18),self.parent.search_result.get_reading_number(18)):
            self.do_stuff(self.parent.search_result.get_expression_number(18),
                                             self.parent.search_result.get_reading_number(18),
                                             self.parent.search_result.get_meaning_number(18))

    def buttonP(self):
        self.parent.buttonP = QPushButton('Click me', self.parent.widget)
        self.parent.buttonP.resize(0, 0)
        self.parent.buttonP.clicked.connect(self.hotkeyP)
        self.parent.buttonP.setShortcut(QKeySequence("ctrl+P"))

    def hotkeyP(self):
        if 19<self.parent.search_result.get_result_count() and not anki_api_interface.is_card_in_collection(self.parent.search_result.get_expression_number(19),self.parent.search_result.get_reading_number(19)):
            self.do_stuff(self.parent.search_result.get_expression_number(19),
                                             self.parent.search_result.get_reading_number(19),
                                             self.parent.search_result.get_meaning_number(19))



