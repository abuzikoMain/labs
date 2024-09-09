
# ---------------lab 8 Task 1 #
print('Task 1')
def find_substr(subst, st):
    if subst.lower() in st.lower():
        return True
    else:
        return False
print(find_substr ('Пит', 'пИтон'))
print(find_substr ('программирование', 'ПрограммироВаНИЕ'))
print(find_substr ('Довод', 'Повод'))

# # ---------------lab 8 Task 2 #
print('Task 2')
def first_last(let, st):
    last_index = -1
    first_index = -1
    is_first_set = False
    for index in range(len(st)):
        if let == st[index] and not is_first_set:
            first_index, last_index = index, index
            is_first_set = True

        if let == st[index] and index > last_index:
            last_index = index
    
    return (first_index, last_index)

print(first_last('a', 'abba'))
print(first_last('a', 'abbaaaab'))
print(first_last('a', 'a'))
print(first_last('a', 'spring'))

# # ----------------lab 8 Task 3 #
from collections import Counter
print('Task 3')
def most_common_top3(st):
    st = st.split()
    st = ''.join(st)
    st = Counter(st)
    st = st.most_common(3)
    st = ', '.join(f'{key} - {val}' for key, val in st)
    return st
print(most_common_top3('Python — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью'))
print(most_common_top3('АаА'))
print(most_common_top3('Тише едешь — дальше будешь'))
# # ----------------lab 8 Task 4 #
import os.path
print('Task 4')
def add_text_to_file(st):
    if os.path.exists('MyFile.txt'):
        with open('MyFile.txt', 'a', encoding='utf-8') as file:
            file.write(st + '\n')
        return 'Строка добавлена к существующим'
    else:
        with open('MyFile.txt', 'w+', encoding='utf-8') as file:
            file.write(st + '\n')
        return 'Файл был создан'
print(add_text_to_file("Первая строка"))
print(add_text_to_file("Вторая строка"))
print(add_text_to_file("Третья строка"))

# # ----------------lab 8 Task 5 #
print('Task 5')
def read_from_last(lines = 1, file_e = 'MyFile.txt'):
    with open(file_e, 'r', encoding='utf-8') as file:
        line = file.readlines()
    if lines > len(line):
        return f'В файле только {len(line)} строк'
    lines = abs(lines)
    return ''.join(line[len(line) - lines:])

print(read_from_last(2))

# # ----------------lab 8 Task 6 #
print('Task 6')
def camel(st):
    st = st.lower()
    func = lambda x: x[1].upper() if x[0] % 2 == 0 else x[1]
    result = ''.join(map(func, enumerate(st)))
    return result
print(camel('Копейка рубль бережет'))
print(camel('Из огня да в полымя'))
print(camel('КРАСОТА)))'))
# ----------------lab 8 Task 7 #
print('Task 7')
is_closed = lambda x: True if x == ')' else False
is_opened = lambda x: True if x == '(' else False

def slicer_st(st):
    pack = []
    reslut = ''
    in_brace = False
    for char in st:
        if is_opened(char):
            pack.append(char)
            in_brace = True
        if not in_brace:
            reslut += char
        if is_closed(char) and pack:
            pack.pop()
            if not pack:
                in_brace = False
        elif is_closed(char) and not pack:
            return ''

    if not pack:
        return reslut
    else:
        return ''

def remove_braces(st):
    out = slicer_st(st)   
    return out

print(remove_braces('Шила(лишнее (лишнее) лишнее) в мешке не утаишь (лишнее)'))
print(remove_braces('(лишнее(лишнее))Шила в мешке не (лишнее(лишнее(лишнее)))утаишь'))

# ----------------lab 8 Task 8 #
print('Task 8')
is_symbol = lambda x: True if x == '@' else False

def delete_backspace(st):
    result = ''
    for char in st:
        if is_symbol(char):
            result = result[:-1]
        else:
            result += char
    return result

# Проверки
#### Очень плохо работает переделать! callback фигня! и сложность n^2
# Update - Оптимизировано 

print(delete_backspace('пп@олс@кр@овт@оде@ец'))
print(delete_backspace('сварка@@@@@лоб@ну@'))

# ----------------lab 8 Task 9 #
print('Task 9')
def create_file(name):
    with open(name, 'w+', encoding='utf-8') as file:
        file.write('''Мороз и солнце; день чудесный!\n
                    Еще ты дремлешь, друг прелестный —\n
                    Пора, красавица, проснись:\n
                    Открой сомкнуты негой взоры\n
                    Навстречу северной Авроры,\n
                    Звездою севера явись!''')

def search_word(name):
    with open(name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    max_lenght = 0
    max_words = []

    for line in lines:
        for word in line.split():
            if len(word) > max_lenght:
                max_lenght = len(word)
                max_words = [word]
            if len(word) == max_lenght and word not in max_words:
                max_words.append(word)
    
    return max_words

def max_length_word(file = 'title.txt'):
    create_file(name = file)
    return search_word(name = file)

print(max_length_word('title.txt'))
