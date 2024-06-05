from random import randint, choices
import string

# Task 1
# digit_counts = {}

# numbers = [randint(0,100) for each in range(50)]

# for number in numbers:
#     for digit in number:
#         digit_counts[digit] = digit_counts.get(digit, 0) + 1

# print("Количество встреч каждой цифры:")
# for digit, count in sorted(digit_counts.items()):
#     print(f"Цифра {digit}: {count} раз(a)")

# Task 2

# set1 = {randint(0,100) for num in range(50)}
# set2 = {randint(0,100) for num in range(50)}

# common_numbers = set1.intersection(set2)

# if common_numbers:
#     print("Числа, которые одновременно встречаются в обоих списках:")
#     print(sorted(common_numbers))
# else:
#     print("В обоих списках нет общих чисел")

# Task 3

# text = [''.join(choices(string.ascii_letters, k=5)) for each in range(50)]
# unique_words = set(text)
# word_count = len(unique_words)
# print(f"Количество слов в тексте: {word_count}")

# Task 4
