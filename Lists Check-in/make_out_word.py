# -*- coding: utf-8 -*-
"""
Created on Mon May 18 19:45:20 2020

@author: dilayerc
"""


# Practice


# Given an "out" string length 4, such as "<<>>", and a word, 
# return a new string where the word is in the middle of the out string, 
# e.g. "<<word>>".


# Examples:
## make_out_word('<<>>', 'Yay') → '<<Yay>>'
## make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
## make_out_word('[[]]', 'word') → '[[word]]'


# Answer
def make_out_word(out, word):
    
    new_string = out[:2] + word + out[2:]
    
    return new_string


# Tests
print(make_out_word('<<>>', 'Yay'))     # correct output
print(make_out_word('<<>>', 'WooHoo'))  # correct output
print(make_out_word('[[]]', 'word'))    # correct output
