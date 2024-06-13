# File: InsertionSort.py  
# Реализация алгоритма сортировки вставками 
# 
# Пример исходных данных и результата:  
# [3,6,8,2,9,1,7,0,5,9,4] -> [0,1,2,3,4,5,6,7,8,9,9] 
# 
# Задача: Дан массив чисел. Необходимо упорядочить его по 
# возрастанию с помощью алгоритма сортировки вставками. 
# 
# Основная идея: 
# Из неупорядоченной последовательности элементов поочередно 
# выбирается элемент, сравнивается с предыдущим (уже упорядоченным) 
# списком и помещается в соответствующее место 
#  
# Отсортированный 
#    участок 
#       | 
#  <---------> 
# [1,2,3,6,8,9,7,0,5,9,4] 
#              |        
#           Текущий 
#           элемент 

def insertionsort(L):
    for i in range(1, len(L)):
        to_insert = L[i]
        j = i - 1
        while j >= 0 and to_insert < L[j]:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = to_insert
    return L

L = [3,6,8,2,9,1,7,0,5,9,4] 

# Пример исходных данных и результата:  
# [3,6,8,2,9,1,7,0,5,9,4] -> [0,1,2,3,4,5,6,7,8,9,9] 
# 
# Задача: Дан массив чисел. Необходимо упорядочить его по 
# возрастанию с помощью алгоритма сортировки слиянием. 
# 
# Основная идея: 
# Рекурсивно разбиваем исходный массив на две части. 
# Рекурсия останавливается, когда получившиеся массивы состоят
# максимум из одного элемента. Такие массивы заведомо отсортированы. 
# Получив отсортированные массивы, начинаем обратное объединение 
# массивов чисел с помощью алгоритма слияния.  
# Алгоритм слияния работает следующим образом. 
# Даны два отсортированных массива чисел.  
# Например: [1,4,6] и [2,3,5] 
# Сравнивая по порядку элементы каждого массива, записываем в 
# результат меньшее значение. 
# Таким образом выполняем следующие действия: 
# [1,4,5], [2,3,6] -> [] 
# [4,5],   [2,3,6] -> [1] 
# [4,5],   [3,5]   -> [1,2] 
# [4,5],   [6]     -> [1,2,3] 
# [5],     [6]     -> [1,2,3,4] 
# [],      [6]     -> [1,2,3,4,5] 
# [],      []      -> [1,2,3,4,5,6] 
# Сложность шага слияния O(n) 


def mergesort(src):
    if len(src) <= 1:
        return src

    mid = len(src) // 2
    left = mergesort(src[:mid])
    right = mergesort(src[mid:])

    return merge(left, right)

def merge(left, right):
    res = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            res.append(left[left_index])
            left_index += 1
        else:
            res.append(right[right_index])
            right_index += 1

    res.extend(left[left_index:])
    res.extend(right[right_index:])

    return res
#------------------------------------
import random, time
LEN_INPUT_LIST = 10000
get_data = lambda y: [random.randint(0,y*10) for _ in range(y)]
data = get_data(LEN_INPUT_LIST)

t1 = time.perf_counter() 
insertionsort(data) 
t2 = time.perf_counter() 
print("Time sorting insert: {:.2f} ms".format((t2 - t1) * 1000.))

t1 = time.perf_counter() 
mergesort(data) 
t2 = time.perf_counter() 
print("Time sorting merge: {:.2f} ms".format((t2 - t1) * 1000.))

# print(mergesort(lst))
# print(insertionsort(lst)) 

 

