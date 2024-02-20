# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishwa Kumaravel
# Section: 579
# Assignment: 7.29
# Date: 10/1/2023
#

#declaring vars
inp = input("Enter a four-digit integer: ")
k = inp
form = ""
iterations = 0
iter_tracker = [inp]

#checking if inp is filled with leading 0s
while len(inp) < 4:
    inp = '0' + inp


#sorting the input in asc and desc order
while inp != '6174':
    num = list(inp)
    num.sort()
    asc_string = ''.join(num)
    dsc_string = asc_string[::-1]
    asc = int(asc_string)
    dsc = int(dsc_string) 
    inp = str(dsc - asc).zfill(4)
    form = str(dsc - asc)
    iter_tracker.append(form)
    iterations += 1

#pr
if(inp == '6174'):
    print(finStr)
    print(f"{k} reaches 6174 via Kaprekar's routine in {iterations} iterations")
