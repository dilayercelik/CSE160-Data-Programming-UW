# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:32:04 2020

@author: dilayerc
"""


# Practice

# Given an array of ints length 3, return a new array with the elements 
# in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

# Examples:
## reverse3([1, 2, 3]) → [3, 2, 1]
## reverse3([5, 11, 9]) → [9, 11, 5]
## reverse3([7, 0, 0]) → [0, 0, 7]


# Answer
def reverse3(nums):
  
    new_nums = [nums[-1], nums[1], nums[0]]
    
    return new_nums


# Tests
print(reverse3([1, 2, 3]))   # correct output
print(reverse3([5, 11, 9]))  # correct output
print(reverse3([7, 0, 0]))   # correct output