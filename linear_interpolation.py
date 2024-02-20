# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Vishwa Kumaravel
#        Diego Reyes
#        Jocelyn Afflerbaugh 
# Section: 579
# Assignment: Lab 2.8
# Date: 8/29/2023
#
#
# YOUR CODE HERE
import math

#part 1

slope = ((23027-2027)/(55-10))
x = 25
y = slope*(x-10) + 2027

print("Part 1:")
print("For t = 25 minutes, the position p =", y, "kilometers")
#part 2
x=300
y = slope*(x-10) + 2027

print("Part 2:")
print("For t = 300 minutes, the position p =", (y%(2*math.pi*6745)))
