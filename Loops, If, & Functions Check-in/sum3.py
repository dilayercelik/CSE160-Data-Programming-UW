# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:45:46 2020

@author: Dilay Ercelik
"""


# Practice


# Given an array of ints length 3, return the sum of all the elements.


# Examples:
## sum3([1, 2, 3]) → 6
## sum3([5, 11, 2]) → 18
## sum3([7, 0, 0]) → 7


# Answer

def sum3(nums):
    
    return nums[0] + nums[1] + nums[2]


#Tests
print(sum3([1, 2, 3]))  # correct output
print(sum3([5, 11, 2])) # correct output
print(sum3([7, 0, 0]))  # correct output