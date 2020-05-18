# -*- coding: utf-8 -*-
"""
Created on Mon May 18 19:58:38 2020

@author: dilayerc
"""


# Practice

# Given a string of even length, return the first half. 
# So the string "WooHoo" yields "Woo".

# Examples:
## first_half('WooHoo') → 'Woo'
## first_half('HelloThere') → 'Hello'
## first_half('abcdef') → 'abc'


# Answer
def first_half(string):
    
    if len(string) % 2 == 0:
        
        return string[: len(string) // 2]
    
    
# Tests
print(first_half('WooHoo'))       # correct output
print(first_half('HelloThere'))   # correct output
print(first_half('abcdef'))       # correct output

    
    
