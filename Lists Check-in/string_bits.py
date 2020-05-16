# -*- coding: utf-8 -*-
"""
Created on Sat May 16 18:51:05 2020

@author: Dilay Ercelik
"""


# Practice

# Given a string, return a new string made of every other char starting with the first, 
# so "Hello" yields "Hlo".

# Examples:
## string_bits('Hello') → 'Hlo'
## string_bits('Hi') → 'H'
## string_bits('Heeololeo') → 'Hello'


# Answer
def string_bits(string):
  
    new_string = ''
    for i in range(0, len(string)):
        
        if i % 2 == 0:
            
            new_string += string[i]
            
    
    return new_string


# Tests
print(string_bits('Hello'))      # correct output
print(string_bits('Hi'))         # correct output
print(string_bits('Heeololeo'))  # correct output







        
