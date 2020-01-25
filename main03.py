#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"
#It is different because it has an if statement in it.
#9-12 is an if statement that checks the input to see if it matches an answer, and changing the response based on that
#answer. 10 and 12 are indented because they are connected to the statements above them.
#It doesn't count red as an answer because the condidtion is with red capitalized. I think it's saying that it has to be capitalized.

print('Greetings!')
color = input("What is my favorite color? ")
if (color == 'Red'):
    print('Correct!')
else:
    print('Sorry, try again.')