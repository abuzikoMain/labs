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

# ---------------lab 8 Task 1 #
# def find_substr(subst, st):
#     if subst.lower() in st.lower():
#         return True
#     else:
#         return False
    
# # ---------------lab 8 Task 2 #
# def first_last(let, st):
#     last_index = 0
#     first_index = 0
#     is_first_set = False
#     for index in range(len(st)):
#         if let == st[index] and not is_first_set:
#             first_index, last_index = index, index
#             is_first_set = True

#         if let == st[index] and index > last_index:
#             last_index = index
    
#     return (first_index, last_index)
# # ----------------lab 8 Task 3 #
# from collections import Counter

# def most_common_top3(st):
#     st = st.split()
#     st = ''.join(st)
#     st = Counter(st)
#     st = st.most_common(3)
#     st = ''.join(f'{key} - {val}\n' for key, val in st)
#     return st
# print(most_common_top3('Python — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью'))

# # ----------------lab 8 Task 4 #
# import os.path

# def add_text_to_file(st):
#     if os.path.exists('MyFile.txt'):
#         with open('MyFile.txt', 'a', encoding='utf-8') as file:
#             file.write(st + '\n')
#         return 'Строка добавлена к существующим'
#     else:
#         with open('MyFile.txt', 'w+', encoding='utf-8') as file:
#             file.write(st + '\n')
#         return 'Файл был создан'

# # ----------------lab 8 Task 5 #

# def read_from_last(lines = 1, file_e = 'seven.txt'):
#     with open(file_e, 'r', encoding='utf-8') as file:
#         line = file.readlines()
#     if lines > len(line):
#         return f'В файле только {len(line)} строк'
#     lines = abs(lines)
#     return '\n'.join(line[len(line) - lines:])

# print(read_from_last(11))

# # ----------------lab 8 Task 6 #

# def camel(st):
#     func = lambda x: x[1].upper() if x[0] % 2 == 0 else x[1]
#     result = ''.join(map(func, enumerate(st)))
#     return result

# ----------------lab 8 Task 7 #

# is_closed = lambda x: True if x == ')' else False
# is_opened = lambda x: True if x == '(' else False

# def counter_braces(st):
#     opened = []
#     for index in range(len(st)):
#         if len(opened) == 0 and is_closed(st[index]):
#             return ''
        
#         if is_opened(st[index]):
#             opened.append([st[index], index])

#         if is_closed(st[index]):
#             temp = opened.pop(-1)
#             st = st[:temp[-1]] + st[index + 1:]
#             break

#         if index == len(st) - 1:
#             return st

#     return counter_braces(st)

# def remove_braces(st):
#     st = counter_braces(st)
    
#     return st

# print(remove_braces('(лишнее(лишнее))Шила в мешке не (лишнее(лишнее(лишнее)))утаишь'))

# ----------------lab 8 Task 8 #

# is_symb = lambda x: True if x == '@' else False

# def recursive(st):
#     for index in range(len(st)):
#         if is_symb(st[index]):
#             to_del = index
#             st = st[:to_del - 1] + st[to_del + 1:]
#             return recursive(st)
        
#         if index == len(st) - 1:
#             return st

# def delete_backspace(st):
#     st = recursive(st)

#     return st
# print(delete_backspace('пп@олс@кр@овт@оде@ец'))

# ----------------lab 8 Task 9 #

# def create_file(name):
#     with open(name, 'w+', encoding='utf-8') as file:
#         file.write('''Мороз и солнце; день чудесный!\n
#                     Еще ты дремлешь, друг прелестный —\n
#                     Пора, красавица, проснись:\n
#                     Открой сомкнуты негой взоры\n
#                     Навстречу северной Авроры,\n
#                     Звездою севера явись!''')

# def search_word(name):
#     with open(name, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
    
#     max_lenght = 0
#     max_words = []

#     for line in lines:
#         for word in line.split():
#             if len(word) > max_lenght:
#                 max_lenght = len(word)
#                 max_words = [word]
#             if len(word) == max_lenght and word not in max_words:
#                 max_words.append(word)
    
#     return max_words

# def max_length_word(file = 'title.txt'):
#     create_file(name = file)
#     return search_word(name = file)

# print(max_length_word())