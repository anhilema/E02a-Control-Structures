#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"
#I expect it to make the input all lowercase in order to solve the problem with capitals.
#It still messes up due to spaces. It doesn't count it as an answer.

print('Greetings!')
color = input("What is my favorite color? ")
if (color.lower() == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')