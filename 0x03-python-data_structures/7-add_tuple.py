#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    new_tup = tuple()
    for t_a, t_b in zip(tuple_a, tuple_b):
        if t_a == () or t_b == ():
            t_a = 0
            t_b = 0
        new_tup += (t_a + t_b,)
    return new_tup
