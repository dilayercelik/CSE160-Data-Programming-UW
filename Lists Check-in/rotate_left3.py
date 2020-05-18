# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:19:01 2020

@author: dilayerc
"""


# Practice

# Given an array of ints length 3, return an array with the elements "rotated left"
# so {1, 2, 3} yields {2, 3, 1}.

# Examples:
## rotate_left3([1, 2, 3]) → [2, 3, 1]
## rotate_left3([5, 11, 9]) → [11, 9, 5]
## rotate_left3([7, 0, 0]) → [0, 0, 7]


# Answer
def rotate_left3(nums):
  
    new_nums = [nums[1], nums[-1], nums[0]]
    
    return new_nums


# Tests
print(rotate_left3([1, 2, 3]))   # correct output
print(rotate_left3([5, 11, 9]))  # correct output
print(rotate_left3([7, 0, 0]))   # correct output