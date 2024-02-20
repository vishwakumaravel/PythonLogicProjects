# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Vishwa Kumaravel
# Section: 579
# Assignment: 10.15
# Date: 11/4/2023
#
print("Guess the secret number! Hint: it's an integer between 1 and 100...")
user_input = input("What is your guess? ")
guess_increment = 1

#two functions
def too_low():
    print("Too low!")

def too_high():
    print("Too high!")

#while loop that runs until break
while True:
    try:
        guess_val = int(user_input)
        if guess_val == 27:
            break
        if guess_val > 27:
            too_high()
        else:
            too_low()
        user_input = input("What is your guess? ")
        guess_increment += 1
    except ValueError:
        user_input = input("Bad input! Try again: ")

#print statement
print(f"You guessed it! It took you {guess_increment} guesses.")


