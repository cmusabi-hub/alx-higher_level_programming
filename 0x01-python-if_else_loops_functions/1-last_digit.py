#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    last_n = (number % 10)
else:
    last_n = (number % 10) * -1

if (last_n > 5):
    print("Last digit of {:d} is {:d} and is greater that 5".format(number, last_n))
elif (last_n < 6 & last_n != 0):
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, last_n))
elif (last_n == 0):
    print("Last digit of {:d} is {:d} and is 0".format(number, last_n))
