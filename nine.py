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
#Task 7
print('Task 7')


#Task 8, 9
print('Task 8, 9')
matrix_f = np.array([0, 1])
matrix_s = np.array([1, 0])

func = lambda x: np.tile(x, (1, 4))

matrix = func(matrix_f)
for line in range(1,8):
    if line % 2 == 1:
        matrix = np.concatenate((matrix,func(matrix_s)), axis=0)
    if line % 2 == 0:
        matrix = np.concatenate((matrix,func(matrix_f)), axis=0)
print(matrix)



