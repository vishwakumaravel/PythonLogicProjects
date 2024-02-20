# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Vishwa Kumaravel
#        Diego Reyes
# Section: 579
# Assignment: 6.12
# Date: 9/23/2023
#
import math

#inputs
x = float(input("Enter the side length in meters: "))
l = int(input("Enter the number of layers: "))

#variables
a = 0.0
side = 0.0

#iteration for sides (side = side length^2 * the # of squares* 3 sides)
side = x*x*3
Sn = (l / 2) * (2 * side + (l - 1) * side)

#area_top is equal to the area of the biggest triangle
area_top = float((((math.sqrt(3))/(4))*((x*l)**2)))
a = area_top + Sn
print(f"You need {round(a,2)} m^2 of gold foil to cover the pyramid")