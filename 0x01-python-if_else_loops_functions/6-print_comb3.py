#!/usr/bin/python3

for i in range(10):
    for j in range(10):
        if i != j and i < 9:
            str_int = str(i) + str(j)
            if int(str_int) < 89:
                print(f"{str_int}", end=", ")
            else:
                print(f"{str_int}")
