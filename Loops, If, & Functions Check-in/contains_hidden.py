# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:18:36 2020

@author: Dilay Ercelik
"""

# Practice

# Returns True if int hidden_num is found in the given array.


# Examples:
## contains_hidden([5, 2, 6, 3, 4], 3) → True
## contains_hidden([3, 6, 11, 2, 5], 19) → False
## contains_hidden([3, 6, 11, 2, 5], 5) → True


# Answer:

def contains_hidden(nums, hidden_num):
    
    if hidden_num in nums:
        
        return True
    
    else:
    
        return False
    

# Tests
print(contains_hidden([5, 2, 6, 3, 4], 3))   # correct ouput
print(contains_hidden([3, 6, 11, 2, 5], 19)) # correct output
print(contains_hidden([3, 6, 11, 2, 5], 5))  # correct output