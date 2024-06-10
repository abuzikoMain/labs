import numpy as np
from random import randint
import math
# #Task 1
# print('Task 1')
# print(np.zeros(15, dtype=int))
# #Task 2
# print('Task 2')
# v = np.zeros(8, dtype=float)
# v.fill(3.2)
# print(v)
# del v
# #Task 3
# print('Task 3')
# v = np.zeros(15, dtype=float)
# v[4] = 1
# print(v)
# del v
# #Task 4
# print('Task 4')
# a = np.array([randint(12,43) for _ in range(10)], float) 
# print(a)
# del a
# #Task 5
# print('Task 5')
# a = np.random.sample(size=(3,3,2))
# print(a)
# del a
#Task 6
# print('Task 6')
# size_1 = int(input('Size 1: '))
# size_2 = int(input('Size 2: '))
# max_elemets = size_1 * size_2
# a = np.random.sample(size=(size_1,size_2))
# print(a.min(), a.max())
# #Task 7
# print('Task 7')

# #Task 8
# print('Task ')
# Z = np.zeros((8,8), dtype=int)
# Z[1::2,::2] = 1
# Z[::2,1::2] = 1

# #Task 9
# print('Task 9')
# matrix_f = np.array([0, 1])
# matrix_s = np.array([1, 0])

# func = lambda x: np.tile(x, (1, 4))

# matrix = func(matrix_f)
# for line in range(1,8):
#     if line % 2 == 1:
#         matrix = np.concatenate((matrix,func(matrix_s)), axis=0)
#     if line % 2 == 0:
#         matrix = np.concatenate((matrix,func(matrix_f)), axis=0)
# print(matrix)
# del matrix, matrix_f, matrix_s

# #Task 10
# print('Task 10')
# first = np.random.sample(size=(4,2))
# second = np.random.sample(size=(2,5))
# print(f'{first}\n||| {second}\n |||')
# print(np.matmul(first, second))
# del first, second

# #Task 11
# print('Task 11')
# matrix = np.array([randint(1,10) for _ in range(10)], float) 
# matrix[(4 < matrix) & (matrix <= 7)] *= -1
# print(matrix)

# del matrix

# #task 12
# print('Task 12')

# matrix = np.zeros((6,6))
# matrix += np.arange(6)
# print(matrix)

# del matrix


# #task 13
# print('Task 13')
# vector = np.array([randint(1,10) for _ in range(10)], float)
# vector = sorted(vector)
# print(vector)
# del vector

# #task 14
# print('Task 14')
# vector1 = np.array([randint(1,10) for _ in range(10)], float)
# vector2 = np.array([randint(1,10) for _ in range(10)], float)

# def eq_vector(vector1, vector2):
#     for x, y in zip(vector1, vector2):
#         if x != y:
#             return 'Not equal'
#     return 'equal'

# print(eq_vector(vector1, vector2))

# print(eq_vector(vector2, vector2))

# #task 15
# print('Task 15')
# len_vector = 10
# vector1 = np.array([randint(1,10) for _ in range(len_vector)], float)
# print(vector1)
# ind_max = vector1.argmax()
# vector1[ind_max] = float(-1)
# print(vector1) 


#task 16
print('Task 16')
def search_nearest_in_sorted_arr(x):
    ... # biqubic search 

#task 17
print('Task 17')
dtype = np.dtype([('x', float), ('y', float), ('color', [('r', int), ('g', int), ('b', int)])])

data = np.zeros(5, dtype=dtype)

data['x'] = [1.0, 2.0, 3.0, 4.0, 5.0]
data['y'] = [6.0, 7.0, 8.0, 9.0, 10.0]
data['color']['r'] = [255, 128, 0, 255, 0]
data['color']['g'] = [0, 255, 128, 255, 0]
data['color']['b'] = [0, 0, 255, 0, 255]

#task 18
print('Task 18')