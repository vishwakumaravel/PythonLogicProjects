# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Vishwa Kumaravel
# Section: 579
# Assignment: 6.13
# Date: 9/23/2023
#

#vars
a  = int(input("Enter an integer: "))
b  = int(input("Enter another integer: "))

#iteration w/ conditions
for i in range(1, 101, 1):
    if(i % a == 0 and i % b == 0):
        print("Howdy Whoop")
    elif(i % a == 0):
        print("Howdy")
    elif(i % b == 0):
        print("Whoop")
    else:
        print(i)