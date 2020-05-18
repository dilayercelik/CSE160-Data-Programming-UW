# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:10:13 2020

@author: dilayerc
"""


# Practice


# Given a string, return a "rotated left 2" version 
# where the first 2 chars are moved to the end. 
# The string length will be at least 2.

# Examples:
## left2('Hello') → 'lloHe'
## left2('java') → 'vaja'
## left2('Hi') → 'Hi'


# Answer
def left2(string):
    
    new_string = string[2:] + string[:2]
    
    return new_string


# Tests
print(left2('Hello'))  # correct output
print(left2('java'))   # correct output
print(left2('Hi'))     # correct output


    
    