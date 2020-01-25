#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"
#Line 13 is adding 1 to the value of count and changing count's number to that of what it is when 1 is added.
#Line 22 is showing how many tries the player got the color in by displaying count's value.

print('Greetings!')
color = ''
count = 0
while (color != 'red'):
    color = input("What is my favorite color? ")
    color = color.lower().strip()
    count = count + 1               # You can also write this as count += 1
    if (color == 'red'):
        print('Correct!')
    elif (color == 'pink'):
        print('Close!')
    else:
        print('Sorry, try again.')

print('You guessed it in {} tries!'.format(count))