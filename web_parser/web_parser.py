#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# get ru, $ rate from bank
# https://github.com/dmitryhd/scripts.git

import urllib
import unittest
from bs4 import BeautifulSoup

def get_rate():
    bank_url = 'http://www.cbr.ru/'
    field_class = 'w_data_wrap'

    html = urllib.request.urlopen(bank_url).read()
    soup = BeautifulSoup(html)
    return float(soup.find(attrs={"class": field_class}).contents[-1].replace(',', '.'))

class TaskWebGet(unittest.TestCase):
    def test_main_page(self):
        assert get_rate()

if __name__ == '__main__':
    unittest.main()
