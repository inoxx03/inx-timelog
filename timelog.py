#!/usr/bin/python
from datetime import datetime
import os
import sys

    # write date then time then user provided tag separately inline to a file
def create_entry():
    tag = raw_input("New Entry: ")
    date = str(datetime.now().date())
    time = str(datetime.now().time().replace(microsecond=0))
    f = open('timelogfile', 'a')
    f.write(date + " " + time + " " + tag + "\n")
    f.close()

print("TimeLog v. 0.1\nby inoxx\nUse the following entry names (for ease of use only):\n - work\n - break\n - arrival\n - departure\n")
create_entry()

while True:
    new_entry = raw_input("Create new entry? [y/n]")
    if new_entry == 'y':
        create_entry()
    elif new_entry == 'n':
        break
    elif new_entry != 'y' != 'n':
        print("Please choose y or n.")

sys.exit()


    # print time in string format
#from time import strftime
#time = strftime("%Y-%m-%d %H:%M:%S")
#print(time)
