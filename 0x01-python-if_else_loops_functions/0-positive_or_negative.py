#!/usr/bin/python3
import random
number = random.randint(-10, 10)
while (number):
    if number > 0:
        print(f"{number} is positive")
    elif number == 0:
        print("{} is zero".formart(number))
    else:
        print(f"{number} is negative")
