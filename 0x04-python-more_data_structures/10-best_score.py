#!/usr/bin/python3
def best_score(a_dictionary):
    bs = 0
    bs_key = ''
    for key in a_dictionary.keys():
        if a_dictionary[key] > bs:
            bs = a_dictionary[key]
            bs_key = key
    return bs_key
