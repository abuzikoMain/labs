
import datetime
import math

def define_dot_first(x:int, y:int) -> str: ## Task 1
    x_line:int = 4
    if x > x_line:
        return 'II'
    else:
        return 'I'
        
def define_dot_second(x: int, y: int) -> str: ## Task 2
    y_line:int = 4
    if y > y_line:
        return 'I'
    else:
        return 'II'
    
def define_y_at_func(func: str, x: float) -> float: ## Task 3
    y: float = 0
    #???????????? Принимаем функцию и по функции получаем значение y при значении x ? 
    return y 

def define_bigger_and_smaller(first: float, second: float) -> str: ## Task 4, 5
    if first != second:
        if first > second:
            return f'{first} максимальное, {second} минимальное'
        else:
            return f'{second} максимальное, а {first} минимальное'
    else:
        return 'Числа равны'

def define_human_age(year_born: int, month_born: int) -> int: ## Task 6
    date = datetime.datetime.now()
    now_year = date.year
    now_month = date.month
    if year_born < now_year and month_born < 12:
        years = now_year - year_born - 1
        if now_month > month_born:
            years += 1  
    else:
        return 0
    
    return years

def output_task_seven(x: float) -> float: ## Task 7
    if x > 0:
        return math.sin(x) ** 2
    else:
        return 1+2*(math.sin(x**2))
    
def output_task_eight(x: float) -> float: ## Task 8
    if x > 0:
        return math.sin(x**2)
    else:
        return 1+2*(math.sin(x)**2)
    
def is_divider_number(divider: float, number: float) -> bool: ## Task 9
    return True if number % divider == 0 else False

def is_number_even_and_last_seven(x: int) -> bool: ## Task 10
    even: bool = True if x % 2 == 0 else False
    seven: bool = True if str(x)[-1] == '7' else False
    return even and seven

def output_task_eleven(x: int) -> str: ## Task 11
    first = int(str(x)[0])
    second = int(str(x)[-1])
    if first == second:
        return f'{first} equal {second}'
    return f'{first} is bigger then {second}' if first > second else f'{second} is bigger then {first}'

 ## Task 12
number = input("Task 12: ")
str_number = str(number)
r: int = len(str_number) - 1
l: int = 0
while l >= r:
    if str_number[r] != str_number[l]:
        print("False")
        break
    r -=1
    l +=1
print("True")

## Task 13
number = input("Task 13: ")
str_number = str(number)
is_some_char_sames: bool = False

temp_dict = {}
for each in str_number:
    temp_dict[each] = temp_dict.get(each, 0) + 1
    if temp_dict[each] > 1:
        is_some_char_sames = True

if len(temp_dict) == 1:
    print('All num\'s is same')
elif is_some_char_sames:
    print('Some num\'s is same')
else:
    print('All num\'s unique')

del number, str_number, is_some_char_sames, temp_dict


 ## Task 14
str_number = input("Task 14: ")
print('At last num is even' if int(str_number[-1]) % 2 == 0 else 'At last num is not even')
del str_number

### Task 15 not necessary 

## Task 16
print("Task 16:", int(input("Task 16 mass: ")) // 1000)

## Task 17
print("Task 17:", 530 // 130)

## Task 18 Непонимаю условие

## Task 19
print(input("Task 19 number: ")[::-1])

## Task 20
number = input("Task 20: ")
print(number[1::] + number[0])
del number

## Task 21
number = input("Task 21: ")
print(number[-1] + number[:1:])
del number

## Task 22
number = input("Task 22: ")
print(number[1:2:] + number[0:1:] + number[2:])
del number

## Task 23
number = input("Task 23: ")
print(number[0:1:] + number[2:] + number[1:2:])
del number

def get_permutations(number: int) -> list: ## Task 24
    str_number = str(number)
    if len(set(str_number)) != len(str_number):
        return "Число должно содержать только различные цифры."
    permutations = []
    generate_permutations(str_number, "", permutations)
    return permutations

def generate_permutations(remaining_digits: str, current_permutation: str, permutations: list) -> None:
    if len(remaining_digits) == 0:
        permutations.append(int(current_permutation))
    else:
        for i in range(len(remaining_digits)):
            next_digit = remaining_digits[i]
            new_remaining = remaining_digits[:i] + remaining_digits[i+1:]
            generate_permutations(new_remaining, current_permutation + next_digit, permutations)

## task 25
number = int(input("Task 25: "))
one_count = 0
ten_count = number // 10
for each in str(number):
    if each == "1":
        one_count += 1
print(f'One count: {one_count}, ten count: {ten_count}')
del number, one_count, ten_count

## Task 26
temp_number = str(237)
last_num, temp_number = temp_number[0], int(temp_number[1::])
temp_number *=10
temp_number += last_num
print(temp_number)

del temp_number, last_num, temp_number

