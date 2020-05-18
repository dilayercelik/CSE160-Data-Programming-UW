# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:06:37 2020

@author: dilayerc
"""


# Practice


# Given 2 strings, return their concatenation, except omit the first char of each.
# The strings will be at least length 1.

# Examples:
## non_start('Hello', 'There') → 'ellohere'
## non_start('java', 'code') → 'avaode'
## non_start('shotl', 'java') → 'hotlava'


# Answer
def non_start(a, b):
    
    new_string = a[1:] + b[1:]
    
    return new_string


# Tests
print(non_start('Hello', 'There'))  # correct output
print(non_start('java', 'code'))    # correct output
print(non_start('shotl', 'java'))   # correct output