#!/usr/bin/python
#-*- coding: utf-8 -*-

""" This module is implementation of simple Hopfield neural network.

    Author: Dmitry Khodakov <dmitryhd@gmail.com>
    date:   19.10.2013
"""

import random
import math


class HopfieldNetwork():
    """ Neural network representation. """
    def __init__(self, num_of_neurons):
        self.num_of_neurons = num_of_neurons
        self.weights = [[0] * num_of_neurons] * num_of_neurons
        self.remembered = []
        self.max_iterations = 1000

    @staticmethod
    def _convert_to_inner(value):
        res = []
        for i in value:
            if i == '-':
                res.append(-1)
            else:
                res.append(1)
        return res

    @staticmethod
    def _convert_to_outer(value):
        res = []
        for i in value:
            if i == -1:
                res.append('-')
            else:
                res.append('*')
        return res

    def learn(self, value):
        """ Remember one value into network. """
        x = HopfieldNetwork._convert_to_inner(value)
        for i in range(self.num_of_neurons):
            for j in range(self.num_of_neurons):
                if i == j:
                    self.weights[i][j] = 0
                else:
                    self.weights[i][j] += x[i] * x[j]
        self.remembered.append(x)
        print('just remember:')
        HopfieldNetwork.print_state(x)
        

    @staticmethod
    def print_state(value):
        x = HopfieldNetwork._convert_to_outer(value)
        res = ''
        for index in range(len(x)):
            if index % 7 == 6:
                res += x[index] + '\n'
            else:
                res += x[index]
        print(res)

    def recognize(self, value):
        """ Recognize value.
            Return: is_match found, and fixed x.
        """
        x = HopfieldNetwork._convert_to_inner(value)
        iter_counter = 0
        is_found = False
        for y in self.remembered:
            print('rememebered:')
            HopfieldNetwork.print_state(y)
        
        r = 0
        while not is_found:
            if x in self.remembered:
                is_found = True
                break
            print('r:', r)
            net = 0
            for i in range(self.num_of_neurons):
                net += x[i] * self.weights[i][r]
            x[r] = math.copysign(1, net)

            HopfieldNetwork.print_state(x)
            iter_counter += 1
            print('counter:', iter_counter)
            if iter_counter > self.max_iterations:
                break
            r += 1
            if r == len(x):
                r = 0
        if is_found:
            index = self.remembered.index(x)
        else:
            index = -1
        return is_found, index


class TestHopfieldNetwork():
    """ Test class. Using TDD here. """
    cross =  "---*---"
    cross += "---*---"
    cross += "---*---"
    cross += "*******"
    cross += "---*---"
    cross += "---*---"
    cross += "---*---"

    b_letter =  "*******"
    b_letter += "*------"
    b_letter += "*------"
    b_letter += "*******"
    b_letter += "*-----*"
    b_letter += "*-----*"
    b_letter += "*******"

    mod_b_letter =  "***-***"
    mod_b_letter += "*----*-"
    mod_b_letter += "*------"
    mod_b_letter += "*******"
    mod_b_letter += "*-----*"
    mod_b_letter += "-*--*-*"
    mod_b_letter += "******-"


    mod_cross =  "---*---"
    mod_cross += "--*----"
    mod_cross += "---*-*-"
    mod_cross += "*-***-*"
    mod_cross += "---*---"
    mod_cross += "---*---"
    mod_cross += "----*--"

    star =  "*--*--*"
    star += "-*-*-*-"
    star += "--***--"
    star += "*******"
    star += "--***--"
    star += "-*-*-*-"
    star += "*--*--*"

    mod_star =  "*---*-*"
    mod_star += "-*-*-*-"
    mod_star += "--***--"
    mod_star += "*******"
    mod_star += "--**-*-"
    mod_star += "-*-*-*-"
    mod_star += "*-*---*"
    def __init__(self):
        pass

    @staticmethod
    def test_network_creation():
        """ Test initialization. """
        hnet = HopfieldNetwork(5)
        assert hnet.num_of_neurons

    @staticmethod
    def test_learning():
        """ Just learn one figure. """
        neuron_number = 49
        hnet = HopfieldNetwork(neuron_number)
        hnet.learn(TestHopfieldNetwork.star)

    @staticmethod
    def test_simple_recognizing():
        """ Learn star and cross and try to classify them without noise. """
        neuron_number = 49
        hnet = HopfieldNetwork(neuron_number)
        hnet.learn(TestHopfieldNetwork.star)
        hnet.learn(TestHopfieldNetwork.cross)
        assert hnet.recognize(TestHopfieldNetwork.star)[1] == 0, 'Cannot recognize star.'
        assert hnet.recognize(TestHopfieldNetwork.cross)[1] == 1, 'Cannot recognize cross.'

    @staticmethod
    def test_complex_recognizing():
        """ Learn star and cross and try to classify them without noise. """
        neuron_number = 49
        hnet = HopfieldNetwork(neuron_number)
        hnet.learn(TestHopfieldNetwork.cross)
        assert hnet.recognize(TestHopfieldNetwork.mod_cross)[1] == 0, 'Cannot recognize cross.'
