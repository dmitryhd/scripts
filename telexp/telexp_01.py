#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""Module docstring
"""
import sys
import os

class CommandTemplate ():
  def __init__ (self):
    self.directory = "./"
    self.command = "test.py"
    self.baseOutputFile = "exp01.dat"
    self.redirection = " > "
  def GetRunString (self):
    return self.directory +  self.command + self.redirection + self.baseOutputFile
  
class PostprocessingTemplate ():
  def __init__ (self):
    inputFile = "exp01.dat"
    self.directory = ""
    self.insertString = "x y"
    self.command = "sed -i \'1i " + self.insertString + "\' " + inputFile 
  def GetRunString (self):
    return self.directory + self.command

class Experiment ():
  def __init__ (self):
    self.commandTemplate = CommandTemplate ()
    self.postprocessingTemplate = PostprocessingTemplate ()
    self.postprocessingTemplate2 = PostprocessingTemplate ()
  def Print (self):
    print self.commandTemplate.GetRunString ()
    print self.postprocessingTemplate.GetRunString ()
    print (self.postprocessingTemplate2.command)
  def Run (self):
    os.system (self.commandTemplate.GetRunString ())
    os.system (self.postprocessingTemplate.GetRunString ())
    os.system (self.postprocessingTemplate2.command)

def main ():
  experiment = Experiment ()
  experiment.postprocessingTemplate2.command = "Rscript plot.R exp01.dat"
  experiment.Print ()
  experiment.Run ()

if __name__ == "__main__":
  main ()
