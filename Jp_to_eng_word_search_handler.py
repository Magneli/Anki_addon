# -*- coding: utf-8 -*-
# python 2.7
class Jp_to_eng_word_search_handler:
    import os, sys
    lib_path = os.path.abspath(os.path.join('C:\Python27\Lib\bs4', 'C:\Python27\Lib', '..', 'lib'))
    sys.path.append(lib_path)

    from bs4 import BeautifulSoup
    import urllib2
    def __init__(self):

        self.MAX_RESULTS = 20
        self.organized_results = None
        self.searchURL = None
        self.search_result_as_html = None
        self.result_count = 0

    def get_search_result(self, search_term):
        self.result_object = Search_result()
        self.make_search_url(search_term)

        if not self.get_data_from_internet():
            return self.result_object

        self.organize_data_into_soup()
        self.get_result_count()
        self.store_results_from_soup()
        return self.result_object

    def make_search_url(self, search_term):
        self.searchURL = "http://classic.jisho.org/words?jap=" + search_term + "&eng=&dict=edict"

    def get_data_from_internet(self):
        try:
            self.search_result_as_html = self.urllib2.urlopen(self.searchURL)
            return True
        except self.urllib2.URLError:
            return False

    def organize_data_into_soup(self):
        soup = self.BeautifulSoup(self.search_result_as_html, "html.parser")
        self.organized_results = soup.find_all('td')

    def get_result_count(self):
        for counter in range(0, self.MAX_RESULTS):
            try:
                self.organized_results[counter * 5]
            except IndexError:
                break
            self.result_object.result_count = counter + 1

    def store_results_from_soup(self):
        for i in range(0, self.result_object.result_count):
            self.save_result_in_object(i)

    def save_result_in_object(self, number):
        self.result_object.add_expression(self.get_expression_from_soup(number))
        self.result_object.add_reading(self.get_reading_from_soup(number))
        self.result_object.add_meaning(self.get_meaning_from_soup(number))

    def get_expression_from_soup(self, number):
        try:
            return self.organized_results[number * 5].span.span.string + \
                   self.organized_results[number * 5].span.contents[1].rstrip()
        except IndexError:
            return self.organized_results[number * 5].span.string
        except AttributeError:
            return self.organized_results[number * 5].span.string.rstrip()

    def get_reading_from_soup(self, number):
        if self.organized_results[(number * 5) + 1].span is not None:

            try:
                return self.organized_results[(number * 5) + 1].span.string + \
                       self.organized_results[(number * 5) + 1].contents[1].rstrip()
            except TypeError:
                return self.organized_results[(number * 5) + 1].span.string
        else:
            return self.organized_results[(number * 5) + 1].string.rstrip().rstrip()

    def get_meaning_from_soup(self, number):
        if self.organized_results[(number * 5) + 2].string is not None:
            return self.organized_results[(number * 5) + 2].string.strip()
        else:
            result = ""
            try:
                for index in range(0, 100):
                    if str(self.organized_results[(number * 5) + 2].contents[index]) == "<br/>":
                        result += self.organized_results[(number * 5) + 2].contents[index - 1].strip()
                        result += "\n"
            except IndexError:
                return result.strip()


class Search_result:
    def __init__(self):
        self.expression = []
        self.reading = []
        self.meaning = []
        self.result_count = 0

    def add_expression(self, word):
        self.expression.append(word)

    def add_reading(self, word):
        self.reading.append(word)

    def add_meaning(self, word):
        self.meaning.append(word)

    def get_expression_number(self, number):
        return self.expression[number]

    def get_reading_number(self, number):
        return self.reading[number]

    def get_meaning_number(self, number):
        return self.meaning[number]

    def get_result_count(self):
        return self.result_count


read = "a"

if __name__ == '__main__':
    print('test {}'.format('code'))

    ducks = Jp_to_eng_word_search_handler()
    asd = ducks.get_search_result("asd")
    result = ducks.get_search_result(read)
    print(result.result_count)
    for x in range(0, result.result_count):
        print(result.get_expression_number(x) + ":" + result.get_reading_number(x))
        print(result.get_meaning_number(x))
