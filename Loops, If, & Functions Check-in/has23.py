# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:48:41 2020

@author: Dilay Ercelik
"""


# Practice


# Given an int array length 2, return True if it contains a 2 or a 3.


# Examples:
## has23([2, 5]) → True
## has23([4, 3]) → True
## has23([4, 5]) → False


# Answer

def has23(nums):
  
    if 2 in nums or 3 in nums:
        
        return True
    
    else:
        
        return False
    
    
# Tests
print(has23([2, 5]))  # correct output
print(has23([4, 3]))  # correct output
print(has23([4, 5]))  # correct output