#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_n = (number % 10)
else:
    last_n = (number % 10) * -1

if (last_n > 5):
    print(f"Last digit of {number} is {last_n} and is greater than 5")
elif (last_n < 6 & last_n != 0):
    print(f"Last digit of {number} is {last_n} and is less than 6 and not 0")
elif (last_n == 0):
    print(f"Last digit of {number} is {last_n} and is 0")