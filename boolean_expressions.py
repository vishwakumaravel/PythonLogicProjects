# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Vishwa Kumaravel
#        Diego Reyes
# Section: 579
# Assignment: Lab 4.15
# Date: 9/10/2023
#

############ Part A ############

a = str(input("Enter True or False for a: "))
b = str(input("Enter True or False for b: "))
c = str(input("Enter True or False for c: "))
A = False
B = False
C = False
if(a == "True" or a== "T" or a=="t" ):
    A = True
else:
    A = False
if(b == "True" or b== "T" or b=="t" ):
    B = True
else:
    B = False
if(c == "True" or c== "T" or c=="t" ):
    C = True
else:
    C = False

############ Part B ############

ad = A and B and C
o = A or B or C
print(f"a and b and c: {ad} ")
print(f"a or b or c: {o} ")

############ Part C ############
xor = (not(A) and B) or (A and not(B))
print(f"XOR: {xor}")
#print(int(A))
t_f = (((int(A) + int(B) + int(C))%2) == 0)
print(f"Odd number: {not(t_f)}")