import math


### ВАЛИДАЦИИ НЕТ!!!!
### ВАЛИДАЦИИ НЕТ!!!!
### ВАЛИДАЦИИ НЕТ!!!!
### ВАЛИДАЦИИ НЕТ!!!!
### ВАЛИДАЦИИ НЕТ!!!!

#TASK 1
print("TASK 1")
exchange = float(input("exchange: "))
for each in range(1,21):
    print(each * exchange)
del exchange

#TASK 2
print("TASK 2")
number = int(input("Number: "))
for each in range(1,11):
    print(number * each)
del number

#TASK 3
print("TASK 3")
a = int(input("a: "))
b = int(input("b: "))
sum = 0
for each in range(a, b + 1):
    sum = sum + each ** 2
print(sum)
del a, b

#TASK 4
print("TASK 4")
a = input("a: ")
new = ""
for each in range(len(a) -1, -1, -1):
    new += a[each]
print(new)
del new, a

#TASK 5
print("TASK 5")
a = int(input("a: "))
factorial = 1
for each in range(1, a + 1):
    factorial *=each
print (factorial)
del a, factorial

#TASK 6
print("TASK 6")

nums = [-1,-2,-3,-5,-6,-7,-7,9,7,4,9]
count = 0
index = 0
while(nums[index]<0):
   
   count+=1
   index+=1

print(count)
del nums, index, count

#TASK 7
print("TASK 7")

number = int(input("n: "))
a, b = 1, 1
while True:
    if a > number:
        break
    a, b = b, a + b
print(a)
del number, a, b

#TASK 8
print("TASK 8")

number = int(input("n: "))
str_number = str(number)
min_num = int(str_number[0])

count = 1
for num in str_number[1:]:
    if int(num) < min_num:
        min_num = int(num)
        count = 1
    elif int(num) == min_num:
        count += 1
print(count)
del number, str_number, min_num

# ##Task 9
print("Task 9")

n = int(input("n: "))
f = int(input("первый член прогрессии: "))
s = int(input("шаг арифметической прогрессии: "))

if (n - f) % s == 0:
    print(f"{n} Является")
else:
    print(f"{n} Не является")

##Task 10
print("Task 10")

number = input("nmber: ")
r = len(number) - 1
l = 0 
min_num = number[0]
ind_min = 0
max_num = number[-1]
ind_max = 0
while l <= r:
    if max_num < number[l]:
        max_num = number[l]
        ind_max = l
    if max_num < number[r]:
        max_num = number[r]
        ind_max = r
    if min_num > number[l]:
        min_num = number[l]
        ind_min = l
    if min_num > number[r]:
        min_num = number[r]    
        ind_min = r
    r -=1
    l +=1

if ind_min < ind_max:
    print(f"Number: {min_num}, index: {ind_min}")
else:
    print(f"Number: {max_num}, index: {ind_max}")
del number, r, l, min_num, ind_min, max_num, ind_max

##Task 12
print("Task 12")
try:
    factorial_n = int(input("number: "))  
    n = 1
    result = 1
    while result < factorial_n:
        n += 1
        result *= n
    if result == factorial_n:
        print("n =", n)
    else:
        print("Значение n не найдено.")
except Exception as e:
    print(f"exc: {e} | \n Иначе ипользуйте формулу стирлинга")
del factorial_n, n, result

##Task 13
print("Task 13")
nums = [64, 32, 16, 8, 4, 2, 1]
number = int(input("number: "))
count = {}
index = 0
while number > 0:
    if number - nums[index] >= 0:
        number -= nums[index]
        count[nums[index]] = count.get(nums[index], 0) + 1
    else:
        index +=1
print(count)
del number, nums, count, index

##Task 14
print("Task 14")

count = 100
payment_bull = 10
payment_cow = 5
payment_calve = 0.5

max_count_bull = count // payment_bull
max_count_cow = count // payment_cow

for bull in range (1, max_count_bull + 1):
    for cow in range(1, max_count_cow + 1):
        calve = count-bull-cow
        if bull*payment_bull+cow*payment_cow+calve*payment_calve == count:
            print("быки:", bull, "коровы:", cow, "телята:", calve);

##Task 15
print("Task 15")
number = int(input("number: "))
output = 0
count = 0
while count < number:
    count +=1
    output += count ** count 
print("output", output)
