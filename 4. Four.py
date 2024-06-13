from random import randint, randrange, choices
import string

#Task 1
print("Task 1")
len_list = 12
print([randrange(163, 191) for i in range(len_list)])
del len_list

#Task 2
print("Task 2")

difference = 2
len_list = 10
a = [1 + difference * each for each in range(len_list)]
print(a)
del len_list, difference

#Task 3
print("Task 3")
nums = [1,2,3,3,4,5,6,7,8,8,10]
for each in range(len(nums) - 1, -1, -1):
    print(nums[each])
del nums

#Task 4
print("Task 4")

#Task 5
print("Task 5")
count = int(input("Classes: "))
sum = 0
for each in [randrange(22,32) for each in range(count)]:
    sum += each
if sum // 1000 > 0:
    print("True", sum)
del count, sum

#Task 6
print("Task 6")
nums = [randrange(35,100) for each in range(50)]
a_output, b_output = [], []
for each in nums:
    if each % 2 == 0:
        a_output.append(each)
    if str(each)[-1] == "0":
        b_output.append(each)
print(f"{a_output} \n{b_output}")
del nums, a_output, b_output

#Task 7
print("Task 7")
MIN_VALUE = 45
math = [randrange(35,101) for each in range(50)]
russian = [randrange(35,101) for each in range(50)]
it = [randrange(35,101) for each in range(50)]
names = [ ''.join(choices(string.ascii_letters, k=5)) for each in range(50)]
count = 1

for abb in range(len(names)):
    if count > 10:
        break
    if math[abb] + russian[abb] + it[abb] > 210 and (math[abb] > MIN_VALUE or russian[abb] > MIN_VALUE or it[abb] > MIN_VALUE):
        count += 1
        print(f"{abb}: {names[abb]} | {math[abb]} | {russian[abb]} | {it[abb]} ")
del MIN_VALUE, math, russian, it, names, count

#Task 8
print("Task 8")
nums = [randrange(0,10) for each in range(100)]

unique = {}
for each in nums:
    unique[each] = unique.get(each, 0)
print(len(unique))
del nums, unique

# Task 9
print("Task 9")
nums = [randrange(0,10) for each in range(6)]
is_even = 0 if len(nums) % 2 == 0 else 1
print(nums)
for index in range(0, len(nums) - 1 - is_even, 2):
    nums[index], nums[index + 1] = nums[index + 1], nums[index]
print(nums)
del nums, is_even

# Task 10
print("Task 10")
nums = [randrange(0,10) for each in range(9)]
k1 = 3
k2 = 6
print(nums)
print(nums[k2:] + nums[k1:k2] + nums[:k1])
del nums, k1, k2

# Task 11
print("Task 11")
names_len = 10
count = 0
# names = [input("Name: ") for each in range(names_len)]
names = ["sdf", "test", "abuziko", "test", "test", "test", "abuziko", "test", "abuziko", "abuziko"]
for index in range(0, names_len - 1):
    if names[index] == names[index + 1]:
        count += 1
    if index == names_len - 2:
        if names[index + 1] == names[0]:
            count += 1

print(count)
del names_len, count, names

# Task 12
print("Task 12")
nums = [randint(39,47) for each in range(30)]
unique = []
for each in nums:
    if not each in unique:
        unique.append(each)
del nums, unique

# Task 13
print("Task 13")
first_count = randint(10,30)

groups = []
for each in range(3):
    count = randint(10,30)
    groups.append([ ''.join(choices(string.ascii_letters, k=5)) for each in range(count)])   

count = 0
min_group = groups[0]
max_group = groups[0]
all_student = []
for each in groups:
    count += len(each)
    if len(each) < len(min_group):
        min_group = each
    if len(each) > len(max_group):
        max_group = each
    all_student += each
all_student = sorted(all_student)

print(f"1. {count} ||| \n ||| \n 2. {min_group} ||| \n ||| \n 3. {max_group} ||| \n ||| \n 4. {all_student}")
del first_count, count, min_group, max_group, all_student

# Task 14
print("Task 14")

grades = [randint(2,5) for each in range(30)]
sum_grades = 0
print(grades)
for each in grades:
    sum_grades += each

print(round(sum_grades / len(grades), 1))

# Task 15
print("Task 15")
print([num for num in range(1, 10001) if num % 21 == 0 or num % 9 == 0])

# Task 16
print("Task 16")
print([num * 11 for num in range(1, 10)])

# Task 17
print("Task 17")
nums = [[1,  10],  [2,  20],  [3,  30],  [4,40]]
print([item for sublist in nums for item in sublist])

# Task 18
print("Task 18")
print([each**2 if each % 2 == 0 else each + 2 for each in range(20)])

