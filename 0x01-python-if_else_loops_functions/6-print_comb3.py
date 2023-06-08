#!/usr/bin/python3
for outter_loop in range(9):
    for inner_loop in range(10):
        if (inner_loop > outter_loop):
            str_num = str(outter_loop) + str(inner_loop)
            if (int(str_num) < 89):
                print("{}".format(str_num), end=", ")
            else:
                print("{}".format(str_num))
