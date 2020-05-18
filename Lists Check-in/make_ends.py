# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:47:03 2020

@author: dilayerc
"""


# Practice


# Given an array of ints, return a new array length 2 containing 
# the first and last elements from the original array. 
# The original array will be length 1 or more.

# Examples:
## make_ends([1, 2, 3]) → [1, 3]
## make_ends([1, 2, 3, 4]) → [1, 4]
## make_ends([7, 4, 6, 2]) → [7, 2]


# Answer
def make_ends(nums):
    
    new_array = [nums[0], nums[-1]]
    
    return new_array


# Tests
print(make_ends([1, 2, 3]))     # correct output
print(make_ends([1, 2, 3, 4]))  # correct output
print(make_ends([7, 4, 6, 2]))  # correct output