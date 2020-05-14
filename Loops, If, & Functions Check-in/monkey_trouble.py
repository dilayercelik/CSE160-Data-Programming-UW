# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:42:25 2020

@author: Dilay Ercelik
"""


# Practice


# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
# We are in trouble if they are both smiling or if neither of them is smiling. 
# Return True if we are in trouble.



# Examples:
## monkey_trouble(True, True) → True
## monkey_trouble(False, False) → True
## monkey_trouble(True, False) → False


def monkey_trouble(a_smile, b_smile):
    
    if (a_smile and b_smile) or (not a_smile and not b_smile):
        
        return True
    
    else:
        
        return False
    
    
# Tests
print(monkey_trouble(True, True))    # correct output
print(monkey_trouble(False, False))  # correct output 
print(monkey_trouble(True, False))   # correct output
    
    
    
    
    
    
    
    
