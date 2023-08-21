#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    main_numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0
    letters = enumerate(main_numbers)

    for letter in roman_string:
        number += main_numbers[letter.upper()]
    # for letter in roman_string:

    return number
roman = "MDCXXVI"
print(f"{roman} is {roman_to_int(roman)}")
