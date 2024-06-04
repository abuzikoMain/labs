
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

def is_number_palindrom(number: int) -> bool: ## Task 12
    str_number = str(number)
    r: int = len(str_number) - 1
    l: int = 0
    while l >= r:
        if str_number[r] != str_number[l]:
            return False
        r -=1
        l +=1
    return True

def output_task_thirteen(number: int) -> str: ## Task 13
    str_number = str(number)
    is_some_char_sames: bool = False
    is_all_chars_same: bool = False

    temp_dict = {}
    for each in str_number:
        temp_dict[each] = temp_dict.get(each, 0) + 1
        if temp_dict[each] > 1:
            is_some_char_sames = True

    if len(temp_dict) == 1:
        is_all_chars_same = True
        return 'All num\'s is same'
    elif is_some_char_sames:
        return 'Some num\'s is same'
    else:
        return 'All num\'s unique'

def output_task_fourteen(number: int) -> str: ## Task 14
    str_number = str(number)
    return 'At last num is even' if int(str_number[-1]) % 2 == 0 else 'At last num is not even'

### Task 15 not necessary 

def output_task_sixteen(mass: int) -> int: ## Task 16
    return mass // 1000

def output_task_seventeen() -> int: ## Task 17
    return 530 // 130

def output_task_eightteen(): ## Task 18 Непонимаю условие
    ...

def output_task_nineteen(number: int) -> int: ## Task 19
    return int(str(number)[::-1])

def output_task_twenty(number: int) -> int: ## Task 20
    return int(str(number)[::-1])

def output_task_twentyone(number: int) -> int: ## Task 21
    return int(str(number)[1::] + str(number)[:1:])

def output_task_twentytwo(number: int) -> int: ## Task 22
    return int(str(number)[1:2:] + str(number)[0:1:] + str(number)[2:])

def output_task_twentythree(number: int) -> int: ## Task 23
    return int(str(number)[0:1:] + str(number)[2:] + str(number)[1:2:])

def output_task_twentyfour(number: int) -> list: ## Task 24
    ...

def get_permutations(number):
    str_number = str(number)
    if len(set(str_number)) != len(str_number):
        return "Число должно содержать только различные цифры."
    permutations = []
    generate_permutations(str_number, "", permutations)
    return permutations

def generate_permutations(remaining_digits, current_permutation, permutations):
    if len(remaining_digits) == 0:
        permutations.append(int(current_permutation))
    else:
        for i in range(len(remaining_digits)):
            next_digit = remaining_digits[i]
            new_remaining = remaining_digits[:i] + remaining_digits[i+1:]
            generate_permutations(new_remaining, current_permutation + next_digit, permutations)

number = int(input("Введите число, в котором все цифры различны: "))

permutations = get_permutations(number)
if isinstance(permutations, list):
    print("Все возможные числа, образованные при перестановке цифр заданного числа:")
    for num in permutations:
        print(num)
else:
    print(permutations)


print(output_task_twentytwo(451))
