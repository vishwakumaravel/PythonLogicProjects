# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishwa Kumaravel
# Section: 1.13
# Assignment: Lab Topic 1
# Date: 8/23/2023
#
#
import math
print("This shows the evaluation of sin(x-1)/(x-1) evaluated close to x=1")
print("My guess is 3")
i=0
#these are my values
xVals = [1.1, 1.01, 1.001, 1.0001, 1.00001, 1.000001, 1.0000001, 1.00000001]

while i<=7:
    eq = math.sin(xVals[i]-1)/(xVals[i]-1)
    print(eq)
    i = i +1
    
print()
print("My guess was a bit off")
