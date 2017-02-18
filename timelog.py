#!/usr/bin/python
from datetime import datetime
# import os
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

#m0 = raw_input("Choose option 'c' or 'e':")

#create_entry()
"""
while True:
    new_entry = raw_input("Create new entry? [y/n]")
    if new_entry == 'y':
        create_entry()
    elif new_entry == 'n':
        break
    elif new_entry != 'y' != 'n':
        print("Please choose y or n.")
"""

def validate_choice(m0):
  if m0 == 'c':
      create_entry() # prevents duplicate entry label prompt
      return True
  elif m0 == 'e':
      return True
  elif m0 != 'e' != 'c':
      print("Invalid Option! Press (c) to create new entry or (e) to exit.")
      return False

while True:
  try:
      m0 = raw_input("Select 'c' to create new entry or 'e' to exit.")
      if validate_choice(m0):
        break
  except ValueError:
      print ("Invalid option!")

while True:
  if m0 == 'c':    
    new_entry = raw_input("Create new entry? [y/n]")
    if new_entry == 'y':
            create_entry()
    elif new_entry == 'n':
        break
  elif m0 == 'e':
    print('Bye!')
    exit()
  if new_entry == 'n':
    break
    print('Bye!')



"""
while True:
    new_entry = raw_input("Create new entry? [y/n]")
    if new_entry == 'y':
        create_entry()
    elif new_entry == 'n':
        break
    elif new_entry != 'y' != 'n':
        print("Please choose y or n.")
"""



sys.exit()


    # print time in string format
#from time import strftime
#time = strftime("%Y-%m-%d %H:%M:%S")
#print(time)
"""
with open("filename.txt") as f:
    for line in f:
        if "Smith" in line:
             print line
"""

"""
def validate_choice(m0):
  if m0 == 'c':
      return True
  elif m0 == 'e':
      return True
  elif m0 != 'e' != 'c':
      print("Invalid Option! Press (c) to convert or (e) to exit.")
      return False

while True:
  try:
      m0 = str(input("Select option and press Enter: "))
      if validate_choice(m0):
        break
  except ValueError:
      print ("Invalid option!")

while True:
# add method to handle KeyError exceptions
  if m0 == 'c':
    msg = input("Input Text: ")
    morse = morsecodify(msg)
    print("Your Message in Morse Code:")
print("\n" + morse + "\n")
    cont = str(input("Would you like to convert another string? [y/n] "))
#    validate_exit(cont)
  elif m0 == 'e':
    print('Bye!')
    exit()
  if cont == 'n':
break
print('Bye!')
# sys.exit()
exit()

"""
