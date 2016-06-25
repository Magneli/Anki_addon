# -*- coding: utf-8 -*-
# python 2.7
from unittest import TestCase
import time

from Jp_to_eng_word_search_handler import Jp_to_eng_word_search_handler

class TestJp_to_eng_word_search_handler(TestCase):

    def test_unfinished(self):
        searcher_handler = Jp_to_eng_word_search_handler()
        search_result_object = searcher_handler.search("tabe")
        self.assertEqual(20, search_result_object.result_count)
        self.assertEqual(u'多弁', search_result_object.get_expression_number(0))
        self.assertEqual(u'たべん', search_result_object.get_reading_number(0))
        self.maxDiff = None
        self.assertEqual(
            u'talkativeness; verbosity',
            search_result_object.get_meaning_number(0))

    def test_no_result(self):
        searcher_handler = Jp_to_eng_word_search_handler()
        search_result_object = searcher_handler.search("nonsensicalgibberish")
        self.assertEqual(0, search_result_object.result_count)
        self.assertEqual([], search_result_object.expression)
        self.assertEqual([], search_result_object.reading)
        self.assertEqual([], search_result_object.meaning)

    def test_empty_search_term(self):
        searcher_handler = Jp_to_eng_word_search_handler()
        search_result_object = searcher_handler.search("")
        self.assertEqual(0, search_result_object.result_count)
        self.assertEqual([], search_result_object.expression)
        self.assertEqual([], search_result_object.reading)
        self.assertEqual([], search_result_object.meaning)

    def test_nasty_example(self):
        searcher_handler = Jp_to_eng_word_search_handler()
        search_result_object = searcher_handler.search("掛ける")
        self.assertEqual(1, search_result_object.result_count)
        self.assertEqual(u'掛ける', search_result_object.get_expression_number(0))
        self.assertEqual(u'かける', search_result_object.get_reading_number(0))
        self.maxDiff = None
        self.assertEqual(
            'to hang (e.g. picture); to hoist (e.g. sail); to raise (e.g. flag);\nto sit;\n() to be partway (verb); to begin (but not complete);\nto take (time, money); to expend (money, time, etc.);\nto make (a call);\nto multiply;\nto secure (e.g. lock);\nto put on (glasses, etc.);\nto cover;\nto burden someone;\nto apply (insurance);\nto turn on (an engine, etc.); to set (a dial, an alarm clock, etc.);\nto put an effect (spell, anaesthetic, etc.) on;\nto hold an emotion for (pity, hope, etc.);\nto bind;\nto pour (or sprinkle, spray, etc.) onto;\nto argue (in court); to deliberate (in a meeting); to present (e.g. idea to a conference, etc.);\nto increase further;\nto catch (in a trap, etc.);\nto set atop;\nto erect (a makeshift building);\nto hold (a play, festival, etc.);\n(Auxiliary verb) (after -masu stem of verb) indicates (verb) is being directed to (someone)',
            search_result_object.get_meaning_number(0))

    def test_simple_example(self):
        searcher_handler = Jp_to_eng_word_search_handler()
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

    def test_a(self):
        searcher_handler = Jp_to_eng_word_search_handler()
        search_result_object = searcher_handler.search("a")
        self.assertEqual(20, search_result_object.result_count)
        self.assertEqual(u'', search_result_object.get_expression_number(0))
        self.assertEqual(u'あ', search_result_object.get_reading_number(0))
        self.assertEqual(u'Ah! (expression of surprise, recollection, etc.); Oh!;\nHey! (to get someone\'s attention)',
                         search_result_object.get_meaning_number(0))

        self.assertEqual(u'亜', search_result_object.get_expression_number(1))
        self.assertEqual(u'あ', search_result_object.get_reading_number(1))
        self.assertEqual(u'sub-;\n-ous (indicating a low oxidation state); -ite',
                         search_result_object.get_meaning_number(1))

        self.assertEqual(u'吾', search_result_object.get_expression_number(2))
        self.assertEqual(u'あ', search_result_object.get_reading_number(2))
        self.assertEqual(u'I; me',
                         search_result_object.get_meaning_number(2))

    def test_wildcard_reading(self):
        searcher_handler = Jp_to_eng_word_search_handler()
        search_result_object = searcher_handler.search("*けたまわる")
        self.assertEqual(2, search_result_object.result_count)
        self.assertEqual(u'承る', search_result_object.get_expression_number(0))
        self.assertEqual(u'うけたまわる', search_result_object.get_reading_number(0))
        self.assertEqual(
            u'(Humble (kenjougo) language)  to hear; to be told; to know;\nto receive (order); to undertake; to comply; to take (a reservation, etc.)',
            search_result_object.get_meaning_number(0))

        self.assertEqual(u'受け賜る', search_result_object.get_expression_number(1))
        self.assertEqual(u'うけたまわる', search_result_object.get_reading_number(1))
        self.assertEqual(
            u'(Humble (kenjougo) language)  to hear; to be told; to know;\nto receive (order); to undertake; to comply; to take (a reservation, etc.)',
            search_result_object.get_meaning_number(1))

    def test_surrounding_wildcards(self):
        searcher_handler = Jp_to_eng_word_search_handler()
        search_result_object = searcher_handler.search("*けたまわ*")
        self.assertEqual(2, search_result_object.result_count)
        self.assertEqual(u'承る', search_result_object.get_expression_number(0))
        self.assertEqual(u'うけたまわる', search_result_object.get_reading_number(0))
        self.assertEqual(
            u'(Humble (kenjougo) language)  to hear; to be told; to know;\nto receive (order); to undertake; to comply; to take (a reservation, etc.)',
            search_result_object.get_meaning_number(0))

        self.assertEqual(u'受け賜る', search_result_object.get_expression_number(1))
        self.assertEqual(u'うけたまわる', search_result_object.get_reading_number(1))
        self.assertEqual(
            u'(Humble (kenjougo) language)  to hear; to be told; to know;\nto receive (order); to undertake; to comply; to take (a reservation, etc.)',
            search_result_object.get_meaning_number(1))

    def test_wildcard_expression(self):
        searcher_handler = Jp_to_eng_word_search_handler()
        search_result_object = searcher_handler.search("*け賜る")
        self.assertEqual(1, search_result_object.result_count)
        self.assertEqual(u'受け賜る', search_result_object.get_expression_number(0))
        self.assertEqual(u'うけたまわる', search_result_object.get_reading_number(0))
        self.assertEqual(
            u'(Humble (kenjougo) language)  to hear; to be told; to know;\nto receive (order); to undertake; to comply; to take (a reservation, etc.)',
            search_result_object.get_meaning_number(0))

    def test_surrounding_expression(self):
        searcher_handler = Jp_to_eng_word_search_handler()
        search_result_object = searcher_handler.search("*け賜*")
        self.assertEqual(1, search_result_object.result_count)
        self.assertEqual(u'受け賜る', search_result_object.get_expression_number(0))
        self.assertEqual(u'うけたまわる', search_result_object.get_reading_number(0))
        self.assertEqual(
            u'(Humble (kenjougo) language)  to hear; to be told; to know;\nto receive (order); to undertake; to comply; to take (a reservation, etc.)',
            search_result_object.get_meaning_number(0))

    def test_kaku(self):
        searcher_handler = Jp_to_eng_word_search_handler()
        search_result_object = searcher_handler.search("各")
        self.assertEqual(20, search_result_object.result_count)
        self.assertEqual(u'各', search_result_object.get_expression_number(0))
        self.assertEqual(u'かく', search_result_object.get_reading_number(0))
        self.assertEqual(
            u'each; every; all',
            search_result_object.get_meaning_number(0))

    def test_syoumetsu(self):
        searcher_handler = Jp_to_eng_word_search_handler()
        search_result_object = searcher_handler.search("消滅")
        self.assertEqual(2, search_result_object.result_count)
        self.assertEqual(u'消滅', search_result_object.get_expression_number(0))
        self.assertEqual(u'しょうめつ', search_result_object.get_reading_number(0))
        self.assertEqual(
            u'lapse; annihilation  (Physics term) ;\nextinguishment; termination (e.g. of legal representation);\n(Mathematical term)  vanishing',
            search_result_object.get_meaning_number(0))


