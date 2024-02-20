# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Vishwa Kumaravel
# Section: 579
# Assignment: 11.11
# Date: 11/6/2023
#

#input and variables
file_name = input("Enter the name of the file: ")
valid_barcodes = []
count = 0

#open file and perform calculations
with open(file_name, 'r') as file:
    for next_line in file:
        next_line = next_line.strip('\n')
        oddSum = 0
        evenSum = 0
        for i in range(len(next_line)-1):
                if i % 2 == 0:
                    oddSum += int(next_line[i])
                else:
                    evenSum += int(next_line[i])
        first_step = evenSum * 3 + oddSum
        lastDig = str(first_step)[-1]
        third_step = 10 - int(lastDig)
        if third_step == int(next_line[-1]):
            count += 1
            valid_barcodes.append(next_line)

with open('valid_barcodes.txt', 'w') as file1:
    file1.write('\n'.join(valid_barcodes))

#print len of valid barcodes list
print(f"There are {count} valid barcodes")


