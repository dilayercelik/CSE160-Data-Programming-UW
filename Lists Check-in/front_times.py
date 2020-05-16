# -*- coding: utf-8 -*-
"""
Created on Sat May 16 18:45:52 2020

@author: dilayerc
"""


# Practice

# Given a string and a non-negative int n, 
# we'll say that the front of the string is the first 3 chars, 
# or whatever is there if the string is less than length 3. 
# Return n copies of the front;

# Examples:
## front_times('Chocolate', 2) → 'ChoCho'
## front_times('Chocolate', 3) → 'ChoChoCho'
## front_times('Abc', 3) → 'AbcAbcAbc'


# Answer
def front_times(str, n):
    
    if len(str) < 3:
        
        return str * n
    
    else:
        
        return str[0:3] * n
    

# Tests
print(front_times('Chocolate', 2))  # correct output
print(front_times('Chocolate', 3))  # correct output
print(front_times('Abc', 3))        # correct output







