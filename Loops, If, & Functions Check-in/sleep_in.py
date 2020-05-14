# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:27:28 2020

@author: Dilay Ercelik
"""


# Practice


# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
# We sleep in if it is not a weekday or we're on vacation. 
# Return True if we sleep in.


# Examples:
## sleep_in(False, False) → True
## sleep_in(True, False) → False
## sleep_in(False, True) → True


# Answer:

def sleep_in(weekday, vacation):
    
    if (not weekday) or (vacation):
        
        return True
    
    else:
        
        return False
    

# Tests
print(sleep_in(False, False))  # correct output
print(sleep_in(True, False))   # correct output
print(sleep_in(False, True))   # correct output

  
      
    

    