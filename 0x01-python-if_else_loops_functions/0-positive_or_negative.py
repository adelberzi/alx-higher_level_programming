#!/usr/bin/python3
import random

number = random.randint(-10, 10)

if number > 0:
    print(f"{number} The following number is postive")
elif number < 0:
    print(f"{number} The following number is negative")
else:
    print(f"{number} The following number is zero")
