# -*- coding: utf-8 -*-
#python 2.7
from unittest import TestCase
import time
__author__ = 'Magne Limi'

from Search_handler import Search_handler
import datetime

class TestSearch_handler(TestCase):
    def test_no_result(self):
        searcher_handler = Search_handler()
        search_result_object = searcher_handler.search("nonsensicalgibberish")
        self.assertEqual(0, search_result_object.result_count)
        self.assertEqual([], search_result_object.expression)
        self.assertEqual([], search_result_object.reading)
        self.assertEqual([], search_result_object.meaning)

    def test_empty_search_term(self):
        searcher_handler = Search_handler()
        search_result_object = searcher_handler.search("")
        self.assertEqual(0, search_result_object.result_count)
        self.assertEqual([], search_result_object.expression)
        self.assertEqual([], search_result_object.reading)
        self.assertEqual([], search_result_object.meaning)

    def test_nasty_example(self):
        searcher_handler = Search_handler()
        search_result_object = searcher_handler.search("掛ける")
        self.assertEqual(1, search_result_object.result_count)
        self.assertEqual(u'掛ける', search_result_object.get_expression_number(0))
        self.assertEqual(u'かける', search_result_object.get_reading_number(0))
        self.maxDiff = None
        self.assertEqual(
            u'to hang (e.g. picture); to hoist (e.g. sail); to raise (e.g. flag);\nto sit;\nto be partway (verb); to begin (but not complete);\nto take (time, money); to expend (money, time, etc.);\nto make (a call);\nto multiply;\nto secure (e.g. lock);\nto put on (glasses, etc.);\nto cover;\nto burden someone;\nto apply (insurance);\nto turn on (an engine, etc.); to set (a dial, an alarm clock, etc.);\nto put an effect (spell, anaesthetic, etc.) on;\nto hold an emotion for (pity, hope, etc.);\nto bind;\nto pour (or sprinkle, spray, etc.) onto;\nto argue (in court); to deliberate (in a meeting); to present (e.g. idea to a conference, etc.);\nto increase further;\nto catch (in a trap, etc.);\nto set atop;\nto erect (a makeshift building);\nto hold (a play, festival, etc.);\n(after -masu stem of verb) indicates (verb) is being directed to (someone)',
            search_result_object.get_meaning_number(0))


    def test_simple_example(self):
        searcher_handler = Search_handler()
        search_result_object = searcher_handler.search("taberu")
        self.assertEqual(2, search_result_object.result_count)
        self.assertEqual(u'食べる', search_result_object.get_expression_number(0))
        self.assertEqual(u'たべる', search_result_object.get_reading_number(0))
        self.assertEqual(u'to eat;\nto live on (e.g. a salary); to live off; to subsist on',
                         search_result_object.get_meaning_number(0))

        self.assertEqual(u'喰べる', search_result_object.get_expression_number(1))
        self.assertEqual(u'たべる', search_result_object.get_reading_number(1))
        self.assertEqual(u'to eat;\nto live on (e.g. a salary); to live off; to subsist on',
                         search_result_object.get_meaning_number(1))

d = datetime.datetime.today()
d -= datetime.timedelta(hours=4)
d = datetime.datetime(d.year, d.month, d.day)
d += datetime.timedelta(hours=4)
print(int(time.time())-int(time.mktime(d.timetuple()))//86400)
print(int(time.time() - time.mktime(d.timetuple()) // 86400)+60)