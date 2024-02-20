# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Vishwa Kumaravel
# Diego Reyes Citalan
# Christopher Chavez
# 
# Section: 579
# Assignment: Team Lab 10
# Date: 02 November 2023

from time import time
from math import *

def list_nums(n):
    '''chatgpt solution'''
    a=0
    b=0
    c=0
    d=0
    square=int(sqrt(n))
    for a in range(square+1):
        if a**2 + b**2 + c**2 + d**2 == n:
            return [a, b, c, d]
        for b in range(a, square+1):
            if a**2 + b**2 + c**2 + d**2 == n:
                return [a, b, c, d]
            for c in range(b, square+1):
                if a**2 + b**2 + c**2 + d**2 == n:
                    return [a, b, c, d]
                for d in range(c, square+1):
                    if a**2 + b**2 + c**2 + d**2 == n:
                        return [a, b, c, d]
#print(list_nums(844474))
#print(list_nums(844474))
# how to measure how long your function takes to run:
t1 = time() # get start time
#print(list_nums(844474)) # run function
t2 = time() # get end time
print(f"This took {t2-t1} seconds") # print result
