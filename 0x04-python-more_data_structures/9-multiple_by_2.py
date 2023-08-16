#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_ = {1: 1}
    dict_.pop(1)
    for key in a_dictionary.keys():
        dict_[key] = a_dictionary[key] * 2
    return dict_
