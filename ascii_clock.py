# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Vishwa Kumaravel
# Diego Reyes
# Chris Chavez
# Section: 579
# Assignment: Topic 8 Team Lab
# Date: 10/20/2023
#
###List of strings for numbers 0-9 and characters a, m, and p
zero = ['000', '0 0', '0 0', '0 0', '000']
one = [' 1 ', '11 ', ' 1 ', ' 1 ', '111']
two = ['222', '  2', '222', '2  ', '222']
three = ['333', '  3', '333', '  3', '333']
four = ['4 4', '4 4', '444', '  4', '  4']
five = ['555', '5  ', '555', '  5', '555']
six = ['666', '6  ', '666', '6 6', '666']
seven = ['777', '  7', '  7', '  7', '  7']
eight = ['888', '8 8', '888', '8 8', '888']
nine = ['999', '9 9', '999', '  9', '999']
colon = [' ', ':', ' ', ':', ' ']
a = [' A ', 'A A', 'AAA', 'A A', 'A A']
m = ['M   M', 'MM MM', 'M M M', 'M   M', 'M   M']
p = ['PPP', 'P P', 'PPP', 'P  ', 'P  ']

###User Input
time = str(input("Enter the time: "))
t_type = int(input("Choose the clock type (12 or 24): "))
char = input("Enter your preferred character: ")
hour_extra = 0 ###Holds the value of the characters prior to ':' before it gets altered

###Splitting the time inputted by the user into a list
time = time.split()
clock = []

###Use of empty list to place every character in time as its own object
for i in time:
  for j in i:
      clock.append(j)

###If there is only '0' before the ':', it gets replace with '1' and '2' to output 12:xx AM
if (clock[0] == '0') and (clock[1] == ':'):
 clock[0] = '1'
 clock.insert(1, '2')

####Check if the character from the user is valid
char_available = 'abcdeghkmnopqrsuvwxyz@$&*='
while not (char in char_available):
    char = input("Character not permitted! Try again: ")

print()

###Defining the hour variable by taking first 2 indexes of clock
###Converts these into an integer
hour_str = clock[0] + clock[1]
hour_str = hour_str.replace(':', '')
hour = int(hour_str)

###If clock to output needs to be in a 24-hr format
if t_type == 24:
  ###If the user choose an available character
   if char != '':  
    ###The i and the j are used in a reverse order (first j and then i)
    ###This allows to go through all the characters in clock in one for i loop
    ###Then the j allows to take every object with index i and place it next to each other
     for i in range(5):
        for j in range(len(clock)):
            if clock[j]==':':
                print(colon[i], end=' ')
            if clock[j] == '0':
                ###.replace use to change a specific character within an object in the list by the character inputted
                print(zero[i].replace('0', char), end=' ')
            if clock[j] == '1':
              print(one[i].replace('1', char), end=' ')
            if clock[j] == '2':
              print(two[i].replace('2', char), end=' ')
            if clock[j] == '3':
              print(three[i].replace('3', char), end=' ')
            if clock[j] =='4':
                if clock[4] == '4':
                    print(four[i].replace('4', char))
                else:
                    print(four[i].replace('4', char), end=' ')
                    print()
            if clock[j] =='5':
                print(five[i].replace('5', char), end=' ')
            if clock[j] =='6':
                print(six[i].replace('6', char), end=' ')
            if clock[j] =='7':
              print(seven[i].replace('7', char), end=' ')
            if clock[j] =='8':
              print(eight[i].replace('8', char), end=' ')
            if clock[j] =='9':
              if clock[4] == '9':
                  print(nine[i].replace('9', char))
              else:
                  print(nine[i].replace('9', char), end=' ')
                  print()
  ###If there is no character input
   else:
    if t_type == 24:
        for i in range(5):
            for j in range(len(clock)):
                if clock[j]==':':
                    print(colon[i], end=' ')
                if clock[j] == '0':
                    print(zero[i], end=' ')
                if clock[j] == '1':
                    print(one[i], end=' ')
                if clock[j] == '2':
                    print(two[i], end=' ')
                if clock[j] == '3':
                    print(three[i], end=' ')
                if clock[j] =='4':
                    if clock[4] == '4':
                        print(four[i])
                    else:
                        print(four[i], end=' ')
                        #print()
                if clock[j] =='5':
                    print(five[i], end=' ')
                if clock[j] =='6':
                    print(six[i], end=' ')
                if clock[j] =='7':
                    print(seven[i], end=' ')
                if clock[j] =='8':
                    print(eight[i], end=' ')
                if clock[j] =='9':
                    if clock[4] == '9':
                        print(nine[i])
                    else:
                        print(nine[i], end=' ')
                        print()
###If clock to output needs to be in a 12-hr format
elif t_type == 12:
    if (t_type == 12):
        ###If statement converts time higher than 12 into 12-hour format ending with PM
        if (hour > 12):
            hour_extra = hour
            hour -= 12
            clock[0] = str(int(hour/10))
            clock[1] = str(int(hour%10))
    if char != '':  
        for i in range(5):
            for j in range(len(clock)):
                if clock[j]==':':
                    print(colon[i], end=' ')
                if clock[j] == '0':
                    if j != 0:
                        print(zero[i].replace('0', char), end=' ')
                if clock[j] == '1':
                  print(one[i].replace('1', char), end=' ')
                if clock[j] == '2':
                  print(two[i].replace('2', char), end=' ')
                if clock[j] == '3':
                  print(three[i].replace('3', char), end=' ')
                if clock[j] =='4':
                    print(four[i].replace('4', char), end=' ')
                if clock[j] =='5':
                    print(five[i].replace('5', char), end=' ')
                if clock[j] =='6':
                    print(six[i].replace('6', char), end=' ')
                if clock[j] =='7':
                  print(seven[i].replace('7', char), end=' ')
                if clock[j] =='8':
                  print(eight[i].replace('8', char), end=' ')
                if clock[j] =='9':
                  print(nine[i].replace('9', char), end=' ')
            ###If the integer value of the first 2 characters in clock is less than 12
            ###Then it prints out AM after printing the time output
            if hour_extra < 12:
              print(a[i], end=' ')
              print(m[i], end= '')
              print()
            ###Else, it print PM after printing the time output
            else:
              print(p[i], end=' ')
              print(m[i], end= '')
              print()
    ###no character input
    else:
        for i in range(5):
          for j in range(len(clock)):
              if clock[j]==':':
                  print(colon[i], end=' ')
              if clock[j] == '0':
                  if j != 0:
                      print(zero[i], end=' ')
              if clock[j] == '1':
                print(one[i], end=' ')
              if clock[j] == '2':
                print(two[i], end=' ')
              if clock[j] == '3':
                print(three[i], end=' ')
              if clock[j] =='4':
                  print(four[i], end=' ')
              if clock[j] =='5':
                  print(five[i], end=' ')
              if clock[j] =='6':
                  print(six[i], end=' ')
              if clock[j] =='7':
                print(seven[i], end=' ')
              if clock[j] =='8':
                print(eight[i], end=' ')
              if clock[j] =='9':
                print(nine[i], end=' ')

          if hour_extra < 12:
            print(a[i], end=' ')
            print(m[i], end= '')
            print()
          else:
            print(p[i], end=' ')
            print(m[i], end= '')
            print()