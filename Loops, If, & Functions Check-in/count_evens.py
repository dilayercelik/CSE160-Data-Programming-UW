# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:51:31 2020

@author: Dilay Ercelik
"""


# Practice

# Return the number of even ints in the given array. 
# Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


# Examples:
## count_evens([2, 1, 2, 3, 4]) → 3
## count_evens([2, 2, 0]) → 3
## count_evens([1, 3, 5]) → 0


# Answer

def count_evens(nums):
    
    count_even = 0
    
    for num in nums:
        
        if num % 2 == 0:
            
            count_even += 1
            
    return count_even


# Tests
print(count_evens([2, 1, 2, 3, 4]))  # correct output
print(count_evens([2, 2, 0]))        # correct output
print(count_evens([1, 3, 5]))        # correct output



