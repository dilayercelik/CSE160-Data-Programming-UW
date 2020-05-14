# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:36:08 2020

@author: Dilay Ercelik
"""


# Practice


# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. 
# In this example, the "i" tag makes <i> and </i> which surround the word "Yay". 
# Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".


# Examples:
## make_tags('i', 'Yay') → '<i>Yay</i>'
## make_tags('i', 'Hello') → '<i>Hello</i>'
## make_tags('cite', 'Yay') → '<cite>Yay</cite>'


# Answer

def make_tags(tag, word):
    
    result = '<' + tag + '>' + word + '</' + tag + '>'
    
    return result


# Tests
print(make_tags('i', 'Yay'))     # correct output
print(make_tags('i', 'Hello'))   # correct output
print(make_tags('cite', 'Yay'))  # correct output



