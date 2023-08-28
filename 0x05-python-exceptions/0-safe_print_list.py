#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for i in range(x):
        try:
            print(my_list[i], end="")
            i += 1
        except (IndexError):
            x = i
            break
    print()
    return x
