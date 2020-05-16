# -*- coding: utf-8 -*-
"""
Created on Sat May 16 18:06:42 2020

@author: dilayerc
"""


# Practice


# Given a string, return a new string where "not " has been added to the front. 
# However, if the string already begins with "not", return the string unchanged.


# Examples: 
## not_string('candy') → 'not candy'
## not_string('x') → 'not x'
## not_string('not bad') → 'not bad'


# Answer
def not_string(str):
    
    if str[0:3] != 'not':
        
        new_string = 'not' + ' ' + str
        
        return new_string
    
    else:
        
        return str
    
# Tests
print(not_string('candy'))    # correct output
print(not_string('x'))        # correct output
print(not_string('not bad'))  # correct output


