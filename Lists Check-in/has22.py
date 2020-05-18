# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:50:33 2020

@author: dilayerc
"""


# Practice


# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

# Examples:
## has22([1, 2, 2]) → True
## has22([1, 2, 1, 2]) → False
## has22([2, 1, 2]) → False


# Answer
def has22(nums):
    
    for i in range(len(nums)-1):
        
        if nums[i : i + 2] == [2,2]:
            
            result = True
    
        else:
        
            result = False
            
            
    return result
    

# Tests
print(has22([1, 2, 2]))    # correct output
print(has22([1, 2, 1, 2])) # correct output
print(has22([2, 1, 2]))    # correct output


