# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:37:15 2020

@author: Dilay Ercelik
"""


# Practice


# Given an int n, return True if it is within 10 of 100 or 200. 


# Examples:
## near_hundred(93) → True
## near_hundred(90) → True
## near_hundred(89) → False


# Answer

def near_hundred(n):
  
    if ( abs(100 - n) <= 10 ) or n == 200:
        
        return True 
    
    else:
        
        return False
    
    

# Tests
print(near_hundred(93)) # correct output
print(near_hundred(90)) # correct output
print(near_hundred(89)) # correct output