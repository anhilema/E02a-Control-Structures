#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"
#it is different bby including both "reds" in the if statement. It's trying to solve capitalization errors
#Anything else won't be counted as a valid answer.
print('Greetings!')
color = input("What is my favorite color? ")
if (color == 'Red' or color == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')