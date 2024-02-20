# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishwa Kumaravel
# Section: 579
# Assignment: 4.16
# Date: 9/11/2023
#
#
#inputs
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
top = float(0)

#conditions
if((num1 >= num2) and (num1 >= num3)):
    top = num1
elif((num2 >= num1) and (num2 >= num3)):
    top = num2
elif((num3 >= num1) and (num3 >= num2)):
    top = num3

#prints
print(f"The largest number is {top}")