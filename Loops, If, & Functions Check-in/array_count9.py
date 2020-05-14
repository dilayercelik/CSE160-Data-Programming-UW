# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:25:52 2020

@author: Dilay Ercelik
"""


# Practice 


# Given an array (= list) of ints, return the number of 9's in the array.

# Examples:
## array_count9([1, 2, 9]) → 1
## array_count9([1, 9, 9]) → 2
## array_count9([1, 9, 9, 3, 9]) → 3



# Answer

def array_count9(nums):
    
    count_9 = 0
    
    for num in nums:
        
        if num == 9:
            
            count_9 += 1
            
    
    return count_9


# Tests
print(array_count9([1, 2, 9]))        # correct output
print(array_count9([1, 9, 9]))        # correct output
print(array_count9([1, 9, 9, 3, 9]))  # correct output


  