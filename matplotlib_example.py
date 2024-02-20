# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Diego Reyes Citalan
# Vishwa Kumaravel
# Chris Chavez
# Section: 579
# Assignment: Lab 12.13
# Date: 19-10-2023
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

import matplotlib.pyplot as plt
import numpy as np
from numpy import pi, sin, cos #import specific functions from numpy

###1st Graph
#function for focal point that returns result with every x value between -2 to 2
def func1(f):
    return (1/(4*f)) * x1**2

x1 = np.linspace(-2.0, 2.0) ###creates an array of all values between -2 to 2

plt.figure(1) ###this leaves this graph in its own window
#Calls function to find x when the focal point = 6 and = 2
plt.plot(x1, func1(6), 'b', label='f=6')
plt.plot(x1, func1(2), 'r^', label='f=2')
plt.legend(loc='lower left') ###The above labels will be located at the lower left part
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parabola plots with varying focal lenghts')

plt.show()

###2nd graph
plt.figure(2)
x2 = np.linspace(-4.0, 4.0, 25) #25 will placed 25 evenly spaced number between -4 to 4 (inclusive)
y2 = (2*x2**3)+(3*x2**2)-(11*x2)-6 #cubic polynomial equation with all 25 x values
plt.plot(x2, y2, 'go')
plt.ylabel('y values')
plt.xlabel('x values')
plt.title('Plot of Cubic Polynomial')

plt.show()

###3rd graph
plt.figure(3) 
x3 = np.linspace(-2*pi, 2*pi) #Restircted domain

plt.subplot(211) ###for cos
plt.plot(x3, cos(x3), 'b', label='cos(x)')
plt.ylabel('y=cos(x)')
plt.title('Plot of cos(x) and sin(x)')
plt.legend(loc='lower right')
plt.grid(True) #This will place the grid on the graph

plt.subplot(212) ###for sin
plt.plot(x3, sin(x3), 'r', label='sin(x)')
plt.ylabel('y=sin(x)')
plt.xlabel('x')
plt.legend(loc='upper right')
plt.grid(True)

plt.show()
