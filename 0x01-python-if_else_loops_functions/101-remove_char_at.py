#!/usr/bin/python3
def remove_char_at(str, n):
    for letter in str:
        if letter == str[n]:
            continue
        if letter == str[-1]:
            print(letter)
            break
        print(letter, end="")
