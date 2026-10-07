# sentence = input("Please enter a series of numbers separated by comma.\n")
# list_of_words = sentence.split(",")
#
# for word in list_of_words:
#     print(f"The length of {word} is {len(word)}")

# The summing program # 1
# total = 0
#
# while True:
#     number = int(input("Please enter a number to sum, enter 0 to exit: "))
#
#     if number == 0:
#         print("Exit the program!")
#         break
#
#     # total = total + number
#     total += number
#
# print(f"The sum is {total}")

# The summing program # 2
# total = 0
# number_list = []
#
# while True:
#     number = int(input("Please enter a number to sum, enter 0 to exit: "))
#     if number == 0:
#         print("Exit the program!")
#         break
#
#     number_list.append(number)
#     # total = total + number
#     total += number
#
# print(f"The sum of {number_list} is {total}")

# The summing program # 3
# total = 0
# number_list = []
#
# while True:
#     try:
#         number = int(input("Please enter a number to sum, enter 0 to exit: "))
#     except:
#         print("The entered value is invalid! Please try again!")
#         continue
#
#     if number == 0:
#         print("Exit the program!")
#         break
#
#     number_list.append(number)
#     # total = total + number
#     total += number
#
# print(f"The sum of {number_list} is {total}")

# 石头、剪刀、布
import random
game_list = ["石头", "剪刀", "布"]

while True:
    try:
        selection = int(input("请输出0~2的数字，0代表石头，1代表剪刀，2代表布！"))
    except:
        print("输入错误，请重试！")

    computer = random.randint(0, 2)

    if selection == 0:
        if computer == 0:
            print("平局！")
        elif computer == 1:
            print("您赢了！")
        elif computer == 2:
            print("您输了！")
    elif selection == 1:
        if computer == 0:
            print("您输了！")
        elif computer == 1:
            print("平局！")
        elif computer == 2:
            print("您赢了！")
    elif selection == 2:
        if computer == 0:
            print("您赢了！")
        elif computer == 1:
            print("您输了！")
        elif computer == 2:
            print("平局！")


