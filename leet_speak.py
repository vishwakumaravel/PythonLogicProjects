# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishwa Kumaravel
# Section: 579
# Assignment: 7.26
# Date: 10/1/2023
#
#establishing inputs, vars, and dictionaries
inp = str(input("Enter some text: "))
wordList = inp.split()
leet = {'a': '4', 'e': '3', 'o': '0', 's': '5','t': '7'}

#iterating through wordlist and the characters in each word then replacing them if they match with a key
for i in range(len(wordList)):
    j = list(wordList[i])
    for x in range(len(j)):
        if(j[x] in leet):
            j[x] = leet[j[x]]
    wordList[i] =''.join(j)
finStr = ' '.join(wordList)
print(f"In leet speak, \"{inp}\" is: {finStr}")
