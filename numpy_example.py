# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Diego Reyes Citalan
# Vishwa Kumaravel
# Chris Chavez
# Section: 579
# Assignment: Lab 12.12
# Date: 19-10-2023
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

import numpy as np
from numpy import sqrt
import matplotlib.pyplot as plt
###Assign A, B, and C Matrices
A = np.arange(12).reshape(3, 4)
print('A =', A)
print()

B = np.arange(8).reshape(4, 2)
print('B =', B)
print()

C = np.arange(6).reshape(2, 3)
print('C =', C)
print()

###'@' is used to find matrix product instead of '*' that is used to find elementwise product
D = A @ B @ C
print('D =', D)
print()

D_tras = D.T
print('D^T =', D_tras)
print()

E = sqrt(D)/2
print('E =', E)
