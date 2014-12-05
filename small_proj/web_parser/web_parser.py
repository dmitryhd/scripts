#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# get ru, $ rate from bank
# https://github.com/dmitryhd/scripts.git

import urllib
import unittest
from bs4 import BeautifulSoup

class WebParser():
    def __init__(self, url):
        self.url = url
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.19 (KHTML, like Gecko) Ubuntu/12.04 Chromium/18.0.1025.168 Chrome/18.0.1025.168 Safari/535.19'
        html = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': user_agent})).read()
        self.soup = BeautifulSoup(html)

    def dowload(self):
        self.__init__(self.url)

    def get_tag_cont(self, attr, value):
        return self.soup.find(attrs={attr: value}).contents[-1]


def get_rate():
    bank_url = 'http://www.cbr.ru/'
    field_class = 'w_data_wrap'

    html = urllib.request.urlopen(bank_url).read()
    soup = BeautifulSoup(html)
    return float(soup.find(attrs={"class": field_class}).contents[-1].replace(',', '.'))

class TaskWebGet(unittest.TestCase):
    def test_main_page(self):
        assert get_rate()

    def test_download_page(self):
        wp = WebParser('http://www.google.com/')
        wp.dowload()

    def test_get_tag_cont(self):
        wp = WebParser('http://www.cbr.ru/')
        res = wp.get_tag_cont('class', 'w_data_wrap')
        assert res


if __name__ == '__main__':
    unittest.main()
