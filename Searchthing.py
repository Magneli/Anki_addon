class Ducks:
    import os, sys
    lib_path = os.path.abspath(os.path.join('C:\Python27\Lib\bs4', 'C:\Python27\Lib', '..', 'lib'))
    sys.path.append(lib_path)
    #import requests
    from bs4 import BeautifulSoup
    import urllib2

    def __init__(self, search_term):
        self.searchTerm = search_term

        self.MAX_RESULTS = 20
        self.organized_results = None
        self.searchURL = None
        self.search_result_as_html = None
        self.result_count = 0
        self.prepare_results()

    def prepare_results(self):

        self.make_search_url()
        self.get_data_from_internet()
        self.organize_results()
        self.count_results()


    def make_search_url(self):
        self.searchURL = "http://classic.jisho.org/words?jap=" + self.searchTerm + "&eng=&dict=edict"

    def get_data_from_internet(self):


        self.search_result_as_html=self.urllib2.urlopen(self.searchURL)


        #raw_result = self.requests.get(self.searchURL)
        #self.search_result_as_html = raw_result.text

    def organize_results(self):
        soup = self.BeautifulSoup(self.search_result_as_html, "html.parser")
        self.organized_results = soup.find_all('td')

    def count_results(self):
        for counter in range(0, self.MAX_RESULTS):
            try:
                self.organized_results[counter * 5]
            except IndexError:
                break
            self.result_count = counter + 1

    def get_kanji(self, number):
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
                        result += self.organized_results[(number * 5) + 2].contents[index - 1].lstrip()
                        result += "\n"
            except IndexError:
                return result.rstrip()




read = "kanashii"

if __name__ == '__main__':
    print('test {}'.format('code'))
    ducks = Ducks(read)
    print(ducks.result_count)
    for x in range(0, ducks.result_count):
        print(ducks.get_kanji(x) + ":" + ducks.get_reading(x))
        print( ducks.get_meaning(x))