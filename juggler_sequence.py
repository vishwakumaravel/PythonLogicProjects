# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Vishwa Kumaravel
# Section: 579
# Assignment: 6.15
# Date: 9/23/2023
#
import math

#vars
a = int(input("Enter a positive integer: "))
b = a
counter = 0
stri = f"{a}"

#conditionals to determine if odd or even
if(a != 1):
    stri = f"{a}, "

while a != 1:
    if(a % 2 == 0):
        a = int(math.sqrt(a))
        #a = a // 1
        #stri += f"{a}, "
        counter += 1

    elif(a % 2 != 0):
        a = int(math.pow(a, 1.5))
        #a = a // 1
        #stri += f"{a},"
        counter+=1

    if a != 1:  
        stri += f"{a}, "

    else:  
        stri += f"{a}"

print(f"The Juggler sequence starting at {b} is:\n{stri}\nIt took {counter} iterations to reach 1")