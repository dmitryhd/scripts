#!/usr/bin/env python3

""" Explanation of using same test suit for 2 different implementations of base class. """

import sys
import unittest

class Base:
    """ Simple container base class, others classes inherit from it. Dont use Base(). """
    storage = []
    def method(self):
        pass

class BaseList(Base):
    """ Implementation of Base, which uses list as a container. """
    def method(self):
        """ Fills storage with 10 pairs of key - value. """
        print('BaseList method')
        for i in range(10):
            self.storage.append([i, i])

    def get_res(self):
        """ Returns storage as list of values [0, 0], [1, 1] etc. """
        return self.storage

class BaseDict(Base):
    """ Implementation of Base, which uses dictionary as a container. """
    storage = {}
    def method(self):
        """ Fills storage with 10 pairs of key - value. """
        print('BaseDict method')
        for i in range(10):
            self.storage[i] = i

    def get_res(self):
        """ Returns storage as list of values [0, 0], [1, 1] etc.
            I.e. it converts original dictionary storage to list form.
            Pay attention to using list comprehension! :-)
            Exlained in http://www.secnetix.de/olli/Python/list_comprehensions.hawk .
        """
        return [[key, item] for key, item in self.storage.items()]


class TestFreqDict(unittest.TestCase):
    """ Simple unittest. """
    ethalon = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]

    def check_realisation(self, chosen_implementation):
        """ Function to check implementation. You can pass class name to it, as argument.
            It will send signal to you, if get res returns value which not equal to ethalon.
        """
        obj = chosen_implementation()
        obj.method()
        assert obj.get_res() == self.ethalon

    def test_base_list(self):
        """ Check if list implementation ok. """
        self.check_realisation(BaseList)

    def test_base_dict(self):
        """ Check if list implementation ok. """
        self.check_realisation(BaseDict)

if __name__ == '__main__':
    unittest.main()

