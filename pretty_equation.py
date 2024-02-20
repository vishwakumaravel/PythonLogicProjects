# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Vishwa Kumaravel
#        Diego Reyes
# Section: 579
# Assignment: Lab 4.14
# Date: 9/10/2023
#

#inputs
A = str(input("Please enter the coefficient A: "))
B = str(input("Please enter the coefficient B: "))
C = str(input("Please enter the coefficient C: "))

#A conditions
if(A == "1"):
    a = "x^2"
elif(A == "-1"):
    a = "- x^2"
elif(int(A) > 0):
    a =  A + "x^2"
elif(int(A) < 0):
    a = "- " + str(abs(int(A))) + "x^2"
else:
    a = ""

#B conditions
if(int(A)!=0 and B == "1" and int(C)!=0):
    b = " + x "
elif(int(A)==0 and B == "1" and int(C) ==0):
    b = "x"
elif(int(A)!=0 and B == "1" and int(C) ==0):
    b = " + x"
elif(int(A)==0 and B == "1" and int(C) !=0):
    b = "x "

#------------------------------------------------
elif(int(A) == 0 and B == "-1" and int(C)!=0):
    b = "- x "
elif(int(A) != 0 and B == "-1" and int(C)==0):
    b = " - x"
elif(int(A) != 0 and B == "-1" and int(C)!=0):
    b = " - x "
elif(int(A) == 0 and B == "-1" and int(C)==0):
    b = "- x"

#------------------------------------------------
elif(int(A) != 0 and int(B) > 0 and int(C) != 0):
    b = " + " + B + "x "
elif(int(A) == 0 and int(B) > 0 and int(C) == 0):
    b = B + "x"
elif(int(A) == 0 and int(B) > 0 and int(C) != 0):
    b = B + "x "
elif(int(A) != 0 and int(B) > 0 and int(C) == 0):
    b = " + " + B + "x"

#------------------------------------------------
elif(int(A) == 0 and int(B) < 0 and int(C) != 0):
    b = "- " + str(abs(int(B))) + "x "
elif(int(A) == 0 and int(B) < 0 and int(C) == 0):
    b = " - " + str(abs(int(B))) + "x"
elif(int(A) != 0 and int(B) < 0 and int(C) != 0):
    b = " - " + str(abs(int(B))) + "x "
elif(int(A) != 0 and int(B) < 0 and int(C) == 0):
    b = " - " + str(abs(int(B))) + "x"

#------------------------------------------------
else:
    b = ""

#C conditions
if( (int(B))==0 and int(C) > 0):
    c = " + " + C
elif( int(B)!=0 and int(C) > 0):
    c = "+ " + C
elif(int(B)!=0 and int(C) < 0):
    c = "- " + str(abs(int(C)))
elif(int(B)==0 and int(C) < 0):
    c = " - " + str(abs(int(C)))
else:
    c = ""

#print
print(f"The quadratic equation is {a}{b}{c} = 0")