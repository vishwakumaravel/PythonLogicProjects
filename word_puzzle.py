# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Vishwa Kumaravel
# Diego Reyes
# Chris Chavez
# Section: 579
# Assignment: 9.15
# Date: 10/29/2023
#
####Function 1
def get_valid_letters(puzzle): #DONE
  puzzle_list = []
  for char in puzzle:
      if char.isalpha() and char not in puzzle_list:
          puzzle_list.append(char)
  puzzle_str = ''.join(puzzle_list)
  return puzzle_str

####Function 2
def is_valid_guess(string1, string2):
  valid = []
  for char in string1:
      for char1 in string2:
          if char == char1:
              valid.append(char1)
  valid_str = ''.join(sorted(valid))
  return (sorted(valid_str) == sorted(string1))


###Function 3
def check_user_guess(dividend, quotient, divisor, remainder): #DONE
  if dividend == (quotient * divisor + remainder):
      return True
  return False

####Function 4
def make_number(quot, guess):
  q_int = ''
  for i in range(len(quot)):
      if quot[i] in guess:
          q_int += str(guess.index(quot[i]))
  q_int = int(q_int)
  return q_int

####Function 5
def make_numbers(puzzle, guess):
  ###Define character positions
    comma = puzzle.index(',')
    stick = puzzle.index('|')
  ###Work!!!
    quotient = make_number(puzzle[:comma], guess)#'TAKEOURSIM'
    divisor = make_number(puzzle[comma+1:stick-1], guess)#'TAKEOURSIM'
  #################################################################    
    puzzle2 = puzzle[comma+1:]
    stick = puzzle2.index('|')
    comma2 = puzzle2.index(',')
    dividend = make_number(puzzle2[stick+2:comma2], guess)#'TAKEOURSIM'
  #################################################################    
    puzzle3 = puzzle[::-1]
    comma3 = puzzle3.index(',')
    rem = puzzle3[:comma3]
    remainder = make_number(rem[::-1], guess)#'TAKEOURSIM'
    all_ints = (dividend, quotient, divisor, remainder)
    return all_ints

def print_puzzle(puzzle):
    ''' Print puzzle as a long division problem. '''
    puzzle = puzzle.split(',')
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f'{puzzle[i]: >16}')
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")

####Function 6
def main(): #DONE
  puzzle_string = input("Enter a word arithmetic puzzle: ")
  print()
  print_puzzle(puzzle_string)
  print()
  user_guess = input("Enter your guess, for example ABCDEFGHIJ: ")
  if is_valid_guess(get_valid_letters(puzzle_string), user_guess):
      dividend, quotient, divisor, remainder = make_numbers(puzzle_string, user_guess)
      if check_user_guess(dividend, quotient, divisor, remainder):
          print("Good job!")
      else:
          print("Try again!")
  else:
      print("Your guess should contain exactly 10 unique letters used in the puzzle.")

if __name__ == '__main__': #DONE
  main()
