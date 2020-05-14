# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:32:19 2020

@author: Dilay Ercelik
"""


# Practice 

# Given an int n, return the absolute difference between n and 21, 
# except return double the absolute difference if n is over 21.


# Examples:
## diff21(19) → 2
## diff21(10) → 11
## diff21(21) → 0


# Answer:

def diff21(n):
    
    if n <= 21:
        
        return abs(21 - n)
    
    else:
        
        return abs(21 - n)*2
    
    
# Tests
print(diff21(19)) # correct output
print(diff21(10)) # correct output
print(diff21(21)) # correct output