# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:32:55 2020

@author: Dilay Ercelik
"""


# Practice


# Given two strings, a and b, return the result of putting them together in the order abba, 
# e.g. "Hi" and "Bye" returns "HiByeByeHi".


# Examples:
## make_abba('Hi', 'Bye') → 'HiByeByeHi'
## make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
## make_abba('What', 'Up') → 'WhatUpUpWhat'


# Answer:

def make_abba(a, b):
    
    abba = a + b*2 + a
    
    return abba


# Tests
print(make_abba('Hi', 'Bye'))   # correct output
print(make_abba('Yo', 'Alice')) # correct output
print(make_abba('What', 'Up'))  # correct output