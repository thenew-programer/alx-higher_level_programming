#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for idx, num  in enumerate(my_list):
        if num % 2 == 0:
            new_list[idx] = True
        else:
            new_list[idx] = False
    return new_list

print(divisible_by_2([10, 11, 12, 13, 15]))
