# -*- coding: utf-8 -*-
"""
Created on Sat May 16 18:20:05 2020

@author: dilayerc
"""


# Practice


# Given a string, we'll say that the front is the first 3 chars of the string. 
# If the string length is less than 3, the front is whatever is there. 
# Return a new string which is 3 copies of the front.

# Examples:
## front3('Java') → 'JavJavJav'
## front3('Chocolate') → 'ChoChoCho'
## front3('abc') → 'abcabcabc'


# Answer
def front3(str):
    
    if len(str) < 3:
        
        copy_3 = str * 3
        
    
    else:
        
        copy_3 = str[0:3] * 3
        
    
    return copy_3



# Tests
print(front3('Java'))       # correct output
print(front3('Chocolate'))  # correct output 
print(front3('abc'))        # correct output



    