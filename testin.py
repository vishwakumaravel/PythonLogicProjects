f = open("scanned_passports.txt", "r")
count = 0
valid = []
l = []
req = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
for line in f:
    l.append(line)
    if line == "\n":
        data = "".join(l)
        c = 0
        for r in req:
            if r in data:
                c += 1
        if c == 7:
            count += 1
            valid.append(data)
            #print(valid)
        l = []

data = "".join(l)
c = 0
for r in req:
    if r in data:
        c += 1
if c == 7:
    count += 1
    valid.append(data)

print("There are", count, "valid passports")

w = open("valid_passports1.txt", "w")
for i in valid:
    w.write(i)

f.close()
w.close()
