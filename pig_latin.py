# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishwa Kumaravel
# Section: 579
# Assignment: 7.25
# Date: 9/30/2023
#

#declaring variables
inp = str(input("Enter word(s) to convert to Pig Latin: "))
wordList = inp.split()
vowels = 'aeiouy'
cons = 'bcdfghjklmnpqrstvwxyz'

#looping through the input and checking if vowel or consonant
for i in range(len(wordList)):
    j = list(wordList[i])
    if(j[0] in vowels):
        wordList[i] += "yay"
    else:
        if(j[0] in cons and j[1] in cons and j[2] in cons):
            j += (j[0:3])
            j.append("ay")
            j[0:3] = ''
            wordList[i] =''.join(j)
        elif(j[0] in cons and j[1] in cons):
            j += (j[0:2])
            j.append("ay")
            j[0:2] = ''
            wordList[i] =''.join(j)
        elif(j[0] in cons):
            j += (j[0])
            j.append("ay")
            j[0] = ''
            wordList[i] =''.join(j)
finStr = ' '.join(wordList)
print(f"In Pig Latin, \"{inp}\" is: {finStr}")

            