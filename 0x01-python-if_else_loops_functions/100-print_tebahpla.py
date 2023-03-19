#!/usr/bin/python3

for let in range(122, 96, -1):
    if (let % 2 != 0):
        let -=32
    else:
        let
    print("{:c}".format(let), end="")
