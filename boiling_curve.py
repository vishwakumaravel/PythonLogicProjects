## By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishwa Kumaravel
# Section: ENG-102 579
# Assignment: Lab 5.14
# Date: 9/18/2023
#

#calling library
import math

#defining inputs
excess_temp_input = float(input("Enter the excess temperature: "))

#creating variables for determining which eq the input should apply to
a = float(1.3)
b = float(5)
c = float(30)
d = float(120)
e = float(1200)

#creating equations for the surfavce heat flux
qs_ab = 1000 * (excess_temp_input/1.3)**1.4445462221
qs_bc = 7000 * (excess_temp_input/5)**2.99555287984
qs_cd = 1500000 * (excess_temp_input/30)**-2.9534452978
qs_de = 25000 * (excess_temp_input/120)**1.77815125038

#Check if input is between A-B and print the a-b eq. Skip to next if and repeat the check and print while making sure to round to the nearest integer
if(a <= excess_temp_input < b):
    print(f"The surface heat flux is approximately {round(qs_ab)} W/m^2 ")
#Else if between B-C
elif(b <= excess_temp_input < c):
    print(f"The surface heat flux is approximately {round(qs_bc)} W/m^2 ")
#Else if between C-D
elif(c <= excess_temp_input < d):
    print(f"The surface heat flux is approximately {round(qs_cd)} W/m^2 ")
#Else if between D-E
elif(d <= excess_temp_input <= e):
    print(f"The surface heat flux is approximately {round(qs_de)} W/m^2 ")
#Else return error message
else:
    print("Surface heat flux is not available")

#And thats it!!!