# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Vishwa Kumaravel
# Section: 579
# Assignment: Lab 12.14
# Date: 11-20-2023

import numpy as np
import matplotlib.pyplot as plt

#Beginning matrix
matrix = np.array([(1.02, 0.095), (-0.095, 1.02)])

#starting point
currp = np.array([[0], [1]])

#initialize arrays
x = np.array([1])
y = np.array([0])

#matrix multiplication
for i in range(250):
    newp = matrix @ currp
    x = np.append(x, newp[0][0])
    y = np.append(y, newp[1][0])
    currp = newp

#plot
plt.plot(x, y, 'b*')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Spiral')
plt.show()
