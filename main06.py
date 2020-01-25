#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"
#It's different by including a .strip(), which should get rid of all of the spaces in the input.
#Yup, you can break it by putting the spaces between the letters as opposed to just the beginning and end.

print('Greetings!')
color = input("What is my favorite color? ")
if (color.lower().strip() == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')