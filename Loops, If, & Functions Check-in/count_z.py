# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:22:47 2020

@author: Dilay Ercelik
"""

# Practice

# Return the number of times the letter z occurs in the given string.


# Examples:
## count_z('lazy') → 1
## count_z('really lazzzy') → 3
## count_z('') → 0


# Answer:

def count_z(input_str):
    
    count_z = 0
    
    for letter in input_str:
        
        if letter == 'z':
            
            count_z += 1
            
    
    return count_z


# Tests
print(count_z('lazy'))           # correct output
print(count_z('really lazzzy'))  # correct output
print(count_z(''))               # correct output





