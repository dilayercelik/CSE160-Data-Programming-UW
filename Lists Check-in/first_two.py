# -*- coding: utf-8 -*-
"""
Created on Mon May 18 19:53:57 2020

@author: dilayerc
"""


# Practice


# Given a string, return the string made of its first two chars, 
# so the String "Hello" yields "He". 
# If the string is shorter than length 2, return whatever there is, 
# so "X" yields "X", and the empty string "" yields the empty string "".


# Examples:
## first_two('Hello') → 'He'
## first_two('abcdefg') → 'ab'
## first_two('ab') → 'ab'


# Answer
def first_two(string):
    
    if len(string) < 2:
        
        return string
    
    else:
        
        return string[:2]
    
    
# Tests
print(first_two('Hello'))    # correct output
print(first_two('abcdefg'))  # correct output
print(first_two('ab'))       # correct output


