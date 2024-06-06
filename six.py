from random import randint, choices
import string

# Task 1
# print("Task 1")
# number_counts = {}
# numbers = [randint(0,100) for each in range(50)]
# for number in numbers:
#     number_counts[number] = number_counts.get(number, 0) + 1
# print("Количество встреч каждой цифры:")
# for digit, count in sorted(number_counts.items()):
#     print(f"Цифра {digit}: {count} раз(a)")
# del digit_counts, numbers

# Task 2
# print("Task 2")
# set1 = {randint(0,100) for num in range(50)}
# set2 = {randint(0,100) for num in range(50)}
# common_numbers = set1.intersection(set2)
# if common_numbers:
#     print("Числа, которые одновременно встречаются в обоих списках:")
#     print(sorted(common_numbers))
# else:
#     print("В обоих списках нет общих чисел")
# del set1, set2, common_numbers

# Task 3
# print("Task 3")
# text = [''.join(choices(string.ascii_letters, k=5)) for each in range(50)]
# unique_words = set(text)
# word_count = len(unique_words)
# print(f"Количество слов в тексте: {word_count}")
# del text, unique_words, word_count

# Task 4

# Task 5
# print("Task 5")
# set1 = {randint(0,10) for num in range(5)}
# set2 = {randint(0,10) for num in range(5)}
# print(set.union(set2))
# del set1, set2

# Task 6
# print("Task 6")

# lines = randint(1, 5)
# text = '\n'.join(
#     ' '.join(
#         ''.join(choices(string.ascii_letters, k=randint(5, 9)))
#         for _ in range(randint(1, 10))
#     )
#     for _ in range(lines)
# )
# print(text)

# count = {}
# for line in text.splitlines():
#     for word in line.split():
#         count[word] = count.get(word, 0) + 1
# for key, val in count.items():
#     print(f" word: {key} count: {val}")