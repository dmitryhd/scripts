#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import unittest
from binaryHeap import *

class TestBuildHeap (unittest.TestCase):
  def testTrivial (self):
    arr = [2, 1]
    expected = [2, 1]
    BuildMaxHeap (arr)
    self.assertEqual (arr, expected)

    arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 5]
    expected = [16, 14, 10,  8, 5, 9, 3, 2, 4, 1]
    BuildMaxHeap (arr)
    self.assertEqual (arr, expected)

class TestHeapSort (unittest.TestCase):
  def testTrivial (self):
    arr = [1, 2, 3, 4, 5]
    expected = [5, 4, 3, 2, 1]
    HeapSort (arr)
    self.assertEqual (arr, expected)

class TestMaxHeapify (unittest.TestCase):
  def testTrivial (self):
    arr = [2, 1]
    expected = [2, 1]
    MaxHeapify (arr, 0, len(arr))
    self.assertEqual (arr, expected)

    arr = [1, 2]
    expected = [2, 1]
    MaxHeapify (arr, 0, len(arr))
    self.assertEqual (arr, expected)

    arr = [1, 2, 3]
    expected = [3, 2, 1]
    MaxHeapify (arr, 0, len(arr))
    self.assertEqual (arr, expected)

    arr = [4, 14, 7, 2, 8, 1]
    expected = [14, 8, 7, 2, 4, 1]
    MaxHeapify (arr, 0, len(arr))
    self.assertEqual (arr, expected)

class TestHeapIndices (unittest.TestCase):
  def testLeft (self):
    self.assertEqual (left (0), 1)
    self.assertEqual (left (1), 3)
    self.assertEqual (left (2), 5)
  def testRight (self):
    self.assertEqual (right (0), 2)
    self.assertEqual (right (1), 4)
    self.assertEqual (right (2), 6)
  def testParent (self):
    self.assertEqual (parent (1), 0)
    self.assertEqual (parent (2), 0)
    self.assertEqual (parent (3), 1)
    self.assertEqual (parent (6), 2)
    self.assertEqual (parent (0), 0)

if __name__ == '__main__':
  unittest.main()
