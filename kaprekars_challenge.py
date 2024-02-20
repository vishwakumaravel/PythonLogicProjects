# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishwa Kumaravel
# Section: 579
# Assignment: 7.29
# Date: 10/1/2023
#

tot = 0
for x in range(9999):
    inp = str(x)
    iterations = 0
    while inp != '6174':
        while len(inp) < 4:
            inp = '0' + inp
        
        num = list(inp)
        num.sort()
        asc_string = ''.join(num)
        dsc_string = asc_string[::-1]
        asc = int(asc_string)
        dsc = int(dsc_string) 
        inp = str(dsc - asc).zfill(4)
        form = str(dsc - asc)
        iterations += 1
        tot += iterations
#pr
print(f"Kaprekar's routine takes {tot} total iterations for all four-digit numbers")
