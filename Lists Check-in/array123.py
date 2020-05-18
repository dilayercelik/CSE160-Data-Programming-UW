# -*- coding: utf-8 -*-
"""
Created on Mon May 18 19:01:57 2020

@author: dilayerc
"""


# Practice


# Given an array of ints, return True if the sequence of numbers 1, 2, 3 
# appears in the array somewhere.

# Examples:
## array123([1, 1, 2, 3, 1]) → True
## array123([1, 1, 2, 4, 1]) → False
## array123([1, 1, 2, 1, 2, 3]) → True


# Answer
def array123(nums):
    
    if len(nums) < 3:
        
        return False
    
    else:
        
        result = False
        
        for num in range(len(nums) - 2):
            
            if nums[num : num + 3] == [1, 2, 3]:
                
                result = True
        
        return result
    
    
# Tests
print(array123([1, 1, 2, 3, 1]))     # correct output
print(array123([1, 1, 2, 4, 1]))     # correct output
print(array123([1, 1, 2, 1, 2, 3]))  # correct output


