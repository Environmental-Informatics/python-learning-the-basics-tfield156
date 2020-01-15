#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:24:18 2020

@author: tfield
"""

# Takes a function and a value as inputs, calls the function with the value, twice
def do_twice(f,v):
    f(v)
    f(v)

# Prints the inputted value twice
def print_twice(bruce):
    print(bruce)
    print(bruce)
    
# Calls the function print_twice with value 'spam', twice. Resulting in 'spam' being printed 4 times
do_twice(print_twice,'spam')