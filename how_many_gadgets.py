# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishwa Kumaravel
# Section: 579
# Assignment: 4.18
# Date: 9/11/2023
#
import math
day = int(input("Please enter a positive value for day: "))
sum = float(0)
#square + trapezoid + rectangle
#day*day + 1/2(11 + day)*(day-11) 
if(0 <= day <= 10):
    sum = day*10
elif( 0 <= day <= 50):
    sum = ((day/2)*(day+1))-(55)+100
elif(101 > day > 50):
    sum = ((50/2)*(50+1))-(55)+100 + (day-50)*50
elif(day >= 101):
    sum = (((50/2)*(50+1))-(55))+100 + ((100-50)*50)
else:
    sum = sum
if(sum != 0):
    print(f"The sum total number of gadgets produced on day {day} is {int(sum)}")
else:
    print("You entered an invalid number!")
