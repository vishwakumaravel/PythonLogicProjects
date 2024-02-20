# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishwa Kumaravel
# Section: 579
# Assignment: 4.19
# Date: 9/15/2023
#
import cmath
import math
a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))

#defining vars
complex_check = (((b*b)-(4*a*c)) < 0)
inside_sqrt = float(((b*b)-(4*a*c))/2*a)
outside_sqrt = float(-b/2*a)
add_complex = outside_sqrt + inside_sqrt
sub_complex = outside_sqrt - inside_sqrt

#complex check
if(complex_check == True):
    inside_sqrt *= -1
    inside_sqrt = math.sqrt(inside_sqrt)
    outside_sqrt = round(float(int(outside_sqrt)), 1)
    inside_sqrt = round(float(int(inside_sqrt)), 1)
    add_complex = str(outside_sqrt) + " + " + str(inside_sqrt) + "i"
    sub_complex = str(outside_sqrt) + " - " + str(inside_sqrt) + "i"
    add = outside_sqrt + inside_sqrt
    sub = outside_sqrt - inside_sqrt
else:
    inside_sqrt = float(math.sqrt(((b*b)-(4*a*c))/2*a))
    outside_sqrt = float(-b/2*a)
    add_complex = outside_sqrt + inside_sqrt
    sub_complex = outside_sqrt - inside_sqrt
    add_complex = round(float(int(add_complex)), 1)
    sub_complex = round(float(int(sub_complex)), 1)
    add = outside_sqrt + inside_sqrt
    sub = outside_sqrt - inside_sqrt

#prints
if(a!=0 and (add > sub)):
    print(f"The roots are x = {add_complex} and x = {sub_complex}")
elif(a!=0 and (add < sub)):
    print(f"The roots are x = {sub_complex} and x = {add_complex}")
elif(a!=0 and (add == sub)):
    print(f"The root is x = {sub_complex}")
elif(a == 0 and b != 0):
    print(f"The root is x = {round(float(-c/b),1)}")
#elif(a == 0 and (sub != 0)):
    #print(f"The root is x = {-c/b}")
else:  
    print("You entered an invalid combination of coefficients!")