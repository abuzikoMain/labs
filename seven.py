from random import randint, choice, choices
import string
import re

# Task 1
# print('Task 1')

# with open('seven.txt', 'w+', encoding='utf-8') as file:
#     file.writelines([f'{str(randint(1, 10))}\n' for _ in range(2)])

# with open('seven.txt', 'r', encoding='utf-8') as file:
#     num1 = int(file.readline().rstrip())
#     num2 = int(file.readline().rstrip())
    
#     print(num1 + num2)
# del num1, num2

# Task 2
# # print('Task 2')

# with open('seven.txt', 'w+', encoding='utf-8') as file:
#     file.writelines(['qwe qwe 12w', '123 asd 1', '! qwe q !'])

# with open('seven.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         if '!' in line:
#             print('Yes')
#             break
#     else:
#         print('No')
       
# # Task 3
# with open('seven.txt', 'w+', encoding='utf-8') as file:
#     file.writelines([f'{' '.join([str(randint(1, 10)) for _ in range(randint(4, 10))])}\n' for _ in range(randint(4, 10))])

# print('Task 3')
# with open('seven.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         numbers = map(int, line.split())
#         total_sum = lambda numbers: sum(numbers)
#         print(total_sum(numbers))

# Task 4
# print('Task 4')

# with open('seven.txt', 'w+', encoding='utf-8') as file:
#     file.writelines([f'{' '.join([''.join(choices(string.ascii_letters, k=randint(5, 9))) for _ in range(randint(5, 10))])}\n' for _ in range(randint(4, 10))])

# count_lines = 0
# count_words = 0
# count_alpha = 0
# with open('seven.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         count_lines += 1
#         iter_line = line.split()
#         count_words += len(iter_line)
#         for word in iter_line:
#             for index_str in word:
#                 if index_str.isalpha:
#                     count_alpha +=1
# print(count_lines, count_words, count_alpha)
# del count_lines, count_words, count_alpha

# Task 5
# print('Task 5')
# read files after run Task 4

# text = {}
# counter = 0
# with open('seven.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         counter +=1
#         text[str(counter)] = line.rstrip()

# def read(key):
#     return text.get(str(key), 'not found').rstrip()

# def readlines(first_key = 0, second_key = len(text)):
#     output = ''
#     for key in range(first_key, second_key):
#         output += f'{text.get(str(key), '')}\n'
#     return output.rstrip()

# def readline(first=0, second=0):
#     if first == 0:
#         return readlines()
#     if second != 0:
#         return readlines(first, second)
#     return read(first)

# print('a')
# print(readline(1))
# print('б')
# print(readline(5))
# print('в')
# print(readline(1, 5))
# print('г')
# print(readline(2, 3))
# print('д')
# print(readline())
# del text, counter

# Task 6
# print('Task 6')

# print('a')
# with open('seven.txt', 'r', encoding='utf-8') as file:
#     max_length = max(len(line.strip()) for line in file)
#     print('Длина самой длинной строки:', max_length)

# print('б, в')
# max_length_line_number = None
# with open('seven.txt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#     for index, line in enumerate(lines):
#         if len(line.strip()) == max_length:
#             max_length_line_number = index + 1  # Нумерация строк с 1
#             print('Номер самой длинной строки:', max_length_line_number)
#             print('Самая длинная строка:', line.strip())
#             break
# del max_length, max_length_line_number

# Task 7
# print('Task 7')

# with open('seven.txt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()

# with open('output.txt', 'w+', encoding='utf-8') as file:
#     file.writelines([f'{str(line.rstrip())[::-1]}\n' for line in lines])
# del lines

# Task 8
# print('Task 8')
# with open('seven.txt', 'r', encoding='utf-8') as file1, open('output.txt', 'r', encoding='utf-8') as file2:
#     line_number = 0
#     for line1, line2 in zip(file1, file2):
#         line_number += 1
#         if line1 != line2:
#             print(f'{line_number}')
#             break
#     else:
#         print('Файлы идентичны.')
# del line_number

# Task 9
# print('Task 9')

Stations = [f'Station: {_}' for _ in range(randint(1,10))]

text_input = '''
Иванов Сергей 1 5 
Сергеев Петр 3 5 
Петров Кирилл 1 2
'''
#