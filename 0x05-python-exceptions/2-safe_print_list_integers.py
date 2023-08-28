#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count_int = 0
    for i in range(x):
        if type(my_list[i]) is int:
            print("{:d}".format(my_list[i]), end="")
            count_int += 1
        else:
            continue
    print()
    return count_int
