# 四则计算器
def addition(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


while True:
    number1 = float(input("Please enter the first number: "))
    operator = input("Please input the operator or input x to exit: ")
    if operator == "x":
        print(f"Exit the calculator")
        break
    number2 = float(input("Please enter the second number: "))

    if operator == "+":
        print(f"{number1} {operator} {number2} is {addition(number1, number2)}")
    elif operator == "-":
        print(f"{number1} {operator} {number2} is {subtract(number1, number2)}")
    elif operator == "*":
        print(f"{number1} {operator} {number2} is {multiply(number1, number2)}")
    elif operator == "/":
        print(f"{number1} {operator} {number2} is {divide(number1, number2)}")
    else:
        print(f"Wrong input, please try again!")
        continue
