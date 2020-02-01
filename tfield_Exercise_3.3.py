#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:41:02 2020

@author: tfield
"""
# Creates a 4x4 grid with + at intersections, - for horizontal lines, | for vertical lines

# Prints a plus sign without going to a new line
def plus():
    print('+', end=' ')

# Prints a minus sign without going to a new line
def minus():
    print('-', end=' ')
    
# Prints a vertical bar without going to a new line
def bar():
    print('|', end=' ')

# Prints a space without going to a new line    
def space():
    print(' ', end=' ')

# Does function f with inputs f1 and f2 four times
def do_four(f, f1, f2):
    f(f1, f2)
    f(f1, f2)
    f(f1, f2)
    f(f1, f2)

# Does function f1 once, then function f2 four times
def do_one_four(f1, f2):
    f1()
    f2()
    f2()
    f2()
    f2()

# Creates a single row using f1 and for plus/bar and f2 for minus/space, returns to next line
def row(f1,f2):
    do_four(do_one_four,f1,f2)
    f1()
    print('')

# Creates the grid, row by row
row(plus,minus)
do_four(row,bar,space)
row(plus,minus)
do_four(row,bar,space)
row(plus,minus)
do_four(row,bar,space)
row(plus,minus)
do_four(row,bar,space)
row(plus,minus)