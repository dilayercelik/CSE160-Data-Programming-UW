# -*- coding: utf-8 -*-
"""
Created on Fri May 15 01:10:22 2020

@author: Dilay Ercelik
"""


# Practice


# The squirrels in Palo Alto spend most of the day playing. 
# In particular, they play if the temperature is between 60 and 90 (inclusive). 
# Unless it is summer, then the upper limit is 100 instead of 90. 
# Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.


# Examples:
## squirrel_play(70, False) → True
## squirrel_play(95, False) → False
## squirrel_play(95, True) → True


# Answer

def squirrel_play(temp, is_summer):
    
    if is_summer:
        
        if 60 <= temp <= 100:
            
            return True
        
        else:
            
            return False
        
    else:
        
        if 60 <= temp <= 90:
            
            return True
        
        else:
            
            return False
        
        
# Tests
print(squirrel_play(70, False))  # correct output
print(squirrel_play(95, False))  # correct output
print(squirrel_play(95, True))   # correct output
           
        
        
        
        
        