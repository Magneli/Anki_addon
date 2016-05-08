# -*- coding: utf-8 -*-
# python 2.7
import os
import sys

from platform import system

if system().lower() == 'windows':
    # lib_path = os.path.abspath(os.path.join('C:\Python27\Lib'))
    # lib_path = os.path.abspath(os.path.join('e:\lib'))
    lib_path = os.path.realpath(os.path.join('...'))
    sys.path.append(lib_path)

from bs4 import BeautifulSoup
import urllib2


class Jp_to_eng_word_search_handler:
    def __init__(self):

        self.MAX_RESULTS = 20
        self.organized_results = None
        self.searchURL = None
        self.search_result_as_html = None
        self.result_count = 0

    def search(self, search_term):
        self.word_result_object = Search_result()
        self.make_search_url(search_term)

        if not self.get_data_from_internet():
            return self.word_result_object

        self.organize_data_into_soup()
        self.get_result_count()
        self.store_results_from_soup()
        return self.word_result_object

    def make_search_url(self, search_term):
        self.searchURL = "http://classic.jisho.org/words?jap=" + search_term + "&eng=&dict=edict"

    def get_data_from_internet(self):
        try:
            self.search_result_as_html = urllib2.urlopen(self.searchURL)
            return True
        except urllib2.URLError:
            return False

    def organize_data_into_soup(self):
        soup = BeautifulSoup(self.search_result_as_html, "html.parser")
        self.organized_results = soup.find_all('td')

    def get_result_count(self):
        for counter in range(0, self.MAX_RESULTS):
            try:
                self.organized_results[counter * 5]
            except IndexError:
                break
            self.word_result_object.result_count = counter + 1

    def store_results_from_soup(self):
        for i in range(0, self.word_result_object.result_count):
            self.save_result_in_object(i)

    def save_result_in_object(self, number):
        self.word_result_object.add_expression(self.get_expression_from_soup(number))
        self.word_result_object.add_reading(self.get_reading_from_soup(number))
        self.word_result_object.add_meaning(self.get_meaning_from_soup(number))
        self.word_result_object.add_note(self.get_note_from_soup(number))

    def get_expression_from_soup(self, number):

        return self.organized_results[number * 5].get_text().strip()

    def get_reading_from_soup(self, number):

        return self.organized_results[(number * 5) + 1].get_text().strip()

    def get_note_from_soup(self, number):
        return self.organized_results[(number * 5) + 3].get_text().strip()

    def get_meaning_from_soup(self, number):
        #print self.organized_results[(number * 5) + 2].get_text().strip()
        print  self.organized_results[(number * 5) + 2]
        new = self.organized_results[(number * 5) + 2].get_text().strip()

        if str.startswith(str(new), ("(Usually written using kana alone)")):
            count = 0
            for letter in new:
                if letter == ')':
                    break
                count += 1
            count += 1
            new = new[count:]
            #print "yay"+new.strip()
            return new.strip()

        if self.organized_results[(number * 5) + 2].string is not None:

            return self.organized_results[(number * 5) + 2].string.strip()
        else:

            result = ""
            try:
                for index in range(0, 100):
                    if str(self.organized_results[(number * 5) + 2].contents[index]) == "<br/>":
                        if self.organized_results[(number * 5) + 2].contents[index - 1].strip() != ';':

                            result += self.organized_results[(number * 5) + 2].contents[index - 1].strip()
                            result += "\n"
                        else:
                            result += self.organized_results[(number * 5) + 2].contents[index - 3].strip() + ";"
                            result += "\n"
            except IndexError:

                return result.strip()


class Search_result:
    def __init__(self):
        self.expression = []
        self.reading = []
        self.meaning = []
        self.note = []
        self.result_count = 0

    def add_note(self, note):
        self.note.append(note)

    def add_expression(self, word):
        self.expression.append(word)

    def add_reading(self, word):
        self.reading.append(word)

    def add_meaning(self, word):
        self.meaning.append(word)

    def get_note_number(self, number):
        return self.note[number]

    def get_expression_number(self, number):
        return self.expression[number]

    def get_reading_number(self, number):
        return self.reading[number]

    def get_meaning_number(self, number):
        return self.meaning[number]

    def get_result_count(self):
        return self.result_count


read = "蛙"

if __name__ == '__main__':
    print('test {}'.format('code'))

    ducks = Jp_to_eng_word_search_handler()
    asd = ducks.search("asd")
    result = ducks.search(read)
    print(result.result_count)
    for x in range(0, 2):
        print(result.get_expression_number(x) + ":" + result.get_reading_number(x) + " " + result.get_note_number(x))
        print(result.get_meaning_number(x))
        pass
