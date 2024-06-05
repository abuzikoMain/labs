import math
from random import randint

# # Task 1
# def task_1():
#     ...

# #### Вариант 1
# #### Вариант 1
# #### Вариант 1
# #### Вариант 1
# #### Вариант 1
# #### Вариант 1

# # Task 2
# def task_2(x):
#     return x ** 6 - 2 * x - 7
# print(task_2(int(input("Task 2 x: "))))

# # Task 3 
# def task_3(x, y):
#     f = math.sin(x + 1) - y - 1.2
#     s = 2 * x + math.cos(y) - 2
#     return (f, s)

# print(task_3(float(input("Task 2 x: ")), float(input("Task 2 y: "))))

# # Task 4
# def remain_of_the_division(lst, element = 2, division = 0):
#     return list(filter(lambda x: x % element == division, lst))

# def task_4(first, second):
#     first = len(remain_of_the_division(first))
#     second = len(remain_of_the_division(second, division = 1))
#     return first, second

# print(task_4([randint(0,100) for each in range(50)], [randint(0,100) for each in range(50)]))

# # Task 5
# def task_5(nums):
#     return min(nums), max(nums)

# count = int(input("Count elements: "))
# print(task_5([randint(0,100) for each in range(count)]))
# del count


# # Task  6
# def task_6(number, counter):
#     symbols = "0123456789ABCDEF"
    
#     def convert_recursive(number, counter):
#         if number == 0:
#             return ''
#         else:
#             return convert_recursive(number // counter, counter) + symbols[number % counter]
    
#     result = convert_recursive(number, counter)
#     return result if result else '0'


# number = int(input("Number: "))
# counter = int(input("counter: "))
# print(task_6(number, counter))
# del number, counter

# # Task 7

# def task_7(number):

#     def is_natural(number, main_number):
#         if number in [1, 0]:
#             return True
        
#         if main_number % number == 0:
#             return False
#         number -= 1
#         return is_natural(number, main_number) and True

#     if number % 1 == 0 and number % number == 0 and is_natural(number - 1, number):
#         return True
#     else:
#         return False
    
# print(task_7(82))

# Task 8

def task_8():
    ...
    