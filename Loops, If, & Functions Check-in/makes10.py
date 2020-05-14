# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:19:06 2020

@author: Dilay Ercelik
"""


# Practice


# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


# Examples:
## makes10(9, 10) → True
## makes10(9, 9) → False
## makes10(1, 9) → True


# Answer

def makes10(a, b):
    
    if a == 10 or b == 10 or (a + b) == 10:
        
        return True
    
    else:
        
        return False
    

# Tests
print(makes10(9, 10)) # correct output
print(makes10(9, 9))  # correct output
print(makes10(1, 9))  # correct output








