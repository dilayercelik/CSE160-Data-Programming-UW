# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:14:16 2020

@author: dilayerc
"""


# Practice

# Return the number of times that the string "hi" appears anywhere in the given string.

# Examples:
## count_hi('abc hi ho') → 1
## count_hi('ABChi hi') → 2
## count_hi('hihi') → 2


# Answer
def count_hi(string):
    
    return string.count('hi')
    

# Tests
print(count_hi('abc hi ho'))  # correct output
print(count_hi('ABChi hi'))   # correct output
print(count_hi('hihi'))       # correct output


    