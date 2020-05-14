# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:55:28 2020

@author: Dilay Ercelik
"""


# Practice


# When squirrels get together for a party, they like to have cigars. 
# A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. 
# Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
# Return True if the party with the given values is successful, or False otherwise.


# Examples:
## cigar_party(30, False) → False
## cigar_party(50, False) → True
## cigar_party(70, True) → True


# Answer

def cigar_party(cigars, is_weekend):
    
    if is_weekend:
        
        if cigars > 40:
            
            return True
        
        else:
            
            return False
       
    
    else:
        
        if 40 < cigars < 60:
            
            return True
        
        else:
            
            return False
        
        
        
# Tests
print(cigar_party(30, False))  # correct output
print(cigar_party(50, False))  # correct output
print(cigar_party(70, True))   # correct output



            
        
        
        
        
        
        
        