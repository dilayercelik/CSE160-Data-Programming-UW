# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:29:30 2020

@author: Dilay Ercelik
"""


# Practice


# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".


# Examples:
## hello_name('Bob') → 'Hello Bob!'
## hello_name('Alice') → 'Hello Alice!'
## hello_name('X') → 'Hello X!'


# Answer

def hello_name(name):
    
    return 'Hello {}!'.format(name)



# Tests
print(hello_name('Bob'))    # correct output
print(hello_name('Alice'))  # correct output
print(hello_name('X'))      # correct output
                              
                              
                              