
import datetime
import math

# Валидации данных нет!
# Валидации данных нет!
# Валидации данных нет!
# Валидации данных нет!
# Валидации данных нет!

## Task 1
print('Task 1')
x  = int(input("x: "))
x_line:int = 4
if x > x_line:
        print('II')
else:
        print('I')


 ## Task 2
print('Task 2')
y  = int(input("y: "))
y_line:int = 4
if y > y_line:
    print('I')
else:
    print('II')

del x, y, y_line

 ## Task 3
print("Task 3")
x = float(input("x: "))
print("a")
if x >= 2:
    print("Y = 2")
else:
    print(f"Y = {x}")

print("b")
if x >= 3:
    print("Y = -3")
else:
    print(f"Y = {x * -1}")
del x

print("Task 4, 5")## Task 4, 5
first = int(input("first: "))
second = int(input("second: ")) 
if first != second:
    if first > second:
        print(f'{first} максимальное, {second} минимальное')
    else:
        print(f'{second} максимальное, а {first} минимальное')
else:
    print('Числа равны')
 
del first, second 

 ## Task 6
print('Task 6')
year_born = int(input("year_born: "))
month_born = int(input("month_born: ")) 

date = datetime.datetime.now()
now_year = date.year
now_month = date.month
if year_born < now_year and month_born < 12:
    years = now_year - year_born - 1
    if now_month > month_born:
        years += 1  
else:
    print(0)

print(years)
del year_born, month_born, date, now_year, now_month

 ## Task 7
x = float(input("Task 7 x: "))
if x > 0:
    print(math.sin(x) ** 2)
else:
    print(1+2*(math.sin(x**2)))
del x

## Task 8  
x = float(input("Task 8 x: "))
if x > 0:
    print(math.sin(x**2)) 
else:
    print(1+2*(math.sin(x)**2)) 
del x

## Task 9    
print("Task 9")
divider = float(input("divider: "))
number = float(input("number: "))
print(True if number % divider == 0 else False) 
del divider, number

## Task 10
x = input("Task 10 x:") 
even: bool = True if int(x) % 2 == 0 else False
seven: bool = True if x[-1] == '7' else False
print(even and seven) 
del x, even, seven

## Task 11
x = input("Task 11 x: ")
first = int(x[0])
second = int(x[-1])
if first == second:
    print(f'{first} equal {second}') 
print(f'{first} is bigger then {second}' if first > second else f'{second} is bigger then {first}') 
del x, first, second

 ## Task 12
number = input("Task 12 number: ")
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
del number, str_number

## Task 13
number = input("Task 13 number: ")
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
print("Task 14")
str_number = input("Task 14 number: ")
print('At last num is even' if int(str_number[-1]) % 2 == 0 else 'At last num is not even')
del str_number

### Task 15 not necessary 

## Task 16
print("Task 16:", int(input("Task 16 mass: ")) // 1000)

## Task 17
print("Task 17:", 530 // 130)

## Task 18 Непонимаю условие
print("Task 18")
months = int(input('Введите кол-во месяцев:'))
years = 1990 + months // 12
days=1
months = months % 12 + 1
if months>12:
  years+=1
  months-=12
elif months<1:
  years-=1
  months+=12
print(datetime.date(years, months, 1)+datetime.timedelta(days-1))
del months, years, days


## Task 19
print(input("Task 19 number: ")[::-1])

## Task 20
number = input("Task 20: ")
print(number[1::] + number[0])
del number

## Task 21
number = input("Task 21: ")
print(number[-1] + number[:2:])
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

## Task 26, 27
print("Task 26, 27")
temp_number = input("n: ")
last_num, temp_number = int(temp_number[0]), int(temp_number[1::])
temp_number *=10
temp_number += last_num
print(temp_number)
del temp_number, last_num

## Task 28
print("Task 28")
temp_number = input("n: ")
last_num, temp_number = int(temp_number[-1]), int(temp_number[:2:])
print(last_num * 100 + temp_number)
del temp_number, last_num

## Task 29
print("Task 29")
temp_number = input("n: ")
print(temp_number[0] + temp_number[-1]  + temp_number[1])
del temp_number

## Task 30  
print("Task 30")
date = datetime.datetime.now()
hour_now, minutes_now, seconds_now = date.hour, date.minute, date.second
print((30*hour_now+minutes_now/2+seconds_now/120)/2)
del date, hour_now, minutes_now, seconds_now

## Task 31
print("Task 31")
y = float(input("y: "))
print(f"Hours: {int(y/620*24)} minutes {int(y/360*24*60)}")
del y

## Task 32
print("Task 32")
date = datetime.datetime.now()
minute = float(date.minute) + float(date.second/60)
angle = minute/5*30
print(f"{date.hour} час {date.minute} минут")
print(f"{math.floor(angle)} Угол")
del date, minute, angle 

## Task 32
print("Task 32")
A = input("A: ")
B = input("B: ")
C = input("C: ")

if A > 100 and B > 100:
    print("True")

if A % 2 == 0 or B % 2 == 0:
    print("True")

if A > 0 or B > 0:
    print("True")

if A % 3 == 0 and B % 3 == 0 and C % 3 == 0:
    print("True")

if (A < 50 and B >= 50 and C >= 50) or (A >= 50 and B < 50 and C >= 50) or (A >= 50 and B >= 50 and C < 50):
    print("True")

if A < 0 or B < 0 or C < 0:
    print("True")
del A, B, C 

## Task 33
print("Task 33")

col1 = input("Столбец 1-й клетки: ")
col2 = input("Столбец 2-й клетки: ")
row1 = input("Строка 1-й клетки: ")
row2 = input("Строка 2-й клетки: ")

if (col1 == col2) or (row1 == row2):
    print ("YES")
else:
    print ("NO")
del col1, row1, col2, row2 

## Task 34
print("Task 34")
x = input("x: ")
y = input("y: ")
## a
print("a")
if x <= -1 and y <= -2:
    print("True")
else:
    print("True")

## b
print("b")
if y >= 1 or y <= -3:
    print("True")
else:
    print("True")
