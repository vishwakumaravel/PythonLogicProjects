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
#file_name = 'scanned_passports.txt'
passports = []

#open file and perform calculations
with open(file_name, 'r') as file:
    passp = {}
    for line in file:
        #print(line)
        if line.strip() != '':
            #print(line)
        ###List of objects separated by \n or \n\n
            keyPairs = line.strip().split()
            #print(keyPairs)
            for pair in keyPairs:
            ###Separates all objects into lists with category and number
                pair = pair.split(':')
                #print(pair)
                key = pair[0]
                value = pair[1]
            ###Creates a dictionary of dictionaries
                passp[key] = value
                #print(passp)
        else:
            #print(line) ###Full of white spaces
            passports.append(passp)
            passp = {}
            #print(passports)


if passp != '':
    passports.append(passp)

###Sets of dictionaries are objects that can be used inside 
#print(len(passports))

###How to call for a specific value within a specific set
temp_pass = passports[-1]
#print(temp_pass['cid'])###should be 555

#pid = passp['pid']
#print(f"Passports: {passports[0]}")
#print(f'pid: {pid}')

expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
expected_fields_copy = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "pid:", "cid:"]
valid_passports = []
count = 0
###Use to write valid passports into file3
string = ''


with open('valid_passports2.txt', 'w') as file3:
###Indent everything once
    for passport in passports:
        expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
        switch = True
    ###Goes trhough all keys in a single dictionary
        for passp in passport:
        ###If one key is not in the expected keys, then the passport is invalid
            if passp not in expected_fields:
                switch = False
                break
        ###If key is actually in dictionary, then it will be removed and loop continues
            else:
                expected_fields.remove(passp)

        ###place to check for the rest of guidelines
#1 = byr – Birth year – four digits, between 1920 and 2007, inclusive
            if passp == 'byr':
                if int(passport['byr']) < 1920 or int(passport['byr']) > 2007:
                    switch = False
                    break
        ################################################################
                else:
            ###Use this as model    
                    string += 'byr:' + passport['byr'] + ' '
        #################################################################

#2 = iyr – Issue year – four digits, between 2013 and 2023, inclusive
            elif passp == 'iyr':
                if int(passport['iyr']) < 2013 or int(passport['iyr']) > 2023:
                    switch = False
                    break
                else:
                    string += 'iyr:' + passport[passp] + ' '
#3 = eyr – Expiration year – four digits, between 2023 and 2033, inclusive
            elif passp == 'eyr':
                if int(passport[passp]) < 2023 or int(passport[passp]) > 2033:
                    switch = False
                    break
                else:
                    string += 'eyr:' + passport[passp] + ' '
#4 = hgt – Height – a number followed by either cm or in
            elif passp == 'hgt':
    #4a = If cm, the number must be between 150 and 193, inclusive 
                if 'cm' in passport[passp]:
                    cm = passport[passp].index('c')
                    if int(passport[passp][:cm]) < 150 or int(passport[passp][:cm]) > 193:
                        switch = False
                        break
                    else:
                        string += 'hgt:' + passport[passp] + ' '
    #4b = If in, the number must be between 59 and 76, inclusive
                elif 'in' in passport[passp]:
                    inc = passport[passp].index('i')
                    if int(passport[passp][:inc]) < 59 or int(passport[passp][:inc]) > 76:
                        switch = False
                        break
                    else:
                        string += 'hgt:' + passport[passp] + ' '
                else:
                    switch = False
                    break
#5 = hcl – Hair color – a # followed by exactly 6 characters (0-9 or a-f)
            elif passp == 'hcl':
                hair_color = '#0123456789abcdef'
                ite1 = True
                for a in range(len(passport[passp])):
                    if passport[passp][0] != '#' or len(passport[passp]) != 7 or passport[passp][a] not in hair_color:
                        ite1 = False
                        break
                    else:
                        continue
                if not ite1:
                    switch = False
                    break
                else:
                    string += 'hcl:' + passport[passp] + ' '
#6 = ecl – Eye color – not required
            elif passp == 'ecl':
                string += 'ecl:' + passport[passp] + ' '
#7 = pid – Passport ID – a nine-digit number, including leading zeroes
            elif passp == 'pid':
                if len(passport[passp]) != 9:
                    switch = False
                    break
                else:
                    digits = '0123456789'
                    ite3 = True
                    for c in range(len(passport[passp])):
                        if passport[passp][c] not in digits:
                            ite3=False
                            break
                        else:
                            continue
                    if not ite3:
                        switch = False
                        break
                    else:
                        string += 'pid:' + passport[passp] + ' '
#8 = cid – Country ID – a three-digit number, NOT including leading zeroes
            elif passp == 'cid':
                ite2 = True
                digits = '0123456789'
                #leadingZero = True
                for b in range(len(passport[passp])):
                    if passport[passp][b] == '0':
                        continue
                    else:
                        if len(passport[passp][b:]) != 3 or passport[passp][b] not in digits:
                            ite2 = False
                            break
                        else:
                            break

                if not ite2:
                    switch = False
                    break
                else:
                    string += 'cid:' + passport[passp] + ' '
        if switch:
###This will add the count of 1 per every passport that gets cleared or that is missing the eye color category
            if expected_fields == [] or ('ecl' in expected_fields and len(expected_fields) == 1):
                valid_passports.append(passport)
                count +=1
                string.strip(' ')
                file3.write(string + '\n\n')
            else:
                string = ''
#print(valid_passports[0]) ###This is the same number as count


print(f"There are {len(valid_passports)} valid passports")

