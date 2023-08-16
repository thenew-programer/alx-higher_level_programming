#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    for element in my_list:
        if element not in uniq_list:
            uniq_add.append(element)
    return uniq_list
