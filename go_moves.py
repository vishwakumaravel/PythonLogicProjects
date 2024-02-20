# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Vishwa Kumaravel
# Diego Reyes
# Chris Chavez
# Section: 579
# Assignment: Topic 7 Team Lab
# Date: 10/5/2023
#

import math
conti = ''

# Game Matrix
g_table = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
           ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
           ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
           ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
           ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
           ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
           ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
           ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
           ['.', '.', '.', '.', '.', '.', '.', '.', '.']]

#Board Display
print("Blank Board:")
for i in range(9):
  for j in range(9):
    print(g_table[i][j], end=' ')
  print()

while conti != "Stop":

    #---------Player 1 Turn -----------------------------------------#

    #Loop that makes sure the player plays a valid piece and 
    #can have the option to try again as much as he/she wants
    while True:
    
        #Player 1 Inputs
        p1_row = int(input("Player 1: Choose row #: "))
        p1_col = int(input("Player 1: Choose column #: "))

        #Check if piece is already in the input position 
        #If not, print the game matrix for the opponent's move
        if 1 <= p1_row <= 9 and 1 <= p1_col <= 9:
            if g_table[p1_row-1][p1_col-1] == '.':
                g_table[p1_row-1][p1_col-1] = '*' 
                for i in range(9):
                    for j in range(9):
                        print(g_table[i][j], end=' ')
                    print()
                break #Exit loop if move is Valid
            else:
                print("There is already a piece there! Try Again")
        else:
            print("This is an invalid row or column. Try Again")
        #Check is they still want to play 
    conti = input("Do you wish to continue(Yes or Stop)? ")
    if conti == 'Stop' or conti =='stop':
        exit()

    
    #---------Player 2 Turn -----------------------------------------#

    #Loop that makes sure the player plays a valid piece and 
    #can have the option to try again as much as he/she wants
    while True: 
        
        #Player 2 Inputs
        p2_row = int(input("Player 2: Choose row #: "))
        p2_col = int(input("Player 2: Choose column #: "))

        #Check if piece is already in the input position
        #If not, print the game matrix for the opponent's move
        if 1 <= p2_row <= 9 and 1 <= p2_col <= 9:
            if g_table[p2_row-1][p2_col-1] == '.':
                g_table[p2_row-1][p2_col-1] = 'O'
                for i in range(9):
                    for j in range(9):
                        print(g_table[i][j], end=' ')
                    print()
                break #Exit loop if move is Valid
            else:
                print("There is already a piece there! Try Again")
        else: 
            print("This is an invalid row or column. Try Again")
        #Check is they still want to play 
    conti = input("Do you wish to continue(Yes or Stop)? ")
    if conti == 'Stop' or conti == 'stop':
        exit()