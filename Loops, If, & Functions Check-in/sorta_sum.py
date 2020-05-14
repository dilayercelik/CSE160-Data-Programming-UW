# -*- coding: utf-8 -*-
"""
Created on Fri May 15 01:20:46 2020

@author: Dilay Ercelik
"""


# Practice

# Given 2 ints, a and b, return their sum. 
# However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.


# Examples:
## sorta_sum(3, 4) → 7
## sorta_sum(9, 4) → 20
## sorta_sum(10, 11) → 21


# Answer

def sorta_sum(a, b):
    
   
    sum_a_b = a + b
    
    if sum_a_b not in list(range(10, 20)):
        
        return sum_a_b
    
    else:
        
        return 20
    
    
# Tests
print(sorta_sum(3, 4))   # correct output
print(sorta_sum(9, 4))   # correct output
print(sorta_sum(10, 11)) # corect output