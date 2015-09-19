# -*- coding: utf-8 -*-
class Search_handler:
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

    def search(self, search_term):
        self.search_result = Search_result()
        self.make_search_url(search_term)
        self.get_data_from_internet()
        self.organize_data_into_soup()
        self.count_results()
        self.store_results_from_soup()
        return self.search_result

    def make_search_url(self, search_term):
        self.searchURL = "http://classic.jisho.org/words?jap=" + search_term + "&eng=&dict=edict"

    def get_data_from_internet(self):
        self.search_result_as_html = self.urllib2.urlopen(self.searchURL)

    def organize_data_into_soup(self):
        soup = self.BeautifulSoup(self.search_result_as_html, "html.parser")
        self.organized_results = soup.find_all('td')

    def count_results(self):
        for counter in range(0, self.MAX_RESULTS):
            try:
                self.organized_results[counter * 5]
            except IndexError:
                break
            self.search_result.result_count = counter + 1

    def store_results_from_soup(self):
        for i in range(0, self.search_result.result_count):
            self.save_result_in_object(i)

    def save_result_in_object(self, number):
        self.search_result.add_expression(self.get_expression(number))
        self.search_result.add_reading(self.get_reading(number))
        self.search_result.add_meaning(self.get_meaning(number))

    def get_expression(self, number):
        try:
            return self.organized_results[number * 5].span.span.string + \
                   self.organized_results[number * 5].span.contents[1].rstrip()
        except IndexError:
            return self.organized_results[number * 5].span.string
        except AttributeError:
            return self.organized_results[number * 5].span.string.rstrip()

    def get_reading(self, number):
        if self.organized_results[(number * 5) + 1].span is not None:
            return self.organized_results[(number * 5) + 1].span.string + \
                   self.organized_results[(number * 5) + 1].contents[1].rstrip()
        else:
            return self.organized_results[(number * 5) + 1].string.rstrip().rstrip()

    def get_meaning(self, number):
        if self.organized_results[(number * 5) + 2].string is not None:
            return self.organized_results[(number * 5) + 2].string.rstrip()
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

    def add_expression(self, result):
        self.expression.append(result)

    def add_reading(self, result):
        self.reading.append(result)

    def add_meaning(self, result):
        self.meaning.append(result)

    def get_expression_number(self, number):
        return self.expression[number]

    def get_reading_number(self, number):
        return self.reading[number]

    def get_meaning_number(self, number):
        return self.meaning[number]


read = "kanashii"

if __name__ == '__main__':
    print('test {}'.format('code'))

    ducks = Search_handler()
    asd = ducks.search("asd")
    result = ducks.search(read)
    print(result.result_count)
    for x in range(0, result.result_count):
        print(result.get_expression_number(x) + ":" + result.get_reading_number(x))
        print(result.get_meaning_number(x))
