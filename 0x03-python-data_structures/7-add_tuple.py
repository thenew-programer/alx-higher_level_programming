#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a.copy()
    b = tuple_b.copy()
    if len(a) < 2:
        if len(a) == 0:
            a = 0, 0
        else:
            a = a[0], 0
    elif len(b) < 2:
        if len(b) == 0:
            b = 0, 0
        else:
            b = b[0], 0

    return (a[0] + b[0], a[1] + b[1])
