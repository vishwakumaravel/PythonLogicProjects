# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Vishwa Kumaravel
#        Diego Reyes
# Section: 579
# Assignment: Lab 3.15
# Date: 9/7/2023
#
import math

x = float(input("Please enter the quantity to be converted: "))

#Pounds (force) to Newtons
rounded_x = "{:.2f}".format(x)
def pounds_to_newtons(conv):
    force = 4.4482189159 * conv
    return float(force)
print(f"{rounded_x} pounds force is equivalent to {pounds_to_newtons(x):.2f} Newtons")

#Meters to feet
def meters_to_feet(conv1):
    feet = 3.28084 * conv1
    return float(feet)
print(f"{rounded_x} meters is equivalent to {meters_to_feet(x):.2f} feet")

#Atmospheres to kilopascals (kPa)
def atm_to_kPa(conv1):
    kPa = 101.325 * conv1
    return float(kPa)
print(f"{rounded_x} atmospheres is equivalent to {atm_to_kPa(x):.2f} kilopascals")

#Watts to BTU per hour
def watt_to_btu(conv1):
    watt = 3.412141633 * conv1
    return float(watt)
print(f"{rounded_x} watts is equivalent to {watt_to_btu(x):.2f} BTU per hour")

#Atmospheres to kilopascals (kPa)
def ltps_to_gpm(conv1):
    kPa = 15.850323141489 * conv1
    return float(kPa)
print(f"{rounded_x} liters per second is equivalent to {ltps_to_gpm(x):.2f} US gallons per minute")

def cel_to_frnh(conv1):
    kPa = 1.8 * conv1 + 32
    return float(kPa)
print(f"{rounded_x} degrees Celsius is equivalent to {cel_to_frnh(x):.2f} degrees Fahrenheit")