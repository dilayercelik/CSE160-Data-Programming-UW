# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:22:41 2020

@author: Dilay Ercelik
"""


# Practice


# Given a string and a non-negative int n, 
# return a larger string that is n copies of the original string.


# Examples:
# string_times('Hi', 2) → 'HiHi'
# string_times('Hi', 3) → 'HiHiHi'
# string_times('Hi', 1) → 'Hi'


# Answer

def string_times(string, n):
    
    if n > 0:
        
        return string*n
    

# Tests
print(string_times('Hi', 2)) # correct output
print(string_times('Hi', 3)) # correct output
print(string_times('Hi', 1)) # correct output