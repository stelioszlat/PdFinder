# pdf class

from Objects.keyword import Keyword
import re


class PDF:
    def __init__(self, name, keyword=None):
        self.name = name
        self.text = ""
        self.info = ""
        self.title = ""
        self.authors = []
        self.keywords = []
        if keyword:
            self.keywords.append(keyword)
        self.pages = 0
        self.abs_path = ""
        self.weight = 0  # adds weigth to file so it is more important

    def __str__(self):
        print('Name: ' + self.name)
        print('Info: ' + self.info)
        print('Authors: ' + str(self.authors))
        print('Keywords: ' + str(self.keywords))
        print('Pages: ' + str(self.pages))
        print('Weight: ' + str(self.weight))

    def find_keyword(self):
        for key in self.keywords:
            if re.match(key, self.text):
                return key
        return False

    def new_keyword(self, word):
        new = Keyword(word)
        self.keywords.append(new)
