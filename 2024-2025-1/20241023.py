# -*- coding: utf-8 -*-
import random
keep_guessing = True
target = random.randint(1,10)
while keep_guessing:
    num = int(input("Please enter a number between 1 and 10: "))
    if num > target:
        print(f"Sorry {num} is too high")
    elif num < target:
        print(f"Sorry {num} is too low")
    else:
        print(f"Congratulations {num} is the correct number")
        keep_guessing = False
