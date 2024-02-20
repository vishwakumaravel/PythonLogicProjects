# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Vishwa Kumaravel
# Section: 579
# Assignment: 10.14
# Date: 11/1/2023
#
def is_empty(s):
    return len(s) == 0

def from_roman(roman_numeral):
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    if is_empty(roman_numeral):
        return 0

    if len(roman_numeral) == 1:
        return symbols[roman_numeral[0]]

    symbol = roman_numeral[-1]
    decimal_value = symbols[symbol]

    for i in range(len(roman_numeral)-1, 0, -1):
        if symbols[roman_numeral[i-1]] >= symbols[roman_numeral[i]]:
            decimal_value += symbols[roman_numeral[i-1]]
        else:
            decimal_value -= symbols[roman_numeral[i-1]]
    return decimal_value

def compare_roman_numerals(roman_numeral_1, roman_numeral_2):
    a = from_roman(roman_numeral_1)
    b = from_roman(roman_numeral_2)
    
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

def main():
    num1 = input("Enter the first Roman numeral: ")
    num2 = input("Enter the second Roman numeral: ")
    result = compare_roman_numerals(num1, num2)

    if result == -1:
        compare = 'smaller than'
    elif result == 0:
        compare = 'equal to'
    else:
        compare = 'larger than'

    print(f'{num1} is {compare} {num2}')

if __name__ == '__main__':
    main()
