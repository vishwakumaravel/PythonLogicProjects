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

input = float(input("Please enter the side length: "))

#triangle
def tri(s):
    area = float(((math.sqrt(3))/4)*s*s)
    return float(area)
print(f"A triangle with side {input:.2f} has area {tri(input):.3f}")

#square
def sqr(p):
    area = float(p*p)
    return float(area)
print(f"A square with side {input:.2f} has area {sqr(input):.3f}")

#pentagon
def pent(q):
    area = float((1/4)*(math.sqrt(5*(5+(2*math.sqrt(5))))*q*q))
    return float(area)
print(f"A pentagon with side {input:.2f} has area {pent(input):.3f}")

#dodecagon
def dod(z):
    area = float(3 * (2 + math.sqrt(3)) * z * z)
    return float(area)
print(f"A dodecagon with side {input:.2f} has area {dod(input):.3f}")

    








"""def pounds_to_newtons(conv):
    force = 4.4482189159 * conv
    return float(force)
print(f"{rounded_x} pounds force is equivalent to {pounds_to_newtons(x):.2f} Newtons")"""