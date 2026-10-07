# print("Hello World")
# print(type(5))


# a = 10
# b = 20
# c = a + b
# print(f"sum of a and b is {c}")

# print("My first program was \"Hello World!\" in PythonStudy\n\nPythonStudy is cool!")
#
# print('''3
# 4
# 5
# 6
# ''')

# str1 = "string 1"
# str2 = "string 2"
# print("String 1 is {}, String 2 is {}.".format(str1,str2))
#
# a = 10
# print(id(a))
# print(id(10))
#
# name = input("What is your name?\n")
# age = input("What is your age?\n")
# year = 2022 - int(age)
# print(f"name is {name}, age is {age}, you born in {year} or {year - 1}")
# print(type(age))
# print(type(int(age)))

# a = "Shenyang University of Technology"
# print(a.upper())
# print(a.lower())
# print(a.title())
# print(a)

# first_name = "Jimmy"
# surname = "Hendrix"
# full_name = first_name + surname
# print(full_name)
#
# a_b = 1
# _a = 2

# name = "Ellen"
# age = 32
# print(name + "is" + age)

# str1 = "ab cd ef"
# print(str1[0:1])
# print(str1[0:2])
# print(str1[0:3])
# print(str1[0:4])
# print(str1[0:5])
# print(str1[0:6])
# print(str1[0:7])
# print(str1[0:8])
# print("Out of range")
# print(str1[0:9])
# print(str1[0:10])
# print(str1[0:50])


# print(str1[-10])
# print("the length of {} is {}".format(str1,len(str1)))
# print(str1[-1])
# print(str1[-10:-1])
# print(str1[-11:-1])
#
# print(str1[1:10])
# print(str1[1:2])

# x = 0
#
# if x < 5:
#   print("1")
# else:
#   print("2")

# astr = 'Hello Bob'
# try:
#     istr = int(astr)
# except:
#     istr = -1
# print('First', istr)
#
# astr = '123'
# try:
#     istr = int(astr)
# except:
#     istr = -1
# print('Second', istr)

# a = 1
# while a <= 100:
#     if a % 2 == 0:
#         print(a)
#     a += 1

# for i in range(4):
# for i in range(0, 4):
# for i in range(0, 10, 2):
#     print(i)
# print(list(range(0, 4)))

"""
import sys
list1 = [10, "5", "Tom"]
print(sys.getsizeof(list1))
print(sys.getsizeof(100))           # 28
print(sys.getsizeof("a"))           # 50
print(sys.getsizeof("50"))          # 51
print(sys.getsizeof("520"))         # 52
print(sys.getsizeof("Tom"))         # 52
print(sys.getsizeof("Jessica"))     # 56
print(sys.getsizeof("Jessicaf"))    # 57
"""

# import datetime


# import random
# for i in range(10):
#     # x = random.random()
#     x = random.random()
#     print(x)

# print(list("Hello world"))

# some = ['1', '2', '3']
# if 1 in some:
#     print("1")
# if 10 not in some:
#     print("2")
# print(" ".join(some))

# line = 'good;bad;ugly'
# print(line.split())
# print(line.split(';'))

# car_list = ['a', 'b', 'c', 'd', 'e']
# print(car_list[1:4])

# fruit = 'Banana'
# print(fruit[0])     # string is immutable here
# fruit_list = ['apple', 'orange', 'watermelon', 'pear']
# fruit_list[0] = 'banana'
# print(fruit_list)   # list is mutable here
# fruit_list.insert(0, 'banana')
# fruit_list2 = ['banana', 'tomato']
# fruit_list.extend(fruit_list2)
# fruit_list.extend('abaca')
# fruit_list3 = [1, 2]
# fruit_list.extend(fruit_list3)
# print(fruit_list)
# fruit_list.remove('a')
# print(fruit_list)
# item_removed = fruit_list.pop(1)
# print(fruit_list)
# print(item_removed)

# fruit_list.sort()
# print(fruit_list)
# fruit_list.reverse()
# print(fruit_list)
# fruit_list.sort()
# print(fruit_list)
# fruit_list.sort(reverse=True)
# print(fruit_list)

# fruit_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in fruit_list:
#     print(i)
#     for j in i:
#         print(j)
# fruit_list.append('a')
# print(fruit_list)
# fruit_list.insert(0, 'b')
# print(fruit_list)
# fruit_list[1].append('c')
# print(fruit_list)
# fruit_list[2].insert(1, 'd')
# print(fruit_list)

# car_tuple = ('a', 'b', 'c')     # immutable
# print(car_tuple)
# print(car_tuple[0:2])

# def func_tuple(x):
#     a = x + 1
#     b = x + 2
#     c = x + 3
#     return (a, b, c)
#
# (d, e, f) = func_tuple(10)
# print(d, e, f)

# car_set = {'a', 'b', 'c'}
# print(car_set)
# car_set[0] = 'd' # immutable
# car_set2 = {'d', 'e', 'f', 'd'}
# print(car_set2)
# car_set.add('g')
# print(car_set)
# car_set2.remove('e')
# print(car_set2)
# car_set3 = car_set.union(car_set2)
# print(car_set3)

# student_dict = {
#     1:      'a',
#     '2':    'b',
#     3:      ['c', 'd']
# }
#
# print(student_dict)
# print(student_dict[1])
# print(student_dict['2'])
# print(student_dict[3])
# student_dict[1] = 'e'   # mutable
# print(student_dict)
# student_dict[2] = 'f'
# print(student_dict)
#
# for k in student_dict.keys():
#     print(k)
# for i in student_dict.items():
#     print(i)
# for k, v in student_dict.items():
#     print(k, v)

# test_dict = {
#     1: {
#         11: 'a',
#         12: 'b'
#     },
#
#     2: {
#         21: 'c',
#         22: 'd'
#     },
#
#     3: {
#         31: 'e',
#         32: 'f',
#         'g': 55
#     }
# }
#
# print(test_dict)
# print(test_dict[2][21])
# print(test_dict[3]['g'])

# test_dict2 = [{1: 'a', 2: 'b', 'e': 55}, {1: 'c', 2: 'd'}]
# print(test_dict2)
# print(test_dict2[0])
# print(test_dict2[0][1])
# print(test_dict2[0]['e'])

# testList = [1, 2, 3]
# print(testList)
# testList.remove(testList[0])
# print(testList)


# def fact(n):
#     if n < 2:
#         return 1
#     return n*fact(n-1)
#
# print(fact(5))

# def recur_print(n):
#     if n == 0:
#         return print(n)
#     else:
#         recur_print(n-1)
#         return print(n)
#
# recur_print(5)

# import platform
# import math
# # import datetime
#
# x = platform.system()
# x1 = platform.version()
# print(x)
# print(x1)
# print(dir(math))
# print(dir(platform))
# print(dir(print))
# print(math.pi)
# print(math.sqrt(math.pi))
# print(datetime.datetime.now())

# import random
# myList = ['a', 'b', 'c']
# for n in range(6):
#     print(random.choice(myList))
# for n in range(10):
#     print(random.randint(3, 9))

# f = open('filetest.txt')
# for x in f:
#     print(x)
# # print(f.read(5))
# # print(f.read(5))
# print(f.readlines())    # returns a list with every line
# f.close()
#
# f = open('filetest.txt', 'a')
# f.write('\nthis is a new line')
# f.close()
# f = open('filetest.txt', 'r')
# print(f.read())

# print(len('x\ny'))
#
# f = open('filetest.txt', 'w')
# f.write('a     f')
# f.close()
#
# f = open('filetest.txt', 'a')
# f.write('\nb')
# f.write('\nc')
# f.close()

# f = open('filetest.txt', 'r')
# print(len(f.read()))
# print(f.read())
# for x in f.read():
#     if x.startswith('a'):
#         print(x)
# print(f.readline())
# print(f.readline())
# print(f.readline())
# for x in f:
#     print('x: ', x, 'is the content before')
#     y = x.rstrip()
#     print('y: ', y, 'is the content after')
# f.close()


# class Pet:
#     x = 5
#
#     def __init__(self, name, age):
#         print(f'a new instance is created {name}')
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         rtn_str = 'this is __str__ '
#         rtn_str += f'with {self.name} and {self.age}'
#         return rtn_str
#
#     def talk(self):
#         print(f'I am a instance of Pet {self.name}')
#
#     def speak(self):
#         print(f'I am an another instance of Pet {self.name}')
#
#     @staticmethod
#     def stamethod():
#         print('1111')
#
#
# pet_one = Pet("Joe", 10)
# pet_one.talk()
# pet_one.speak()
# print(pet_one.x)
# print(type(pet_one))
# print(pet_one.name)
# pet_one.name = 'Ellie'
# print(pet_one.name)
# print(pet_one)
# pet_one.stamethod()

# import numpy as np
#
# x = np.array([1, 2, 3])
# print(x)
