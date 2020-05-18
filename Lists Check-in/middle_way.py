# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:41:24 2020

@author: dilayerc
"""


# Practice


# Given 2 int arrays, a and b, each length 3, return a new array length 2 
# containing their middle elements.

# Examples:
## middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
## middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
## middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]


# Answer
def middle_way(a, b):
    
    new_array = [a[1], b[1]]
    
    return new_array


# Tests
print(middle_way([1, 2, 3], [4, 5, 6]))  # correct output
print(middle_way([7, 7, 7], [3, 8, 0]))  # correct output
print(middle_way([5, 2, 9], [1, 4, 5]))  # correct output
