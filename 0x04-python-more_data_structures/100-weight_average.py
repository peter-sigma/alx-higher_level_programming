#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    n = 0
    d = 0

    for x in my_list:
        n += x[0] * x[1]
        d += x[1]

    return (n / d)
