# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:02:40 2020

@author: Dilay Ercelik
"""


# Practice


# Given 2 int values, return True if one is negative and one is positive. 
# Except if the parameter "negative" is True, then return True only if both are negative.


# Examples:
## pos_neg(1, -1, False) → True
## pos_neg(-1, 1, False) → True
## pos_neg(-4, -5, True) → True


# Answer

def pos_neg(a, b, negative):
    
    if negative == False:
    
        if (a < 0 and b > 0) or (a > 0 and b < 0):
        
            return True
        
        else: 
            
            return False
    
    else:
        
        if a < 0 and b < 0:
            
            return True
        
        else: 
            
            return False
        
        

# Tests
print(pos_neg(1, -1, False))  # correct output
print(pos_neg(-1, 1, False))  # correct output
print(pos_neg(-4, -5, True))  # correct output
    
        