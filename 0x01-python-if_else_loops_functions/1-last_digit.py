#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
rem = number % 10
s1 = "Last digit of"
if (number < 0):
    rem = ((number * -1) % 10) * -1
if (rem > 5):
    print("Last digit of {} is {} and is greater than 5".format(number, rem))
elif (rem == 0):
    print("Last digit of {} is {} and is 0".format(number, rem))
else:
    print("{} {} is {} and is less than 6 and not 0".format(s1, number, rem))
