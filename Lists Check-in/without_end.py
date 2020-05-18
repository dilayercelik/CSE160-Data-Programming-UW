# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:02:55 2020

@author: dilayerc
"""


# Practice


# Given a string, return a version without the first and last char, 
# so "Hello" yields "ell". The string length will be at least 2.

# Examples:
## without_end('Hello') → 'ell'
## without_end('java') → 'av'
## without_end('coding') → 'odin'


# Answer
def without_end(string):
    
    new_string = string[1:-1]
    
    return new_string


# Tests
print(without_end('Hello'))   # correct output
print(without_end('java'))    # correct output
print(without_end('coding'))  # correct output

    
    