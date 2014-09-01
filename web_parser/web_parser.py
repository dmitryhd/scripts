#!/usr/bin/python
#-*- coding: utf-8 -*-

# get ru, $ rate from bank
# https://github.com/dmitryhd/scripts.git

import urllib
from bs4 import BeautifulSoup

def get_rate():
    bank_url = 'http://www.cbr.ru/'
    field_class = 'w_data_wrap'

    html = urllib.request.urlopen(bank_url).read()
    soup = BeautifulSoup(html)
    return float(soup.find(attrs={"class": field_class}).contents[-1].replace(',', '.'))

if __name__ == '__main__':
    print(get_rate())
