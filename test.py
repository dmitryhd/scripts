#!/usr/bin/python3


class TestSimple ():
    def __init__(self):
        pass

    @staticmethod
    def test_multiplication():
        assert 5*3 == 15, 'omg, wtf!'
    @staticmethod
    def test_multiplication2():
        assert 5*4 == 20, 'omg, wtf!'