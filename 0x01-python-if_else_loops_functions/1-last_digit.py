#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
la = abs(number) % 10
if number < 0:
    la = -la
if la > 5:
    print(f"Last digit of {number} is {la} and is greater than 5")
elif la == 0:
    print(f"Last digit of {number} is {la} and is 0")
else:
    print(f"Last digit of {number} is {la} and is less than 6 and not 0")
