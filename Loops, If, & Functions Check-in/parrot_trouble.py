# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:47:19 2020

@author: Dilay Ercelik
"""


# Practice


# We have a loud talking parrot. 
# The "hour" parameter is the current hour time in the range 0..23. 
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. 
# Return True if we are in trouble.


# Examples:
## parrot_trouble(True, 6) → True
## parrot_trouble(True, 7) → False
## parrot_trouble(False, 6) → False



# Answer:

def parrot_trouble(talking, hour):
    
    if (talking == True and hour < 7) or (talking == True and hour > 20):
        
        return True
    
    else:
        
        return False
    
    
    
# Tests
print(parrot_trouble(True, 6))   # correct output   
print(parrot_trouble(True, 7))   # correct output
print(parrot_trouble(False, 6))  # correct output

    