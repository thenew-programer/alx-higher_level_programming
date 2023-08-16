#!/usr/bin/python3
def best_score(a_dictionary):
    bs = 0
    for key in a_dictionary.keys():
        if a_dictionary[key] > bs:
            bs = a_dictionary[key]
    return bs
