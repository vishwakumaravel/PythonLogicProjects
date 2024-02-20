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
###List of strings for numbers 0, 4, 5, 6
from types import prepare_class

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
char = input("Enter your preferred character: "'\n')
hour_extra = 0
time = time.split()
clock = []

for i in time:
  for j in i:
      clock.append(j)
if (clock[0] == '0') and (clock[1] == ':'):
 clock[0] = '1'
 clock.insert(1, '2')

####Check if the character from the user is valid
char_available = 'abcdeghkmnopqrsuvwxyz@$&*='
while not (char in char_available):
    char = input("Character not permitted! Try again: ")
    if(char in char_available):
       print('\n')
  
# for i in time:
#   for j, char in enumerate(i):
#       if j == 1 and char == ':':
#           clock.pop(0)
#           clock.append('1')
#           clock.append('2')# Add '0' to the front
#       clock.append(char)


#hour = int(clock[0] + clock[1])
hour_str = clock[0] + clock[1]
hour_str = hour_str.replace(':', '')
hour = int(hour_str)
###If block to output time in a 24-hr format
if t_type == 24:
  if char != '':  
    for i in range(5):
        for j in range(len(clock)):
            if clock[j]==':':
                print(colon[i], end=' ')
            if clock[j] == '0':
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
              print(nine[i].replace('9', char), end='')
        print()
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
                    print(nine[i], end='')
            print()

elif t_type == 12:
    if (t_type == 12):
        if (hour > 12):
            hour_extra = hour
            hour -= 12
            clock[0] = str(int(hour/10))
            clock[1] = str(int(hour%10))
#   print(clock)
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
            #if len(clock)==4:  
            #  print(a[i], end=' ')
            #  print(m[i], end= ' ')
             # print()
            if hour_extra < 12:
              print(a[i], end=' ')
              print(m[i], end= '')
              print()
            else:
              print(p[i], end=' ')
              print(m[i], end= '')
              print()
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
#          if len(clock)==4:  
#            print(a[i], end=' ')
#            print(m[i], end= ' ')
#            print()
#          elif int(clock[0]+clock[1]) < 12:
#            print(a[i], end=' ')
#            print(m[i], end= ' ')
#            print()
#          else:
#            print(p[i], end=' ')
#            print(m[i], end= ' ')
#            print()
          if hour_extra < 12:
            print(a[i], end=' ')
            print(m[i], end= '')
            print()
          else:
            print(p[i], end=' ')
            print(m[i], end= '')
            print()