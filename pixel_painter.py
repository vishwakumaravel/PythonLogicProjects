# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Vishwa Kumaravel
# Section: 579
# Assignment: 11.12
# Date: 11/7/2023
#

file_name = input("Enter the filename: ")
chara = input("Enter a character: ")

pixels = []

with open(file_name, 'r') as file:
    for line in file:
        pixel = []
        values = line.strip().split(',')
        #print(line)
        #print(values)
        for i in range(len(values)):
            if i % 2 == 0:
                pixel.append(" " * int(values[i]))
            else:
                pixel.append(chara * int(values[i]))
        art_line = ''.join(pixel)
        pixels.append(art_line)

with open(f"{file_name[:-3]}txt", 'w') as file1:
    file1.write('\n'.join(pixels))

print(f"{file_name[:-3]}txt created!")
