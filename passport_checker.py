# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Vishwa Kumaravel
#        Diego Reyes
#        Chris Chavez
# Section: 579
# Assignment: 11.9
# Date: 11/10/2023
#
file_name = input("Enter the name of the file: ")
passports = []

#open file and perform calculations
with open(file_name, 'r') as file:
    passp = {}
    for line in file:
        if line.strip() != '':
            keyPairs = line.strip().split()
            for pair in keyPairs:
                pair = pair.split(':')
                key = pair[0]
                value = pair[1]
                passp[key] = value
        else:
            passports.append(passp)
            passp = {}

if passp != '':
    passports.append(passp)

#print(f"Passports: {passports}")

expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
expected_fields_copy = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "pid:", "cid:"]
valid_passports = []
count = 0

for passport in passports:
    expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    switch = True
    for passp in passport:
        if passp not in expected_fields:
            switch = False
            break
        else:
            expected_fields.remove(passp)

    if switch:
        if expected_fields == [] or ('ecl' in expected_fields and len(expected_fields) == 1):
            valid_passports.append(passport)
            count += 1

print(f"There are {count} valid passports")

with open('scanned_passports.txt', 'r') as file:
    valid_print = []
    line_join = []
    for line in file:
        line_join.append(line)
        if line == "\n":
            pass_data = "".join(line_join)
            counter = 0
            for field in expected_fields_copy:
                if field in pass_data or (field == "ecl:" and "ecl" not in pass_data):
                    counter += 1
            if counter == 7 or counter == 8:
                valid_print.append(pass_data)
            line_join = []

pass_data = "".join(line_join)
counter = 0
for field in expected_fields_copy:
    if field in pass_data or (field == "ecl:" and "ecl" not in pass_data):
        counter += 1
if counter == 7 or counter == 8:
    valid_print.append(pass_data)

with open('valid_passports.txt', 'w') as file3:
    for print in valid_print:
        file3.write(print)
        

