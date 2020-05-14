# -*- coding: utf-8 -*-
"""
Created on Fri May 15 01:33:48 2020

@author: Dilay Ercelik
"""


# Practice

# Given a number n, return True if n is in the range 1..10, inclusive. 
# Unless outside_mode is True, 
# in which case return True if the number is less or equal to 1, 
# or greater or equal to 10.


# Examples:
## in1to10(5, False) → True
## in1to10(11, False) → False
## in1to10(11, True) → True


# Answer

def in1to10(n, outside_mode):
    
    if outside_mode:
        
        if n <= 1 or n >= 10:
            
            return True
        
        else:
            
            return False
        
    else:
        
        if n in list(range(1, 11)):
            
            return True
        
        else:
            
            return False
        


# Tests
print(in1to10(5, False))  # correct output
print(in1to10(11, False)) # correct output
print(in1to10(11, True))  # correct output            
        
        