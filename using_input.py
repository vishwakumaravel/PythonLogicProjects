# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishwa Kumaravel
# Section: 3.17
# Assignment: Lab Topic 2 (Individual)
# Date: 9/9/2023
#
#
import math

#Force
print("This program calculates the applied force given mass and acceleration")
m = float(input("Please enter the mass (kg): "))
a = float(input("Please enter the acceleration (m/s^2): "))
print(f"Force is {m*a:.1f} N")

#Wavelength
print("This program calculates the wavelength given distance and angle")
d = float(input("Please enter the distance (nm): "))
ang = float(input("Please enter the angle (degrees): "))
print(f"Wavelength is {float(2*d*(math.sin(math.radians(ang)))):.4f} nm")

#Radon-222
print("This program calculates how much Radon-222 is left given time and initial amount")
days = float(input("Please enter the time (days): "))
g = float(input("Please enter the initial amount (g): "))
print(f"Radon-222 left is {float(g*math.pow(2,(-days/3.8))):.2f} g")

#Pressure
print("This program calculates the pressure given moles, volume, and temperature")
m = float(input("Please enter the number of moles: "))
v = float(input("Please enter the volume (m^3): "))
t = float(input("Please enter the temperature (K): "))
print(f"Pressure is {float(((m*8.314*t)/v)/1000):.0f} kPa")


"""

This program calculates how much Radon-222 is left given time and initial amount
Please enter the time (days): 
Please enter the initial amount (g): 
Radon-222 left is 10.85 g

This program calculates the pressure given moles, volume, and temperature
Please enter the number of moles: 
Please enter the volume (m^3): 
Please enter the temperature (K): 
Pressure is 64 kPa

f = 27*1.5
w = 2*0.025*(math.sin(math.radians(35)))
r = 27*math.pow(2,(-5/3.8))
p = ((5*8.314*415)/0.27)/1000
print("Force is", f, "N")
print("Wavelength is", w,"nm")
print("Radon-222 left is",r,"g")
print("Pressure is", p, "kPa" )"""