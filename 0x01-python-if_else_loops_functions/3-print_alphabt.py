#!/usr/bin/python3

for alpha in range(ord('a'), (ord('z') + 1)):
    if (alpha == ord('q') | alpha == ord('e')):
        continue
    else:
        print("{:c}". format(alpha), end ="")
