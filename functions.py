import os
import time
import sys
import colours
from colours import *

def printslow(text):
  for x in text:
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.05)

def printfast(text):
  for x in text:
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.01)

def play(text):
  if text == 1:
    print("")
  else:
    print(Red + "This is not available. Current available difficulties: (1)")
  
