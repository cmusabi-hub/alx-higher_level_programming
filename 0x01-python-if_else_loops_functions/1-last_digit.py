#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    mod_num = number % 10
else:
    mod_num = ((number * -1) % 10) * -1

message = "Last digit of {} is {} and is".format(number, mod_num)

if mod_num == 0:
    message += " 0"
elif mod_num > 5:
    message += " greater than 5"
else:
    message += " less than 6 and not 0"
print(message)
