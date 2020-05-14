# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:11:57 2020

@author: Dilay Ercelik
"""



# Return the sum of the odd ints in the given list. 
# Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

# Examples:
## sum_odds([5, 2, 6, 3, 4]) → 8
## sum_odds([3, 6, 11, 2, 5]) → 19
## sum_odds([]) → 0


# Answer:

def sum_odds(nums):
    
    sum_odd = 0
    
    
    for num in nums:
        
        if num % 2 == 1:
            
            sum_odd += num
        
        
    return sum_odd


        
# Tests:
print(sum_odds([5, 2, 6, 3, 4]))  # correct output
print(sum_odds([3, 6, 11, 2, 5])) # correct output
print(sum_odds([]))               # correct ouput

            