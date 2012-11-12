#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def left (arg):
  return 2*(arg + 1)-1

def right (arg):
  return 2*(arg + 1)

def parent (arg):
  return (arg + 1)/2 - 1 if (arg + 1)/2 -1 >=0 else 0

def HeapSort (array):
  BuildMaxHeap (array)
  size = len(array)
  for i in reversed (xrange (1, len(array) - 1)):
    size -= 1
    tmp = array[0]
    array[0] = array [i]
    array[i] = tmp
    MaxHeapify (array, 0, size)

  return array

def BuildMaxHeap (array):
  for i in reversed (xrange (0, len(array)/2-1)):
    MaxHeapify (array, i, len(array))
  return array

def MaxHeapify (array, index, size):
  l = left (index)
  r = right (index)
  if (l < size and array[l] > array[index]):
    largest = l
  else:
    largest = index
  if (r < size and array[r] > array[largest]):
    largest = r
  if (largest != index):
    tmp = array[index]
    array[index] = array[largest]
    array[largest] = tmp
    array = MaxHeapify (array, largest, len(array))

def main():
  arr = [10, 9, 12, 3, 11, 1]
#a = [1,2]
# MaxHeapify (a, 0)
# print "after", a
if __name__ == '__main__':
  main()
