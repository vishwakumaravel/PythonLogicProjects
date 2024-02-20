# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishwa Kumaravel
# Section: 579
# Assignment: 7.27
# Date: 10/1/2023
#

#inputs and vars
inp = str(input("Enter numbers: "))
wordList = inp.split()
intList = [int(x) for x in wordList]
sum = 0
lval = 0
rval = 0
bl = False
left = []
right = intList

#creating sum
for i in range(len(intList)):
    sum+=intList[i]

rval = sum

#finding a point to split
for k in range(len(intList)):
    rval -= intList[k]
    lval += intList[k]
    if(lval < rval):
        left.append(intList[k])
    elif(lval == rval):
        left.append(intList[k])
        right = intList[k + 1:]
        bl = True
        break
    else:
        bl = False



if(bl == True):
    print(f"Left: {left}")
    print(f"Right: {right}")
    print(f"Both sum to {lval}")
else:
    print(f"Cannot split evenly")
        
     

