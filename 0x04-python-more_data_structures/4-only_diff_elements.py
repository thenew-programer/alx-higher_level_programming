#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    only_diff_set = {"dummy"}
    only_diff_set.remove("dummy")
    for e in set_1:
        if e not in set_2:
            only_diff_set.add(e)
    for e in set_2:
        if e not in set_1:
            only_diff_set.add(e)
    return only_diff_set
