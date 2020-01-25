#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"
#Line 9 is the start of a loop, it will keep going until that condition is met.
#It wouldn't repeat the question
#It's so broken, oh my gosh, it just keeps looping because it doesn't ask for new feedback and keeps inputing
#The same one.
print('Greetings!')
color = ''
color = input("What is my favorite color? ")
while (color != 'red'):
    color = color.lower().strip()
    if (color == 'red'):
        print('Correct!')
    elif (color == 'pink'):
        print('Close!')
    else:
        print('Sorry, try again.')