# -*- coding: utf-8 -*-
"""
Created on Mon May 18 19:50:32 2020

@author: dilayerc
"""


# Practice


# Given a string, return a new string made of 3 copies of the last 2 chars 
# of the original string. The string length will be at least 2.

# Examples:
## extra_end('Hello') → 'lololo'
## extra_end('ab') → 'ababab'
## extra_end('Hi') → 'HiHiHi'


# Answer
def extra_end(str):
    
    new_string = str[-2:] * 3
    
    return new_string


# Tests
print(extra_end('Hello'))  # correct output
print(extra_end('ab'))     # correct output
print(extra_end('Hi'))     # correct output