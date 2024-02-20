# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Vishwa Kumaravel
# Section: 579
# Assignment: 6.16
# Date: 9/23/2023
#
import math

#vars
x = int(input("Enter a value for n: "))
y = x
left = 0
right = y + 1
inc = x + 1
r = 1

#conditions to get the left and right side of the equation matching
for i in range(1, x):
    left += i

#print("left:" + str(left))
while right != left and right < left:
    inc = inc + 1 
    right += inc
    r += 1
    

if(right == left):
    print(f"{y} is a balancing number with r={r}")
else:
    print(f"{y} is not a balancing number")
