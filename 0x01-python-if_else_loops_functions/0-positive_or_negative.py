#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(number)
if number > 0:
    print("{} is positive".format(number))
elif number == 0:
    print(f"{} is zero".format(number))
else:
    print(f"{} is negative".format(number))
