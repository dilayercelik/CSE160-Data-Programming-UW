# -*- coding: utf-8 -*-
"""
Created on Mon May 18 18:55:45 2020

@author: dilayerc
"""


# Practice

# Given an array of ints, return True if one of the first 4 elements in the array is a 9. 
# The array length may be less than 4.


# Examples
## array_front9([1, 2, 9, 3, 4]) → True
## array_front9([1, 2, 3, 4, 9]) → False
## array_front9([1, 2, 3, 4, 5]) → False


# Answer
def array_front9(nums):
    
    if len(nums) >= 4:
    
        if nums[0] == 9 or nums[1] == 9 or nums[2] == 9 or nums[3] == 9:
        
            return True
        
        else:
            
            return False
        
    else:
        
        if 9 in nums:
            
            return True
        
        else:
            
            return False
        
        

# Tests
print(array_front9([1, 2, 9, 3, 4]))   # correct output
print(array_front9([1, 2, 3, 4, 9]))   # correct output
print(array_front9([1, 2, 3, 4, 5]))   # correct output
        
        