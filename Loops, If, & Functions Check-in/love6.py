# -*- coding: utf-8 -*-
"""
Created on Fri May 15 01:29:47 2020

@author: Dilay Ercelik
"""


# Practice

# The number 6 is a truly great number. 
# Given two int values, a and b, return True if either one is 6. 
# Or if their sum or difference is 6. 
# Note: the function abs(num) computes the absolute value of a number.


# Examples:
## love6(6, 4) → True
## love6(4, 5) → False
## love6(1, 5) → True


# Answer

def love6(a, b):
    
    if a == 6 or b == 6 or (a + b) == 6 or abs(a - b) == 6:
        
        return True
    
    else:
        
        return False
    

# Tests
print(love6(6, 4))  # correct output
print(love6(4, 5))  # correct output
print(love6(1, 5))  # correct output




       
    