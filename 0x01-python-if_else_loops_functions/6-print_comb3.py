#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1, 10):
        str_int = str(i) + str(j)
        if int(str_int) < 89:
            print("{}".format(str_int), end=", ")
        else:
            print("{}".format(str_int))
