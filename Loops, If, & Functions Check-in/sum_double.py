# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:15:33 2020

@author: Dilay Ercelik
"""


# Practice


# Given two int values, return their sum. 
# Unless the two values are the same, then return double their sum.


# Examples:
## sum_double(1, 2) → 3
## sum_double(3, 2) → 5
## sum_double(2, 2) → 8


# Answer

def sum_double(a, b):
    
    if a == b:
        
        return (a + b)*2
    
    else:
        
        return a + b
    
    
# Tests
print(sum_double(1, 2)) # correct output
print(sum_double(3, 2)) # correct output
print(sum_double(2, 2)) # correct output


    
    
    
    
    
    
    
    