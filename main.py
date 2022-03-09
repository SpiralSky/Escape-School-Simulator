import time
import multiprocessing
import functions
from functions import printslow
from functions import printfast
from functions import play
import sys
import os
import replit
from colours import *
from replit import db

#Variables
db["menu_difficulty"] += 0
menu_difficulty = db["menu_difficulty"]

while (True):  #Main Code
    printslow(Red + "Welcome to Escape School Simulator")
    time.sleep(0.5)
    printslow(bright_red + "\nOptions:")
    print(" \n1. Start\n2. Difficulty")
    print("\nCurrent Difficulty " + str(menu_difficulty))
    menu_option = input(" ")

    if int(menu_option) == 1:
        replit.clear
        sys.stdout.write("Loading.")
        time.sleep(0.5)
        sys.stdout.write(".")
        time.sleep(0.5)
        sys.stdout.write(".")
        time.sleep(0.5)
        play(menu_difficulty)
    elif int(menu_option) == 2:
        replit.clear()
        printfast("Please select your difficulty from the options below.")
        time.sleep(0.5)
        print("\n1. Dream\n2. School\n3. Boys Home\n4. Failure")
        menu_difficulty = input(" ")
        if int(menu_difficulty) > 0 and int(menu_difficulty) < 5:
          print(Red + "Selected")
          time.sleep(0.5)
          replit.clear()
          db["menu_difficulty"] = int(menu_difficulty)
        else:
          replit.clear()
          print("Unavailable!")
          print("Difficulty set to default (1)")
          menu_difficulty = 1
          db["menu_difficulty"] = int(menu_difficulty)
          time.sleep(2)
          replit.clear()
