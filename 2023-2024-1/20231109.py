# num = 1
#
# while num != 0:
#     num = int(input("Please enter a number: "))
#     print(f"The number you've entered is {num}")
#
# print(f"End of while loop due to entered number is {num}")

# keep_going = True
#
# while keep_going:
#     num = int(input("Please enter a number: "))
#     print(f"The number you've entered is {num}, ", end="")
#     if num == 0:
#         keep_going = False
#     elif num % 2 == 0:
#         print(f"{num} is an even number!")
#     elif num % 2 != 0:
#         print(f"{num} is an odd number!")
#
# print("End of while loop")

# Number guessing game
# 方案一
# secret_guess = 7
#
# guess = int(input("Please enter a number between 1 and 10: "))
#
# while guess != secret_guess:
#     print("It is not the correct answer, please try again!")
#     guess = int(input("Please enter a number between 1 and 10: "))
#
# print("Congratulations, it is the correct answer!")

# 方案二
# secret_guess = 7
# keep_guessing = True
#
# while keep_guessing:
#     guess = int(input("Please enter a number between 1 and 10: "))
#     if guess == secret_guess:
#         print("Congratulations, it is the correct answer!")
#         keep_guessing = False
#     else:
#         print("It is not the correct answer, please try again!")

# 方案三
# import random
# secret_guess = random.randint(1, 10)
# keep_guessing = True
#
# while keep_guessing:
#     guess = int(input("Please enter a number between 1 and 10: "))
#     if guess == secret_guess:
#         print("Congratulations, it is the correct answer!")
#         keep_guessing = False
#     else:
#         print("It is not the correct answer, please try again!")

# 方案四
# import random
# range_min = 5
# range_max = 20
# secret_guess = random.randint(range_min, range_max)
# keep_guessing = True
#
# while keep_guessing:
#     guess = int(input(f"Please enter a number between {range_min} and {range_max}: "))
#     if guess < range_min or guess > range_max:
#         print("The entered number is out of range, please try again!")
#     elif guess == secret_guess:
#         print("Congratulations, it is the correct answer!")
#         keep_guessing = False
#     else:
#         print("It is not the correct answer, please try again!")

# 方案五
# import random
# range_min = 1
# range_max = 1000
# secret_guess = random.randint(range_min, range_max)
# keep_guessing = True
#
# while keep_guessing:
#     guess = int(input(f"Please enter a number between {range_min} and {range_max}: "))
#     if guess < range_min or guess > range_max:
#         print("The entered number is out of range, please try again!")
#     elif guess == secret_guess:
#         print("Congratulations, it is the correct answer!")
#         keep_guessing = False
#     elif guess > secret_guess:
#         print("The entered number is too large, please try again!")
#     elif guess < secret_guess:
#         print("The entered number is too small, please try again!")

# 方案六
import random
range_min = 1
range_max = 1000
secret_guess = random.randint(range_min, range_max)
keep_guessing = True

while keep_guessing:
    guess = input(f"Please enter a number between {range_min} and {range_max} or enter x to exit: ")
    if guess == 'x':
        print("Exit the game!")
        keep_guessing = False
    else:
        guess = int(guess)

        if guess < range_min or guess > range_max:
            print("The entered number is out of range, please try again!")
        elif guess == secret_guess:
            print("Congratulations, it is the correct answer!")
            keep_guessing = False
        elif guess > secret_guess:
            print("The entered number is too large, please try again!")
        elif guess < secret_guess:
            print("The entered number is too small, please try again!")