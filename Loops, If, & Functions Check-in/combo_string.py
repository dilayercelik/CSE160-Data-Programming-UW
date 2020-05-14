# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:40:03 2020

@author: Dilay Ercelik
"""


# Practice


# Given 2 strings, a and b, return a string of the form short+long+short, 
# with the shorter string on the outside and the longer string on the inside. 
# The strings will not be the same length, but they may be empty (length 0).


# Examples:
## combo_string('Hello', 'hi') → 'hiHellohi'
## combo_string('hi', 'Hello') → 'hiHellohi'
## combo_string('aaa', 'b') → 'baaab'


# Answer

def combo_string(a, b):
    
    if len(a) < len(b):
        
        return a + b + a
    
    elif len(a) > len(b):
        
        return b + a + b
    

# Tests
print(combo_string('Hello', 'hi'))  # correct output
print(combo_string('hi', 'Hello'))  # correct output
print(combo_string('aaa', 'b'))     # correct output  
    
    
    
    
    